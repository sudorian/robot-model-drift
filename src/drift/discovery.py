"""Offline discovery from READMEs, CHANGELOGs and their folder history."""
from pathlib import PurePosixPath
import re
from .loader import files_at
from .network import ROOT
import yaml

IGNORE_REPOS = {"kevinzakka/obj2mjcf","kmammou/v-hacd","google-deepmind/dm_control",
                "google-deepmind/mujoco","Rhoban/onshape-to-robot","3dlg-hcvc/visacd",
                "discoverse-dev/urdf-to-mjcf"}


def urls_in(text):
    return sorted(set(re.findall(r"https://github\.com/[^\s)<>\"\]]+",text)))


def inventory(menagerie, commit,allow_fetch=False):
    files=files_at(menagerie,commit)
    models=[]
    recipes=yaml.safe_load((ROOT/'config/xacro_recipes.yaml').read_text()) if (ROOT/'config/xacro_recipes.yaml').exists() else {}
    for readme in files:
        if readme.count("/") != 1 or not readme.endswith("/README.md") or readme.startswith("test/"):
            continue
        name=readme.split("/")[0]
        xml=[p for p in files if p.startswith(name+"/") and p.endswith(".xml") and p.count("/")==1 and not PurePosixPath(p).name.startswith("scene")]
        fragments=[]
        for p in list(xml):
            raw=menagerie.read(commit,p)
            if '<worldbody' not in raw and '<include' not in raw:
                fragments.append(p)
                xml.remove(p)
            elif '<worldbody' not in raw and '<include' in raw:
                from .loader import expand_includes
                if expand_includes(menagerie,commit,p).find('worldbody') is None:
                    fragments.append(p)
                    xml.remove(p)
            elif '<actuator' in raw and '<worldbody' in raw:
                from .loader import expand_includes
                expanded=expand_includes(menagerie,commit,p)
                world=expanded.find('worldbody')
                bodies=world.findall('.//body') if world is not None else []
                if not bodies or all(b.get('mocap')=='true' for b in bodies) and not world.findall('.//joint'):
                    fragments.append(p)
                    xml.remove(p)
        if not xml:
            continue
        text=menagerie.read(commit,readme)
        overview=re.split(r'(?:URDF\s*→\s*MJCF|URDF\s*->\s*MJCF|MJCF)?\s*derivation steps',text,flags=re.I)[0]
        preferred_format='urdf' if re.search(r'(?:derived|original|provided|converted|based|available)[\s\S]{0,220}?\bURDF\b',overview,re.I) else None
        evidence=[]
        messages=menagerie.git('log','--format=%H%x00%B%x00',commit,'--',name).split('\x00')
        for i in range(0,len(messages)-1,2):
            sha=messages[i].strip();message=messages[i+1]
            for url in urls_in(message):
                evidence.append({'url':url,'document':'git commit message','commit':sha,'current':False})
        for doc in (readme,name+"/CHANGELOG.md"):
            if doc in files:
                for url in urls_in(menagerie.read(commit,doc)):
                    evidence.append({"url":url,"document":doc,"commit":commit,"current":True})
            # Older documentation can preserve links lost during later rewrites.
            for row in menagerie.history(doc,allow_fetch=allow_fetch):
                try:
                    oldtext=menagerie.read(row['commit'],row.get('file',doc))
                    if doc.endswith('README.md'):
                        stop={'description','mjcf','model','robot','robotics','the'}
                        title=lambda t:set(w for w in re.findall(r'[a-z0-9]+',t.splitlines()[0].lower()) if len(w)>2 and w not in stop)
                        if title(text) and title(oldtext) and not title(text)&title(oldtext):
                            from .network import log
                            log(f"Rejected unrelated historical README template for {name}: {row['commit']} heading {oldtext.splitlines()[0]!r}")
                            continue
                    for url in urls_in(oldtext):
                        if not any(e['url']==url for e in evidence):
                            evidence.append({"url":url,"document":doc,"commit":row['commit'],"current":False})
                except Exception:
                    # Deleted documents are expected during history walks; record later
                    # source-file errors separately from document absence.
                    pass
        sources=[]
        for e in evidence:
            parts=e['url'].split('github.com/',1)[1].split('/')
            if len(parts)<2:
                continue
            repo='/'.join(parts[:2]);tail=parts[2:]
            if repo in IGNORE_REPOS or repo.lower()=='google-deepmind/mujoco_menagerie':
                continue
            if tail and any(x=='meshes' for x in tail) and not any(x.endswith(('.urdf','.xacro','.xml')) for x in tail):
                continue
            ref=tail[1] if len(tail)>1 and tail[0] in ('tree','blob','commit') else None
            path='/'.join(tail[2:]).split('#',1)[0] if len(tail)>2 and tail[0] in ('tree','blob') else ''
            pinned=bool(ref and re.fullmatch(r'[0-9a-f]{40}',ref) and e['document'].endswith('README.md'))
            score=(30 if path.endswith(('.urdf','.xacro','.xml')) else 0)+(10 if pinned else 0)+(2 if e['current'] else 0)
            sources.append({**e,"repo":"https://github.com/"+repo,"ref":ref,"path":path,"pinned":pinned,"score":score})
        specific=name.split('_',1)[-1]
        if '_' in specific:
            family,variant=specific.rsplit('_',1)
            kept=[]
            for source in sources:
                match=re.search(re.escape(family)+r'_([a-z0-9]+)',source['repo'].rsplit('/',1)[-1].lower())
                if len(variant)<=2 and match and len(match.group(1))<=2 and match.group(1)!=variant and not source['pinned']:
                    from .network import log
                    log(f"Rejected conflicting robot-variant link for {name}: {source['url']} (repository variant {match.group(1)}, model variant {variant})")
                else:
                    kept.append(source)
            sources=kept
        if name=='unitree_h1':
            sources.append({"repo":"https://github.com/unitreerobotics/unitree_ros","ref":"master","path":"robots/h1_description/urdf/h1.urdf","pinned":False,"score":50,"url":"user-provided upstream lead","document":readme,"commit":commit,"current":True})
        if sources:
            primary=max(sources,key=lambda s:s['score'])
            linked_shas={s['ref'] for s in sources if s.get('pinned')}
            for line_number,line in enumerate(text.splitlines(),1):
                if not re.search(r'commit|copied|sha',line,re.I):
                    continue
                for sha in re.findall(r'\b[0-9a-f]{40}\b',line):
                    if sha not in linked_shas:
                        sources.append({**primary,'ref':sha,'pinned':True,'score':primary['score']+5,
                                        'url':f"plain SHA in README line {line_number}",'document':readme,'commit':commit,'current':True,
                                        'pin_context':line})
                        linked_shas.add(sha)
        cad_web_source=bool(re.search(r'SOLIDWORKS\s*(?:->|→)',text,re.I) and 'docs.google.com/document/' in text and not any(s.get('current') for s in sources))
        if cad_web_source:
            sources=[] # keep historical URLs as evidence, not as the current CAD source
        if name in recipes:
            recipe=recipes[name]
            sources.append({'repo':recipe['repo'],'path':recipe['file'],'arguments':recipe['arguments'],
                            'recipe':True,'pinned':False,'ref':None,'score':100,'current':True,'commit':commit,
                            'document':'config/xacro_recipes.yaml','url':recipe['repo'],'recipe_evidence':recipe['evidence']})
        models.append({"model":name,"menagerie_files":xml,"xml_fragments":fragments,"cad_web_source":cad_web_source,"preferred_format":preferred_format,"sources":sorted(sources,key=lambda s:-s['score']),
                       "evidence":evidence,"readme":readme,"derivation_lines":[line for line in text.splitlines() if any(w in line.lower() for w in ('mass','inertia','range','limit','fuse','merge','fixed','scale'))]})
    return models


def candidate_paths(source,commit,entry):
    files=files_at(source,commit)
    candidates=[p for p in files if p.endswith(('.urdf','.xacro','.xml')) and not PurePosixPath(p).name.startswith('scene')]
    linked=entry.get('path','').rstrip('/')
    if linked in candidates:
        return [linked]
    if linked and any(p.startswith(linked+'/') for p in candidates):
        candidates=[p for p in candidates if p.startswith(linked+'/')]
    else:
        def stem(p):
            value=PurePosixPath(p).name
            for suffix in ('.xacro','.urdf','.xml'):
                if value.endswith(suffix):
                    value=value[:-len(suffix)]
            return value
        stems=set(entry.get('menagerie_stems',[]))
        same_stem=[p for p in candidates if stem(p) in stems]
        if same_stem:
            return sorted(same_stem,key=lambda p:('/build' in p or '/test' in p,len(p)))
        # A missing model-specific directory must not silently select a different
        # robot from a large manufacturer repository (for example A2 for A1).
        marker=entry.get('model','').split('_',1)[-1]
        if linked and marker and any(part==marker or part==marker+'_description' for part in linked.lower().split('/')):
            matching=[p for p in candidates if any(part==marker or part==marker+'_description' or stem(part)==marker for part in p.lower().split('/'))]
            if not matching:
                return []
            candidates=matching
        if entry.get('preferred_format')=='urdf':
            urdfs=[p for p in candidates if p.endswith(('.urdf','.xacro'))]
            if 0<len(urdfs)<=12:
                return sorted(urdfs,key=lambda p:('macro' in p or '/test' in p,len(p)))
        tokens=[x for x in re.split(r'[_\W]+',entry.get('model','')) if len(x)>1]
        scores={p:sum(3 if t in PurePosixPath(p).stem.lower() else 1 for t in tokens if t in p.lower()) for p in candidates}
        best=max(scores.values(),default=0)
        if best:
            candidates=[p for p in candidates if scores[p]>=best]
    return sorted(candidates,key=lambda p:('macro' in p or '/test' in p,len(p),p))
