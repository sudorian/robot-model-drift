"""Serial, resumable survey. Explicit network is enabled only with --fetch."""
from __future__ import annotations
import argparse
import configparser
import dataclasses
import json
import os
from pathlib import Path
import re
import subprocess
import time
import xml.etree.ElementTree as ET
import yaml
from .compare import Tolerances
from .discovery import inventory,candidate_paths
from .engine import source_match,compare
from .gate import GitSource,compile_snapshot
from .network import ROOT,clone_repo,fetch_blobs,log,disk_bytes
from .provenance import select_source
from .publication import public_data
from .reports import write_model,write_summary,h1_annex


class Runner:
    def __init__(self,fetch=False,tolerances=Tolerances()):
        self.fetch=fetch
        self.tolerances=tolerances
        self.sources={}
        self.fetch_attempts=set()
        self.snapshot_cache={}

    def repo(self,url):
        if url in self.sources:
            return self.sources[url]
        if url.endswith('/unitreerobotics/unitree_ros'):
            directory=ROOT/'.cache/unitree_ros'
        else:
            directory=ROOT/'.cache'/url.split('github.com/',1)[1].replace('/','__')
        existed=(directory/'.git').is_dir()
        if not (directory/'.git').is_dir():
            if not self.fetch:
                raise ValueError(f"Source clone absent: {url}; use --fetch")
            clone_repo(url,str(directory))
        source=GitSource(directory,url)
        if self.fetch and existed:
            from .network import refresh_repo
            refresh_repo(source)
        self.sources[url]=source
        return source

    def compile(self,source,commit,path,arguments=None):
        key=(str(source.directory),commit,path,json.dumps(arguments or {},sort_keys=True))
        if key in self.snapshot_cache:
            return self.snapshot_cache[key]
        from .network import fetch_objects
        last=None
        attempted=set()
        for attempt in range(150):
            try:
                value=compile_snapshot(source,commit,path,arguments=arguments)
                self.snapshot_cache[key]=value
                if len(self.snapshot_cache)>300:
                    self.snapshot_cache.pop(next(iter(self.snapshot_cache)))
                return value
            except subprocess.CalledProcessError as exc:
                last=exc
                if not self.fetch:
                    break
                revision=str(exc.cmd[-1])
                if ':' not in revision:
                    break
                try:
                    oid=source.git('rev-parse',revision).strip()
                    if not re.fullmatch(r'[0-9a-f]{40}',oid) or oid in attempted:
                        break
                    attempted.add(oid)
                    fetch_objects(source.directory,[oid])
                except Exception as fetch_error:
                    log(f"Targeted fetch failed for {source.url} {revision}: {fetch_error}")
                    break
            except (ValueError,OSError,ImportError,ET.ParseError) as exc:
                last=exc
                break
        raise last or ValueError(f"Cannot compile {path}")

    def view(self,source,commit,path,snapshot=None):
        return {'repo':source.url,'commit':commit,'file':path,'cache':str(source.directory.relative_to(ROOT)),
                **({'snapshot':snapshot} if snapshot is not None else {})}

    def check(self,entry,m,commit):
        name=entry['model']
        result={'model':name,'status':'incomplete','source':{'method':'unknown','confidence':'unknown','candidate':None},
                'tolerances':dataclasses.asdict(self.tolerances),
                'source_evidence':entry['evidence'],'derivation_evidence':entry['derivation_lines'],
                'candidate_errors':[],'self_comparisons':[],'xml_fragments':entry.get('xml_fragments',[])}
        variants=[]
        for path in entry['menagerie_files']:
            try:
                snap=self.compile(m,commit,path)
                identity=compare(snap,snap,snap,'dated match',self.tolerances)
                result['self_comparisons'].append({'file':path,'status':'passed','findings':len(identity['findings'])})
                variants.append((path,snap))
            except Exception as exc:
                message=f"Menagerie self-comparison compile failed: {path}: {type(exc).__name__}: {exc}"
                log(message);result['self_comparisons'].append({'file':path,'status':'error','error':message})
        if not variants:
            result['reason']='No Menagerie variant compiled; source comparisons unavailable.'
            return result
        # Prefer simplest complete robot entry; scene includes and companion components
        # remain covered by the self-comparison inventory.
        variants.sort(key=lambda v:(-len(v[1]['joints']),len(v[0])))
        result['menagerie']=self.view(m,commit,*variants[0])
        if not entry['sources']:
            result['status']='unknown upstream'
            result['reason']='No machine-readable upstream repository found in README, CHANGELOG, or their history. Vendor/CAD/web descriptions were not fetched under the network rules.'
            if entry.get('cad_web_source'):
                result['reason']='Current README describes a SolidWorks conversion from a Google Docs CAD source. No public machine-readable upstream is named; unrelated historical template links are retained only as evidence.'
            return result
        choices=[]
        seen=set()
        source_links=list(entry['sources'])
        for link in source_links:
            try:
                upstream=self.repo(link['repo'])
                head=upstream.git('rev-parse','HEAD').strip()
                tree=upstream.git('ls-tree','-r','--name-only',head).splitlines()
                if '.gitmodules' in tree:
                    config=configparser.ConfigParser()
                    config.read_string(upstream.read(head,'.gitmodules'))
                    for section in config.sections():
                        module_path=config.get(section,'path',fallback='')
                        module_url=config.get(section,'url',fallback='').removesuffix('.git')
                        if not module_url.startswith('https://github.com/'):
                            continue
                        if link.get('path','').startswith(module_path+'/') or 'description' in module_path and not link.get('path'):
                            child={**link,'repo':module_url,'path':link.get('path','')[len(module_path):].lstrip('/'),
                                   'ref':None,'pinned':False,'url':module_url,'document':'.gitmodules',
                                   'commit':head,'score':link['score']+1}
                            if not any(s['repo']==module_url and s.get('path')==child['path'] for s in source_links):
                                source_links.append(child)
                                result['source_evidence'].append({'url':module_url,'document':'.gitmodules','commit':head,'parent_repo':upstream.url})
                discovery_entry={**link,'model':name,'preferred_format':entry.get('preferred_format'),'menagerie_stems':[Path(p).stem for p in entry['menagerie_files']]}
                paths=candidate_paths(upstream,head,discovery_entry)
                if not paths and link.get('path'):
                    # Search only already-authorized, already-cloned sources from
                    # the same manufacturer for an exact robot filename.
                    owner=link['repo'].split('github.com/',1)[1].split('/')[0].lower()
                    stems={Path(p).stem for p in entry['menagerie_files']}
                    for directory in (ROOT/'.cache').iterdir():
                        if not (directory/'.git').is_dir() or directory==upstream.directory:
                            continue
                        try:
                            probe=GitSource(directory,'')
                            url=probe.git('config','--get','remote.origin.url').strip().removesuffix('.git')
                            if not url.lower().startswith('https://github.com/'+owner+'/'):
                                continue
                            existing=GitSource(directory,url)
                            for p in existing.git('ls-tree','-r','--name-only','HEAD').splitlines():
                                basename=Path(p).name
                                for suffix in ('.xacro','.urdf','.xml'):
                                    if basename.endswith(suffix):basename=basename[:-len(suffix)]
                                if basename in stems and p.endswith(('.urdf','.xml','.xacro')) and not any(s['repo']==url and s.get('path')==p for s in source_links):
                                    extra={**link,'repo':url,'path':p,'pinned':False,'ref':None,'score':link['score']+1,'url':'exact model filename in an already-cloned repository from the same manufacturer'}
                                    source_links.append(extra)
                                    result['source_evidence'].append({'url':url,'file':p,'document':'manufacturer source Git tree','reason':'README-linked path missing at current HEAD; exact model filename in same-manufacturer referenced source repository'})
                        except subprocess.CalledProcessError:
                            pass
                # A pinned historical file may have been moved or removed from HEAD.
                if link.get('pinned'):
                    paths=list(dict.fromkeys(candidate_paths(upstream,link['ref'],discovery_entry)+paths))
                for upath in paths:
                    key=link['repo'],upath
                    if key in seen:
                        continue
                    seen.add(key)
                    try:
                        raw=upstream.read(head,upath)
                        if not re.search(r'<(?:robot|mujoco)\b',raw):
                            continue
                        hs=self.compile(upstream,head,upath,arguments=link.get('arguments'))
                        for mpath,ms in variants:
                            matched=source_match(ms,hs,self.tolerances)
                            coverage=len(matched['mapping']['bodies'])+len(matched['mapping']['joints'])
                            preferred=entry.get('preferred_format')=='urdf' and upath.endswith(('.urdf','.xacro'))
                            mobility_compatible=bool(ms['joints'])==bool(hs['joints'])
                            score=(bool(link.get('pinned')),bool(link.get('recipe')),preferred,mobility_compatible,coverage/max(1,len(ms['bodies'])+len(ms['joints'])),coverage,-matched['mismatch_count'],link['score'])
                            choices.append((score,upstream,head,upath,hs,mpath,ms,link))
                    except Exception as exc:
                        message=f"{link['repo']} {upath} at {head}: {type(exc).__name__}: {exc}"
                        log(message);result['candidate_errors'].append(message)
            except Exception as exc:
                message=f"Source discovery {link['repo']}: {type(exc).__name__}: {exc}"
                log(message);result['candidate_errors'].append(message)
        if not choices:
            result['reason']='Machine-readable sources were identified, but no standalone source entry compiled. See all candidate errors.'
            if not result['candidate_errors']:
                result['status']='unknown upstream'
                result['reason']='Linked repository inspected, but no standalone URDF/MJCF robot description was found. No M/H drift classification is made.'
            return result
        _,u,hsha,upath,hs,mpath,ms,link=max(choices,key=lambda c:c[0])
        result['source_options']=[{'repo':c[1].url,'file':c[3],'menagerie_file':c[5],'score':c[0],'evidence':c[7].get('url')} for c in choices]
        result['menagerie']=self.view(m,commit,mpath,ms)
        history=m.history(mpath,allow_fetch=self.fetch)
        origin=min(history,key=lambda row:int(row['timestamp']))
        # Locate introduction of the current physical values, walking backwards from
        # current file changes until a prior physical version differs.
        for row in sorted(history,key=lambda row:int(row['timestamp']),reverse=True):
            if int(row['timestamp'])>int(m.git('log','-1','--format=%ct',commit).strip()):
                continue
            try:
                old=self.compile(m,row['commit'],row.get('file',mpath))
                if source_match(ms,old,self.tolerances)['matches']:
                    origin=row
                else:
                    break
            except Exception as exc:
                log(f"Historical Menagerie compile failed {name} {row['commit']}: {exc}")
                result['candidate_errors'].append(f"Menagerie history {row['commit']}: {exc}")
                break
        result['menagerie']['origin']=origin
        result['menagerie']['commits_involved']=[{k:row[k] for k in ('commit','date','file') if k in row} for row in history]
        result['upstream']=self.view(u,hsha,upath,hs)
        candidates=[]
        main_history=u.history(upath,allow_fetch=self.fetch)
        pending={row['commit']:dict(row) for row in main_history}
        dependencies=set(hs.get('source_dependencies',[upath]))|{upath}
        covered=set()
        inspected=set()
        history_warning=next((row.get('history_incomplete') for row in main_history if row.get('history_incomplete')),None)
        old_paths=list(dict.fromkeys([upath]+[row.get('file',upath) for row in main_history]))
        while True:
            if dependencies-covered:
                for row in u.history_for_paths(dependencies):
                    if row['commit'] not in pending:
                        pending[row['commit']]={**row,'file':upath,'dependency_change':True}
                covered=set(dependencies)
            todo=[row for sha,row in pending.items() if sha not in inspected]
            if not todo:
                break
            for row in sorted(todo,key=lambda r:int(r['timestamp']),reverse=True):
                inspected.add(row['commit'])
                candidate=dict(row)
                if history_warning:candidate['history_incomplete']=history_warning
                candidate_file=row.get('file',upath)
                available=u.git('ls-tree','-r','--name-only',row['commit'],'--',candidate_file).strip()
                if not available:
                    for alternate in old_paths:
                        if u.git('ls-tree','-r','--name-only',row['commit'],'--',alternate).strip():
                            candidate_file=alternate;available=alternate;break
                if not available:
                    candidate.update({'deleted':True,'matches':False,'note':'Source entry absent at this revision; no numeric value to compile'})
                    candidates.append(candidate)
                    continue
                candidate['file']=candidate_file
                try:
                    candidate['snapshot']=self.compile(u,row['commit'],candidate_file,arguments=link.get('arguments'))
                    candidate.update(source_match(ms,candidate['snapshot'],self.tolerances))
                    dependencies.update(candidate['snapshot'].get('source_dependencies',[candidate_file]))
                except Exception as exc:
                    candidate['error']=str(exc);candidate['matches']=False
                    log(f"Historical source compile failed {name} {row['commit']} {candidate_file}: {exc}")
                candidates.append(candidate)
        candidates.sort(key=lambda c:int(c['timestamp']),reverse=True)
        result['history_inputs']=sorted(dependencies)
        pinned=None
        if link.get('pinned'):
            psha=link['ref']
            try:
                psha=u.git('rev-parse',link['ref']+'^{commit}').strip()
                options=[]
                pin_entry={**link,'model':name,'preferred_format':entry.get('preferred_format'),'menagerie_stems':[Path(p).stem for p in entry['menagerie_files']]}
                for pin_path in candidate_paths(u,psha,pin_entry):
                    try:
                        raw=u.read(psha,pin_path)
                        if not re.search(r'<(?:robot|mujoco)\b',raw):
                            continue
                        ps=self.compile(u,psha,pin_path,arguments=link.get('arguments'))
                        matched=source_match(ms,ps,self.tolerances)
                        coverage=len(matched['mapping']['bodies'])+len(matched['mapping']['joints'])
                        options.append(((coverage,-matched['mismatch_count']),pin_path,ps,matched))
                    except Exception as exc:
                        log(f"Pinned source candidate failed {name} {pin_path}: {exc}")
                if not options:
                    raise ValueError('No pinned source entry could be compiled')
                _,pin_path,ps,matched=max(options,key=lambda option:option[0])
                meta=u.git('log','-1','--format=%ct|%cI',psha).strip().split('|')
                pinned={'commit':psha,'file':pin_path,'timestamp':meta[0],'date':meta[1],'snapshot':ps,**matched}
            except Exception as exc:
                log(f"Pinned source compilation failed {name}: {exc}")
                result['candidate_errors'].append(f"Pinned source: {exc}")
                pinned={'commit':psha,'file':link.get('path',upath),'error':str(exc),'matches':False}
        provenance=select_source(candidates,origin['timestamp'],pinned)
        result['source']=provenance
        result['source_candidates']=candidates
        selected=provenance['candidate']
        ss=selected.get('snapshot') if selected else None
        if selected:
            result['source_view']=self.view(u,selected['commit'],selected.get('file',upath),ss)
        # Derivation differences are documented only when the README explicitly names
        # the affected quantity. Broad edits are not automatically blessed.
        documented=[]
        for line in entry['derivation_lines']:
            if re.search(r'(mass|inertia|range|limit)',line,re.I):
                # Require the exact entity name in the documented operation.
                for body in ms['bodies']:
                    if body in line:
                        for field in ('mass','subtree_mass','principal_moments'):
                            if (field=='principal_moments' and 'inertia' in line.lower()) or (field!='principal_moments' and 'mass' in line.lower()):
                                documented.append((body,field))
        result['comparison']=compare(ms,ss,hs,provenance['method'],self.tolerances,documented)
        errors=[c for c in candidates if c.get('error') or c.get('history_incomplete')]+([pinned] if pinned and pinned.get('error') else [])
        result['status']='complete' if not errors else 'partial history'
        result['reason']='No public revision matches all comparable quantities.' if provenance['method']=='none' else 'Source selected using the ordered amended provenance rules.'
        if provenance['method']=='unknown':
            result['reason']=provenance.get('reason') or 'Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.'
        if errors and provenance['method']=='none':
            result['reason']='No matching revision among successfully compiled candidates; failed history entries prevent an exhaustive no-match claim.'
            result['source']['confidence']='incomplete'
        available=[c for c in candidates if 'snapshot' in c]
        earliest=min(available,key=lambda c:int(c['timestamp'])) if available else None
        baseline=ss or (earliest['snapshot'] if earliest else None)
        hchanges=compare(baseline,baseline,hs,'dated match',self.tolerances) if baseline else None
        result['upstream_changed']='yes' if hchanges and hchanges['findings'] else ('no' if hchanges else 'unknown')
        result['sensitivity']={}
        baseclasses={(r['entity'],r['quantity']):r['class'] for r in result['comparison']['rows']}
        for scale in (.5,2):
            t=dataclasses.replace(self.tolerances,scale=self.tolerances.scale*scale)
            scaled=[]
            for c in candidates:
                scaled.append({**c,**source_match(ms,c['snapshot'],t)} if 'snapshot' in c else c)
            sp=select_source(scaled,origin['timestamp'],pinned)
            sc=compare(ms,sp['candidate'].get('snapshot') if sp['candidate'] else None,hs,sp['method'],t,documented)
            classes={(r['entity'],r['quantity']):r['class'] for r in sc['rows']}
            result['sensitivity'][str(scale)]={'provenance_method':sp['method'],'counts':sc['counts'],
                'classifications_changed':sum(baseclasses.get(k)!=v for k,v in classes.items()),
                'finding_membership_changes':len(set((r['entity'],r['quantity']) for r in sc['findings']) ^ set((r['entity'],r['quantity']) for r in result['comparison']['findings']))}
        metadata=('geometry_stripped','missing_explicit_inertials','assets_loaded','mesh_conversions','nonphysical_normalizations',
                  'xacro_arguments','source_dependencies','registration','compiler_warnings','limit_semantics')
        result['compilation']={'M':{k:ms[k] for k in metadata if k in ms},'H':{k:hs[k] for k in metadata if k in hs}}
        if ss:result['compilation']['S']={k:ss[k] for k in metadata if k in ss}
        if link.get('recipe'):
            result['construction_recipe']={'file':link['path'],'arguments':link.get('arguments',{}),'evidence':link.get('recipe_evidence')}
        return result


def save(results):
    temporary=ROOT/'report/results.json.tmp'
    temporary.write_text(json.dumps(public_data(results, ROOT),indent=2)+'\n')
    temporary.replace(ROOT/'report/results.json')
    write_summary(results)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fetch',action='store_true')
    parser.add_argument('--model')
    parser.add_argument('--resume',action='store_true')
    parser.add_argument('--menagerie-ref',default='HEAD')
    args=parser.parse_args()
    m=GitSource(ROOT/'.cache/menagerie','https://github.com/google-deepmind/mujoco_menagerie')
    commit=m.git('rev-parse',args.menagerie_ref+'^{commit}').strip()
    from .network import ensure_menagerie_texts
    ensure_menagerie_texts(m,commit,args.fetch)
    entries=inventory(m,commit,allow_fetch=args.fetch)
    (ROOT/'report/inventory.json').write_text(json.dumps(public_data(entries, ROOT),indent=2)+'\n')
    runner=Runner(args.fetch)
    runner.sources[m.url]=m
    results=json.loads((ROOT/'report/results.json').read_text()) if args.resume and (ROOT/'report/results.json').exists() else []
    done={r['model'] for r in results}
    for entry in entries:
        if args.model and entry['model']!=args.model or args.resume and entry['model'] in done:
            continue
        print(f"START {entry['model']} ({len(results)+1}/{len(entries)})",flush=True)
        started=time.monotonic()
        try:
            result=runner.check(entry,m,commit)
        except Exception as exc:
            log(f"Model check failed {entry['model']}: {type(exc).__name__}: {exc}")
            result={'model':entry['model'],'status':'error','reason':str(exc),'source':{'method':'unknown','confidence':'unknown'}}
        results=[r for r in results if r['model']!=entry['model']]+[result]
        result['elapsed_seconds']=round(time.monotonic()-started,3)
        annex=h1_annex(json.loads((ROOT/'report/acceptance.json').read_text())) if entry['model']=='unitree_h1' else ''
        write_model(result,annex)
        save(sorted(results,key=lambda r:r['model']))
        print(f"DONE {entry['model']}: {result['status']} / {result['source']['method']} / {result.get('comparison',{}).get('counts',{})} ({result['elapsed_seconds']}s); disk {disk_bytes()/1e9:.3f} GB",flush=True)


if __name__=='__main__':
    main()
