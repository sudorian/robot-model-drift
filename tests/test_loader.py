from pathlib import Path
from drift.loader import expand_xacro,prepare


class Repository:
    def __init__(self,files,directory):
        self.files=files
        self.directory=directory

    def read(self,commit,path):
        return self.files[path]

    def git(self,*args,**kwargs):
        if args[0]=='ls-tree':
            return '\n'.join(self.files)
        if args[0]=='show':
            return self.files[args[1].split(':',1)[1]].encode()
        raise AssertionError(args)


def test_xacro_resolves_local_package_without_rejecting_unused_external_package(tmp_path):
    files={
      'description/package.xml':'<package><name>description</name></package>',
      'description/robot.urdf.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="test"><xacro:include filename="$(find description)/part.xacro"/><xacro:part/></robot>',
      'description/part.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:macro name="part"><link name="body"/></xacro:macro></robot>',
      'description/unused.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:include filename="$(find unavailable_optional_sensor)/sensor.xacro"/></robot>',
    }
    result=expand_xacro(Repository(files,tmp_path),'synthetic','description/robot.urdf.xacro',{})
    assert '<link name="body"' in result


def test_assetdir_applies_to_virtual_resources_and_implicit_mesh_name_is_preserved(tmp_path):
    files={'model.xml':'<mujoco><compiler assetdir="assets"/><asset><mesh file="body.obj"/></asset><worldbody><body name="body"><geom type="mesh" mesh="body"/></body></worldbody></mujoco>',
           'assets/body.obj':'v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n'}
    root,assets,_=prepare(Repository(files,tmp_path),'synthetic','model.xml')
    assert root.find('asset/mesh').get('name')=='body'
    assert len(assets)==1
    assert root.find('asset/mesh').get('file') in assets
    assert root.find('compiler').get('assetdir') is None


def test_macro_only_sensor_records_a_zero_pose_instantiation(tmp_path):
    files={'sensor.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:macro name="sensor" params="parent *origin"><link name="camera"/><joint name="mount" type="fixed"><parent link="${parent}"/><child link="camera"/><xacro:insert_block name="origin"/></joint></xacro:macro></robot>'}
    args={}
    result=expand_xacro(Repository(files,tmp_path),'test','sensor.xacro',args)
    assert '<link name="camera"' in result
    assert args['__macro_instance__']=='sensor'


def test_old_private_xacro_property_is_renamed_without_changing_the_value(tmp_path):
    files={'robot.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:property name="__mass" value="2"/><link name="base"><inertial><mass value="${__mass}"/></inertial></link></robot>'}
    args={}
    result=expand_xacro(Repository(files,tmp_path),'test','robot.xacro',args)
    assert '<mass value="2"' in result
    assert '__compatibility_property_renames__' in args


def test_old_ros_package_directory_without_package_xml_resolves_locally(tmp_path):
    files={
        'legacy/manifest.xml':'<package><description>old ROS package</description></package>',
        'legacy/model.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:include filename="$(find legacy)/part.xacro"/><xacro:part/></robot>',
        'legacy/part.xacro':'<robot xmlns:xacro="http://www.ros.org/wiki/xacro"><xacro:macro name="part"><link name="body"/></xacro:macro></robot>',
    }
    args={}
    assert '<link name="body"' in expand_xacro(Repository(files,tmp_path),'test','legacy/model.xacro',args)
    assert '__package_directory_fallbacks__' in args
