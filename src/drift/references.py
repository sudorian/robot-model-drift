"""Locate literal declarations, inherited defaults, and xacro/YAML inputs."""
import re
from pathlib import Path
from lxml import etree
import yaml
from .sources import GitSource

_cache={}
_expanded_cache={}


def expanded_declaration(view,name,quantity):
    """Trace generated identities using a separate annotated xacro expansion."""
    from .loader import expand_xacro
    key=(view['cache'],view['commit'],view['file'])
    if key not in _expanded_cache:
        source=GitSource(view['cache'],view['repo'])
        text=expand_xacro(source,view['commit'],view['file'],dict(view.get('snapshot',{}).get('xacro_arguments',{})),source_markers=True)
        _expanded_cache[key]=etree.fromstring(text.encode(),etree.XMLParser(resolve_entities=False,no_network=True))
    root=_expanded_cache[key]
    tag='joint' if quantity in ('range','effort','force','velocity') else 'link'
    node=next((n for n in root.iter(tag) if n.get('name')==name),None)
    if node is None:return None
    paths={'mass':'inertial/mass','com_registered':'inertial/origin','principal_moments':'inertial/inertia',
           'range':'limit','effort':'limit','force':'limit','velocity':'limit'}
    actual=node.find(paths[quantity]) if quantity in paths else node
    if actual is None:actual=node
    marker=actual.find('drift_source')
    if marker is None:return None
    source=GitSource(view['cache'],view['repo'])
    file=marker.get('file');line=int(marker.get('line'))
    link=f"[macro declaration L{line}]({source.permalink(view['commit'],file,line)})"
    field={'mass':'mass','principal_moments':'inertia','com_registered':'origin'}.get(quantity)
    if field:
        for path in view.get('snapshot',{}).get('source_dependencies',[]):
            if not path.endswith(('.yaml','.yml')):continue
            tree=yaml.compose(source.read(view['commit'],path))
            if not isinstance(tree,yaml.MappingNode):continue
            for k,v in tree.value:
                if not (name==k.value or name.endswith('_'+k.value) or name.endswith('/'+k.value)):
                    continue
                if not isinstance(v,yaml.MappingNode):continue
                value=next((child for key,child in v.value if key.value==field),None)
                if value is not None:
                    n=value.start_mark.line+1
                    link+=f"; [YAML numeric inputs L{n}]({source.permalink(view['commit'],path,n)})"
                    return link
    return link


def documents(view):
    key=(view['cache'],view['commit'],view['file'])
    if key in _cache:return _cache[key]
    source=GitSource(view['cache'],view['repo']);path=view['file']
    files=source.git('ls-tree','-r','--name-only',view['commit']).splitlines()
    dependencies=view.get('snapshot',{}).get('source_dependencies',[])
    preferred=[path]+[p for p in dependencies if p!=path]
    prefix=path.rsplit('/',1)[0]+'/' if '/' in path else ''
    preferred += [p for p in files if p.startswith(prefix) and p.endswith(('.xml','.urdf','.xacro')) and p not in preferred]
    # Macro definitions can reside in sibling package directories.
    if path.endswith('.xacro'):
        preferred += [p for p in files if p.endswith(('.xml','.urdf','.xacro')) and p not in preferred]
    parsed=[]
    parser=etree.XMLParser(resolve_entities=False,no_network=True,recover=False)
    for file in preferred:
        if not file.endswith(('.xml','.urdf','.xacro')):continue
        try:
            text=source.read(view['commit'],file)
            parsed.append((file,text.splitlines(),etree.fromstring(text.encode(),parser)))
        except (etree.XMLSyntaxError,ValueError):
            continue
    result=source,files,parsed,dependencies
    _cache[key]=result
    return result


def attribute_line(node,attribute,lines):
    start=(node.sourceline or 1)-1
    for n in range(start,min(len(lines),start+20)):
        if re.search(r'\b'+re.escape(attribute)+r'\s*=',lines[n]):return n+1
        if '>' in lines[n]:break
    return start+1


def defaults_for(root):
    result={}
    def walk(node,inherited):
        current={key:dict(value) for key,value in inherited.items()}
        for child in node:
            if child.tag=='default':continue
            for attr,value in child.attrib.items():current.setdefault(child.tag,{})[attr]=(value,child,attr)
        result[node.get('class','main')]=current
        for child in node.findall('default'):walk(child,current)
    for node in root.findall('default'):walk(node,{})
    return result


def matching_name(template,name):
    if template==name:return True
    if '${' not in template:return False
    literal=re.sub(r'\$\{[^}]+\}','',template).strip('_-/')
    if len(literal)<2:return False
    pattern=re.escape(template)
    pattern=re.sub(r'\\\$\\\{.*?\\\}',r'.*',pattern)
    return bool(re.fullmatch(pattern,name))


def declaration(view,entity,quantity,source_entity=None):
    if not view or not view.get('commit') or not view.get('file'):return 'unavailable'
    name=source_entity or entity
    try:source,files,docs,dependencies=documents(view)
    except Exception:
        return f"[unresolved input]({view['repo']}/blob/{view['commit']}/{view['file']}#L1)"
    if entity=='robot':
        return f"[aggregate inputs]({source.permalink(view['commit'],view['file'],1)})"
    for file,lines,root in docs:
        def bound(template):
            arguments=view.get('snapshot',{}).get('xacro_arguments',{})
            return re.sub(r'\$\(arg\s+([\w-]+)\)',lambda m:str(arguments.get(m.group(1),m.group(0))),template)
        body_nodes=[n for n in root.iter() if n.tag in ('body','link') and matching_name(bound(n.get('name','')),name)]
        joint_nodes=[n for n in root.iter() if n.tag=='joint' and matching_name(bound(n.get('name','')),name)]
        candidates=body_nodes if quantity in ('mass','subtree_mass','com_registered','principal_moments') else joint_nodes
        for node in candidates:
            actual=None;attr=None;label='input'
            if quantity=='mass':
                actual=node.find('inertial/mass') if node.tag=='link' else node.find('inertial')
                attr='value' if node.tag=='link' else 'mass'
            elif quantity=='subtree_mass':actual=node;label='subtree root'
            elif quantity=='com_registered':
                actual=node.find('inertial/origin') if node.tag=='link' else node.find('inertial')
                attr='xyz' if node.tag=='link' else 'pos';label='CoM/kinematic input'
            elif quantity=='principal_moments':
                actual=node.find('inertial/inertia') if node.tag=='link' else node.find('inertial')
                attr=None if node.tag=='link' else ('diaginertia' if actual is not None and actual.get('diaginertia') is not None else 'fullinertia');label='inertia input'
            elif node.getparent() is not None and root.tag=='robot':
                actual=node.find('limit');attr={'range':'lower','effort':'effort','velocity':'velocity','force':'effort'}.get(quantity)
            elif quantity=='range':
                if node.get('range') is not None:actual=node;attr='range'
                else:
                    cls=node.get('class')
                    parent=node.getparent()
                    while cls is None and parent is not None:
                        cls=parent.get('childclass');parent=parent.getparent()
                    defaults=defaults_for(root).get(cls or 'main',{}).get('joint',{})
                    if 'range' in defaults:_,actual,attr=defaults['range'];label='inherited default'
            else:
                if quantity=='force' and node.get('actuatorfrcrange') is not None:
                    actual=node;attr='actuatorfrcrange'
                else:
                    for actuator in root.findall('actuator/*'):
                        if not matching_name(actuator.get('joint',''),name):continue
                        group=defaults_for(root).get(actuator.get('class','main'),{})
                        defaults={**group.get('general',{}),**group.get(actuator.tag,{})}
                        for field in ('forcerange','ctrlrange'):
                            if actuator.get(field) is not None:actual=actuator;attr=field;break
                            if field in defaults:_,actual,attr=defaults[field];label='inherited actuator input';break
                        if actual is not None:break
            if actual is None:
                actual=node;label='geometry/inference input'
            n=attribute_line(actual,attr,lines) if attr else actual.sourceline or 1
            link=f"[{label} L{n}]({source.permalink(view['commit'],file,n)})"
            # A variable declaration can take its numeric values from a YAML table.
            text=actual.get(attr,'') if attr else ' '.join(actual.attrib.values())
            keys=re.findall(r"\[['\"]([^'\"]+)['\"]\]",text)
            if '${' in text and keys:
                for yaml_file in dependencies:
                    if not yaml_file.endswith(('.yaml','.yml')):continue
                    try:
                        tree=yaml.compose(source.read(view['commit'],yaml_file))
                        def locate(current,key):
                            if isinstance(current,yaml.MappingNode):
                                for k,v in current.value:
                                    if k.value==key:return v
                                    found=locate(v,key)
                                    if found is not None:return found
                            elif isinstance(current,yaml.SequenceNode):
                                for v in current.value:
                                    found=locate(v,key)
                                    if found is not None:return found
                            return None
                        target=locate(tree,keys[0])
                        for field in keys[1:]:
                            if isinstance(target,yaml.MappingNode):
                                child=next((v for k,v in target.value if k.value==field),None)
                                if child is not None:target=child
                            else:break
                        if target is not None:
                            yn=target.start_mark.line+1
                            link+=f"; [YAML numeric inputs L{yn}]({source.permalink(view['commit'],yaml_file,yn)})"
                            break
                    except (yaml.YAMLError,ValueError):pass
            return link
    if view['file'].endswith('.xacro') or view.get('snapshot',{}).get('xacro_expanded'):
        try:
            traced=expanded_declaration(view,name,quantity)
            if traced:return traced
        except Exception:
            pass
    return f"[expanded-source inputs; exact declaration unresolved]({source.permalink(view['commit'],view['file'],1)})"
