# libMCDS/python/bm.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:52f948f2ce15b18652a8cbfe7d5ccd47cd462e6c
# Generated 2016-11-27 21:16:28.667985 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace basement [xmlns:bm]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d081bdce-b529-11e6-8dd4-0800272323b7')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import mesh as _ImportedBinding_mesh
import common as _ImportedBinding_common

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('basement', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {basement}nodes with content type ELEMENT_ONLY
class nodes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {basement}nodes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nodes')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 30, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element node uses Python identifier node
    __node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'node'), 'node', '__basement_nodes_node', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 32, 12), )

    
    node = property(__node.value, __node.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__basement_nodes_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 33, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __node.name() : __node,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.nodes = nodes
Namespace.addCategoryObject('typeBinding', 'nodes', nodes)


# Complex type {basement}egdes with content type ELEMENT_ONLY
class egdes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {basement}egdes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'egdes')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 37, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element edge uses Python identifier edge
    __edge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edge'), 'edge', '__basement_egdes_edge', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 39, 12), )

    
    edge = property(__edge.value, __edge.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__basement_egdes_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 40, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __edge.name() : __edge,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.egdes = egdes
Namespace.addCategoryObject('typeBinding', 'egdes', egdes)


# Complex type {basement}faces with content type ELEMENT_ONLY
class faces (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {basement}faces with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'faces')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 44, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element face uses Python identifier face
    __face = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'face'), 'face', '__basement_faces_face', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 46, 12), )

    
    face = property(__face.value, __face.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__basement_faces_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 47, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __face.name() : __face,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.faces = faces
Namespace.addCategoryObject('typeBinding', 'faces', faces)


# Complex type {basement}basement_membrane with content type ELEMENT_ONLY
class basement_membrane (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {basement}basement_membrane with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'basement_membrane')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element nodes uses Python identifier nodes
    __nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nodes'), 'nodes', '__basement_basement_membrane_nodes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 53, 12), )

    
    nodes = property(__nodes.value, __nodes.set, None, None)

    
    # Element edges uses Python identifier edges
    __edges = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__basement_basement_membrane_edges', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 54, 12), )

    
    edges = property(__edges.value, __edges.set, None, None)

    
    # Element faces uses Python identifier faces
    __faces = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'faces'), 'faces', '__basement_basement_membrane_faces', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 55, 12), )

    
    faces = property(__faces.value, __faces.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__basement_basement_membrane_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 56, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__basement_basement_membrane_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 58, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 58, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __nodes.name() : __nodes,
        __edges.name() : __edges,
        __faces.name() : __faces,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.basement_membrane = basement_membrane
Namespace.addCategoryObject('typeBinding', 'basement_membrane', basement_membrane)


# Complex type {basement}basement_edge with content type ELEMENT_ONLY
class basement_edge (_ImportedBinding_mesh.edge):
    """Complex type {basement}basement_edge with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'basement_edge')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 8, 4)
    _ElementMap = _ImportedBinding_mesh.edge._ElementMap.copy()
    _AttributeMap = _ImportedBinding_mesh.edge._AttributeMap.copy()
    # Base type is _ImportedBinding_mesh.edge
    
    # Element tensile_strength uses Python identifier tensile_strength
    __tensile_strength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tensile_strength'), 'tensile_strength', '__basement_basement_edge_tensile_strength', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 12, 20), )

    
    tensile_strength = property(__tensile_strength.value, __tensile_strength.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__basement_basement_edge_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 13, 20), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Element node_ID (node_ID) inherited from {mesh}edge
    
    # Attribute ID inherited from {mesh}edge
    _ElementMap.update({
        __tensile_strength.name() : __tensile_strength,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.basement_edge = basement_edge
Namespace.addCategoryObject('typeBinding', 'basement_edge', basement_edge)


# Complex type {basement}basement_face with content type ELEMENT_ONLY
class basement_face (_ImportedBinding_mesh.face):
    """Complex type {basement}basement_face with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'basement_face')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 19, 4)
    _ElementMap = _ImportedBinding_mesh.face._ElementMap.copy()
    _AttributeMap = _ImportedBinding_mesh.face._AttributeMap.copy()
    # Base type is _ImportedBinding_mesh.face
    
    # Element thickness uses Python identifier thickness
    __thickness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thickness'), 'thickness', '__basement_basement_face_thickness', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 23, 20), )

    
    thickness = property(__thickness.value, __thickness.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__basement_basement_face_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 24, 20), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Element edge_ID (edge_ID) inherited from {mesh}face
    
    # Attribute ID inherited from {mesh}face
    _ElementMap.update({
        __thickness.name() : __thickness,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.basement_face = basement_face
Namespace.addCategoryObject('typeBinding', 'basement_face', basement_face)




nodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'node'), _ImportedBinding_mesh.node, scope=nodes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 32, 12)))

nodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=nodes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 33, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nodes._UseForTag(pyxb.namespace.ExpandedName(None, 'node')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 32, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nodes._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 33, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nodes._Automaton = _BuildAutomaton()




egdes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edge'), basement_edge, scope=egdes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 39, 12)))

egdes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=egdes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 40, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(egdes._UseForTag(pyxb.namespace.ExpandedName(None, 'edge')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 39, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(egdes._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 40, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
egdes._Automaton = _BuildAutomaton_()




faces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'face'), basement_face, scope=faces, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 46, 12)))

faces._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=faces, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 47, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(faces._UseForTag(pyxb.namespace.ExpandedName(None, 'face')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 46, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(faces._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 47, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
faces._Automaton = _BuildAutomaton_2()




basement_membrane._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nodes'), nodes, scope=basement_membrane, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 53, 12)))

basement_membrane._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edges'), egdes, scope=basement_membrane, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 54, 12)))

basement_membrane._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'faces'), faces, scope=basement_membrane, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 55, 12)))

basement_membrane._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=basement_membrane, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 56, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basement_membrane._UseForTag(pyxb.namespace.ExpandedName(None, 'nodes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basement_membrane._UseForTag(pyxb.namespace.ExpandedName(None, 'edges')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 54, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basement_membrane._UseForTag(pyxb.namespace.ExpandedName(None, 'faces')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 55, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(basement_membrane._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 56, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
basement_membrane._Automaton = _BuildAutomaton_3()




basement_edge._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tensile_strength'), _ImportedBinding_common.units_decimal_nonnegative, scope=basement_edge, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 12, 20)))

basement_edge._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=basement_edge, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 13, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 67, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basement_edge._UseForTag(pyxb.namespace.ExpandedName(None, 'node_ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 67, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basement_edge._UseForTag(pyxb.namespace.ExpandedName(None, 'tensile_strength')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 12, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(basement_edge._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 13, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
basement_edge._Automaton = _BuildAutomaton_4()




basement_face._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thickness'), _ImportedBinding_common.units_decimal_nonnegative, scope=basement_face, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 23, 20)))

basement_face._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=basement_face, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 24, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 76, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basement_face._UseForTag(pyxb.namespace.ExpandedName(None, 'edge_ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basement_face._UseForTag(pyxb.namespace.ExpandedName(None, 'thickness')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 23, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(basement_face._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/basement_membrane.xsd', 24, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
basement_face._Automaton = _BuildAutomaton_5()

