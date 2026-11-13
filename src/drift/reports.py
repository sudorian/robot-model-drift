"""Reviewable Markdown reports with exact-revision source references."""
from collections import Counter
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import yaml
from .sources import GitSource
from .network import ROOT
from .publication import public_data,public_text

_sources = {}


def number(value):
    if value is None:
        return "unavailable"
    if isinstance(value, list):
        return "[" + ", ".join(number(v) for v in value) + "]"
    return f"{value:.9g}" if isinstance(value,(int,float)) else str(value)


def reference(view,entity,quantity,source_entity=None):
    from .references import declaration
    return declaration(view,entity,quantity,source_entity)


def h1_annex(result):
    m = result["menagerie"]["snapshot"]
    lines = ["## H1 nine-revision acceptance", "",
             'The Menagerie README states:', '',
             '> The original URDF and assets were provided directly by [Unitree Robotics](https://www.unitree.com/) under a BSD-3-Clause License.', '',
             '[README, exact revision and lines](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/README.md#L13). The quote joins wrapped source lines; the linked README preserves the original Markdown.', '',
             "Menagerie release: **2023-11-06**. Earliest public H1 revision: **2023-12-07**. Every compiled candidate fails the match criteria; no proxy is selected. In particular, Menagerie ankle masses are 0.446 kg, while the earliest source has 0.552448 kg and the closest later source has 0.474 kg. A total mass within tolerance does not establish a body-level match.", '',
             "All differences below are **upstream revision minus Menagerie**. Masses are compiled with MuJoCo, including inferred sensor mass. Both leg subtrees are rooted at their hip-yaw body. Joint ranges show lower/upper endpoint differences in radians.", '',
             "| Revision/date | Total kg (Δ) | Left leg kg (Δ) | Right leg kg (Δ) | Left hip-pitch range (Δ rad) | Right hip-pitch range (Δ rad) | Match? |",
             "|---|---:|---:|---:|---|---|---|"]
    for c in sorted(result["source_candidates"],key=lambda c:int(c["timestamp"])):
        s = c.get("snapshot")
        if not s:
            lines.append(f"| {c['commit'][:7]} / {c['date'][:10]} | ERROR | ERROR | ERROR | ERROR | ERROR | unavailable |")
            continue
        mass = lambda field,name=None: s["total_mass"] if field == "total" else s["bodies"][name]["subtree_mass"]
        columns = []
        for key,name in (("total",None),("subtree","left_hip_yaw_link"),("subtree","right_hip_yaw_link")):
            value = mass(key,name); mv=m["total_mass"] if name is None else m["bodies"][name]["subtree_mass"]
            columns.append(f"{value:.9f} ({value-mv:+.9f})")
        for side in ("left","right"):
            sj=s["joints"][side+"_hip_pitch_joint"]["range"];mj=m["joints"][side+"_hip_pitch"]["range"]
            columns.append(f"{number(sj)} ({number([sj[i]-mj[i] for i in range(2)])})")
        link=f"{result['upstream']['repo']}/blob/{c['commit']}/{result['upstream']['file']}#L1"
        lines.append(f"| [{c['commit'][:7]}]({link}) / {c['date'][:10]} | "+" | ".join(columns)+f" | {'yes' if c['matches'] else 'no'} ({c.get('mismatch_count','?')} quantities differ) |")
    lines += ["", f"Acceptance: **{result['status']}**; model class **{result['three_way_total_mass_class']}**. No candidate has been silently treated as the source. These discrepancies are excluded from STALE totals.", ""]
    return "\n".join(lines)


def write_model(result, annex=""):
    model = result["model"]
    p = result.get("source",{})
    lines = [f"# {model}", "",f"Status: **{result['status']}**. Provenance: **{p.get('method','unknown')}**, confidence **{p.get('confidence','unknown')}**.", "",
             result.get("reason",""), ""]
    if result.get('xml_fragments'):
        lines += ['XML include fragments (checked through their parent models, not as standalone robots): '+', '.join('`'+p+'`' for p in result['xml_fragments']),'']
    for label,key in (("M","menagerie"),("H","upstream")):
        view=result.get(key)
        if view:
            lines.append(f"{label}: `{view.get('repo')}`, `{view.get('file')}`, commit `{view.get('commit')}`.")
    candidate=p.get("candidate")
    if candidate:
        lines += [f"S: `{candidate['commit']}` ({candidate.get('date')}). Menagerie release/change: {result.get('menagerie',{}).get('origin',{}).get('date','unknown')}."]
    else:
        lines += ["S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE."]
    lines += ['', 'Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.', '']
    if result.get('source_evidence'):
        lines += ['', '## Source evidence', '', '```json',json.dumps(result['source_evidence'],indent=2),'```','']
    if result.get('derivation_evidence'):
        lines += ['', '## README derivation evidence', '',
                  'Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.', '']
        lines += ['> '+line for line in result['derivation_evidence']]
    comp=result.get("comparison")
    if comp:
        def row_sources(row):
            sources=row.get('source_references') or [reference(result.get('menagerie'),row['entity'],row['quantity']),
                reference(result.get('source_view'),row['entity'],row['quantity'],row.get('source_entity')),
                reference(result.get('upstream'),row['entity'],row['quantity'],row.get('other_entity'))]
            row['source_references']=sources
            return sources
        if comp.get('kinematics'):
            lines += ['', '## Kinematics consistency', '',
                      'A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.', '',
                      '| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |',
                      '|---|---|---:|---:|---:|']
            for label,k in comp['kinematics'].items():
                mm=lambda value:number(value*1000) if value is not None else 'unavailable'
                lines.append(f"| {label} | {k['status']} | {k['matched_body_origins']} / {k['fit_rank']} | {mm(k['rms_residual_m'])} / {mm(k['max_residual_m'])} | {len(k['axis_disagreements'])} / {len(k['axis_checks'])} |")
            lines += ['', 'Exact fitted transforms, per-origin residuals, thresholds and axis vectors:', '', '```json',json.dumps(comp['kinematics'],indent=2),'```','']
        lines += ["", "## Every reported quantity difference", "", "Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.", "",
                  "| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |", "|---|---|---|---|---|---|---|---|---|"]
        for row in comp["findings"]:
            sources=row_sources(row)
            lines.append(f"| {row['entity']} / {row['quantity']} | {number(row['m'])} | {number(row['s'])} | {number(row['h'])} | {number(row['h_minus_m'])} | {row['class']} | "+" | ".join(sources)+" |")
        if not comp["findings"]:
            lines.append("No differences exceeded the configured tolerances among the compared quantities.")
        com_rows=[r for r in comp['rows'] if 'raw_values' in r]
        if com_rows:
            lines += ['', '## Raw CoM records and reporting decisions', '',
                      'Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.', '',
                      '| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |',
                      '|---|---|---|---|---|---|---|---|---|']
            for row in com_rows:
                import numpy as np
                raw=row['raw_values'];delta=(np.asarray(raw['h'])-np.asarray(raw['m'])).tolist()
                decision=row.get('exclusion_reason','eligible; compared after Kabsch alignment')
                lines.append(f"| {row['entity']} / {row['quantity']} | {number(raw['m'])} | {number(raw['s'])} | {number(raw['h'])} | {number(delta)} | {decision} | "+' | '.join(row_sources(row))+' |')
        lines += ['', '## Mass accounting', '',
                  'Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.', '',
                  '| M body | M kg / source | S kg / source | H kg / source |','|---|---|---|---|']
        ms=result['menagerie']['snapshot'];hs=result['upstream']['snapshot'];ss=result.get('source_view',{}).get('snapshot')
        cached_mass=result.setdefault('mass_source_references',{})
        for name,body in ms['bodies'].items():
            hn=comp['mapping_h']['bodies'].get(name);sn=comp['mapping_s']['bodies'].get(name) if comp['mapping_s'] else None
            refs=cached_mass.get(name) or [reference(result['menagerie'],name,'mass'),reference(result.get('source_view'),name,'mass',sn) if ss and sn else 'unavailable',reference(result['upstream'],name,'mass',hn) if hn else 'unmatched']
            cached_mass[name]=refs
            columns=[number(body['mass'])+' / '+refs[0]]
            columns.append(number(ss['bodies'][sn]['mass'])+' / '+refs[1] if ss and sn else 'unavailable')
            columns.append(number(hs['bodies'][hn]['mass'])+' / '+refs[2] if hn else 'unmatched')
            lines.append('| '+name+' | '+' | '.join(columns)+' |')
        for hn in comp['mapping_h']['unmatched_upstream_bodies']:
            key='upstream-only '+hn
            ref=cached_mass.get(key) or reference(result['upstream'],hn,'mass')
            cached_mass[key]=ref
            lines.append('| '+key+' | unavailable | unavailable | '+number(hs['bodies'][hn]['mass'])+' / '+ref+' |')
        lines += ["", "## Coverage and unmatched elements", "", "```json", json.dumps({"mapping_h":comp['mapping_h'],"mapping_s":comp['mapping_s'],"unavailable":comp['unavailable']},indent=2), "```", ""]
        limits=[r for r in comp['unavailable'] if r['quantity'] in ('effort','force','velocity')]
        if limits:
            lines += ['## Limits unavailable for a like-for-like simulator comparison','',
                      'URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.', '',
                      '| Joint / quantity | M | S | H / declared upstream |','|---|---|---|---|']
            for r in limits:
                lines.append(f"| {r['entity']} / {r['quantity']} | {number(r['m'])} | {number(r['s'])} | {number(r['other'])} |")
    for key in ("tolerances","candidate_errors","history_inputs","construction_recipe","self_comparisons","sensitivity","compilation","rerun"):
        if key in result:
            lines += [f"## {key.replace('_',' ').capitalize()}", "", "```json", json.dumps(result[key],indent=2), "```", ""]
    if annex:
        lines += [annex]
    (ROOT/"report"/f"{model}.md").write_text(public_text("\n".join(lines).rstrip()+"\n", ROOT))
    write_provenance(result)


def write_provenance(result):
    source=result.get('source',{})
    candidate=source.get('candidate')
    upstream=result.get('upstream',{})
    menagerie=result.get('menagerie',{})
    def compact(c):
        return {k:v for k,v in c.items() if k not in ('snapshot','mapping','mismatches')}
    output={'model':result['model'],'method':source.get('method','unknown'),'confidence':source.get('confidence','unknown'),
            'upstream_repo':upstream.get('repo'),'upstream_file':candidate.get('file',upstream.get('file')) if candidate else upstream.get('file'),
            'upstream_commit':candidate.get('commit') if candidate else None,'latest_upstream_commit':upstream.get('commit'),
            'menagerie_repo':menagerie.get('repo'),'menagerie_file':menagerie.get('file'),'menagerie_commit':menagerie.get('commit'),
            'menagerie_change':menagerie.get('origin'),'menagerie_commits_involved':menagerie.get('commits_involved',[]),
            'source_candidate':compact(candidate) if candidate else None,
            'source_candidates':[compact(c) for c in result.get('source_candidates',[])],
            'evidence':result.get('source_evidence',[]),'reason':result.get('reason'),
            'compilation':result.get('compilation',{})}
    (ROOT/'provenance'/f"{result['model']}.yaml").write_text(yaml.safe_dump(public_data(output, ROOT),sort_keys=False))


def write_summary(results):
    totals=Counter()
    for r in results:
        totals.update(r.get("comparison",{}).get("counts",{}))
    stale_models=[r['model'] for r in results if any(row['class'].removesuffix(' (inferred)')=='STALE' for row in r.get('comparison',{}).get('findings',[]))]
    stale_rows=[row for r in results for row in r.get('comparison',{}).get('findings',[]) if row['class'].removesuffix(' (inferred)')=='STALE']
    statuses=Counter(r['status'] for r in results)
    convention_models=[r['model'] for r in results if any(k['status']=='kinematic convention differs' for k in r.get('comparison',{}).get('kinematics',{}).values())]
    insufficient_models=[r['model'] for r in results if any(k['status']=='insufficient kinematic coverage' for k in r.get('comparison',{}).get('kinematics',{}).values())]
    excluded=sum(len(r.get('comparison',{}).get('excluded_findings',[])) for r in results)
    lines=["# Robot model drift survey", "", "All values and errors below are measured results from this run. Unknown or failed coverage is listed explicitly. Proxy classes carry `(inferred)`; `NO MATCHING SOURCE` never contributes to STALE counts.", "",
           f"**{len(stale_rows)} STALE quantity records across {len(stale_models)} models:** "+', '.join('`'+m+'`' for m in stale_models)+'. '+f"{sum(row['quantity'] in ('effort','force','velocity') for row in stale_rows)} of these are limit-declaration/envelope comparisons; see the limit semantics below.",'',
           f"Coverage: {sum(bool(r.get('comparison')) for r in results)}/{len(results)} folders have compiled M/H comparisons; "+json.dumps(dict(statuses))+'. Body/joint coverage within each comparison is specified by its unmatched lists.','',
           f"Kinematics guard: **{excluded} raw CoM differences excluded** from counts and largest discrepancies. Convention differs in {len(convention_models)} models; insufficient unique-fit coverage in {len(insufficient_models)}. Raw numbers, residuals, fitted transforms and axis comparisons remain in each model report. Mass and principal-moment records are retained. Joint ranges remain raw and are marked for convention review when flagged.",'',
           '“Upstream changed?” compares S with H when S compiled, otherwise the earliest successfully compiled public revision with H. It concerns the compared physical quantities, not merely different Git SHAs. It does not assert that every intermediate revision was unchanged.','',
           "| Model | Provenance / confidence | Upstream changed? | Class counts | Largest discrepancy | Kinematics / CoM exclusion | Status |", "|---|---|---|---|---|---|---|"]
    for r in results:
        p=r.get('source',{});c=r.get('comparison',{});rows=c.get('findings',[])
        largest=None
        if rows:
            row=max(rows,key=lambda row:row.get('tolerance_multiple',0))
            largest=f"{row['entity']} {row['quantity']}: Δ {number(row['h_minus_m'])}; {number(row.get('tolerance_multiple'))}× tolerance"
        checks=c.get('kinematics',{})
        labels='; '.join(label+': '+k['status'] for label,k in checks.items()) or 'unavailable'
        labels+=f"; {len(c.get('excluded_findings',[]))} raw CoM differences excluded" if checks else ''
        lines.append(f"| [{r['model']}]({r['model']}.md) | {p.get('method','unknown')} / {p.get('confidence','unknown')} | {r.get('upstream_changed','unknown')} | {json.dumps(c.get('counts',{}))} | {largest or 'unavailable / no discrepancy'} | {labels} | {r['status']} |")
    lines += ["", "## Counts", "", "```json",json.dumps(dict(totals),indent=2),"```", "",f"Models listed: {len(results)}. Machine-readable detailed results: `report/results.json`.", "",
              "Eligible CoM values use a best-fit proper rigid alignment of matched body origins at zero pose. A maximum per-origin residual exceeding the configured 5 mm default, or a matched signed axis disagreement above the 0.005 rad default, is marked kinematic convention differs. RMS residual is also recorded. Underdetermined fits are marked insufficient kinematic coverage. Both exclude CoM from counts and largest discrepancies; raw coordinates and transforms remain available. Joint effort/velocity declarations from URDF are metadata: MuJoCo does not enforce those tags. MJCF force/effort values are reported only for supported direct scalar actuators. Missing limits are coverage gaps, never zero limits.", ""]
    lines += ['## Tolerance sensitivity','', 'Physical relative and absolute thresholds are multiplied together. The configurable kinematic quality thresholds remain fixed. Matching and provenance are reselected at each scale; counts exclude gated CoM records and apply only to models with a compiled comparison.', '', '| Scale | Models evaluated | Changed quantity classifications | Findings added/removed | Total finding records |', '|---|---:|---:|---:|---:|']
    for scale in ('0.5','2'):
        values=[r['sensitivity'][scale] for r in results if scale in r.get('sensitivity',{})]
        lines.append(f"| {scale} | {len(values)} | {sum(v['classifications_changed'] for v in values)} | {sum(v['finding_membership_changes'] for v in values)} | {sum(sum(v['counts'].values()) for v in values)} |")
    (ROOT/"report/summary.md").write_text(public_text("\n".join(lines).rstrip()+"\n", ROOT))
