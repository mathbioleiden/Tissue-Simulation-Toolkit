# libMCDS/python/pc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ec26f65cb8262f6eb29729a6b234fe3dcd20a738
# Generated 2016-11-29 16:42:21.899737 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace phenotype_common [xmlns:pc]

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
import var as _ImportedBinding_var

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('phenotype_common', create_if_missing=True)
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


# Complex type {phenotype_common}adhesion with content type ELEMENT_ONLY
class adhesion (pyxb.binding.basis.complexTypeDefinition):
    """
                These elements deal with adhesion.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'adhesion')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 26, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element adhesion_bond_breaking_rate uses Python identifier adhesion_bond_breaking_rate
    __adhesion_bond_breaking_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion_bond_breaking_rate'), 'adhesion_bond_breaking_rate', '__phenotype_common_adhesion_adhesion_bond_breaking_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 33, 12), )

    
    adhesion_bond_breaking_rate = property(__adhesion_bond_breaking_rate.value, __adhesion_bond_breaking_rate.set, None, '\n                        This is also known as the dissocation rate\n                    ')

    
    # Element adhesion_bond_formation_rate uses Python identifier adhesion_bond_formation_rate
    __adhesion_bond_formation_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion_bond_formation_rate'), 'adhesion_bond_formation_rate', '__phenotype_common_adhesion_adhesion_bond_formation_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 40, 12), )

    
    adhesion_bond_formation_rate = property(__adhesion_bond_formation_rate.value, __adhesion_bond_formation_rate.set, None, '\n                        This is also known as the bimolecular association rate\n                    ')

    
    # Element adhesion_spring_constant uses Python identifier adhesion_spring_constant
    __adhesion_spring_constant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion_spring_constant'), 'adhesion_spring_constant', '__phenotype_common_adhesion_adhesion_spring_constant', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 47, 12), )

    
    adhesion_spring_constant = property(__adhesion_spring_constant.value, __adhesion_spring_constant.set, None, '\n                        Hook-ian spring constant for a binding molecule.\n                    ')

    
    # Element adhesion_receptor_density uses Python identifier adhesion_receptor_density
    __adhesion_receptor_density = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion_receptor_density'), 'adhesion_receptor_density', '__phenotype_common_adhesion_adhesion_receptor_density', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 54, 12), )

    
    adhesion_receptor_density = property(__adhesion_receptor_density.value, __adhesion_receptor_density.set, None, None)

    
    # Element surface_binding_energy uses Python identifier surface_binding_energy
    __surface_binding_energy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'surface_binding_energy'), 'surface_binding_energy', '__phenotype_common_adhesion_surface_binding_energy', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 55, 12), )

    
    surface_binding_energy = property(__surface_binding_energy.value, __surface_binding_energy.set, None, None)

    
    # Element number_of_adhered_cells uses Python identifier number_of_adhered_cells
    __number_of_adhered_cells = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number_of_adhered_cells'), 'number_of_adhered_cells', '__phenotype_common_adhesion_number_of_adhered_cells', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 56, 12), )

    
    number_of_adhered_cells = property(__number_of_adhered_cells.value, __number_of_adhered_cells.set, None, None)

    
    # Element maximum_number_of_adhered_cells uses Python identifier maximum_number_of_adhered_cells
    __maximum_number_of_adhered_cells = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum_number_of_adhered_cells'), 'maximum_number_of_adhered_cells', '__phenotype_common_adhesion_maximum_number_of_adhered_cells', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 57, 12), )

    
    maximum_number_of_adhered_cells = property(__maximum_number_of_adhered_cells.value, __maximum_number_of_adhered_cells.set, None, None)

    
    # Element adhered_surface_area uses Python identifier adhered_surface_area
    __adhered_surface_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhered_surface_area'), 'adhered_surface_area', '__phenotype_common_adhesion_adhered_surface_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 58, 12), )

    
    adhered_surface_area = property(__adhered_surface_area.value, __adhered_surface_area.set, None, None)

    
    # Element maximum_adhered_surface_area uses Python identifier maximum_adhered_surface_area
    __maximum_adhered_surface_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum_adhered_surface_area'), 'maximum_adhered_surface_area', '__phenotype_common_adhesion_maximum_adhered_surface_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 59, 12), )

    
    maximum_adhered_surface_area = property(__maximum_adhered_surface_area.value, __maximum_adhered_surface_area.set, None, None)

    
    # Element adhesion_force_per_surface_area uses Python identifier adhesion_force_per_surface_area
    __adhesion_force_per_surface_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion_force_per_surface_area'), 'adhesion_force_per_surface_area', '__phenotype_common_adhesion_adhesion_force_per_surface_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 60, 12), )

    
    adhesion_force_per_surface_area = property(__adhesion_force_per_surface_area.value, __adhesion_force_per_surface_area.set, None, None)

    
    # Element adhesion_probability uses Python identifier adhesion_probability
    __adhesion_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adhesion_probability'), 'adhesion_probability', '__phenotype_common_adhesion_adhesion_probability', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 61, 12), )

    
    adhesion_probability = property(__adhesion_probability.value, __adhesion_probability.set, None, '\n                        This is a coarser model of adhesion bond formation rate (or the association rate)\n                    ')

    
    # Element detachment_proability uses Python identifier detachment_proability
    __detachment_proability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'detachment_proability'), 'detachment_proability', '__phenotype_common_adhesion_detachment_proability', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 68, 12), )

    
    detachment_proability = property(__detachment_proability.value, __detachment_proability.set, None, '\n                        This is a coarser model of adhesion bond breaking rate (or the dissociation rate)\n                    ')

    
    # Element rolling_observation uses Python identifier rolling_observation
    __rolling_observation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rolling_observation'), 'rolling_observation', '__phenotype_common_adhesion_rolling_observation', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 75, 12), )

    
    rolling_observation = property(__rolling_observation.value, __rolling_observation.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_adhesion_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 76, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __adhesion_bond_breaking_rate.name() : __adhesion_bond_breaking_rate,
        __adhesion_bond_formation_rate.name() : __adhesion_bond_formation_rate,
        __adhesion_spring_constant.name() : __adhesion_spring_constant,
        __adhesion_receptor_density.name() : __adhesion_receptor_density,
        __surface_binding_energy.name() : __surface_binding_energy,
        __number_of_adhered_cells.name() : __number_of_adhered_cells,
        __maximum_number_of_adhered_cells.name() : __maximum_number_of_adhered_cells,
        __adhered_surface_area.name() : __adhered_surface_area,
        __maximum_adhered_surface_area.name() : __maximum_adhered_surface_area,
        __adhesion_force_per_surface_area.name() : __adhesion_force_per_surface_area,
        __adhesion_probability.name() : __adhesion_probability,
        __detachment_proability.name() : __detachment_proability,
        __rolling_observation.name() : __rolling_observation,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.adhesion = adhesion
Namespace.addCategoryObject('typeBinding', 'adhesion', adhesion)


# Complex type {phenotype_common}rolling_observation with content type ELEMENT_ONLY
class rolling_observation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}rolling_observation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rolling_observation')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 80, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element rolling_velocity uses Python identifier rolling_velocity
    __rolling_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rolling_velocity'), 'rolling_velocity', '__phenotype_common_rolling_observation_rolling_velocity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 82, 12), )

    
    rolling_velocity = property(__rolling_velocity.value, __rolling_velocity.set, None, None)

    
    # Element shear_stress uses Python identifier shear_stress
    __shear_stress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shear_stress'), 'shear_stress', '__phenotype_common_rolling_observation_shear_stress', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 83, 12), )

    
    shear_stress = property(__shear_stress.value, __shear_stress.set, None, None)

    _ElementMap.update({
        __rolling_velocity.name() : __rolling_velocity,
        __shear_stress.name() : __shear_stress
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.rolling_observation = rolling_observation
Namespace.addCategoryObject('typeBinding', 'rolling_observation', rolling_observation)


# Complex type {phenotype_common}friction with content type ELEMENT_ONLY
class friction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}friction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'friction')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 104, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element compression uses Python identifier compression
    __compression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'compression'), 'compression', '__phenotype_common_friction_compression', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 106, 12), )

    
    compression = property(__compression.value, __compression.set, None, None)

    
    # Element ECM uses Python identifier ECM
    __ECM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ECM'), 'ECM', '__phenotype_common_friction_ECM', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 107, 12), )

    
    ECM = property(__ECM.value, __ECM.set, None, None)

    
    # Element shear uses Python identifier shear
    __shear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shear'), 'shear', '__phenotype_common_friction_shear', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 108, 12), )

    
    shear = property(__shear.value, __shear.set, None, None)

    _ElementMap.update({
        __compression.name() : __compression,
        __ECM.name() : __ECM,
        __shear.name() : __shear
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.friction = friction
Namespace.addCategoryObject('typeBinding', 'friction', friction)


# Complex type {phenotype_common}mechanics with content type ELEMENT_ONLY
class mechanics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}mechanics with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mechanics')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 113, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element poisson_ratio uses Python identifier poisson_ratio
    __poisson_ratio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'poisson_ratio'), 'poisson_ratio', '__phenotype_common_mechanics_poisson_ratio', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12), )

    
    poisson_ratio = property(__poisson_ratio.value, __poisson_ratio.set, None, None)

    
    # Element youngs_modulus uses Python identifier youngs_modulus
    __youngs_modulus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'youngs_modulus'), 'youngs_modulus', '__phenotype_common_mechanics_youngs_modulus', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12), )

    
    youngs_modulus = property(__youngs_modulus.value, __youngs_modulus.set, None, '')

    
    # Element friction uses Python identifier friction
    __friction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'friction'), 'friction', '__phenotype_common_mechanics_friction', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 115, 16), )

    
    friction = property(__friction.value, __friction.set, None, None)

    
    # Element maximum_cell_deformation uses Python identifier maximum_cell_deformation
    __maximum_cell_deformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum_cell_deformation'), 'maximum_cell_deformation', '__phenotype_common_mechanics_maximum_cell_deformation', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 116, 16), )

    
    maximum_cell_deformation = property(__maximum_cell_deformation.value, __maximum_cell_deformation.set, None, None)

    
    # Element mechanical_pressure uses Python identifier mechanical_pressure
    __mechanical_pressure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mechanical_pressure'), 'mechanical_pressure', '__phenotype_common_mechanics_mechanical_pressure', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 117, 16), )

    
    mechanical_pressure = property(__mechanical_pressure.value, __mechanical_pressure.set, None, None)

    
    # Element indentation_observation uses Python identifier indentation_observation
    __indentation_observation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'indentation_observation'), 'indentation_observation', '__phenotype_common_mechanics_indentation_observation', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 118, 16), )

    
    indentation_observation = property(__indentation_observation.value, __indentation_observation.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_mechanics_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 120, 16), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __poisson_ratio.name() : __poisson_ratio,
        __youngs_modulus.name() : __youngs_modulus,
        __friction.name() : __friction,
        __maximum_cell_deformation.name() : __maximum_cell_deformation,
        __mechanical_pressure.name() : __mechanical_pressure,
        __indentation_observation.name() : __indentation_observation,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.mechanics = mechanics
Namespace.addCategoryObject('typeBinding', 'mechanics', mechanics)


# Complex type {phenotype_common}indentation_observation with content type ELEMENT_ONLY
class indentation_observation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}indentation_observation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'indentation_observation')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 124, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element poisson_ratio uses Python identifier poisson_ratio
    __poisson_ratio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'poisson_ratio'), 'poisson_ratio', '__phenotype_common_indentation_observation_poisson_ratio', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12), )

    
    poisson_ratio = property(__poisson_ratio.value, __poisson_ratio.set, None, None)

    
    # Element youngs_modulus uses Python identifier youngs_modulus
    __youngs_modulus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'youngs_modulus'), 'youngs_modulus', '__phenotype_common_indentation_observation_youngs_modulus', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12), )

    
    youngs_modulus = property(__youngs_modulus.value, __youngs_modulus.set, None, '')

    
    # Element depth uses Python identifier depth
    __depth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'depth'), 'depth', '__phenotype_common_indentation_observation_depth', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 126, 16), )

    
    depth = property(__depth.value, __depth.set, None, None)

    _ElementMap.update({
        __poisson_ratio.name() : __poisson_ratio,
        __youngs_modulus.name() : __youngs_modulus,
        __depth.name() : __depth
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.indentation_observation = indentation_observation
Namespace.addCategoryObject('typeBinding', 'indentation_observation', indentation_observation)


# Complex type {phenotype_common}motility with content type ELEMENT_ONLY
class motility (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}motility with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'motility')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 131, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element unrestricted uses Python identifier unrestricted
    __unrestricted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'unrestricted'), 'unrestricted', '__phenotype_common_motility_unrestricted', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 133, 16), )

    
    unrestricted = property(__unrestricted.value, __unrestricted.set, None, None)

    
    # Element restricted uses Python identifier restricted
    __restricted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'restricted'), 'restricted', '__phenotype_common_motility_restricted', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 134, 16), )

    
    restricted = property(__restricted.value, __restricted.set, None, '\n                            Need to insert requirement that restricted requires the element restriction.\n                            Should be a key constraint. Something like \n                            xs:key name="required"\n                                xs:selector xpath="restriction" /\n                                xs:field xpath="ID" /\n                            /xs:key\n                        ')

    _ElementMap.update({
        __unrestricted.name() : __unrestricted,
        __restricted.name() : __restricted
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.motility = motility
Namespace.addCategoryObject('typeBinding', 'motility', motility)


# Complex type {phenotype_common}motility_types with content type ELEMENT_ONLY
class motility_types (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}motility_types with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'motility_types')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 149, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element timescale uses Python identifier timescale
    __timescale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'timescale'), 'timescale', '__phenotype_common_motility_types_timescale', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 151, 16), )

    
    timescale = property(__timescale.value, __timescale.set, None, None)

    
    # Element restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'restriction'), 'restriction', '__phenotype_common_motility_types_restriction', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 152, 16), )

    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Element net_displacement uses Python identifier net_displacement
    __net_displacement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_displacement'), 'net_displacement', '__phenotype_common_motility_types_net_displacement', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 153, 16), )

    
    net_displacement = property(__net_displacement.value, __net_displacement.set, None, None)

    
    # Element total_displacement uses Python identifier total_displacement
    __total_displacement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'total_displacement'), 'total_displacement', '__phenotype_common_motility_types_total_displacement', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 154, 16), )

    
    total_displacement = property(__total_displacement.value, __total_displacement.set, None, None)

    
    # Element mean_square_displacement uses Python identifier mean_square_displacement
    __mean_square_displacement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean_square_displacement'), 'mean_square_displacement', '__phenotype_common_motility_types_mean_square_displacement', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 155, 16), )

    
    mean_square_displacement = property(__mean_square_displacement.value, __mean_square_displacement.set, None, None)

    
    # Element mean_speed uses Python identifier mean_speed
    __mean_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean_speed'), 'mean_speed', '__phenotype_common_motility_types_mean_speed', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 156, 16), )

    
    mean_speed = property(__mean_speed.value, __mean_speed.set, None, None)

    
    # Element net_speed uses Python identifier net_speed
    __net_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_speed'), 'net_speed', '__phenotype_common_motility_types_net_speed', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 157, 16), )

    
    net_speed = property(__net_speed.value, __net_speed.set, None, None)

    
    # Element persistence uses Python identifier persistence
    __persistence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'persistence'), 'persistence', '__phenotype_common_motility_types_persistence', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 158, 16), )

    
    persistence = property(__persistence.value, __persistence.set, None, None)

    
    # Element mean_path_length uses Python identifier mean_path_length
    __mean_path_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean_path_length'), 'mean_path_length', '__phenotype_common_motility_types_mean_path_length', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 159, 16), )

    
    mean_path_length = property(__mean_path_length.value, __mean_path_length.set, None, None)

    
    # Element diffusion_coefficient uses Python identifier diffusion_coefficient
    __diffusion_coefficient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diffusion_coefficient'), 'diffusion_coefficient', '__phenotype_common_motility_types_diffusion_coefficient', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 160, 16), )

    
    diffusion_coefficient = property(__diffusion_coefficient.value, __diffusion_coefficient.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_motility_types_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 161, 16), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__phenotype_common_motility_types_ID', pyxb.binding.datatypes.unsignedInt)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 163, 12)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 163, 12)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __timescale.name() : __timescale,
        __restriction.name() : __restriction,
        __net_displacement.name() : __net_displacement,
        __total_displacement.name() : __total_displacement,
        __mean_square_displacement.name() : __mean_square_displacement,
        __mean_speed.name() : __mean_speed,
        __net_speed.name() : __net_speed,
        __persistence.name() : __persistence,
        __mean_path_length.name() : __mean_path_length,
        __diffusion_coefficient.name() : __diffusion_coefficient,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })
_module_typeBindings.motility_types = motility_types
Namespace.addCategoryObject('typeBinding', 'motility_types', motility_types)


# Complex type {phenotype_common}transport_processes with content type ELEMENT_ONLY
class transport_processes (pyxb.binding.basis.complexTypeDefinition):
    """
                    This is known as transport processes in NCIT C21079
                """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transport_processes')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 174, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element variable uses Python identifier variable
    __variable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variable'), 'variable', '__phenotype_common_transport_processes_variable', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 181, 16), )

    
    variable = property(__variable.value, __variable.set, None, None)

    _ElementMap.update({
        __variable.name() : __variable
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.transport_processes = transport_processes
Namespace.addCategoryObject('typeBinding', 'transport_processes', transport_processes)


# Complex type {phenotype_common}geometrical_parameters with content type ELEMENT_ONLY
class geometrical_parameters (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}geometrical_parameters with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geometrical_parameters')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 213, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element aspect_ratio uses Python identifier aspect_ratio
    __aspect_ratio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aspect_ratio'), 'aspect_ratio', '__phenotype_common_geometrical_parameters_aspect_ratio', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 215, 12), )

    
    aspect_ratio = property(__aspect_ratio.value, __aspect_ratio.set, None, None)

    
    # Element circularity uses Python identifier circularity
    __circularity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'circularity'), 'circularity', '__phenotype_common_geometrical_parameters_circularity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 216, 12), )

    
    circularity = property(__circularity.value, __circularity.set, None, None)

    
    # Element eccentricity uses Python identifier eccentricity
    __eccentricity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'eccentricity'), 'eccentricity', '__phenotype_common_geometrical_parameters_eccentricity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 217, 12), )

    
    eccentricity = property(__eccentricity.value, __eccentricity.set, None, None)

    
    # Element sphericity uses Python identifier sphericity
    __sphericity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sphericity'), 'sphericity', '__phenotype_common_geometrical_parameters_sphericity', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 218, 12), )

    
    sphericity = property(__sphericity.value, __sphericity.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_geometrical_parameters_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 219, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__phenotype_common_geometrical_parameters_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        __aspect_ratio.name() : __aspect_ratio,
        __circularity.name() : __circularity,
        __eccentricity.name() : __eccentricity,
        __sphericity.name() : __sphericity,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __units.name() : __units
    })
_module_typeBindings.geometrical_parameters = geometrical_parameters
Namespace.addCategoryObject('typeBinding', 'geometrical_parameters', geometrical_parameters)


# Complex type {phenotype_common}lengths with content type ELEMENT_ONLY
class lengths (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}lengths with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengths')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 224, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element diameter uses Python identifier diameter
    __diameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diameter'), 'diameter', '__phenotype_common_lengths_diameter', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 226, 12), )

    
    diameter = property(__diameter.value, __diameter.set, None, None)

    
    # Element major_axis uses Python identifier major_axis
    __major_axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'major_axis'), 'major_axis', '__phenotype_common_lengths_major_axis', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 227, 12), )

    
    major_axis = property(__major_axis.value, __major_axis.set, None, None)

    
    # Element minor_axis uses Python identifier minor_axis
    __minor_axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'minor_axis'), 'minor_axis', '__phenotype_common_lengths_minor_axis', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 228, 12), )

    
    minor_axis = property(__minor_axis.value, __minor_axis.set, None, None)

    
    # Element perimeter uses Python identifier perimeter
    __perimeter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'perimeter'), 'perimeter', '__phenotype_common_lengths_perimeter', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 229, 12), )

    
    perimeter = property(__perimeter.value, __perimeter.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__phenotype_common_lengths_radius', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 230, 12), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_lengths_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 231, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__phenotype_common_lengths_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        __diameter.name() : __diameter,
        __major_axis.name() : __major_axis,
        __minor_axis.name() : __minor_axis,
        __perimeter.name() : __perimeter,
        __radius.name() : __radius,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __units.name() : __units
    })
_module_typeBindings.lengths = lengths
Namespace.addCategoryObject('typeBinding', 'lengths', lengths)


# Complex type {phenotype_common}areas_3D with content type ELEMENT_ONLY
class areas_3D (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}areas_3D with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areas_3D')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 236, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element free_surface_area uses Python identifier free_surface_area
    __free_surface_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'free_surface_area'), 'free_surface_area', '__phenotype_common_areas_3D_free_surface_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 238, 12), )

    
    free_surface_area = property(__free_surface_area.value, __free_surface_area.set, None, None)

    
    # Element total_surface_area uses Python identifier total_surface_area
    __total_surface_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'total_surface_area'), 'total_surface_area', '__phenotype_common_areas_3D_total_surface_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 239, 12), )

    
    total_surface_area = property(__total_surface_area.value, __total_surface_area.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_areas_3D_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 240, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__phenotype_common_areas_3D_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        __free_surface_area.name() : __free_surface_area,
        __total_surface_area.name() : __total_surface_area,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __units.name() : __units
    })
_module_typeBindings.areas_3D = areas_3D
Namespace.addCategoryObject('typeBinding', 'areas_3D', areas_3D)


# Complex type {phenotype_common}areas_2D with content type ELEMENT_ONLY
class areas_2D (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}areas_2D with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areas_2D')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 245, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element total_area uses Python identifier total_area
    __total_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'total_area'), 'total_area', '__phenotype_common_areas_2D_total_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 247, 12), )

    
    total_area = property(__total_area.value, __total_area.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_areas_2D_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 248, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__phenotype_common_areas_2D_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        __total_area.name() : __total_area,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __units.name() : __units
    })
_module_typeBindings.areas_2D = areas_2D
Namespace.addCategoryObject('typeBinding', 'areas_2D', areas_2D)


# Complex type {phenotype_common}volumes with content type ELEMENT_ONLY
class volumes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}volumes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumes')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 253, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element fluid_volume uses Python identifier fluid_volume
    __fluid_volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fluid_volume'), 'fluid_volume', '__phenotype_common_volumes_fluid_volume', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 255, 12), )

    
    fluid_volume = property(__fluid_volume.value, __fluid_volume.set, None, None)

    
    # Element fluid_volume_fraction uses Python identifier fluid_volume_fraction
    __fluid_volume_fraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fluid_volume_fraction'), 'fluid_volume_fraction', '__phenotype_common_volumes_fluid_volume_fraction', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 256, 12), )

    
    fluid_volume_fraction = property(__fluid_volume_fraction.value, __fluid_volume_fraction.set, None, None)

    
    # Element solid_calcified_volume uses Python identifier solid_calcified_volume
    __solid_calcified_volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'solid_calcified_volume'), 'solid_calcified_volume', '__phenotype_common_volumes_solid_calcified_volume', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 257, 12), )

    
    solid_calcified_volume = property(__solid_calcified_volume.value, __solid_calcified_volume.set, None, None)

    
    # Element solid_volume uses Python identifier solid_volume
    __solid_volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'solid_volume'), 'solid_volume', '__phenotype_common_volumes_solid_volume', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 258, 12), )

    
    solid_volume = property(__solid_volume.value, __solid_volume.set, None, None)

    
    # Element solid_volume_fraction uses Python identifier solid_volume_fraction
    __solid_volume_fraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'solid_volume_fraction'), 'solid_volume_fraction', '__phenotype_common_volumes_solid_volume_fraction', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 259, 12), )

    
    solid_volume_fraction = property(__solid_volume_fraction.value, __solid_volume_fraction.set, None, None)

    
    # Element total_volume uses Python identifier total_volume
    __total_volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'total_volume'), 'total_volume', '__phenotype_common_volumes_total_volume', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 260, 12), )

    
    total_volume = property(__total_volume.value, __total_volume.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_volumes_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 261, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__phenotype_common_volumes_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/common.xsd', 20, 8)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        __fluid_volume.name() : __fluid_volume,
        __fluid_volume_fraction.name() : __fluid_volume_fraction,
        __solid_calcified_volume.name() : __solid_calcified_volume,
        __solid_volume.name() : __solid_volume,
        __solid_volume_fraction.name() : __solid_volume_fraction,
        __total_volume.name() : __total_volume,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __units.name() : __units
    })
_module_typeBindings.volumes = volumes
Namespace.addCategoryObject('typeBinding', 'volumes', volumes)


# Complex type {phenotype_common}geometrical_properties with content type ELEMENT_ONLY
class geometrical_properties (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}geometrical_properties with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geometrical_properties')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 267, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parameters'), 'parameters', '__phenotype_common_geometrical_properties_parameters', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 269, 12), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    
    # Element lengths uses Python identifier lengths
    __lengths = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lengths'), 'lengths', '__phenotype_common_geometrical_properties_lengths', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 270, 12), )

    
    lengths = property(__lengths.value, __lengths.set, None, None)

    
    # Element areas uses Python identifier areas
    __areas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'areas'), 'areas', '__phenotype_common_geometrical_properties_areas', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 271, 12), )

    
    areas = property(__areas.value, __areas.set, None, None)

    
    # Element volumes uses Python identifier volumes
    __volumes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'volumes'), 'volumes', '__phenotype_common_geometrical_properties_volumes', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 272, 12), )

    
    volumes = property(__volumes.value, __volumes.set, None, None)

    
    # Element cross_section uses Python identifier cross_section
    __cross_section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cross_section'), 'cross_section', '__phenotype_common_geometrical_properties_cross_section', True, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 273, 12), )

    
    cross_section = property(__cross_section.value, __cross_section.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_geometrical_properties_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 274, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __parameters.name() : __parameters,
        __lengths.name() : __lengths,
        __areas.name() : __areas,
        __volumes.name() : __volumes,
        __cross_section.name() : __cross_section,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.geometrical_properties = geometrical_properties
Namespace.addCategoryObject('typeBinding', 'geometrical_properties', geometrical_properties)


# Complex type {phenotype_common}cross_section with content type ELEMENT_ONLY
class cross_section (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}cross_section with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cross_section')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 278, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parameters'), 'parameters', '__phenotype_common_cross_section_parameters', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 280, 12), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    
    # Element lengths uses Python identifier lengths
    __lengths = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lengths'), 'lengths', '__phenotype_common_cross_section_lengths', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 281, 12), )

    
    lengths = property(__lengths.value, __lengths.set, None, None)

    
    # Element areas uses Python identifier areas
    __areas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'areas'), 'areas', '__phenotype_common_cross_section_areas', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 282, 12), )

    
    areas = property(__areas.value, __areas.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_cross_section_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 283, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    _ElementMap.update({
        __parameters.name() : __parameters,
        __lengths.name() : __lengths,
        __areas.name() : __areas,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cross_section = cross_section
Namespace.addCategoryObject('typeBinding', 'cross_section', cross_section)


# Complex type {phenotype_common}mass with content type ELEMENT_ONLY
class mass (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}mass with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mass')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 297, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element biomass uses Python identifier biomass
    __biomass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'biomass'), 'biomass', '__phenotype_common_mass_biomass', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 299, 12), )

    
    biomass = property(__biomass.value, __biomass.set, None, None)

    
    # Element fluid_mass uses Python identifier fluid_mass
    __fluid_mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fluid_mass'), 'fluid_mass', '__phenotype_common_mass_fluid_mass', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 300, 12), )

    
    fluid_mass = property(__fluid_mass.value, __fluid_mass.set, None, None)

    
    # Element total_mass uses Python identifier total_mass
    __total_mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'total_mass'), 'total_mass', '__phenotype_common_mass_total_mass', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 301, 12), )

    
    total_mass = property(__total_mass.value, __total_mass.set, None, None)

    _ElementMap.update({
        __biomass.name() : __biomass,
        __fluid_mass.name() : __fluid_mass,
        __total_mass.name() : __total_mass
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.mass = mass
Namespace.addCategoryObject('typeBinding', 'mass', mass)


# Complex type {phenotype_common}transport_variable with content type ELEMENT_ONLY
class transport_variable (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {phenotype_common}transport_variable with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transport_variable')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 185, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element export_rate uses Python identifier export_rate
    __export_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'export_rate'), 'export_rate', '__phenotype_common_transport_variable_export_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 187, 12), )

    
    export_rate = property(__export_rate.value, __export_rate.set, None, None)

    
    # Element export_rate_per_unit_surface_area uses Python identifier export_rate_per_unit_surface_area
    __export_rate_per_unit_surface_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'export_rate_per_unit_surface_area'), 'export_rate_per_unit_surface_area', '__phenotype_common_transport_variable_export_rate_per_unit_surface_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 188, 12), )

    
    export_rate_per_unit_surface_area = property(__export_rate_per_unit_surface_area.value, __export_rate_per_unit_surface_area.set, None, None)

    
    # Element import_rate uses Python identifier import_rate
    __import_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'import_rate'), 'import_rate', '__phenotype_common_transport_variable_import_rate', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 189, 12), )

    
    import_rate = property(__import_rate.value, __import_rate.set, None, None)

    
    # Element import_rate_per_unit_surface_area uses Python identifier import_rate_per_unit_surface_area
    __import_rate_per_unit_surface_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'import_rate_per_unit_surface_area'), 'import_rate_per_unit_surface_area', '__phenotype_common_transport_variable_import_rate_per_unit_surface_area', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 190, 12), )

    
    import_rate_per_unit_surface_area = property(__import_rate_per_unit_surface_area.value, __import_rate_per_unit_surface_area.set, None, None)

    
    # Element saturation_density uses Python identifier saturation_density
    __saturation_density = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'saturation_density'), 'saturation_density', '__phenotype_common_transport_variable_saturation_density', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 191, 12), )

    
    saturation_density = property(__saturation_density.value, __saturation_density.set, None, None)

    
    # Element custom uses Python identifier custom
    __custom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'custom'), 'custom', '__phenotype_common_transport_variable_custom', False, pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 192, 12), )

    
    custom = property(__custom.value, __custom.set, None, None)

    
    # Attribute ChEBI_ID uses Python identifier ChEBI_ID
    __ChEBI_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ChEBI_ID'), 'ChEBI_ID', '__phenotype_common_transport_variable_ChEBI_ID', pyxb.binding.datatypes.string)
    __ChEBI_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    __ChEBI_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 65, 8)
    
    ChEBI_ID = property(__ChEBI_ID.value, __ChEBI_ID.set, None, None)

    
    # Attribute MeSH_ID uses Python identifier MeSH_ID
    __MeSH_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MeSH_ID'), 'MeSH_ID', '__phenotype_common_transport_variable_MeSH_ID', pyxb.binding.datatypes.string)
    __MeSH_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    __MeSH_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 66, 8)
    
    MeSH_ID = property(__MeSH_ID.value, __MeSH_ID.set, None, None)

    
    # Attribute DrugBank_ID uses Python identifier DrugBank_ID
    __DrugBank_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DrugBank_ID'), 'DrugBank_ID', '__phenotype_common_transport_variable_DrugBank_ID', pyxb.binding.datatypes.string)
    __DrugBank_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    __DrugBank_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 67, 8)
    
    DrugBank_ID = property(__DrugBank_ID.value, __DrugBank_ID.set, None, None)

    
    # Attribute GMO_ID uses Python identifier GMO_ID
    __GMO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GMO_ID'), 'GMO_ID', '__phenotype_common_transport_variable_GMO_ID', pyxb.binding.datatypes.string)
    __GMO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    __GMO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 68, 8)
    
    GMO_ID = property(__GMO_ID.value, __GMO_ID.set, None, None)

    
    # Attribute GO_ID uses Python identifier GO_ID
    __GO_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GO_ID'), 'GO_ID', '__phenotype_common_transport_variable_GO_ID', pyxb.binding.datatypes.string)
    __GO_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    __GO_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 69, 8)
    
    GO_ID = property(__GO_ID.value, __GO_ID.set, None, None)

    
    # Attribute UniProt_ID uses Python identifier UniProt_ID
    __UniProt_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UniProt_ID'), 'UniProt_ID', '__phenotype_common_transport_variable_UniProt_ID', pyxb.binding.datatypes.string)
    __UniProt_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    __UniProt_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 70, 8)
    
    UniProt_ID = property(__UniProt_ID.value, __UniProt_ID.set, None, None)

    
    # Attribute PR_ID uses Python identifier PR_ID
    __PR_ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PR_ID'), 'PR_ID', '__phenotype_common_transport_variable_PR_ID', pyxb.binding.datatypes.string)
    __PR_ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    __PR_ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 71, 8)
    
    PR_ID = property(__PR_ID.value, __PR_ID.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__phenotype_common_transport_variable_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 75, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 75, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__phenotype_common_transport_variable_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 76, 8)
    __units._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 76, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__phenotype_common_transport_variable_ID', pyxb.binding.datatypes.unsignedLong)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 77, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 77, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__phenotype_common_transport_variable_type', _ImportedBinding_var.amount_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 78, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/variables.xsd', 78, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __export_rate.name() : __export_rate,
        __export_rate_per_unit_surface_area.name() : __export_rate_per_unit_surface_area,
        __import_rate.name() : __import_rate,
        __import_rate_per_unit_surface_area.name() : __import_rate_per_unit_surface_area,
        __saturation_density.name() : __saturation_density,
        __custom.name() : __custom
    })
    _AttributeMap.update({
        __ChEBI_ID.name() : __ChEBI_ID,
        __MeSH_ID.name() : __MeSH_ID,
        __DrugBank_ID.name() : __DrugBank_ID,
        __GMO_ID.name() : __GMO_ID,
        __GO_ID.name() : __GO_ID,
        __UniProt_ID.name() : __UniProt_ID,
        __PR_ID.name() : __PR_ID,
        __name.name() : __name,
        __units.name() : __units,
        __ID.name() : __ID,
        __type.name() : __type
    })
_module_typeBindings.transport_variable = transport_variable
Namespace.addCategoryObject('typeBinding', 'transport_variable', transport_variable)


# Complex type {phenotype_common}timescale with content type SIMPLE
class timescale (_ImportedBinding_common.units_decimal):
    """Complex type {phenotype_common}timescale with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timescale')
    _XSDLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 166, 8)
    _ElementMap = _ImportedBinding_common.units_decimal._ElementMap.copy()
    _AttributeMap = _ImportedBinding_common.units_decimal._AttributeMap.copy()
    # Base type is _ImportedBinding_common.units_decimal
    
    # Attribute units inherited from {common}units_decimal
    
    # Attribute measurement_type inherited from {common}units_decimal
    
    # Attribute uncertainty inherited from {common}units_decimal
    
    # Attribute negative_uncertainty inherited from {common}units_decimal
    
    # Attribute positive_uncertainty inherited from {common}units_decimal
    
    # Attribute uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute negative_uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute positive_uncertainty_percentage inherited from {common}units_decimal
    
    # Attribute median inherited from {common}units_decimal
    
    # Attribute standard_deviation inherited from {common}units_decimal
    
    # Attribute interquartile_range inherited from {common}units_decimal
    
    # Attribute range inherited from {common}units_decimal
    
    # Attribute min inherited from {common}units_decimal
    
    # Attribute max inherited from {common}units_decimal
    
    # Attribute standard_error inherited from {common}units_decimal
    
    # Attribute standard_error_of_the_mean inherited from {common}units_decimal
    
    # Attribute number_obs inherited from {common}units_decimal
    
    # Attribute skewnesss inherited from {common}units_decimal
    
    # Attribute kurtosis inherited from {common}units_decimal
    
    # Attribute mitotic uses Python identifier mitotic
    __mitotic = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mitotic'), 'mitotic', '__phenotype_common_timescale_mitotic', pyxb.binding.datatypes.boolean)
    __mitotic._DeclarationLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 169, 20)
    __mitotic._UseLocation = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 169, 20)
    
    mitotic = property(__mitotic.value, __mitotic.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mitotic.name() : __mitotic
    })
_module_typeBindings.timescale = timescale
Namespace.addCategoryObject('typeBinding', 'timescale', timescale)




adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion_bond_breaking_rate'), _ImportedBinding_common.units_decimal, scope=adhesion, documentation='\n                        This is also known as the dissocation rate\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 33, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion_bond_formation_rate'), _ImportedBinding_common.units_decimal, scope=adhesion, documentation='\n                        This is also known as the bimolecular association rate\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 40, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion_spring_constant'), _ImportedBinding_common.units_decimal_nonnegative, scope=adhesion, documentation='\n                        Hook-ian spring constant for a binding molecule.\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 47, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion_receptor_density'), _ImportedBinding_common.units_decimal_nonnegative, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 54, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'surface_binding_energy'), _ImportedBinding_common.units_decimal, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 55, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number_of_adhered_cells'), _ImportedBinding_common.units_decimal_nonnegative, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 56, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum_number_of_adhered_cells'), _ImportedBinding_common.units_unsignedShort, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 57, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhered_surface_area'), _ImportedBinding_common.units_decimal_nonnegative, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 58, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum_adhered_surface_area'), _ImportedBinding_common.units_decimal_nonnegative, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 59, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion_force_per_surface_area'), _ImportedBinding_common.units_decimal, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 60, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adhesion_probability'), _ImportedBinding_common.units_fraction, scope=adhesion, documentation='\n                        This is a coarser model of adhesion bond formation rate (or the association rate)\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 61, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'detachment_proability'), _ImportedBinding_common.units_fraction, scope=adhesion, documentation='\n                        This is a coarser model of adhesion bond breaking rate (or the dissociation rate)\n                    ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 68, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rolling_observation'), rolling_observation, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 75, 12)))

adhesion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=adhesion, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 76, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 33, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 40, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 47, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 54, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 55, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 56, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 57, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 58, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 59, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 60, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 61, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 68, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 75, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 76, 12))
    counters.add(cc_13)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion_bond_breaking_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 33, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion_bond_formation_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 40, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion_spring_constant')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 47, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion_receptor_density')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 54, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'surface_binding_energy')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 55, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'number_of_adhered_cells')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 56, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum_number_of_adhered_cells')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 57, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'adhered_surface_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 58, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum_adhered_surface_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 59, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion_force_per_surface_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 60, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'adhesion_probability')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 61, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'detachment_proability')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 68, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'rolling_observation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 75, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(adhesion._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 76, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
adhesion._Automaton = _BuildAutomaton()




rolling_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rolling_velocity'), _ImportedBinding_common.units_decimal, scope=rolling_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 82, 12)))

rolling_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shear_stress'), _ImportedBinding_common.units_decimal, scope=rolling_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 83, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(rolling_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'rolling_velocity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 82, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(rolling_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'shear_stress')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 83, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
rolling_observation._Automaton = _BuildAutomaton_()




friction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'compression'), _ImportedBinding_common.units_decimal_nonnegative, scope=friction, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 106, 12)))

friction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ECM'), _ImportedBinding_common.units_decimal_nonnegative, scope=friction, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 107, 12)))

friction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shear'), _ImportedBinding_common.units_decimal_nonnegative, scope=friction, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 108, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 106, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 107, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 108, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(friction._UseForTag(pyxb.namespace.ExpandedName(None, 'compression')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 106, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(friction._UseForTag(pyxb.namespace.ExpandedName(None, 'ECM')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 107, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(friction._UseForTag(pyxb.namespace.ExpandedName(None, 'shear')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 108, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
friction._Automaton = _BuildAutomaton_2()




mechanics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'poisson_ratio'), _ImportedBinding_common.units_decimal, scope=mechanics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12)))

mechanics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'youngs_modulus'), _ImportedBinding_common.units_decimal, scope=mechanics, documentation='', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12)))

mechanics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'friction'), friction, scope=mechanics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 115, 16)))

mechanics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum_cell_deformation'), _ImportedBinding_common.units_decimal, scope=mechanics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 116, 16)))

mechanics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mechanical_pressure'), _ImportedBinding_common.units_decimal, scope=mechanics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 117, 16)))

mechanics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'indentation_observation'), indentation_observation, scope=mechanics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 118, 16)))

mechanics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=mechanics, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 120, 16)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 115, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 116, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 117, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 118, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 120, 16))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mechanics._UseForTag(pyxb.namespace.ExpandedName(None, 'friction')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 115, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mechanics._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum_cell_deformation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 116, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mechanics._UseForTag(pyxb.namespace.ExpandedName(None, 'mechanical_pressure')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 117, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mechanics._UseForTag(pyxb.namespace.ExpandedName(None, 'indentation_observation')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 118, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mechanics._UseForTag(pyxb.namespace.ExpandedName(None, 'poisson_ratio')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mechanics._UseForTag(pyxb.namespace.ExpandedName(None, 'youngs_modulus')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(mechanics._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 120, 16))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mechanics._Automaton = _BuildAutomaton_3()




indentation_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'poisson_ratio'), _ImportedBinding_common.units_decimal, scope=indentation_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12)))

indentation_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'youngs_modulus'), _ImportedBinding_common.units_decimal, scope=indentation_observation, documentation='', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12)))

indentation_observation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'depth'), _ImportedBinding_common.units_decimal, scope=indentation_observation, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 126, 16)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(indentation_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'depth')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 126, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(indentation_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'poisson_ratio')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 89, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(indentation_observation._UseForTag(pyxb.namespace.ExpandedName(None, 'youngs_modulus')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 90, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
indentation_observation._Automaton = _BuildAutomaton_4()




motility._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'unrestricted'), motility_types, scope=motility, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 133, 16)))

motility._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restricted'), motility_types, scope=motility, documentation='\n                            Need to insert requirement that restricted requires the element restriction.\n                            Should be a key constraint. Something like \n                            xs:key name="required"\n                                xs:selector xpath="restriction" /\n                                xs:field xpath="ID" /\n                            /xs:key\n                        ', location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 134, 16)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 133, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 134, 16))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(motility._UseForTag(pyxb.namespace.ExpandedName(None, 'unrestricted')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 133, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(motility._UseForTag(pyxb.namespace.ExpandedName(None, 'restricted')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 134, 16))
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
motility._Automaton = _BuildAutomaton_5()




motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'timescale'), timescale, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 151, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restriction'), _ImportedBinding_var.experimental_conditions, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 152, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_displacement'), _ImportedBinding_common.units_decimal, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 153, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'total_displacement'), _ImportedBinding_common.units_decimal_nonnegative, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 154, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean_square_displacement'), _ImportedBinding_common.units_decimal_nonnegative, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 155, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean_speed'), _ImportedBinding_common.units_decimal, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 156, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_speed'), _ImportedBinding_common.units_decimal, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 157, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'persistence'), _ImportedBinding_common.units_decimal, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 158, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean_path_length'), _ImportedBinding_common.units_decimal, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 159, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diffusion_coefficient'), _ImportedBinding_common.units_decimal, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 160, 16)))

motility_types._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=motility_types, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 161, 16)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 151, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 152, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 153, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 154, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 155, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 156, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 157, 16))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 158, 16))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 159, 16))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 160, 16))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 161, 16))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'timescale')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 151, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'restriction')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 152, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'net_displacement')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 153, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'total_displacement')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 154, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'mean_square_displacement')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 155, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'mean_speed')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 156, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'net_speed')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 157, 16))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'persistence')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 158, 16))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'mean_path_length')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 159, 16))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'diffusion_coefficient')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 160, 16))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(motility_types._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 161, 16))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
motility_types._Automaton = _BuildAutomaton_6()




transport_processes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variable'), transport_variable, scope=transport_processes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 181, 16)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(transport_processes._UseForTag(pyxb.namespace.ExpandedName(None, 'variable')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 181, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
transport_processes._Automaton = _BuildAutomaton_7()




geometrical_parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aspect_ratio'), _ImportedBinding_common.units_decimal_nonnegative, scope=geometrical_parameters, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 215, 12)))

geometrical_parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'circularity'), _ImportedBinding_common.units_decimal_nonnegative, scope=geometrical_parameters, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 216, 12)))

geometrical_parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'eccentricity'), _ImportedBinding_common.units_decimal_nonnegative, scope=geometrical_parameters, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 217, 12)))

geometrical_parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sphericity'), _ImportedBinding_common.units_decimal_nonnegative, scope=geometrical_parameters, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 218, 12)))

geometrical_parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=geometrical_parameters, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 219, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 215, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'aspect_ratio')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 215, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 216, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'circularity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 216, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 217, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'eccentricity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 217, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 218, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'sphericity')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 218, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 219, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 219, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 215, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 216, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 217, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 218, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 219, 12))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_9())
    sub_automata.append(_BuildAutomaton_10())
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 214, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
geometrical_parameters._Automaton = _BuildAutomaton_8()




lengths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diameter'), _ImportedBinding_common.units_decimal_nonnegative, scope=lengths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 226, 12)))

lengths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'major_axis'), _ImportedBinding_common.units_decimal_nonnegative, scope=lengths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 227, 12)))

lengths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'minor_axis'), _ImportedBinding_common.units_decimal_nonnegative, scope=lengths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 228, 12)))

lengths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'perimeter'), _ImportedBinding_common.units_decimal_nonnegative, scope=lengths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 229, 12)))

lengths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), _ImportedBinding_common.units_decimal_nonnegative, scope=lengths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 230, 12)))

lengths._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=lengths, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 231, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 226, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lengths._UseForTag(pyxb.namespace.ExpandedName(None, 'diameter')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 226, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 227, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lengths._UseForTag(pyxb.namespace.ExpandedName(None, 'major_axis')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 227, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 228, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lengths._UseForTag(pyxb.namespace.ExpandedName(None, 'minor_axis')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 228, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 229, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lengths._UseForTag(pyxb.namespace.ExpandedName(None, 'perimeter')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 229, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 230, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lengths._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 230, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 231, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lengths._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 231, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 226, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 227, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 228, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 229, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 230, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 231, 12))
    counters.add(cc_5)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 225, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
lengths._Automaton = _BuildAutomaton_14()




areas_3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'free_surface_area'), _ImportedBinding_common.units_decimal_nonnegative, scope=areas_3D, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 238, 12)))

areas_3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'total_surface_area'), _ImportedBinding_common.units_decimal_nonnegative, scope=areas_3D, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 239, 12)))

areas_3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=areas_3D, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 240, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 238, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(areas_3D._UseForTag(pyxb.namespace.ExpandedName(None, 'free_surface_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 238, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 239, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(areas_3D._UseForTag(pyxb.namespace.ExpandedName(None, 'total_surface_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 239, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 240, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(areas_3D._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 240, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 238, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 239, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 240, 12))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 237, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
areas_3D._Automaton = _BuildAutomaton_21()




areas_2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'total_area'), _ImportedBinding_common.units_decimal_nonnegative, scope=areas_2D, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 247, 12)))

areas_2D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=areas_2D, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 248, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 247, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(areas_2D._UseForTag(pyxb.namespace.ExpandedName(None, 'total_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 247, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 248, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(areas_2D._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 248, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 247, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 248, 12))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_26())
    sub_automata.append(_BuildAutomaton_27())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 246, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
areas_2D._Automaton = _BuildAutomaton_25()




volumes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fluid_volume'), _ImportedBinding_common.units_decimal_nonnegative, scope=volumes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 255, 12)))

volumes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fluid_volume_fraction'), _ImportedBinding_common.units_fraction, scope=volumes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 256, 12)))

volumes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'solid_calcified_volume'), _ImportedBinding_common.units_decimal_nonnegative, scope=volumes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 257, 12)))

volumes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'solid_volume'), _ImportedBinding_common.units_decimal_nonnegative, scope=volumes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 258, 12)))

volumes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'solid_volume_fraction'), _ImportedBinding_common.units_fraction, scope=volumes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 259, 12)))

volumes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'total_volume'), _ImportedBinding_common.units_decimal_nonnegative, scope=volumes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 260, 12)))

volumes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=volumes, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 261, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 255, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumes._UseForTag(pyxb.namespace.ExpandedName(None, 'fluid_volume')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 255, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 256, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumes._UseForTag(pyxb.namespace.ExpandedName(None, 'fluid_volume_fraction')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 256, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 257, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumes._UseForTag(pyxb.namespace.ExpandedName(None, 'solid_calcified_volume')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 257, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 258, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumes._UseForTag(pyxb.namespace.ExpandedName(None, 'solid_volume')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 258, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 259, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumes._UseForTag(pyxb.namespace.ExpandedName(None, 'solid_volume_fraction')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 259, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 260, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumes._UseForTag(pyxb.namespace.ExpandedName(None, 'total_volume')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 260, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 261, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(volumes._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 261, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 255, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 256, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 257, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 258, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 259, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 260, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 261, 12))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_29())
    sub_automata.append(_BuildAutomaton_30())
    sub_automata.append(_BuildAutomaton_31())
    sub_automata.append(_BuildAutomaton_32())
    sub_automata.append(_BuildAutomaton_33())
    sub_automata.append(_BuildAutomaton_34())
    sub_automata.append(_BuildAutomaton_35())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 254, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
volumes._Automaton = _BuildAutomaton_28()




geometrical_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parameters'), geometrical_parameters, scope=geometrical_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 269, 12)))

geometrical_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lengths'), lengths, scope=geometrical_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 270, 12)))

geometrical_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'areas'), areas_3D, scope=geometrical_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 271, 12)))

geometrical_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'volumes'), volumes, scope=geometrical_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 272, 12)))

geometrical_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cross_section'), cross_section, scope=geometrical_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 273, 12)))

geometrical_properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=geometrical_properties, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 274, 12)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 269, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 270, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 271, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 272, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 273, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 274, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'parameters')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 269, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'lengths')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 270, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'areas')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 271, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'volumes')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 272, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'cross_section')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 273, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(geometrical_properties._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 274, 12))
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
geometrical_properties._Automaton = _BuildAutomaton_36()




cross_section._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parameters'), geometrical_parameters, scope=cross_section, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 280, 12)))

cross_section._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lengths'), lengths, scope=cross_section, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 281, 12)))

cross_section._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'areas'), areas_2D, scope=cross_section, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 282, 12)))

cross_section._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=cross_section, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 283, 12)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 280, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 281, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 282, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 283, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cross_section._UseForTag(pyxb.namespace.ExpandedName(None, 'parameters')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 280, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cross_section._UseForTag(pyxb.namespace.ExpandedName(None, 'lengths')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 281, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cross_section._UseForTag(pyxb.namespace.ExpandedName(None, 'areas')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 282, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cross_section._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 283, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cross_section._Automaton = _BuildAutomaton_37()




mass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'biomass'), _ImportedBinding_common.units_decimal_nonnegative, scope=mass, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 299, 12)))

mass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fluid_mass'), _ImportedBinding_common.units_decimal_nonnegative, scope=mass, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 300, 12)))

mass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'total_mass'), _ImportedBinding_common.units_decimal_nonnegative, scope=mass, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 301, 12)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 299, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mass._UseForTag(pyxb.namespace.ExpandedName(None, 'biomass')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 299, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 300, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mass._UseForTag(pyxb.namespace.ExpandedName(None, 'fluid_mass')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 300, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 301, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mass._UseForTag(pyxb.namespace.ExpandedName(None, 'total_mass')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 301, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 299, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 300, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 301, 12))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_39())
    sub_automata.append(_BuildAutomaton_40())
    sub_automata.append(_BuildAutomaton_41())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 298, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mass._Automaton = _BuildAutomaton_38()




transport_variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'export_rate'), _ImportedBinding_common.units_decimal, scope=transport_variable, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 187, 12)))

transport_variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'export_rate_per_unit_surface_area'), _ImportedBinding_common.units_decimal, scope=transport_variable, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 188, 12)))

transport_variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'import_rate'), _ImportedBinding_common.units_decimal, scope=transport_variable, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 189, 12)))

transport_variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'import_rate_per_unit_surface_area'), _ImportedBinding_common.units_decimal, scope=transport_variable, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 190, 12)))

transport_variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'saturation_density'), _ImportedBinding_common.units_decimal, scope=transport_variable, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 191, 12)))

transport_variable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'custom'), _ImportedBinding_common.custom, scope=transport_variable, location=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 192, 12)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 187, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transport_variable._UseForTag(pyxb.namespace.ExpandedName(None, 'export_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 187, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 188, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transport_variable._UseForTag(pyxb.namespace.ExpandedName(None, 'export_rate_per_unit_surface_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 188, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 189, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transport_variable._UseForTag(pyxb.namespace.ExpandedName(None, 'import_rate')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 189, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 190, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transport_variable._UseForTag(pyxb.namespace.ExpandedName(None, 'import_rate_per_unit_surface_area')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 190, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 191, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transport_variable._UseForTag(pyxb.namespace.ExpandedName(None, 'saturation_density')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 191, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 192, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(transport_variable._UseForTag(pyxb.namespace.ExpandedName(None, 'custom')), pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 192, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 186, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 187, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 188, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 189, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 190, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 191, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 192, 12))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_43())
    sub_automata.append(_BuildAutomaton_44())
    sub_automata.append(_BuildAutomaton_45())
    sub_automata.append(_BuildAutomaton_46())
    sub_automata.append(_BuildAutomaton_47())
    sub_automata.append(_BuildAutomaton_48())
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.utils.utility.Location('/home/samuel/codes/MultiCellDS/v0.5/v0.5.0/phenotype_common.xsd', 186, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
transport_variable._Automaton = _BuildAutomaton_42()

