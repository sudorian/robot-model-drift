"""Compile source XML without changing its physical quantities.

Git blobs remain in ignored clones; xacro temporarily materializes text under the
clone. Resource paths are resolved only inside that exact repository revision.
"""
from pathlib import Path, PurePosixPath
import io
import os
import re
import shutil
import tempfile
import xml.etree.ElementTree as ET
from collections import OrderedDict
import hashlib

_converted_meshes=OrderedDict()
_converted_bytes=0


def normalized(path):
    return os.path.normpath(path).replace(os.sep, "/")


def files_at(source, commit):
    key = (commit, "files")
    cache = getattr(source, "_tree_cache", {})
    if key not in cache:
        cache[key] = source.git("ls-tree", "-r", "--name-only", commit).splitlines()
        source._tree_cache = cache
    return cache[key]


def resolve(source, commit, filename, base="", meshdir="", staging=None):
    files = files_at(source, commit)
    if filename.startswith('file://'):
        filename=filename[len('file://'):]
    if staging and filename.startswith(str(staging)):
        filename = str(Path(filename).relative_to(staging))
        if filename in files:
            return filename
    if filename.startswith("package://"):
        remainder = filename[len("package://"):]
        matches = [p for p in files if p == remainder or p.endswith("/" + remainder)]
        if not matches:
            package, relative = remainder.split("/", 1)
            for p in files:
                if p.endswith("/package.xml") or p == "package.xml":
                    try:
                        if ET.fromstring(source.read(commit, p)).findtext("name") == package:
                            candidate = normalized(str(PurePosixPath(p).parent / relative))
                            if candidate in files:
                                matches.append(candidate)
                    except ET.ParseError:
                        pass
        if len(matches) == 1:
            return matches[0]
        raise ValueError(f"Unresolved or ambiguous package path {filename}: {matches}")
    candidate = normalized(str(PurePosixPath(base).parent / meshdir / filename))
    if candidate in files:
        return candidate
    if filename in files:
        return filename
    raise ValueError(f"Resource missing at {commit}: {candidate}")


def expand_xacro(source, commit, path, arguments,return_dependencies=False,source_markers=False):
    import xacro
    files = files_at(source, commit)
    parent = source.directory / ".drift_xacro"
    parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=parent) as temporary:
        staging = Path(temporary)
        texts = {}
        for p in files:
            if p.endswith((".xacro", ".urdf", ".xml", ".yaml", ".yml", ".csv", ".srdf")):
                texts[p] = source.read(commit, p)
        packages = {}
        for p, text in texts.items():
            if p.endswith("package.xml"):
                try:
                    name = ET.fromstring(text).findtext("name")
                    packages[name] = str(staging / PurePosixPath(p).parent)
                except ET.ParseError:
                    pass
        # Early ROS repositories can use manifest.xml, or a package directory
        # without package.xml. Accept an exact unique directory name in this
        # repository; never search another repository or the host ROS install.
        fallback_packages={}
        def package_directory(name):
            if name not in packages:
                choices={str(parent) for filename in files for parent in PurePosixPath(filename).parents if parent.name==name}
                if len(choices)==1:
                    relative=next(iter(choices))
                    packages[name]=str(staging/relative)
                    fallback_packages[name]=relative
            return packages.get(name,str(staging/'.unresolved_package'/name))
        for p, text in texts.items():
            if source_markers and p.endswith(('.xml','.urdf','.xacro')):
                # A separate, never-compiled expansion carries declaration
                # locations through parameterized macros for report links.
                from lxml import etree
                try:
                    document=etree.fromstring(text.encode(),etree.XMLParser(resolve_entities=False,no_network=True))
                    for node in list(document.iter()):
                        if node.tag not in ('body','link','joint','inertial','mass','inertia','origin','limit','geom'):
                            continue
                        marker=etree.Element('drift_source',file=p,line=str(node.sourceline or 1))
                        node.insert(0,marker)
                    text=etree.tostring(document,encoding='unicode')
                except etree.XMLSyntaxError:
                    pass
            def find_package(match):
                name = match.group(1)
                return package_directory(name)
            text = re.sub(r"\$\(find\s+([^)\s]+)\)", find_package, text)
            def package_uri(match):
                package,relative=match.group(1),match.group(2)
                directory=package_directory(package)
                return str(Path(directory)/relative)
            text=re.sub(r'package://([\w-]+)/([^\s"\'<>]+)',package_uri,text)
            target = staging / p
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        if fallback_packages:
            arguments['__package_directory_fallbacks__']=str(fallback_packages)
        # Older xacro sources used private property names now rejected by xacro.
        # Alpha-renaming declared symbols and their references changes syntax only.
        private=set()
        for text in texts.values():
            private.update(re.findall(r'<xacro:property\b[^>]*\bname=["\'](__\w+)["\']',text))
        renames={name:'drift_internal_'+name[2:] for name in sorted(private)}
        if renames:
            for p in texts:
                target=staging/p
                changed=target.read_text()
                for old,new in renames.items():changed=re.sub(r'\b'+re.escape(old)+r'\b',new,changed)
                target.write_text(changed)
            arguments['__compatibility_property_renames__']=str(renames)
        xacro.all_includes=[]
        for name,value in list(arguments.items()):
            if isinstance(value,str) and value in files:
                arguments[name]=str(staging/value)
        main_root=ET.fromstring(texts[path])
        macros=[n for n in main_root if n.tag.endswith('}macro')]
        macro_names={n.get('name') for n in macros}
        def has_call(node):
            if node.tag.endswith('}macro'):
                return False
            local=node.tag.split('}')[-1]
            return local in macro_names or any(has_call(c) for c in node)
        input_path=staging/path
        if macros and not main_root.findall('link') and not has_call(main_root):
            stem=PurePosixPath(path).name
            for suffix in ('.xacro','.urdf'):
                if stem.endswith(suffix):stem=stem[:-len(suffix)]
            stem=stem.lstrip('_')
            matching=[n for n in macros if stem in n.get('name','')]
            macro=matching[0] if len(matching)==1 else (macros[0] if len(macros)==1 else None)
            if macro is None:
                raise ValueError('Macro-only input has no uniquely identified robot macro')
            params=macro.get('params','').split()
            required=[p for p in params if ':=' not in p and '=' not in p]
            unsupported=[p for p in required if p not in ('parent','prefix','name','*origin')]
            if unsupported:
                raise ValueError(f'Macro {macro.get("name")} requires unsupported explicit arguments: {unsupported}')
            namespace='http://www.ros.org/wiki/xacro'
            wrapper=ET.Element('robot',{'name':'drift_macro_instance','xmlns:xacro':namespace})
            ET.SubElement(wrapper,'link',{'name':'__drift_world'})
            ET.SubElement(wrapper,'xacro:include',{'filename':str(staging/path)})
            values={p:('__drift_world' if p=='parent' else '' if p=='prefix' else stem) for p in required if not p.startswith('*')}
            call=ET.SubElement(wrapper,'xacro:'+macro.get('name'),values)
            if '*origin' in required:
                ET.SubElement(call,'origin',{'xyz':'0 0 0','rpy':'0 0 0'})
            arguments['__macro_instance__']=macro.get('name')
            arguments['__macro_parameters__']=str(values)
            arguments['__macro_origin__']='xyz=0 0 0 rpy=0 0 0'
            input_path=staging/'.drift_macro_instance.urdf.xacro'
            input_path.write_text(ET.tostring(wrapper,encoding='unicode'))
        document = xacro.process_file(str(input_path), mappings=arguments)
        expanded = document.toxml().replace(str(staging) + "/", "")
        for name,value in list(arguments.items()):
            if isinstance(value,str):arguments[name]=value.replace(str(staging)+'/', '')
        dependencies=[path]+[str(Path(p).relative_to(staging)) for p in xacro.all_includes if str(p).startswith(str(staging)+'/') and str(Path(p).relative_to(staging)) in files]
    return (expanded,sorted(set(dependencies))) if return_dependencies else expanded


def expand_includes(source, commit, path, stack=(),origins=None,main_path=None):
    if path in stack:
        raise ValueError(f"Include cycle: {stack} -> {path}")
    root = ET.fromstring(source.read(commit, path))
    main_path=main_path or path
    if origins is not None:
        for node in root.iter():origins[id(node)]=path
    for parent in list(root.iter()):
        for child in list(parent):
            if child.tag == "include":
                target = normalized(str(PurePosixPath(path).parent / child.attrib["file"]))
                known=files_at(source,commit)
                if target not in known:
                    root_relative=normalized(str(PurePosixPath(main_path).parent/child.attrib['file']))
                    if root_relative in known:
                        target=root_relative
                included = expand_includes(source, commit, target, (*stack, path),origins,main_path)
                index = list(parent).index(child)
                parent.remove(child)
                for offset, node in enumerate(list(included)):
                    parent.insert(index + offset, node)
    return root


def dae_to_obj(blob):
    global _converted_bytes
    key=hashlib.sha256(blob).digest()
    if key in _converted_meshes:
        _converted_meshes.move_to_end(key)
        return _converted_meshes[key]
    import trimesh
    mesh = trimesh.load(io.BytesIO(blob), file_type="dae", force="scene", process=False)
    # dump concatenates scene transforms rather than discarding them.
    geometry = mesh.to_geometry()
    result=trimesh.exchange.obj.export_obj(geometry, include_texture=False).encode()
    if len(result)<64*1024**2:
        while _converted_meshes and _converted_bytes+len(result)>128*1024**2:
            _,old=_converted_meshes.popitem(last=False);_converted_bytes-=len(old)
        _converted_meshes[key]=result;_converted_bytes+=len(result)
    return result


def prepare(source, commit, path, strip_geometry=None, arguments=None):
    arguments = dict(arguments or {})
    text = source.read(commit, path)
    xacro_used = path.endswith(".xacro") or "xacro:" in text
    origins={}
    if xacro_used:
        text,dependencies = expand_xacro(source, commit, path, arguments,return_dependencies=True)
        root = ET.fromstring(text)
    else:
        root = expand_includes(source, commit, path,origins=origins)
        dependencies=sorted(set(origins.values())) or [path]
    urdf = root.tag == "robot"
    extension = root.find("mujoco") if urdf else root
    if extension is None:
        extension = ET.SubElement(root, "mujoco")
    compiler = extension.find("compiler")
    if compiler is None:
        compiler = ET.SubElement(extension, "compiler")
    assetdir=compiler.get("assetdir", "")
    meshdir, texturedir = compiler.get("meshdir", assetdir), compiler.get("texturedir", assetdir)
    compiler.set("fusestatic", "false")
    compiler.set("discardvisual", "false")
    compiler.set("strippath", "false")
    compiler.attrib.pop("meshdir", None)
    compiler.attrib.pop("texturedir", None)
    compiler.attrib.pop("assetdir", None)
    bodies = root.findall("link") if urdf else root.findall("worldbody//body")
    missing = [b.get("name", "<unnamed>") for b in bodies if b.find("inertial") is None]
    if strip_geometry is None:
        strip_geometry = bool(bodies) and not missing and compiler.get('inertiafromgeom')!='true'
    if strip_geometry and missing:
        raise ValueError(f"Refusing to strip geometry: missing explicit inertials on {missing}")
    if strip_geometry and compiler.get('inertiafromgeom')=='true':
        raise ValueError('Refusing to strip geometry when compiler forces geometry-derived inertia')
    assets, conversions = {}, []
    normalizations=[]
    if urdf:
        for visual in root.findall('.//visual'):
            materials=visual.findall('material')
            if len(materials)>1:
                for material in materials[1:]:visual.remove(material)
                normalizations.append('Retained first of duplicate visual material tags; geometry, inertials and joints unchanged')
    if strip_geometry:
        tags = {"visual", "collision"} if urdf else {"geom", "mesh", "texture", "hfield", "skin"}
        for parent in root.iter():
            for child in list(parent):
                if child.tag in tags:
                    parent.remove(child)
                elif child.tag=='pair' and ('geom1' in child.attrib or 'geom2' in child.attrib):
                    parent.remove(child)
                elif child.get('objtype')=='geom':
                    parent.remove(child)
            # Materials may remain referenced by sites/defaults. Their textures are
            # visual resources and were removed together with geometry.
            if parent.tag == "material":
                parent.attrib.pop("texture",None)
    else:
        for i, node in enumerate(root.iter()):
            key = "filename" if node.tag == "mesh" and urdf else "file"
            filename = node.get(key)
            if not filename:
                continue
            if not urdf and node.tag in ("mesh","texture","hfield","skin") and not node.get("name"):
                # MJCF derives an unnamed mesh's name from its source filename.
                # Preserve that name before mapping the file to a virtual asset.
                node.set("name",PurePosixPath(filename).stem)
            directory = texturedir if node.tag == "texture" else meshdir
            try:
                resolved = resolve(source, commit, filename, path, directory)
            except ValueError:
                included_path=origins.get(id(node),path)
                if included_path==path:
                    raise
                resolved=resolve(source,commit,filename,included_path,directory)
            dependencies.append(resolved)
            blob = source.blob(commit,resolved) if hasattr(source,'blob') else source.git("show", f"{commit}:{resolved}", binary=True)
            suffix = PurePosixPath(filename).suffix
            if suffix.lower() == ".dae":
                blob = dae_to_obj(blob)
                suffix = ".obj"
                conversions.append({"file": resolved, "conversion": "COLLADA to OBJ with scene transforms, no textures"})
            asset_name = f"resource_{i}{suffix}"
            assets[asset_name] = blob
            node.set(key, asset_name)
    return root, assets, {"geometry_stripped": strip_geometry, "missing_explicit_inertials": missing,
                          "assets_loaded": len(assets), "mesh_conversions": conversions,
                          "xacro_arguments": arguments, "xacro_expanded": xacro_used,"source_dependencies":dependencies,
                          "nonphysical_normalizations":normalizations}
