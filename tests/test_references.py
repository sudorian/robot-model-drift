from drift.references import matching_name


def test_macro_name_mapping_requires_a_literal_identity():
    assert matching_name('${prefix}${arm_id}_link0','fr3_link0')
    assert not matching_name('${name}','arbitrary_unrelated_body')


def test_parameterized_body_reference_traces_macro_and_yaml(monkeypatch,tmp_path):
    from drift.references import declaration
    from test_loader import Repository
    files={
      'robot.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:include filename="part.xacro"/><xacro:part name="link0" prefix="arm_"/></robot>',
      'part.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:macro name="part" params="name prefix"><link name="${prefix}${name}"><inertial><mass value="2"/><inertia ixx="1" iyy="1" izz="1" ixy="0" ixz="0" iyz="0"/></inertial></link></xacro:macro></robot>',
      'inertials.yaml':'link0:\n  mass: 2\n',
    }
    repository=Repository(files,tmp_path)
    repository.permalink=lambda c,p,n:f'https://github.com/synthetic/test/blob/{c}/{p}#L{n}'
    monkeypatch.setattr('drift.references.GitSource',lambda *a:repository)
    view={'cache':str(tmp_path),'repo':'https://github.com/synthetic/test','commit':'synthetic','file':'robot.xacro','snapshot':{'xacro_arguments':{},'source_dependencies':list(files)}}
    ref=declaration(view,'arm_link0','mass')
    assert 'part.xacro#L1' in ref
    assert 'inertials.yaml#L2' in ref
    assert 'unresolved' not in ref
