from drift.gate import compile_snapshot
from drift.engine import compare
from test_gate import MemorySource


def test_all_three_com_values_use_the_same_registration_anchor():
    xml='<mujoco><worldbody><body name="base"><inertial mass="2" pos="0 0 0" diaginertia="1 1 1"/><body name="arm" pos="1 0 0"><inertial mass="1" pos="0 0 0" diaginertia="1 1 1"/></body></body></worldbody></mujoco>'
    changed=xml.replace('name="base"','name="new_base"').replace('</body></worldbody>','<body name="camera" pos="0.5 0 0"><inertial mass="0.1" pos="0 0 0" diaginertia="0.1 0.1 0.1"/></body></body></worldbody>')
    m=compile_snapshot(MemorySource(xml),'test','model.xml')
    h=compile_snapshot(MemorySource(changed),'test','model.xml')
    result=compare(m,m,h,'dated match')
    row=next(r for r in result['rows'] if r['quantity']=='total_com_registered')
    assert row['m']==row['s']
    assert row['class']=='STALE'
    assert result['mapping_h']['registration_anchor']['M']=='arm'
    assert row['excluded_from_findings']
    assert result['kinematics']['M/H']['status']=='insufficient kinematic coverage'
