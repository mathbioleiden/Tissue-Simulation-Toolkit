# libMCDS/python/vas.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8cddc43d00e74f8ce0a1bc5f112a92170ab8999b
# Generated 2016-11-27 21:16:28.668235 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace vascular [xmlns:vas]

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
import mesh as _ImportedBinding_mesh
import pyxb.binding.datatypes
import pc as _ImportedBinding_pc
import common as _ImportedBinding_common
import var as _ImportedBinding_var

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('vascular', create_if_missing=True)
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


# Atomic simple type: {vascular}boundary_type
class boundary_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boundary_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 63, 4)
    _Documentation = None
boundary_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=boundary_type, enum_prefix=None)
boundary_type.Neumann = boundary_type._CF_enumeration.addEnumeration(unicode_value='Neumann', tag='Neumann')
boundary_type.Dirichlet = boundary_type._CF_enumeration.addEnumeration(unicode_value='Dirichlet', tag='Dirichlet')
boundary_type.Periodic = boundary_type._CF_enumeration.addEnumeration(unicode_value='Periodic', tag='Periodic')
boundary_type.Anti_Periodic = boundary_type._CF_enumeration.addEnumeration(unicode_value='Anti-Periodic', tag='Anti_Periodic')
boundary_type.Reflecting = boundary_type._CF_enumeration.addEnumeration(unicode_value='Reflecting', tag='Reflecting')
boundary_type.Anti_Reflecting = boundary_type._CF_enumeration.addEnumeration(unicode_value='Anti-Reflecting', tag='Anti_Reflecting')
boundary_type._InitializeFacetMap(boundary_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'boundary_type', boundary_type)
_module_typeBindings.boundary_type = boundary_type

# Complex type {vascular}list_of_vascular_nodes with content type ELEMENT_ONLY
class list_of_vascular_nodes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}list_of_vascular_nodes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'list_of_vascular_nodes')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 20, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vascular_node uses Python identifier vascular_node
    __vascular_node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vascular_node'), 'vascular_node', '__vascular_list_of_vascular_nodes_vascular_node', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 22, 12), )

    
    vascular_node = property(__vascular_node.value, __vascular_node.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_list_of_vascular_nodes_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 23, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __vascular_node.name() : __vascular_node,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.list_of_vascular_nodes = list_of_vascular_nodes
Namespace.addCategoryObject('typeBinding', 'list_of_vascular_nodes', list_of_vascular_nodes)


# Complex type {vascular}boundary_node with content type ELEMENT_ONLY
class boundary_node (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}boundary_node with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boundary_node')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 27, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element fluid_flow_velocity uses Python identifier fluid_flow_velocity
    __fluid_flow_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), 'fluid_flow_velocity', '__vascular_boundary_node_fluid_flow_velocity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 29, 12), )

    
    fluid_flow_velocity = property(__fluid_flow_velocity.value, __fluid_flow_velocity.set, None, None)

    
    # Element variables uses Python identifier variables
    __variables = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variables'), 'variables', '__vascular_boundary_node_variables', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 30, 12), )

    
    variables = property(__variables.value, __variables.set, None, None)

    
    # Element boundary_conditions uses Python identifier boundary_conditions
    __boundary_conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundary_conditions'), 'boundary_conditions', '__vascular_boundary_node_boundary_conditions', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 31, 12), )

    
    boundary_conditions = property(__boundary_conditions.value, __boundary_conditions.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_boundary_node_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 32, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute node_ID uses Python identifier node_ID
    __node_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'node_ID'), 'node_ID', '__vascular_boundary_node_node_ID', pyxb.binding.datatypes.unsignedInt)
    __node_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 34, 8)
    __node_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 34, 8)
    
    node_ID = property(__node_ID.value, __node_ID.set, None, None)

    _ElementMap.update({
        __fluid_flow_velocity.name() : __fluid_flow_velocity,
        __variables.name() : __variables,
        __boundary_conditions.name() : __boundary_conditions,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __node_ID.name() : __node_ID
    })
_module_typeBindings.boundary_node = boundary_node
Namespace.addCategoryObject('typeBinding', 'boundary_node', boundary_node)


# Complex type {vascular}list_of_boundary_nodes with content type ELEMENT_ONLY
class list_of_boundary_nodes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}list_of_boundary_nodes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'list_of_boundary_nodes')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 37, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element boundary_node uses Python identifier boundary_node
    __boundary_node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundary_node'), 'boundary_node', '__vascular_list_of_boundary_nodes_boundary_node', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 39, 12), )

    
    boundary_node = property(__boundary_node.value, __boundary_node.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_list_of_boundary_nodes_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 40, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __boundary_node.name() : __boundary_node,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.list_of_boundary_nodes = list_of_boundary_nodes
Namespace.addCategoryObject('typeBinding', 'list_of_boundary_nodes', list_of_boundary_nodes)


# Complex type {vascular}boundary_conditions with content type ELEMENT_ONLY
class boundary_conditions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}boundary_conditions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boundary_conditions')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 44, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element boundary_condition uses Python identifier boundary_condition
    __boundary_condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundary_condition'), 'boundary_condition', '__vascular_boundary_conditions_boundary_condition', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 46, 12), )

    
    boundary_condition = property(__boundary_condition.value, __boundary_condition.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_boundary_conditions_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 47, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__vascular_boundary_conditions_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 49, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 49, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __boundary_condition.name() : __boundary_condition,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.boundary_conditions = boundary_conditions
Namespace.addCategoryObject('typeBinding', 'boundary_conditions', boundary_conditions)


# Complex type {vascular}boundary_condition with content type ELEMENT_ONLY
class boundary_condition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}boundary_condition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boundary_condition')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 52, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element boundary_type uses Python identifier boundary_type
    __boundary_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundary_type'), 'boundary_type', '__vascular_boundary_condition_boundary_type', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 54, 12), )

    
    boundary_type = property(__boundary_type.value, __boundary_type.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__vascular_boundary_condition_value', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 55, 12), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element direction uses Python identifier direction
    __direction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'direction'), 'direction', '__vascular_boundary_condition_direction', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 56, 12), )

    
    direction = property(__direction.value, __direction.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_boundary_condition_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 57, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__vascular_boundary_condition_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 59, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 59, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute variable_ID uses Python identifier variable_ID
    __variable_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variable_ID'), 'variable_ID', '__vascular_boundary_condition_variable_ID', pyxb.binding.datatypes.unsignedInt, required=True)
    __variable_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 60, 8)
    __variable_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 60, 8)
    
    variable_ID = property(__variable_ID.value, __variable_ID.set, None, None)

    _ElementMap.update({
        __boundary_type.name() : __boundary_type,
        __value.name() : __value,
        __direction.name() : __direction,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __variable_ID.name() : __variable_ID
    })
_module_typeBindings.boundary_condition = boundary_condition
Namespace.addCategoryObject('typeBinding', 'boundary_condition', boundary_condition)


# Complex type {vascular}vascular_segments with content type ELEMENT_ONLY
class vascular_segments (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}vascular_segments with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vascular_segments')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vascular_segment uses Python identifier vascular_segment
    __vascular_segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vascular_segment'), 'vascular_segment', '__vascular_vascular_segments_vascular_segment', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 76, 12), )

    
    vascular_segment = property(__vascular_segment.value, __vascular_segment.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_vascular_segments_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 77, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __vascular_segment.name() : __vascular_segment,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.vascular_segments = vascular_segments
Namespace.addCategoryObject('typeBinding', 'vascular_segments', vascular_segments)


# Complex type {vascular}vascular_segment with content type ELEMENT_ONLY
class vascular_segment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}vascular_segment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vascular_segment')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 81, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element endpoint_1 uses Python identifier endpoint_1
    __endpoint_1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'endpoint_1'), 'endpoint_1', '__vascular_vascular_segment_endpoint_1', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 83, 12), )

    
    endpoint_1 = property(__endpoint_1.value, __endpoint_1.set, None, None)

    
    # Element endpoint_2 uses Python identifier endpoint_2
    __endpoint_2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'endpoint_2'), 'endpoint_2', '__vascular_vascular_segment_endpoint_2', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 84, 12), )

    
    endpoint_2 = property(__endpoint_2.value, __endpoint_2.set, None, None)

    
    # Element surface uses Python identifier surface
    __surface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'surface'), 'surface', '__vascular_vascular_segment_surface', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 85, 12), )

    
    surface = property(__surface.value, __surface.set, None, None)

    
    # Element interior uses Python identifier interior
    __interior = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'interior'), 'interior', '__vascular_vascular_segment_interior', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 86, 12), )

    
    interior = property(__interior.value, __interior.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_vascular_segment_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 87, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __endpoint_1.name() : __endpoint_1,
        __endpoint_2.name() : __endpoint_2,
        __surface.name() : __surface,
        __interior.name() : __interior,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.vascular_segment = vascular_segment
Namespace.addCategoryObject('typeBinding', 'vascular_segment', vascular_segment)


# Complex type {vascular}endpoint with content type ELEMENT_ONLY
class endpoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}endpoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'endpoint')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 91, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lengths uses Python identifier lengths
    __lengths = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lengths'), 'lengths', '__vascular_endpoint_lengths', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 97, 12), )

    
    lengths = property(__lengths.value, __lengths.set, None, None)

    
    # Element areas uses Python identifier areas
    __areas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'areas'), 'areas', '__vascular_endpoint_areas', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 98, 12), )

    
    areas = property(__areas.value, __areas.set, None, None)

    
    # Element fluid_flow_velocity uses Python identifier fluid_flow_velocity
    __fluid_flow_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), 'fluid_flow_velocity', '__vascular_endpoint_fluid_flow_velocity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 99, 12), )

    
    fluid_flow_velocity = property(__fluid_flow_velocity.value, __fluid_flow_velocity.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_endpoint_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 100, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute node_ID uses Python identifier node_ID
    __node_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'node_ID'), 'node_ID', '__vascular_endpoint_node_ID', pyxb.binding.datatypes.unsignedInt)
    __node_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 102, 8)
    __node_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 102, 8)
    
    node_ID = property(__node_ID.value, __node_ID.set, None, None)

    _ElementMap.update({
        __lengths.name() : __lengths,
        __areas.name() : __areas,
        __fluid_flow_velocity.name() : __fluid_flow_velocity,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __node_ID.name() : __node_ID
    })
_module_typeBindings.endpoint = endpoint
Namespace.addCategoryObject('typeBinding', 'endpoint', endpoint)


# Complex type {vascular}surface_properties with content type ELEMENT_ONLY
class surface_properties (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}surface_properties with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'surface_properties')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 105, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element areas uses Python identifier areas
    __areas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'areas'), 'areas', '__vascular_surface_properties_areas', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 107, 12), )

    
    areas = property(__areas.value, __areas.set, None, None)

    
    # Element fluid_flow_velocity uses Python identifier fluid_flow_velocity
    __fluid_flow_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), 'fluid_flow_velocity', '__vascular_surface_properties_fluid_flow_velocity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 108, 12), )

    
    fluid_flow_velocity = property(__fluid_flow_velocity.value, __fluid_flow_velocity.set, None, None)

    
    # Element mechanics uses Python identifier mechanics
    __mechanics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mechanics'), 'mechanics', '__vascular_surface_properties_mechanics', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 109, 12), )

    
    mechanics = property(__mechanics.value, __mechanics.set, None, None)

    
    # Element permeability uses Python identifier permeability
    __permeability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'permeability'), 'permeability', '__vascular_surface_properties_permeability', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 110, 12), )

    
    permeability = property(__permeability.value, __permeability.set, None, None)

    
    # Element surface_proteins uses Python identifier surface_proteins
    __surface_proteins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'surface_proteins'), 'surface_proteins', '__vascular_surface_properties_surface_proteins', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 111, 12), )

    
    surface_proteins = property(__surface_proteins.value, __surface_proteins.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_surface_properties_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 112, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __areas.name() : __areas,
        __fluid_flow_velocity.name() : __fluid_flow_velocity,
        __mechanics.name() : __mechanics,
        __permeability.name() : __permeability,
        __surface_proteins.name() : __surface_proteins,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.surface_properties = surface_properties
Namespace.addCategoryObject('typeBinding', 'surface_properties', surface_properties)


# Complex type {vascular}volume_properties with content type ELEMENT_ONLY
class volume_properties (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}volume_properties with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volume_properties')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 116, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element fluid_flow_velocity uses Python identifier fluid_flow_velocity
    __fluid_flow_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), 'fluid_flow_velocity', '__vascular_volume_properties_fluid_flow_velocity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 118, 12), )

    
    fluid_flow_velocity = property(__fluid_flow_velocity.value, __fluid_flow_velocity.set, None, None)

    
    # Element variables uses Python identifier variables
    __variables = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variables'), 'variables', '__vascular_volume_properties_variables', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 119, 12), )

    
    variables = property(__variables.value, __variables.set, None, None)

    
    # Element volumes uses Python identifier volumes
    __volumes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'volumes'), 'volumes', '__vascular_volume_properties_volumes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 120, 12), )

    
    volumes = property(__volumes.value, __volumes.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_volume_properties_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 121, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __fluid_flow_velocity.name() : __fluid_flow_velocity,
        __variables.name() : __variables,
        __volumes.name() : __volumes,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.volume_properties = volume_properties
Namespace.addCategoryObject('typeBinding', 'volume_properties', volume_properties)


# Complex type {vascular}vascular_network with content type ELEMENT_ONLY
class vascular_network (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {vascular}vascular_network with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vascular_network')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 125, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vascular_nodes uses Python identifier vascular_nodes
    __vascular_nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vascular_nodes'), 'vascular_nodes', '__vascular_vascular_network_vascular_nodes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 127, 12), )

    
    vascular_nodes = property(__vascular_nodes.value, __vascular_nodes.set, None, None)

    
    # Element boundary_nodes uses Python identifier boundary_nodes
    __boundary_nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundary_nodes'), 'boundary_nodes', '__vascular_vascular_network_boundary_nodes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 128, 12), )

    
    boundary_nodes = property(__boundary_nodes.value, __boundary_nodes.set, None, None)

    
    # Element vascular_segments uses Python identifier vascular_segments
    __vascular_segments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vascular_segments'), 'vascular_segments', '__vascular_vascular_network_vascular_segments', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 129, 12), )

    
    vascular_segments = property(__vascular_segments.value, __vascular_segments.set, None, None)

    
    # Element voxels uses Python identifier voxels
    __voxels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'voxels'), 'voxels', '__vascular_vascular_network_voxels', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 130, 12), )

    
    voxels = property(__voxels.value, __voxels.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__vascular_vascular_network_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 131, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__vascular_vascular_network_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 133, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 133, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'keywords'), 'keywords', '__vascular_vascular_network_keywords', pyxb.binding.datatypes.string)
    __keywords._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 134, 8)
    __keywords._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 134, 8)
    
    keywords = property(__keywords.value, __keywords.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__vascular_vascular_network_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 135, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 135, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __vascular_nodes.name() : __vascular_nodes,
        __boundary_nodes.name() : __boundary_nodes,
        __vascular_segments.name() : __vascular_segments,
        __voxels.name() : __voxels,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __keywords.name() : __keywords,
        __name.name() : __name
    })
_module_typeBindings.vascular_network = vascular_network
Namespace.addCategoryObject('typeBinding', 'vascular_network', vascular_network)


# Complex type {vascular}vascular_node with content type ELEMENT_ONLY
class vascular_node (_ImportedBinding_mesh.node):
    """Complex type {vascular}vascular_node with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vascular_node')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 12, 4)
    _ElementMap = _ImportedBinding_mesh.node._ElementMap.copy()
    _AttributeMap = _ImportedBinding_mesh.node._AttributeMap.copy()
    # Base type is _ImportedBinding_mesh.node
    
    # Element position (position) inherited from {mesh}node
    
    # Element custom (custom) inherited from {mesh}node
    
    # Attribute ID inherited from {mesh}node
    
    # Attribute boundary_node uses Python identifier boundary_node
    __boundary_node = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'boundary_node'), 'boundary_node', '__vascular_vascular_node_boundary_node', pyxb.binding.datatypes.boolean)
    __boundary_node._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 15, 16)
    __boundary_node._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 15, 16)
    
    boundary_node = property(__boundary_node.value, __boundary_node.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __boundary_node.name() : __boundary_node
    })
_module_typeBindings.vascular_node = vascular_node
Namespace.addCategoryObject('typeBinding', 'vascular_node', vascular_node)




list_of_vascular_nodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vascular_node'), vascular_node, scope=list_of_vascular_nodes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 22, 12)))

list_of_vascular_nodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=list_of_vascular_nodes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 23, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 23, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(list_of_vascular_nodes._UseForTag(pyxb.namespace.ExpandedName(None, 'vascular_node')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 22, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(list_of_vascular_nodes._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 23, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
list_of_vascular_nodes._Automaton = _BuildAutomaton()




boundary_node._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), _ImportedBinding_common.units_decimal, scope=boundary_node, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 29, 12)))

boundary_node._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variables'), _ImportedBinding_var.list_of_variables, scope=boundary_node, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 30, 12)))

boundary_node._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundary_conditions'), boundary_conditions, scope=boundary_node, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 31, 12)))

boundary_node._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=boundary_node, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 32, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 29, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(boundary_node._UseForTag(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 29, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 30, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(boundary_node._UseForTag(pyxb.namespace.ExpandedName(None, 'variables')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 30, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 31, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(boundary_node._UseForTag(pyxb.namespace.ExpandedName(None, 'boundary_conditions')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 31, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 32, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(boundary_node._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 32, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 29, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 30, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 31, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 32, 12))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 28, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
boundary_node._Automaton = _BuildAutomaton_()




list_of_boundary_nodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundary_node'), boundary_node, scope=list_of_boundary_nodes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 39, 12)))

list_of_boundary_nodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=list_of_boundary_nodes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 40, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 40, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(list_of_boundary_nodes._UseForTag(pyxb.namespace.ExpandedName(None, 'boundary_node')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 39, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(list_of_boundary_nodes._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 40, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
list_of_boundary_nodes._Automaton = _BuildAutomaton_6()




boundary_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundary_condition'), boundary_condition, scope=boundary_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 46, 12)))

boundary_conditions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=boundary_conditions, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 47, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 47, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(boundary_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'boundary_condition')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 46, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(boundary_conditions._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 47, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
boundary_conditions._Automaton = _BuildAutomaton_7()




boundary_condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundary_type'), boundary_type, scope=boundary_condition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 54, 12)))

boundary_condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), _ImportedBinding_common.units_decimal, scope=boundary_condition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 55, 12)))

boundary_condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'direction'), pyxb.binding.datatypes.string, scope=boundary_condition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 56, 12)))

boundary_condition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=boundary_condition, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 57, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 55, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 56, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 57, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(boundary_condition._UseForTag(pyxb.namespace.ExpandedName(None, 'boundary_type')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 54, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(boundary_condition._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 55, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(boundary_condition._UseForTag(pyxb.namespace.ExpandedName(None, 'direction')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 56, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(boundary_condition._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 57, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
boundary_condition._Automaton = _BuildAutomaton_8()




vascular_segments._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vascular_segment'), vascular_segment, scope=vascular_segments, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 76, 12)))

vascular_segments._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=vascular_segments, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 77, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 77, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vascular_segments._UseForTag(pyxb.namespace.ExpandedName(None, 'vascular_segment')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vascular_segments._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 77, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vascular_segments._Automaton = _BuildAutomaton_9()




vascular_segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'endpoint_1'), endpoint, scope=vascular_segment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 83, 12)))

vascular_segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'endpoint_2'), endpoint, scope=vascular_segment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 84, 12)))

vascular_segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'surface'), surface_properties, scope=vascular_segment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 85, 12)))

vascular_segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'interior'), volume_properties, scope=vascular_segment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 86, 12)))

vascular_segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=vascular_segment, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 87, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vascular_segment._UseForTag(pyxb.namespace.ExpandedName(None, 'endpoint_1')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 83, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vascular_segment._UseForTag(pyxb.namespace.ExpandedName(None, 'endpoint_2')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 84, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 85, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vascular_segment._UseForTag(pyxb.namespace.ExpandedName(None, 'surface')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 85, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 86, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vascular_segment._UseForTag(pyxb.namespace.ExpandedName(None, 'interior')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 86, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 87, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vascular_segment._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 87, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 85, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 86, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 87, 12))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 82, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vascular_segment._Automaton = _BuildAutomaton_10()




endpoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lengths'), _ImportedBinding_pc.lengths, scope=endpoint, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 97, 12)))

endpoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'areas'), _ImportedBinding_pc.areas_2D, scope=endpoint, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 98, 12)))

endpoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), _ImportedBinding_common.units_decimal, scope=endpoint, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 99, 12)))

endpoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=endpoint, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 100, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 97, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(endpoint._UseForTag(pyxb.namespace.ExpandedName(None, 'lengths')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 97, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 98, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(endpoint._UseForTag(pyxb.namespace.ExpandedName(None, 'areas')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 98, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 99, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(endpoint._UseForTag(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 99, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 100, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(endpoint._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 100, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 97, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 98, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 99, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 100, 12))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 92, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
endpoint._Automaton = _BuildAutomaton_16()




surface_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'areas'), _ImportedBinding_pc.areas_3D, scope=surface_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 107, 12)))

surface_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), _ImportedBinding_common.units_decimal, scope=surface_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 108, 12)))

surface_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mechanics'), _ImportedBinding_pc.mechanics, scope=surface_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 109, 12)))

surface_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'permeability'), _ImportedBinding_common.units_decimal, scope=surface_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 110, 12)))

surface_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'surface_proteins'), _ImportedBinding_var.list_of_variables, scope=surface_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 111, 12)))

surface_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=surface_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 112, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 107, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(surface_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'areas')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 108, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(surface_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 108, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 109, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(surface_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'mechanics')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 109, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 110, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(surface_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'permeability')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 110, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 111, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(surface_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'surface_proteins')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 111, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 112, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(surface_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 112, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 107, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 108, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 109, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 110, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 111, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 112, 12))
    counters.add(cc_5)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    sub_automata.append(_BuildAutomaton_25())
    sub_automata.append(_BuildAutomaton_26())
    sub_automata.append(_BuildAutomaton_27())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 106, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
surface_properties._Automaton = _BuildAutomaton_21()




volume_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity'), _ImportedBinding_common.units_decimal, scope=volume_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 118, 12)))

volume_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variables'), _ImportedBinding_var.list_of_variables, scope=volume_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 119, 12)))

volume_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'volumes'), _ImportedBinding_pc.volumes, scope=volume_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 120, 12)))

volume_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=volume_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 121, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 118, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volume_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'fluid_flow_velocity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 118, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 119, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volume_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'variables')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 119, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 120, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volume_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'volumes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 120, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 121, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volume_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 121, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 118, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 119, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 120, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 121, 12))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_29())
    sub_automata.append(_BuildAutomaton_30())
    sub_automata.append(_BuildAutomaton_31())
    sub_automata.append(_BuildAutomaton_32())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 117, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
volume_properties._Automaton = _BuildAutomaton_28()




vascular_network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vascular_nodes'), list_of_vascular_nodes, scope=vascular_network, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 127, 12)))

vascular_network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundary_nodes'), list_of_boundary_nodes, scope=vascular_network, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 128, 12)))

vascular_network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vascular_segments'), vascular_segments, scope=vascular_network, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 129, 12)))

vascular_network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'voxels'), _ImportedBinding_mesh.int_list_xpath, scope=vascular_network, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 130, 12)))

vascular_network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=vascular_network, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 131, 12)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 127, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 128, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 129, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 130, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 131, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vascular_network._UseForTag(pyxb.namespace.ExpandedName(None, 'vascular_nodes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 127, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vascular_network._UseForTag(pyxb.namespace.ExpandedName(None, 'boundary_nodes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 128, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(vascular_network._UseForTag(pyxb.namespace.ExpandedName(None, 'vascular_segments')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 129, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(vascular_network._UseForTag(pyxb.namespace.ExpandedName(None, 'voxels')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 130, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(vascular_network._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/vascular.xsd', 131, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
vascular_network._Automaton = _BuildAutomaton_33()




def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 60, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vascular_node._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 59, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vascular_node._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 60, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vascular_node._Automaton = _BuildAutomaton_34()

