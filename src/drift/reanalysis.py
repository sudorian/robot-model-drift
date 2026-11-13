"""Frozen-revision survey rerun with fresh primary compiles and saved history."""
import dataclasses
import json
import re
import numpy as np
from .compare import Tolerances
from .engine import compare,source_match
from .provenance import select_source


def _same_physics(a,b):
    if isinstance(a,dict):return a.keys()==b.keys() and all(_same_physics(a[k],b[k]) for k in a)
    if isinstance(a,str) or a is None:return a==b
    return bool(np.allclose(a,b,rtol=1e-12,atol=1e-12))


def recheck(result,entry,runner,menagerie,commit):
    if result['menagerie']['commit']!=commit:
        raise ValueError('--recompare target differs from the saved Menagerie commit')
    t=runner.tolerances
    result['tolerances']=dataclasses.asdict(t)
    result['self_comparisons']=[]
    for path in entry['menagerie_files']:
        snap=runner.compile(menagerie,commit,path)
        identity=compare(snap,snap,snap,'dated match',t)
        result['self_comparisons'].append({'file':path,'status':'passed' if not identity['findings'] else 'failed','findings':len(identity['findings'])})
    if not result.get('comparison'):
        result['rerun']={'mode':'frozen revisions','self_variants_recompiled':len(result['self_comparisons']),
                        'upstream_comparison':'unavailable, previously recorded source/compilation gap retained'}
        return result
    refreshed={}
    for label,key in (('M','menagerie'),('H','upstream'),('S','source_view')):
        view=result.get(key)
        if not view or not view.get('snapshot'):continue
        old=view['snapshot']
        source=menagerie if label=='M' else runner.repo(view['repo'])
        snapshot=runner.compile(source,view['commit'],view['file'],arguments=old.get('xacro_arguments'))
        if not all(_same_physics(old[field],snapshot[field]) for field in ('total_mass','total_com_registered','bodies','joints')):
            raise ValueError('Fresh compile changed saved physics for '+result['model']+' '+label)
        view['snapshot']=snapshot;refreshed[label]=snapshot
    m,h=refreshed['M'],refreshed['H']
    pinned=result['source']['candidate'] if result['source']['method']=='pinned' else None
    for candidate in result['source_candidates']:
        if 'snapshot' not in candidate:continue
        sv=result.get('source_view',{})
        if 'S' in refreshed and candidate['commit']==sv.get('commit') and candidate.get('file',result['upstream']['file'])==sv.get('file'):
            candidate['snapshot']=refreshed['S']
        candidate.update(source_match(m,candidate['snapshot'],t))
    if pinned and 'S' in refreshed:pinned['snapshot']=refreshed['S']
    provenance=select_source(result['source_candidates'],result['menagerie']['origin']['timestamp'],pinned)
    selected=provenance['candidate']
    result['source']=provenance
    s=selected.get('snapshot') if selected else None
    if selected:
        result['source_view']={k:v for k,v in result['upstream'].items() if k!='snapshot'}
        result['source_view'].update(commit=selected['commit'],file=selected.get('file',result['upstream']['file']))
        if s:result['source_view']['snapshot']=s
    else:result.pop('source_view',None)
    documented=[]
    for line in entry['derivation_lines']:
        if re.search(r'(mass|inertia|range|limit)',line,re.I):
            for name in m['bodies']:
                if name in line:
                    for field in ('mass','subtree_mass','principal_moments'):
                        if (field=='principal_moments' and 'inertia' in line.lower()) or (field!='principal_moments' and 'mass' in line.lower()):documented.append((name,field))
    # Keep exact-line reference caches for records whose values remain unchanged.
    refs={(r['entity'],r['quantity']):r.get('source_references') for r in result['comparison']['rows']}
    result['comparison']=compare(m,s,h,provenance['method'],t,documented)
    for row in result['comparison']['rows']:
        if refs.get((row['entity'],row['quantity'])):row['source_references']=refs[row['entity'],row['quantity']]
    base={(r['entity'],r['quantity']):r['class'] for r in result['comparison']['rows']}
    result['sensitivity']={}
    for scale in (.5,2):
        st=dataclasses.replace(t,scale=t.scale*scale)
        candidates=[{**c,**source_match(m,c['snapshot'],st)} if 'snapshot' in c else c for c in result['source_candidates']]
        p=select_source(candidates,result['menagerie']['origin']['timestamp'],pinned)
        c=compare(m,p['candidate'].get('snapshot') if p['candidate'] else None,h,p['method'],st,documented)
        result['sensitivity'][str(scale)]={'provenance_method':p['method'],'counts':c['counts'],
            'classifications_changed':sum(base.get((r['entity'],r['quantity']))!=r['class'] for r in c['rows']),
            'finding_membership_changes':len({(r['entity'],r['quantity']) for r in c['findings']} ^ {(r['entity'],r['quantity']) for r in result['comparison']['findings']})}
    candidates=[c for c in result['source_candidates'] if 'snapshot' in c]
    baseline=s or (min(candidates,key=lambda c:int(c['timestamp']))['snapshot'] if candidates else None)
    changes=compare(baseline,baseline,h,'dated match',t) if baseline else None
    result['upstream_changed']='yes' if changes and changes['findings'] else ('no' if changes else 'unknown')
    result['rerun']={'mode':'frozen revisions','primary_views_recompiled':sorted(refreshed),
                   'self_variants_recompiled':len(result['self_comparisons']),
                   'historical_snapshots_reused':len(candidates),'primary_physics_unchanged':True,
                   'source_matching':'original raw-value provenance criteria retained; kinematic guard applies to reported CoM'}
    return result
