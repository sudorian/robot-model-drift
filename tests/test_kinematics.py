import copy
import dataclasses
import numpy as np
import pytest
from drift.compare import Tolerances
from drift.engine import compare
from drift.kinematics import check
from drift.gate import compile_snapshot
from test_gate import MemorySource


def cloud(joints=False):
    joint='<joint name="hinge" range="-1 1"/>' if joints else ''
    xml=f'''<mujoco><compiler angle="radian"/><worldbody><body name="base">
      <inertial mass="1" pos="0.01 0.02 0" diaginertia="1 1 1"/>
      <body name="a" pos="1 0 0"><inertial mass="1" pos="0.1 0 0" diaginertia="1 1 1"/>{joint}</body>
      <body name="b" pos="0 1 0"><inertial mass="1" pos="0 0.1 0" diaginertia="1 1 1"/></body>
      </body></worldbody></mujoco>'''
    return copy.deepcopy(compile_snapshot(MemorySource(xml),'synthetic','cloud.xml'))


def test_best_fit_removes_a_rigid_frame_convention_and_preserves_raw_values():
    m=cloud(joints=True);h=copy.deepcopy(m)
    rotation=np.array([[1.,0,0],[0,0,-1.],[0,1.,0]]);translation=np.array([2.,-3.,.5])
    for body in h['bodies'].values():
        for key in ('position_registered','com_registered'):
            body[key]=(rotation@body[key]+translation).tolist()
    h['total_com_registered']=(rotation@h['total_com_registered']+translation).tolist()
    for name in h['joint_axes_registered']:
        h['joint_axes_registered'][name]=(rotation@h['joint_axes_registered'][name]).tolist()
        h['joints'][name]['axis']=(rotation@h['joints'][name]['axis']).tolist()
    result=compare(m,m,h,'dated match')
    k=result['kinematics']['M/H']
    assert k['status']=='consistent'
    assert k['rms_residual_m']<1e-12
    assert np.linalg.det(k['rotation_other_to_m'])==pytest.approx(1)
    assert result['findings']==[]
    row=next(row for row in result['rows'] if row['quantity']=='total_com_registered')
    assert not np.allclose(row['raw_values']['m'],row['raw_values']['h'])
    assert np.allclose(row['m'],row['h'])


def test_nonrigid_origins_exclude_only_com_and_keep_mass_and_inertia_findings():
    m=cloud();h=copy.deepcopy(m)
    h['bodies']['a']['position_registered'][0]+=.1
    h['bodies']['a']['com_registered'][0]+=.1
    h['bodies']['a']['mass']=2
    h['bodies']['a']['principal_moments']=[2,2,2]
    result=compare(m,m,h,'dated match')
    assert result['kinematics']['M/H']['status']=='kinematic convention differs'
    assert result['excluded_findings']
    assert all(row['quantity'] not in ('com_registered','total_com_registered') for row in result['findings'])
    assert {'mass','principal_moments'} <= {row['quantity'] for row in result['findings']}
    assert all(row['class']=='STALE' for row in result['findings'])
    assert any(row['raw_values']['h']!=row['raw_values']['m'] for row in result['excluded_findings'])
    relaxed=compare(m,m,h,'dated match',dataclasses.replace(Tolerances(),kinematic_residual=.1))
    assert relaxed['kinematics']['M/H']['status']=='consistent'


def test_signed_axis_disagreement_is_detected_even_with_zero_origin_residual():
    m=cloud(joints=True);h=copy.deepcopy(m)
    h['joints']['hinge']['axis']=[0,0,-1]
    h['joint_axes_registered']['hinge']=[0,0,-1]
    h['joints']['hinge']['range']=[-1,1+np.pi]
    h['bodies']['a']['com_registered'][0]+=.02
    result=compare(m,m,h,'dated match')
    k=result['kinematics']['M/H']
    assert k['rms_residual_m']<1e-12
    assert k['status']=='kinematic convention differs'
    assert k['axis_disagreements'][0]['angle_rad']==pytest.approx(np.pi)
    assert any(row['quantity']=='range' for row in result['findings'])
    assert all(row['quantity']!='com_registered' for row in result['findings'])


def test_one_point_or_collinear_origins_cannot_certify_com_alignment():
    m=cloud();h=copy.deepcopy(m)
    for snapshot in (m,h):
        snapshot['bodies']['b']['position_registered']=[2,0,0]
    result=compare(m,m,h,'dated match')
    assert result['kinematics']['M/H']['status']=='insufficient kinematic coverage'
    assert result['kinematics']['M/H']['fit_rank']==1
    assert result['kinematics']['M/H']['axis_disagreements']==[]
    assert result['findings']==[]
    assert all(row['excluded_from_findings'] for row in result['rows'] if 'raw_values' in row)


def test_invalid_source_alignment_also_excludes_three_way_com():
    m=cloud();s=copy.deepcopy(m)
    s['bodies']['a']['position_registered'][0]+=.1
    result=compare(m,s,m,'pinned')
    assert result['kinematics']['M/H']['status']=='consistent'
    assert result['kinematics']['M/S']['status']=='kinematic convention differs'
    assert all(row['excluded_from_findings'] for row in result['rows'] if 'raw_values' in row)


def test_reflections_are_rejected_as_rigid_alignment():
    m=cloud();m['bodies']['c']=copy.deepcopy(m['bodies']['a'])
    m['bodies']['c']['position_registered']=[0,0,1]
    h=copy.deepcopy(m)
    for body in h['bodies'].values():body['position_registered'][0]*=-1
    result=compare(m,m,h,'dated match')
    k=result['kinematics']['M/H']
    assert k['fit_rank']==3
    assert np.linalg.det(k['rotation_other_to_m'])==pytest.approx(1)
    assert k['status']=='kinematic convention differs'


def test_large_residual_is_flagged_even_when_the_rotation_is_underdetermined():
    m=cloud();h=copy.deepcopy(m)
    m['bodies']['b']['position_registered']=[2,0,0]
    h['bodies']['b']['position_registered']=[3,0,0]
    result=compare(m,m,h,'dated match')
    k=result['kinematics']['M/H']
    assert k['fit_rank']==1
    assert k['rms_residual_m']>.005
    assert k['status']=='kinematic convention differs'


def test_maximum_residual_guards_outliers_that_rms_alone_would_accept():
    m=cloud();h=copy.deepcopy(m)
    h['bodies']['a']['position_registered'][0]+=.02
    diagnostic=compare(m,m,h,'dated match')['kinematics']['M/H']
    threshold=(diagnostic['rms_residual_m']+diagnostic['max_residual_m'])/2
    result=compare(m,m,h,'dated match',dataclasses.replace(Tolerances(),kinematic_residual=threshold))
    assert result['kinematics']['M/H']['rms_residual_m']<threshold
    assert result['kinematics']['M/H']['status']=='kinematic convention differs'


def test_axis_check_uses_simulator_axes_for_multiple_joints_with_nonzero_refs():
    xml='''<mujoco><compiler angle="radian"/><worldbody><body name="root"><inertial mass="1" pos="0 0 0" diaginertia="1 1 1"/>
      <body name="a" pos="1 0 0"><inertial mass="1" pos="0 0 0" diaginertia="1 1 1"/>
      <joint name="first" axis="1 0 0" ref="0.3"/><joint name="second" axis="0 1 0" ref="0.4"/></body>
      <body name="b" pos="0 1 0"><inertial mass="1" pos="0 0 0" diaginertia="1 1 1"/></body>
      </body></worldbody></mujoco>'''
    m=compile_snapshot(MemorySource(xml),'test','multi.xml')
    naive=np.asarray(m['bodies']['a']['rotation_registered'])@m['joints']['first']['axis']
    actual=m['joint_axes_registered']['first']
    assert not np.allclose(naive,actual)
    result=compare(m,m,m,'dated match')
    axis=next(a for a in result['kinematics']['M/H']['axis_checks'] if a['joint_m']=='first')
    assert np.allclose(axis['axis_m'],actual)
    assert axis['axis_source_m']=='MuJoCo xaxis at zero pose'
    assert result['kinematics']['M/H']['status']=='consistent'
