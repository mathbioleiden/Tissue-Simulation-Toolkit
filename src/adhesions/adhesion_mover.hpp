#pragma once

#include "adhesion_index.hpp"
#include "ca_fwd.hpp"
#include "ecm_boundary_state.hpp"
#include "vec2.hpp"
#include "act.hpp"


/** Describes where the adhesions go during a copy attempt. */
class AdhesionDisplacements {
    public:
        /** Create an object where no adhesions move. */
        AdhesionDisplacements();

        /** Create an object representing the given displacements.
         *
         * @param source Displacement of adhesions in the source pixel.
         * @param target Displacement of adhesions in the target pixel.
         */
        AdhesionDisplacements(
                PixelDisplacement source, PixelDisplacement target);

        /// Location relative to source pixel where adhesions go
        PixelDisplacement source;

        /// Location relative to target pixel where adhesions go
        PixelDisplacement target;

        /// Special value signalling that the adhesions got annihilated
        static const PixelDisplacement annihilated;
};


/** Decide how adhesions will move during a copy.
 *
 * This class implements the logic required to evaluate a copy attempt that
 * requires moving one or more adhesion particles along with or out of the way
 * of the copied pixel.
 */
class AdhesionMover {
    public:
        /** Construct an AdhesionMover object.
         *
         * @param ca The CPM to work with.
         */
        AdhesionMover(CellularPotts const & ca);

        /** Compute the amount of work involved in an attempted copy.
         *
         * A Cellular Potts copy attempt from and/or to a grid cell that has
         * adhesions may move those adhesions along, dragging along the ECM in
         * turn. This involves work (a change in the overall energy of the
         * system), the amount of which is calculated by this function for a
         * given potential move.
         *
         * Note that there are multiple options for whether and where to move
         * the adhesions on a copy attempt, in particular for retractions. This
         * function returns the work required along with the corresponding
         * chosen displacement. If the copy attempt succeeds, then the latter
         * should be passed back to commit_move() to ensure the correct
         * displacement is made.
         *
         * @param from Pixel to be copied from
         * @param to Pixel to copied to
         * @param displacements Out parameter returning the chosen adhesion
         *      displacements
         * @return The work required.
         */
        double move_dh(
                PixelPos from, PixelPos to,
                AdhesionDisplacements & displacements) const;

        /** Update the adhesions following a move.
         *
         * This modifies the associated ECM as well as the cache, so update()
         * does not need to be called afterwards.
         *
         * This will not do a simultaneous swap if the displacements are in
         * opposite directions aligned with the move. That should never happen,
         * as it requires attempting a copy within a cell which would have been
         * short-circuited long before this got called.
         *
         * @param from Pixel that was copied from
         * @param to Pixel that was copied to
         * @param displacements Adhesion displacements as previously returned
         *      by move_dh()
         */
        void commit_move(
                PixelPos source_pixel, PixelPos target_pixel,
                AdhesionDisplacements const & displacements);

        /** Get accumulated changes to the adhesions.
         *
         * AdhesionMover keeps track of any changes to the adhesions it applies.
         * This function returns the accumulated changes.
         */
         CellECMInteractions get_cell_ecm_interactions() const;

        /** Reset the adhesion change administration.
         *
         * This clears the recorded adhesion change history.
         */
        void reset_cell_ecm_interactions();

        /** Update the internal administration after an update to the ECM.
         *
         * AdhesionMover keeps a partial copy of the ECM internally for faster
         * access. It keeps this up to date when any adhesions are moved via
         * commit_move, but if external changes are made to the ECM then this
         * function must be called to get the AdhesionMover back in sync.
         *
         * @param ecm_boundary ECM boundary state to update from
         */
        void update(ECMBoundaryState const & ecm_boundary);

        void ContractAdhesionInCells(double); 
        
        void update_myosin(const ACT::ActField act_field); 

        
        
    private:
        /// The CPM grid to work with
        CellularPotts const & ca_;
        
        /// Adhesion index for efficiently calculating work
        AdhesionIndex index_;

        /// Hack right now, this function gets updated at some poitn 
        friend CellularPotts;

};

