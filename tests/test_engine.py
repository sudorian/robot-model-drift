from drift.engine import compare,source_match
from drift.gate import compile_snapshot
from test_gate import MemorySource,robot


def snapshot(xml):
    return compile_snapshot(MemorySource(xml),'test','test.xml',strip_geometry=True)


def test_every_self_quantity_has_zero_findings():
    m=snapshot(robot())
    assert compare(m,m,m,'dated match')['findings']==[]


def test_tree_fallback_matches_renamed_bodies_and_joints():
    a=snapshot(robot())
    b=snapshot(robot().replace('name="base"','name="renamed"').replace('name="hinge"','name="other_joint"'))
    match=source_match(a,b)
    assert match['matches']
    assert match['mapping']['bodies']=={'base':'renamed'}


def test_no_match_reports_delta_without_stale():
    a=snapshot(robot());b=snapshot(robot(mass=2))
    result=compare(a,None,b,'none')
    assert result['findings']
    assert all(r['class']=='NO MATCHING SOURCE' for r in result['findings'])
    assert result['rows'][0]['h_minus_m']==1


def test_proxy_classes_are_always_inferred():
    a=snapshot(robot());b=snapshot(robot(mass=2))
    result=compare(a,a,b,'proxy')
    assert all(row['class'].endswith(' (inferred)') for row in result['rows'])


def test_stripped_visual_texture_does_not_leave_dangling_material():
    xml=robot().replace('<worldbody>','<asset><texture name="t" type="2d" builtin="flat" width="2" height="2"/><material name="m" texture="t"/></asset><worldbody>')
    assert snapshot(xml)['total_mass']==1
