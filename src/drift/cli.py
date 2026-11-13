"""CLI for source acquisition, checks, reports, and fixed H1 acceptance."""
import argparse
import json
from pathlib import Path
from .network import ROOT
from .publication import public_data


def main():
    parser=argparse.ArgumentParser(description='Compare robot descriptions across their source history')
    parser.add_argument('--root',type=Path,default=ROOT)
    sub=parser.add_subparsers(dest='command',required=True)
    check=sub.add_parser('check')
    check.add_argument('model',help='model folder name, or all')
    check.add_argument('--fetch',action='store_true',help='allow logged GitHub clone/fetch')
    check.add_argument('--resume',action='store_true')
    check.add_argument('--recompare',action='store_true',help='recompile saved M/S/H and self-check variants; reuse historical snapshots at the saved commits')
    check.add_argument('--menagerie-ref',default='HEAD')
    check.add_argument('--tolerance-scale',type=float,default=1.0)
    for name,default in [('mass-relative',.005),('mass-absolute',.001),('com-absolute',.0005),('inertia-relative',.01),('range-absolute',.005),('slide-range-absolute',.0005),('limit-relative',.01),('kinematic-residual',.005),('kinematic-axis-angle',.005)]:
        check.add_argument('--'+name,type=float,default=default)
    sub.add_parser('report')
    sub.add_parser('acceptance')
    cross=sub.add_parser('cross-check')
    cross.add_argument('--all-stale',action='store_true',help='independently recheck every counted STALE record')
    args=parser.parse_args()
    if args.command=='check' and args.recompare and (args.fetch or args.resume):
        parser.error('--recompare uses frozen saved commits and cannot be combined with --fetch or --resume')
    if args.command=='acceptance':
        from .gate import run
        result=run(args.root)
        (args.root/'report/acceptance.json').write_text(json.dumps(public_data(result, args.root),indent=2)+'\n')
        print(f"H1 acceptance: {result['status']}; {result['three_way_total_mass_class']}")
        raise SystemExit(0 if result['status']=='passed' else 2)
    if args.command=='report':
        from .reports import write_model,write_summary,h1_annex
        results=json.loads((args.root/'report/results.json').read_text())
        for result in results:
            annex=h1_annex(json.loads((args.root/'report/acceptance.json').read_text())) if result['model']=='unitree_h1' else ''
            write_model(result,annex)
        # Keep resolved declaration links in the published JSON too, so reports
        # can be rendered offline after the ignored source caches are removed.
        from .survey import save
        save(results)
        write_summary(results)
        print(f"Rendered {len(results)} model reports and report/summary.md")
        return
    if args.command=='cross-check':
        from .direct import cross_check,audit_stale
        if args.all_stale:
            output=audit_stale(json.loads((args.root/'report/results.json').read_text()))
            print(f"Every-STALE XML audit: {sum(c['agree'] for c in output['checks'])}/{len(output['checks'])} agree")
            raise SystemExit(0 if all(c['agree'] for c in output['checks']) else 2)
        output=cross_check(json.loads((args.root/'report/results.json').read_text()))
        print(f"Independent direct XML checks: {sum(c['agree'] for c in output['checks'])}/{len(output['checks'])} agree")
        raise SystemExit(0 if len(output['checks'])==3 and all(c['agree'] for c in output['checks']) else 2)
    from .compare import Tolerances
    from .survey import Runner,inventory,save
    from .gate import GitSource
    from .reports import write_model,h1_annex
    if not (args.root/'.cache/menagerie/.git').is_dir() and args.fetch:
        from .network import clone_repo
        clone_repo('https://github.com/google-deepmind/mujoco_menagerie',str(args.root/'.cache/menagerie'))
    if not (args.root/'.cache/menagerie/.git').is_dir():
        parser.error('Menagerie source cache is absent; use check <model> --fetch')
    m=GitSource(args.root/'.cache/menagerie','https://github.com/google-deepmind/mujoco_menagerie')
    if args.fetch and args.menagerie_ref=='HEAD':
        from .network import refresh_repo
        refresh_repo(m)
    commit=m.git('rev-parse',args.menagerie_ref+'^{commit}').strip()
    from .network import ensure_menagerie_texts
    ensure_menagerie_texts(m,commit,args.fetch)
    entries=inventory(m,commit,allow_fetch=args.fetch)
    (args.root/'report').mkdir(exist_ok=True)
    (args.root/'report/inventory.json').write_text(json.dumps(public_data(entries, args.root),indent=2)+'\n')
    if args.model!='all' and not any(e['model']==args.model for e in entries):
        parser.error(f'Unknown model {args.model}')
    tolerance=Tolerances(**{name:getattr(args,name) for name in ('mass_relative','mass_absolute','com_absolute','inertia_relative','range_absolute','slide_range_absolute','limit_relative','kinematic_residual','kinematic_axis_angle')},scale=args.tolerance_scale)
    runner=Runner(args.fetch,tolerance)
    path=args.root/'report/results.json'
    results=json.loads(path.read_text()) if path.exists() and (args.model!='all' or args.resume or args.recompare) else []
    if args.recompare and not results:
        parser.error('--recompare requires saved report/results.json')
    completed={r['model'] for r in results}
    failed=False
    for entry in entries:
        if args.model!='all' and entry['model']!=args.model or args.resume and entry['model'] in completed:
            continue
        print(f"Checking {entry['model']}",flush=True)
        if args.recompare:
            from .reanalysis import recheck
            previous=next((r for r in results if r['model']==entry['model']),None)
            if previous is None:parser.error('No saved result for '+entry['model'])
            result=recheck(previous,entry,runner,m,commit)
        else:
            result=runner.check(entry,m,commit)
        results=[r for r in results if r['model']!=entry['model']]+[result]
        write_model(result,h1_annex(json.loads((args.root/'report/acceptance.json').read_text())) if entry['model']=='unitree_h1' else '')
        save(sorted(results,key=lambda r:r['model']))
        failed |= result['status'] in ('error','incomplete','partial history')
        print(f"{entry['model']}: {result['status']} / {result['source']['method']} / {result.get('comparison',{}).get('counts',{})}",flush=True)
    raise SystemExit(2 if failed else 0)
