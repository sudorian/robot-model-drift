from drift.engine import source_match
from drift.gate import compile_snapshot
from test_gate import MemorySource


def test_massless_fixed_sensor_frames_do_not_obscure_physical_tree_match():
    mjcf='<mujoco><worldbody><body name="camera"><inertial mass="1" pos="0 0 0" diaginertia="1 1 1"/></body></worldbody></mujoco>'
    urdf='<robot name="camera"><link name="world"/><link name="sensor"><inertial><mass value="1"/><inertia ixx="1" iyy="1" izz="1" ixy="0" ixz="0" iyz="0"/></inertial></link><link name="optical"/><joint name="mount" type="fixed"><parent link="world"/><child link="sensor"/></joint><joint name="frame" type="fixed"><parent link="sensor"/><child link="optical"/></joint></robot>'
    a=compile_snapshot(MemorySource(mjcf),'test','test.xml')
    # No geometry/resources are present, so no stripping is needed for massless frames.
    b=compile_snapshot(MemorySource(urdf),'test','test.urdf',strip_geometry=False)
    result=source_match(a,b)
    assert result['mapping']['bodies']['camera']=='sensor'
    assert result['matches']
