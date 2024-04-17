#pragma once

#ifdef _MOCK_ADHESION_INDEX_HPP_
#include _MOCK_ADHESION_INDEX_HPP_
#else

#include "ecm_boundary_state.hpp"
#include "ecm_interaction_tracker.hpp"
#include "vec2.hpp"
#include "force_calculation.hpp"
#include "act.hpp"

#include <unordered_map>
#include <vector>

/** A bond from the perspective of a particle it's attached to.
 *
 * This also implements the linear-spring physics of the bonds.
 */
struct AttachedBond {
    /** Create an AttachedBond.
     *
     * @param neighbour Position of the bonded neighbour
     * @param bond_type Type (properties) of the bond
     */
    AttachedBond(ParPos const & neighbour, BondType const & bond_type);

    /// Position of the neighbouring particle
    ParPos neighbour;

    /// The physical properties of the bond's linear spring
    BondType bond_type;

    /** Calculate the work required to move the focal particle
     *
     * @param from The old location of the focal particle
     * @param to The new location of the focal particle
     * @return The required work (energy difference)
     */
    double move_dh(ParPos from, ParPos to) const;
};


/** An angle constraint from the perspective of a particle it acts on.
 *
 * This also implements the torsion-spring physics of the constraint.
 */
struct AttachedAngleCst {
    /** Create an AttachedAngleCst.
     *
     * @param middle Position and type of the middle particle
     * @param far Position and type of the far particle
     * @param angle_cst_type Type (properties) of the angle constraint
     */
    AttachedAngleCst(
            ParPos const & middle, ParPos const & far,
            AngleCstType const & angle_cst_type);

    /// The other particles in the constraint
    ParPos middle, far;

    /// The physical properties of the torsion spring
    AngleCstType angle_cst_type;

    /** Calculate the work required to move the focal particle
     *
     * @param from The old location of the focal particle
     * @param to The new location of the focal particle
     * @return The required work (energy difference)
     */
    double move_dh(ParPos from, ParPos to) const;
};


/** Represents an adhesion particle and its interface with the ECM.
 *
 * This computes the influence of the ECM on the adhesion.
 */
struct AdhesionWithEnvironment {
    /** Create an AdhesionWithEnvironment.
     *
     * @param position Position of the adhesion particle
     */
    AdhesionWithEnvironment(ParId par_id, ParPos const & position, Integrin size = 1, double myosin_force_fraction = 0.1);

    /// Adhesion particle id
    ParId par_id;

    /// Adhesion particle position
    ParPos position;
    
    /// Number of bound Integrin
    Integrin size;
    
    /// Tension on adhesion
    double tension;
    
    /// Force fraction applied by myosin
    double myosin_force_fraction;

    /// Bond constraints for this particle
    std::vector<AttachedBond> bonds;

    /// Angle constraints for this particle
    std::vector<AttachedAngleCst> angle_csts;

    /** Calculate the work required to move the particle
     *
     * @param from The old location of the particle
     * @param to The new location of the particle
     * @return The required work (energy difference)
     */
    double move_dh(PixelDisplacement move) const;
};


/** Tracks location of adhesions in the ECM grid.
 *
 * This class provides the adhesion particles and their bonds and angle
 * constraints per ECM pixel, in a format that allows for efficient force
 * calculations. Bonds or angle constraints involving other particles that
 * are themselves adhesions or that are excluded are ignored.
 */
class AdhesionIndex {
    public:
        /** Rebuild the cached data to match the ECM boundary again.
         *
         * This must be called after every change to the ECM, except for
         * changes that only move adhesions from one pixel to another, for
         * which move_adhesions() should be used because it's more efficient.
         *
         * @param ecm_boundary The current state of the ECM boundary
         */
        void rebuild(ECMBoundaryState const & ecm_boundary);

        /** Get adhesions at a given pixel.
         *
         * Note that this function returns a reference to a vector. This
         * reference will be invalidated by any subsequent call to update() or
         * move_adhesions() on this object.
         *
         * @param pixel Pixel for which to get adhesions.
         */
        std::vector<AdhesionWithEnvironment> const & get_adhesions(
                PixelPos pixel) const;

        /** Move adhesions from one pixel to another.
         *
         * This modifies only the cache, the ECM needs to be updated
         * separately.
         *
         * @param from Pixel to move adhesions from
         * @param to Pixel to move adhesions to
         */
        void move_adhesions(PixelPos from, PixelPos to);
        
        /** Moves a single adhesion to a place
         * 
         * Note, the from parameter is needed because of the way adhesion are stored in this class. 
         * TODO: refactor this.
         * 
        */
        void move_adhesion(ParId who, PixelPos from, ParPos to);

        /** Remove adhesions at the given pixel.
         *
         * This modifies only the cache, the ECM needs to be updated
         * separately.
         *
         * @param pixel Pixel to move adhesions from
         */
        void remove_adhesions(PixelPos pixel);

        /** Get accumulated changes to the adhesions.
         *
         * AdhesionIndex keeps track of any changes to the adhesions it applies.
         * This function returns the accumulated changes.
         */
         CellECMInteractions get_cell_ecm_interactions() const;

        /** Reset the adhesion change administration.
         *
         * This clears the recorded adhesion change history.
         */
        void reset_cell_ecm_interactions();
        
        const std::unordered_map<
            PixelPos, std::vector<AdhesionWithEnvironment>> get_all_adhesions() const;
        
        void remove_adhesion(ParId Particle);
        
        /** Set the myosin concentration based on the actfield value.
         * 
         * @param act_field Actin field on which myosin is based.
        */
        void set_myosin(const ACT::ActField);

        /// Helper function in rebuild(), run before  setting_size.
        void setting_force_on_adhesions(std::vector<ParPos> midpoints, int** sigma);
        
        /// Helper function in rebuild(), run after setting_force.
        void setting_size_on_adhesions();

    private:
        // TODO: short string optimisation?
        /// Index of adhesion beads per grid cell, (re)created by update().
        std::unordered_map<
            PixelPos, std::vector<AdhesionWithEnvironment>> adhesions_by_pixel_;

        // Tracks changes for later communication with ECM
        ECMInteractionTracker ecm_interaction_tracker_;

        // Return value for get_adhesions if there are none
        static std::vector<AdhesionWithEnvironment> no_adhesions_;
        

        // accessor for tests
        friend std::unordered_map<
                PixelPos, std::vector<AdhesionWithEnvironment>
            > const &
            adhesions_by_pixel(AdhesionIndex const & index);
};

#endif

