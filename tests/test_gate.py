from pathlib import Path
import pytest
from drift.gate import compile_snapshot, run
from drift.compare import classify


class MemorySource:
    def __init__(self, xml):
        self.xml = xml

    def read(self, commit, path):
        return self.xml


def robot(mass=1, joint_range="-1 1", quat="1 0 0 0"):
    # Entirely synthetic fixture, not copied from any robot repository.
    return f'''<mujoco><compiler angle="radian"/><worldbody><body name="base">
    <inertial mass="{mass}" pos="0 0 0" diaginertia="0.01 0.02 0.025" quat="{quat}"/>
    <joint name="hinge" type="hinge" range="{joint_range}"/>
    </body></worldbody></mujoco>'''


def compile_synthetic(xml):
    return compile_snapshot(MemorySource(xml), "synthetic", "robot.xml", strip_geometry=True)


def test_compiled_synthetic_change_and_self_comparison():
    m = compile_synthetic(robot())
    s = compile_synthetic(robot())
    h = compile_synthetic(robot(mass=2, joint_range="-2 1"))
    assert m['total_mass']==s['total_mass']
    assert m['bodies']==s['bodies']
    assert m['joints']==s['joints']
    assert classify(m["total_mass"], s["total_mass"], h["total_mass"], "mass") == "STALE"
    assert classify(m["joints"]["hinge"]["range"], s["joints"]["hinge"]["range"], h["joints"]["hinge"]["range"], "range") == "STALE"
    assert classify(m["total_mass"], m["total_mass"], m["total_mass"], "mass") == "unchanged"


def test_principal_moments_ignore_inertial_frame_rotation():
    a = compile_synthetic(robot())
    b = compile_synthetic(robot(quat="0.7071067811865476 0 0 0.7071067811865476"))
    assert a["bodies"]["base"]["principal_moments"] == b["bodies"]["base"]["principal_moments"]


def test_stripping_requires_explicit_inertial_on_every_body():
    with pytest.raises(ValueError, match="Refusing to strip"):
        compile_synthetic('<mujoco><worldbody><body name="missing"><geom type="sphere" size="1"/></body></worldbody></mujoco>')


def test_extension_fragment_is_not_treated_as_a_zero_mass_robot():
    with pytest.raises(ValueError,match='not a standalone source'):
        compile_synthetic('<mujoco><worldbody/></mujoco>')


def test_ball_joint_cone_range_is_compared():
    xml=robot().replace('type="hinge" range="-1 1"','type="ball" range="0 0.5"')
    result=compile_synthetic(xml)
    assert result['joints']['hinge']['range']==[0,0.5]


def test_forced_geometry_inertia_is_never_stripped():
    xml='<mujoco><compiler inertiafromgeom="true"/><worldbody><body name="body"><inertial mass="1" pos="0 0 0" diaginertia="1 1 1"/><geom type="sphere" size="0.1" density="1000"/></body></worldbody></mujoco>'
    result=compile_snapshot(MemorySource(xml),'test','test.xml')
    assert not result['geometry_stripped']
    assert result['total_mass']==pytest.approx(4.188790204786391)


@pytest.mark.integration
def test_real_h1_amended_acceptance():
    root = Path(__file__).resolve().parents[1]
    if not (root / ".cache/unitree_ros/.git").is_dir():
        pytest.skip("Manufacturer Git cache unavailable; no network from tests")
    result = run(root)
    assert result["menagerie"]["snapshot"]["total_mass"] == pytest.approx(51.437)
    assert result["upstream"]["snapshot"]["total_mass"] == pytest.approx(59.338, abs=0.001)
    assert result["menagerie"]["snapshot"]["joints"]["left_hip_pitch"]["range"] == [-1.57, 1.57]
    assert result["upstream"]["snapshot"]["joints"]["left_hip_pitch_joint"]["range"] == [-3.14, 2.53]
    assert not any(c["eligible"] for c in result["source_candidates"])
    assert result["status"] == "passed"
    assert result["source"]["method"] == "none"
    assert result["three_way_total_mass_class"] == "NO MATCHING SOURCE"
    assert len(result["source_candidates"]) == 9
    assert all("snapshot" in c for c in result["source_candidates"])
