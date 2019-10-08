# libMCDS/python/mesh.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:52da7846e396ff38cd6729bec21b6f9159f9bd1c
# Generated 2016-11-29 16:42:21.871799 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace mesh [xmlns:mesh]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:da1167f0-b695-11e6-8a8c-0800272323b7')

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
import common as _ImportedBinding_common

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('mesh', create_if_missing=True)
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


# Complex type {mesh}mesh with content type ELEMENT_ONLY
class mesh (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {mesh}mesh with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mesh')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 16, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element bounding_box uses Python identifier bounding_box
    __bounding_box = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bounding_box'), 'bounding_box', '__mesh_mesh_bounding_box', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 18, 12), )

    
    bounding_box = property(__bounding_box.value, __bounding_box.set, None, None)

    
    # Element x_coordinates uses Python identifier x_coordinates
    __x_coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x_coordinates'), 'x_coordinates', '__mesh_mesh_x_coordinates', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 19, 12), )

    
    x_coordinates = property(__x_coordinates.value, __x_coordinates.set, None, None)

    
    # Element y_coordinates uses Python identifier y_coordinates
    __y_coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y_coordinates'), 'y_coordinates', '__mesh_mesh_y_coordinates', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 20, 12), )

    
    y_coordinates = property(__y_coordinates.value, __y_coordinates.set, None, None)

    
    # Element z_coordinates uses Python identifier z_coordinates
    __z_coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'z_coordinates'), 'z_coordinates', '__mesh_mesh_z_coordinates', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 21, 12), )

    
    z_coordinates = property(__z_coordinates.value, __z_coordinates.set, None, None)

    
    # Element voxels uses Python identifier voxels
    __voxels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'voxels'), 'voxels', '__mesh_mesh_voxels', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 22, 12), )

    
    voxels = property(__voxels.value, __voxels.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__mesh_mesh_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 23, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__mesh_mesh_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__mesh_mesh_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 25, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 25, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute uniform uses Python identifier uniform
    __uniform = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uniform'), 'uniform', '__mesh_mesh_uniform', pyxb.binding.datatypes.boolean)
    __uniform._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 26, 8)
    __uniform._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 26, 8)
    
    uniform = property(__uniform.value, __uniform.set, None, None)

    
    # Attribute regular uses Python identifier regular
    __regular = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'regular'), 'regular', '__mesh_mesh_regular', pyxb.binding.datatypes.boolean)
    __regular._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 27, 8)
    __regular._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 27, 8)
    
    regular = property(__regular.value, __regular.set, None, None)

    _ElementMap.update({
        __bounding_box.name() : __bounding_box,
        __x_coordinates.name() : __x_coordinates,
        __y_coordinates.name() : __y_coordinates,
        __z_coordinates.name() : __z_coordinates,
        __voxels.name() : __voxels,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __units.name() : __units,
        __type.name() : __type,
        __uniform.name() : __uniform,
        __regular.name() : __regular
    })
_module_typeBindings.mesh = mesh
Namespace.addCategoryObject('typeBinding', 'mesh', mesh)


# Complex type {mesh}voxel with content type ELEMENT_ONLY
class voxel (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {mesh}voxel with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'voxel')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 47, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element center uses Python identifier center
    __center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'center'), 'center', '__mesh_voxel_center', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 49, 12), )

    
    center = property(__center.value, __center.set, None, None)

    
    # Element volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'volume'), 'volume', '__mesh_voxel_volume', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 50, 12), )

    
    volume = property(__volume.value, __volume.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__mesh_voxel_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 51, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__mesh_voxel_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 53, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 53, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__mesh_voxel_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 54, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 54, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __center.name() : __center,
        __volume.name() : __volume,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __type.name() : __type
    })
_module_typeBindings.voxel = voxel
Namespace.addCategoryObject('typeBinding', 'voxel', voxel)


# Complex type {mesh}node with content type ELEMENT_ONLY
class node (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {mesh}node with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'node')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 57, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__mesh_node_position', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 59, 12), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__mesh_node_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 60, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__mesh_node_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 62, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 62, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __position.name() : __position,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.node = node
Namespace.addCategoryObject('typeBinding', 'node', node)


# Complex type {mesh}edge with content type ELEMENT_ONLY
class edge (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {mesh}edge with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'edge')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 65, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element node_ID uses Python identifier node_ID
    __node_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'node_ID'), 'node_ID', '__mesh_edge_node_ID', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 67, 12), )

    
    node_ID = property(__node_ID.value, __node_ID.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__mesh_edge_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 71, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 71, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __node_ID.name() : __node_ID
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.edge = edge
Namespace.addCategoryObject('typeBinding', 'edge', edge)


# Complex type {mesh}face with content type ELEMENT_ONLY
class face (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {mesh}face with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'face')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element edge_ID uses Python identifier edge_ID
    __edge_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edge_ID'), 'edge_ID', '__mesh_face_edge_ID', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 76, 12), )

    
    edge_ID = property(__edge_ID.value, __edge_ID.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__mesh_face_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 80, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 80, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __edge_ID.name() : __edge_ID
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.face = face
Namespace.addCategoryObject('typeBinding', 'face', face)


# Complex type {mesh}list_of_voxels with content type ELEMENT_ONLY
class list_of_voxels (pyxb.binding.basis.complexTypeDefinition):
    """
                This should be a choice between filename and voxels. Removed
                because custom should be allowed with filename and to make
                C++ API easier.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'list_of_voxels')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 31, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element filename uses Python identifier filename
    __filename = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__mesh_list_of_voxels_filename', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 40, 12), )

    
    filename = property(__filename.value, __filename.set, None, None)

    
    # Element voxel uses Python identifier voxel
    __voxel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'voxel'), 'voxel', '__mesh_list_of_voxels_voxel', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 41, 12), )

    
    voxel = property(__voxel.value, __voxel.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__mesh_list_of_voxels_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 42, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__mesh_list_of_voxels_type', _ImportedBinding_common.data_storage_formats)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 44, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 44, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __filename.name() : __filename,
        __voxel.name() : __voxel,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.list_of_voxels = list_of_voxels
Namespace.addCategoryObject('typeBinding', 'list_of_voxels', list_of_voxels)


# Complex type {mesh}int_list_xpath with content type SIMPLE
class int_list_xpath (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {mesh}int_list_xpath with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_common.unsigned_int_list
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'int_list_xpath')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 83, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_common.unsigned_int_list
    
    # Attribute xpath uses Python identifier xpath
    __xpath = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'xpath'), 'xpath', '__mesh_int_list_xpath_xpath', pyxb.binding.datatypes.string)
    __xpath._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 86, 16)
    __xpath._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 86, 16)
    
    xpath = property(__xpath.value, __xpath.set, None, None)

    
    # Attribute grouping_number uses Python identifier grouping_number
    __grouping_number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'grouping_number'), 'grouping_number', '__mesh_int_list_xpath_grouping_number', pyxb.binding.datatypes.unsignedShort)
    __grouping_number._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 87, 16)
    __grouping_number._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 87, 16)
    
    grouping_number = property(__grouping_number.value, __grouping_number.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __xpath.name() : __xpath,
        __grouping_number.name() : __grouping_number
    })
_module_typeBindings.int_list_xpath = int_list_xpath
Namespace.addCategoryObject('typeBinding', 'int_list_xpath', int_list_xpath)


# Complex type {mesh}bounding_box with content type SIMPLE
class bounding_box (_ImportedBinding_common.units_double_list):
    """Complex type {mesh}bounding_box with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_common.double_list
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bounding_box')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 7, 4)
    _ElementMap = _ImportedBinding_common.units_double_list._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.units_double_list._AttributeMap.copy()
    # Base type is _ImportedBinding_common.units_double_list
    
    # Attribute units inherited from {common}units_double_list
    
    # Attribute measurement_type inherited from {common}units_double_list
    
    # Attribute uncertainty inherited from {common}units_double_list
    
    # Attribute negative_uncertainty inherited from {common}units_double_list
    
    # Attribute positive_uncertainty inherited from {common}units_double_list
    
    # Attribute uncertainty_percentage inherited from {common}units_double_list
    
    # Attribute negative_uncertainty_percentage inherited from {common}units_double_list
    
    # Attribute positive_uncertainty_percentage inherited from {common}units_double_list
    
    # Attribute median inherited from {common}units_double_list
    
    # Attribute standard_deviation inherited from {common}units_double_list
    
    # Attribute interquartile_range inherited from {common}units_double_list
    
    # Attribute range inherited from {common}units_double_list
    
    # Attribute min inherited from {common}units_double_list
    
    # Attribute max inherited from {common}units_double_list
    
    # Attribute standard_error inherited from {common}units_double_list
    
    # Attribute standard_error_of_the_mean inherited from {common}units_double_list
    
    # Attribute number_obs inherited from {common}units_double_list
    
    # Attribute skewnesss inherited from {common}units_double_list
    
    # Attribute kurtosis inherited from {common}units_double_list
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__mesh_bounding_box_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 10, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 10, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.bounding_box = bounding_box
Namespace.addCategoryObject('typeBinding', 'bounding_box', bounding_box)




mesh._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bounding_box'), bounding_box, scope=mesh, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 18, 12)))

mesh._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x_coordinates'), _ImportedBinding_common.units_double_list, scope=mesh, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 19, 12)))

mesh._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y_coordinates'), _ImportedBinding_common.units_double_list, scope=mesh, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 20, 12)))

mesh._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'z_coordinates'), _ImportedBinding_common.units_double_list, scope=mesh, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 21, 12)))

mesh._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'voxels'), list_of_voxels, scope=mesh, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 22, 12)))

mesh._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=mesh, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 23, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 18, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesh._UseForTag(pyxb.namespace.ExpandedName(None, 'bounding_box')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 18, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 19, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesh._UseForTag(pyxb.namespace.ExpandedName(None, 'x_coordinates')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 19, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 20, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesh._UseForTag(pyxb.namespace.ExpandedName(None, 'y_coordinates')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 20, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 21, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesh._UseForTag(pyxb.namespace.ExpandedName(None, 'z_coordinates')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 21, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 22, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesh._UseForTag(pyxb.namespace.ExpandedName(None, 'voxels')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 22, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 23, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesh._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 18, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 19, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 20, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 21, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 22, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 23, 12))
    counters.add(cc_5)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 17, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mesh._Automaton = _BuildAutomaton()




voxel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'center'), _ImportedBinding_common.units_double_list, scope=voxel, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 49, 12)))

voxel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'volume'), _ImportedBinding_common.units_decimal_nonnegative, scope=voxel, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 50, 12)))

voxel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=voxel, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 51, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(voxel._UseForTag(pyxb.namespace.ExpandedName(None, 'center')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 49, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(voxel._UseForTag(pyxb.namespace.ExpandedName(None, 'volume')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 50, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 51, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(voxel._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 51, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 51, 12))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    sub_automata.append(_BuildAutomaton_10())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 48, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
voxel._Automaton = _BuildAutomaton_7()




node._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), _ImportedBinding_common.units_double_list, scope=node, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 59, 12)))

node._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=node, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 60, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 60, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(node._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 59, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(node._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 60, 12))
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
node._Automaton = _BuildAutomaton_11()




edge._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'node_ID'), pyxb.binding.datatypes.unsignedInt, scope=edge, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 67, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 67, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge._UseForTag(pyxb.namespace.ExpandedName(None, 'node_ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 67, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
edge._Automaton = _BuildAutomaton_12()




face._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edge_ID'), pyxb.binding.datatypes.unsignedInt, scope=face, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 76, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 76, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(face._UseForTag(pyxb.namespace.ExpandedName(None, 'edge_ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
face._Automaton = _BuildAutomaton_13()




list_of_voxels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'filename'), pyxb.binding.datatypes.string, scope=list_of_voxels, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 40, 12)))

list_of_voxels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'voxel'), voxel, scope=list_of_voxels, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 41, 12)))

list_of_voxels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=list_of_voxels, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 42, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 40, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 42, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(list_of_voxels._UseForTag(pyxb.namespace.ExpandedName(None, 'filename')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 40, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(list_of_voxels._UseForTag(pyxb.namespace.ExpandedName(None, 'voxel')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 41, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(list_of_voxels._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/mesh.xsd', 42, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
list_of_voxels._Automaton = _BuildAutomaton_14()

