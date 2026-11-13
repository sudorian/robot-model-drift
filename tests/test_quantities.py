from drift.gate import compile_snapshot
from drift.engine import compare
from test_gate import MemorySource


def compiled(text):
    return compile_snapshot(MemorySource(text),'synthetic','model.xml')


def test_injected_changes_cover_every_compiled_quantity_family():
    base='''<mujoco><compiler angle="radian"/><worldbody><body name="base">
      <inertial mass="1" pos="0 0 0" diaginertia="0.01 0.02 0.025"/>
      <joint name="hinge" range="-1 1"/>
      <body name="payload" pos="1 0 0"><inertial mass="1" pos="0 0 0" diaginertia="0.01 0.02 0.025"/></body>
      <body name="side" pos="0 1 0"><inertial mass="1" pos="0 0 0" diaginertia="0.01 0.02 0.025"/></body>
      </body></worldbody><actuator><motor name="drive" joint="hinge" ctrlrange="-5 5" gear="2"/></actuator></mujoco>'''
    changed=base.replace('name="payload" pos="1 0 0"><inertial mass="1" pos="0 0 0"','name="payload" pos="1 0 0"><inertial mass="2" pos="0.02 0 0"')
    changed=changed.replace('diaginertia="0.01 0.02 0.025"','diaginertia="0.02 0.03 0.04"')
    changed=changed.replace('range="-1 1"','range="-2 1"').replace('ctrlrange="-5 5"','ctrlrange="-6 6"')
    m,s,h=compiled(base),compiled(base),compiled(changed)
    result=compare(m,s,h,'dated match')
    detected={r['quantity'] for r in result['findings'] if r['class']=='STALE'}
    assert {'total_mass','mass','subtree_mass','com_registered','principal_moments','range','effort','force'}<=detected
    assert m['joints']['hinge']['effort']==10
    assert h['joints']['hinge']['effort']==12


def test_velocity_metadata_changes_are_detected_and_labeled_as_declarations():
    urdf='''<robot name="synthetic"><link name="base"><inertial><mass value="1"/><inertia ixx="1" iyy="1" izz="1" ixy="0" ixz="0" iyz="0"/></inertial></link>
      <link name="tip"><inertial><mass value="1"/><inertia ixx="1" iyy="1" izz="1" ixy="0" ixz="0" iyz="0"/></inertial></link>
      <joint name="hinge" type="revolute"><parent link="base"/><child link="tip"/><limit lower="-1" upper="1" effort="5" velocity="2"/></joint></robot>'''
    m=compiled(urdf);h=compiled(urdf.replace('velocity="2"','velocity="3"'))
    row=next(r for r in compare(m,m,h,'dated match')['findings'] if r['quantity']=='velocity')
    assert row['class']=='STALE'
    assert 'not enforced' in h['limit_semantics']
