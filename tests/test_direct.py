import numpy as np
from drift.direct import physical_xml,extract
from test_gate import robot


def view(path):
    return {'cache':str(path),'repo':'https://github.com/synthetic/test','commit':'test','file':'test.xml'}


def test_direct_eigenvalues_and_com_use_independent_xml_math(monkeypatch,tmp_path):
    xml=robot().replace('pos="0 0 0"','pos="0.1 0.2 0.3"')
    monkeypatch.setattr('drift.direct.GitSource.read',lambda *args:xml)
    bodies,joints=physical_xml(view(tmp_path))
    assert bodies['base']['mass']==1
    assert np.allclose(bodies['base']['com'],[.1,.2,.3])
    assert extract(view(tmp_path),'base','principal_moments')==[.01,.02,.025]
    assert extract(view(tmp_path),'robot','total_mass')==1


def test_direct_full_tensor_sorted_eigenvalues(monkeypatch,tmp_path):
    xml='<robot name="test"><link name="base"><inertial><origin xyz="1 2 3"/><mass value="2"/><inertia ixx="3" iyy="2" izz="1" ixy="0" ixz="0" iyz="0"/></inertial></link></robot>'
    monkeypatch.setattr('drift.direct.GitSource.read',lambda *args:xml)
    assert extract(view(tmp_path),'base','principal_moments')==[1,2,3]
    assert extract(view(tmp_path),'base','com_registered')==[1,2,3]


def test_direct_com_recomputes_kabsch_from_xml_not_cached_transform(monkeypatch,tmp_path):
    from drift.direct import direct_values
    from drift.engine import compare
    from drift.gate import compile_snapshot
    from test_gate import MemorySource
    xml='''<mujoco><worldbody><body name="root"><inertial mass="1" pos="0.01 0.02 0" diaginertia="1 1 1"/>
      <body name="a" pos="1 0 0"><inertial mass="1" pos="0.1 0 0" diaginertia="1 1 1"/></body>
      <body name="b" pos="0 1 0"><inertial mass="1" pos="0 0.1 0" diaginertia="1 1 1"/></body>
      </body></worldbody></mujoco>'''
    rotated=xml.replace('0.01 0.02 0','-0.01 -0.02 0').replace('pos="1 0 0"','pos="-1 0 0"').replace('pos="0 1 0"','pos="0 -1 0"').replace('pos="0.1 0 0"','pos="-0.1 0 0"').replace('pos="0 0.1 0"','pos="0 -0.1 0"')
    m=compile_snapshot(MemorySource(xml),'m','model.xml')
    h=compile_snapshot(MemorySource(rotated),'h','model.xml')
    def v(commit,snapshot):return {'cache':str(tmp_path),'repo':'https://github.com/synthetic/test','commit':commit,'file':'model.xml','snapshot':snapshot}
    result={'menagerie':v('m',m),'source_view':v('m',m),'upstream':v('h',h),'comparison':compare(m,m,h,'dated match')}
    row=next(r for r in result['comparison']['rows'] if r['quantity']=='total_com_registered')
    # A bogus cached rotation must not affect this separate XML computation.
    result['comparison']['kinematics']['M/H']['rotation_other_to_m']=[[0,0,0]]*3
    monkeypatch.setattr('drift.direct.GitSource.read',lambda self,commit,path:xml if commit=='m' else rotated)
    values=direct_values(result,row)
    assert all(np.allclose(values[k],row[k],atol=1e-12) for k in values)


def test_geometry_derived_com_is_unextractable_not_a_zero_origin(monkeypatch,tmp_path):
    import pytest
    xml='<mujoco><worldbody><body name="body"><geom type="sphere" size="0.1" pos="1 0 0"/></body></worldbody></mujoco>'
    monkeypatch.setattr('drift.direct.GitSource.read',lambda *args:xml)
    with pytest.raises(ValueError,match='geometry-derived'):
        extract(view(tmp_path),'body','com_registered')
