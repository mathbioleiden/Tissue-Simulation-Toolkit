# libMCDS/python/s.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aa4a5f8125f234182e2dea92805afdfb747a86be
# Generated 2016-11-29 16:42:21.934203 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace state [xmlns:s]

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
import pc as _ImportedBinding_pc
import common as _ImportedBinding_common
import mesh as _ImportedBinding_mesh

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('state', create_if_missing=True)
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


# Atomic simple type: {state}orientation_formalism
class orientation_formalism (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'orientation_formalism')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 44, 4)
    _Documentation = None
orientation_formalism._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=orientation_formalism, enum_prefix=None)
orientation_formalism.axis_angle = orientation_formalism._CF_enumeration.addEnumeration(unicode_value='axis-angle', tag='axis_angle')
orientation_formalism.quaternion = orientation_formalism._CF_enumeration.addEnumeration(unicode_value='quaternion', tag='quaternion')
orientation_formalism.Euler_Angles = orientation_formalism._CF_enumeration.addEnumeration(unicode_value='Euler Angles', tag='Euler_Angles')
orientation_formalism.Tait_Bryan = orientation_formalism._CF_enumeration.addEnumeration(unicode_value='Tait-Bryan', tag='Tait_Bryan')
orientation_formalism.polar = orientation_formalism._CF_enumeration.addEnumeration(unicode_value='polar', tag='polar')
orientation_formalism.Polar = orientation_formalism._CF_enumeration.addEnumeration(unicode_value='Polar', tag='Polar')
orientation_formalism.Unit_Vector = orientation_formalism._CF_enumeration.addEnumeration(unicode_value='Unit Vector', tag='Unit_Vector')
orientation_formalism._InitializeFacetMap(orientation_formalism._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'orientation_formalism', orientation_formalism)
_module_typeBindings.orientation_formalism = orientation_formalism

# Complex type {state}phase with content type ELEMENT_ONLY
class phase (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {state}phase with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phase')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element model_name uses Python identifier model_name
    __model_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'model_name'), 'model_name', '__state_phase_model_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 13, 12), )

    
    model_name = property(__model_name.value, __model_name.set, None, None)

    
    # Element phase_name uses Python identifier phase_name
    __phase_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phase_name'), 'phase_name', '__state_phase_phase_name', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 14, 12), )

    
    phase_name = property(__phase_name.value, __phase_name.set, None, None)

    
    # Element cell_cycle_model_index uses Python identifier cell_cycle_model_index
    __cell_cycle_model_index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_cycle_model_index'), 'cell_cycle_model_index', '__state_phase_cell_cycle_model_index', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 15, 12), )

    
    cell_cycle_model_index = property(__cell_cycle_model_index.value, __cell_cycle_model_index.set, None, None)

    
    # Element cell_cycle_phase_index uses Python identifier cell_cycle_phase_index
    __cell_cycle_phase_index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_cycle_phase_index'), 'cell_cycle_phase_index', '__state_phase_cell_cycle_phase_index', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 16, 12), )

    
    cell_cycle_phase_index = property(__cell_cycle_phase_index.value, __cell_cycle_phase_index.set, None, None)

    
    # Element elapsed_time uses Python identifier elapsed_time
    __elapsed_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'elapsed_time'), 'elapsed_time', '__state_phase_elapsed_time', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 17, 12), )

    
    elapsed_time = property(__elapsed_time.value, __elapsed_time.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__state_phase_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 18, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __model_name.name() : __model_name,
        __phase_name.name() : __phase_name,
        __cell_cycle_model_index.name() : __cell_cycle_model_index,
        __cell_cycle_phase_index.name() : __cell_cycle_phase_index,
        __elapsed_time.name() : __elapsed_time,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.phase = phase
Namespace.addCategoryObject('typeBinding', 'phase', phase)


# Complex type {state}phase_name with content type SIMPLE
class phase_name (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {state}phase_name with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phase_name')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 22, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute GO_ID uses Python identifier GO_ID
    __GO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GO_ID'), 'GO_ID', '__state_phase_name_GO_ID', pyxb.binding.datatypes.string)
    __GO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 26, 16)
    __GO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 26, 16)
    
    GO_ID = property(__GO_ID.value, __GO_ID.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __GO_ID.name() : __GO_ID
    })
_module_typeBindings.phase_name = phase_name
Namespace.addCategoryObject('typeBinding', 'phase_name', phase_name)


# Complex type {state}cell_parts with content type ELEMENT_ONLY
class cell_parts (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {state}cell_parts with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cell_parts')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 65, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__state_cell_parts_orientation', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__state_cell_parts_position', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Element velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__state_cell_parts_velocity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12), )

    
    velocity = property(__velocity.value, __velocity.set, None, None)

    
    # Element voxels uses Python identifier voxels
    __voxels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'voxels'), 'voxels', '__state_cell_parts_voxels', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12), )

    
    voxels = property(__voxels.value, __voxels.set, None, None)

    
    # Element cell_part uses Python identifier cell_part
    __cell_part = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_part'), 'cell_part', '__state_cell_parts_cell_part', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 68, 12), )

    
    cell_part = property(__cell_part.value, __cell_part.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__state_cell_parts_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 69, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__state_cell_parts_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 293, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 293, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__state_cell_parts_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 294, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 294, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __orientation.name() : __orientation,
        __position.name() : __position,
        __velocity.name() : __velocity,
        __voxels.name() : __voxels,
        __cell_part.name() : __cell_part,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __name.name() : __name,
        __ID.name() : __ID
    })
_module_typeBindings.cell_parts = cell_parts
Namespace.addCategoryObject('typeBinding', 'cell_parts', cell_parts)


# Complex type {state}state with content type ELEMENT_ONLY
class state (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {state}state with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'state')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__state_state_orientation', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__state_state_position', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Element velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__state_state_velocity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12), )

    
    velocity = property(__velocity.value, __velocity.set, None, None)

    
    # Element voxels uses Python identifier voxels
    __voxels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'voxels'), 'voxels', '__state_state_voxels', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12), )

    
    voxels = property(__voxels.value, __voxels.set, None, None)

    
    # Element cell_part uses Python identifier cell_part
    __cell_part = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cell_part'), 'cell_part', '__state_state_cell_part', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 77, 12), )

    
    cell_part = property(__cell_part.value, __cell_part.set, None, None)

    
    # Element phase uses Python identifier phase
    __phase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phase'), 'phase', '__state_state_phase', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 78, 12), )

    
    phase = property(__phase.value, __phase.set, None, None)

    
    # Element adhered_cells uses Python identifier adhered_cells
    __adhered_cells = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhered_cells'), 'adhered_cells', '__state_state_adhered_cells', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 79, 12), )

    
    adhered_cells = property(__adhered_cells.value, __adhered_cells.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__state_state_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 80, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __orientation.name() : __orientation,
        __position.name() : __position,
        __velocity.name() : __velocity,
        __voxels.name() : __voxels,
        __cell_part.name() : __cell_part,
        __phase.name() : __phase,
        __adhered_cells.name() : __adhered_cells,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.state = state
Namespace.addCategoryObject('typeBinding', 'state', state)


# Complex type {state}adhered_cell with content type ELEMENT_ONLY
class adhered_cell (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {state}adhered_cell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'adhered_cell')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 84, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__state_adhered_cell_ID', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 86, 12), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element contact_area uses Python identifier contact_area
    __contact_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact_area'), 'contact_area', '__state_adhered_cell_contact_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 87, 12), )

    
    contact_area = property(__contact_area.value, __contact_area.set, None, None)

    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__state_adhered_cell_contact', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 88, 12), )

    
    contact = property(__contact.value, __contact.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__state_adhered_cell_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 89, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __ID.name() : __ID,
        __contact_area.name() : __contact_area,
        __contact.name() : __contact,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.adhered_cell = adhered_cell
Namespace.addCategoryObject('typeBinding', 'adhered_cell', adhered_cell)


# Complex type {state}list_of_adhered_cells with content type ELEMENT_ONLY
class list_of_adhered_cells (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {state}list_of_adhered_cells with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'list_of_adhered_cells')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 93, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element adhered_cell uses Python identifier adhered_cell
    __adhered_cell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhered_cell'), 'adhered_cell', '__state_list_of_adhered_cells_adhered_cell', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 95, 12), )

    
    adhered_cell = property(__adhered_cell.value, __adhered_cell.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__state_list_of_adhered_cells_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 96, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __adhered_cell.name() : __adhered_cell,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.list_of_adhered_cells = list_of_adhered_cells
Namespace.addCategoryObject('typeBinding', 'list_of_adhered_cells', list_of_adhered_cells)


# Complex type {state}orientation with content type SIMPLE
class orientation (_ImportedBinding_common.units_double_list):
    """Complex type {state}orientation with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding_common.double_list
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'orientation')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 31, 4)
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
    
    # Attribute formalism uses Python identifier formalism
    __formalism = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'formalism'), 'formalism', '__state_orientation_formalism', _module_typeBindings.orientation_formalism)
    __formalism._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 39, 16)
    __formalism._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 39, 16)
    
    formalism = property(__formalism.value, __formalism.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __formalism.name() : __formalism
    })
_module_typeBindings.orientation = orientation
Namespace.addCategoryObject('typeBinding', 'orientation', orientation)




phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'model_name'), pyxb.binding.datatypes.string, scope=phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 13, 12)))

phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phase_name'), phase_name, scope=phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 14, 12)))

phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_cycle_model_index'), pyxb.binding.datatypes.unsignedShort, scope=phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 15, 12)))

phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_cycle_phase_index'), pyxb.binding.datatypes.unsignedShort, scope=phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 16, 12)))

phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'elapsed_time'), _ImportedBinding_common.units_decimal, scope=phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 17, 12)))

phase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=phase, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 18, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 13, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phase._UseForTag(pyxb.namespace.ExpandedName(None, 'model_name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 13, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 14, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phase._UseForTag(pyxb.namespace.ExpandedName(None, 'phase_name')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 14, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 15, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phase._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_cycle_model_index')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 15, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 16, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phase._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_cycle_phase_index')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 16, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 17, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phase._UseForTag(pyxb.namespace.ExpandedName(None, 'elapsed_time')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 17, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 18, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phase._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 18, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 18, 12))
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
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 12, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
phase._Automaton = _BuildAutomaton()




cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), orientation, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12)))

cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), _ImportedBinding_common.units_double_list, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12)))

cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity'), _ImportedBinding_common.units_double_list, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12)))

cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'voxels'), _ImportedBinding_mesh.int_list_xpath, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12)))

cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_part'), cell_parts, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 68, 12)))

cell_parts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cell_parts, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 69, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 68, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 69, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'voxels')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_part')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 68, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cell_parts._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 69, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cell_parts._Automaton = _BuildAutomaton_7()




state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), orientation, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), _ImportedBinding_common.units_double_list, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity'), _ImportedBinding_common.units_double_list, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'voxels'), _ImportedBinding_mesh.int_list_xpath, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cell_part'), cell_parts, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 77, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phase'), phase, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 78, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhered_cells'), list_of_adhered_cells, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 79, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=state, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 80, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 77, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 78, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 79, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 80, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 58, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 59, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 60, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'voxels')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 61, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'cell_part')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 77, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'phase')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 78, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'adhered_cells')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 79, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 80, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
state._Automaton = _BuildAutomaton_8()




adhered_cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ID'), pyxb.binding.datatypes.unsignedInt, scope=adhered_cell, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 86, 12)))

adhered_cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact_area'), _ImportedBinding_common.units_decimal_nonnegative, scope=adhered_cell, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 87, 12)))

adhered_cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), _ImportedBinding_pc.cross_section, scope=adhered_cell, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 88, 12)))

adhered_cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=adhered_cell, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 89, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 89, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(adhered_cell._UseForTag(pyxb.namespace.ExpandedName(None, 'ID')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 86, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(adhered_cell._UseForTag(pyxb.namespace.ExpandedName(None, 'contact_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 87, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(adhered_cell._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 88, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(adhered_cell._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 89, 12))
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
adhered_cell._Automaton = _BuildAutomaton_9()




list_of_adhered_cells._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhered_cell'), adhered_cell, scope=list_of_adhered_cells, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 95, 12)))

list_of_adhered_cells._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=list_of_adhered_cells, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 96, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 95, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 96, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(list_of_adhered_cells._UseForTag(pyxb.namespace.ExpandedName(None, 'adhered_cell')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 95, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(list_of_adhered_cells._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/state.xsd', 96, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
list_of_adhered_cells._Automaton = _BuildAutomaton_10()

