#include <cuda_profiler_api.h>
#include <cusparse.h>
#include "pdetype.h"

/*! \brief Check whether a GPU is available
 */
inline void gpuAssert(cudaError_t code, const char *file, int line,
                      bool abort = true) {
  if (code != cudaSuccess) {
    fprintf(stderr, "GPUassert: %s %s %d\n", cudaGetErrorString(code), file,
            line);
    if (abort)
      exit(code);
  }
}


/*! \brief Assign the derivatives to solve for the CUDA reaction diffusion
  solver As an example, the PDE for secretion diffusion from vessel.cpp is
  implemented Any ODE system can be implemented here 
  * \param current_time The
  derivatives may be time dependent 
  * \param y Current values of the PDE variables
  * \param dydt Vector that returns the derivatives at index id
  * \param sigmalfield The current CPM configuration
  * \param id The index for which the derivatives need to be computed
  * \param secr_rate Vector of secretion rates
  * \param decay_rate Vector of diffusion rates
*/
void DerivativesPDE(PDEFIELD_TYPE current_time, PDEFIELD_TYPE *y,
                               PDEFIELD_TYPE *dydt, int *sigmafield, int id,
                               PDEFIELD_TYPE *secr_rate,
                               PDEFIELD_TYPE *decay_rate);

/*! \brief Error checking function for CUDA functions
  Can return synchronized and synchronized errors for CUDA code.
  * \param errSync Synchronized error handle
  * \param errAsync Synchronized error handle
*/
void cuErrorChecker(cudaError_t errSync, cudaError_t errAsync);



/*! \
*/

/**
 * @brief Initialises the diagonals required for alternating direction implicit
   method. 

 *  This initialises the tridiagonal diffusion matrices that are required
   for solving per row / column For Ax=b, this initialises the matrix A for
   every row and column.
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param twooverdt 2/dt
 * @param dx2 dx*dx
 * @param lowerH Lower-diagonal required for the horizontal ADI sweep.
 * @param upperH Upper-diagonal for the horizontal ADI sweep.
 * @param diagH Diagonal for the horizontal ADI sweep.
 * @param lowerV Lower-diagonal required for the vertical ADI sweep.
 * @param upperV Upper-diagonal required for the vertical ADI sweep.
 * @param diagV Diagonal for the vertical ADI sweep.
 * @param diffusioncoefficient 
 */
__global__ void InitialiseDiagonals(int sizex, int sizey,
                                    PDEFIELD_TYPE twooverdt, PDEFIELD_TYPE dx2,
                                    PDEFIELD_TYPE *lowerH,
                                    PDEFIELD_TYPE *upperH, PDEFIELD_TYPE *diagH,
                                    PDEFIELD_TYPE *lowerV,
                                    PDEFIELD_TYPE *upperV, PDEFIELD_TYPE *diagV,
                                    PDEFIELD_TYPE *diffusioncoefficient);


/*! \brief  For Ax=b, this initialises the vectorb b for every column
*/

/**
 * @brief Intialises the righthandside vectors of the implicit ADI solver for
  rows.

 * For Ax=b, this initialises the vectorb b for every row.
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param twooverdt 2/dt
 * @param dx2 dx*dx
 * @param BH The vector b for the horizontal ADI sweep
 * @param diffusioncoefficient Vector of diffusion coefficients
 * @param alt_PDEvars The second PDE field
 */
__global__ void InitialiseHorizontalVectors(int sizex, int sizey,
                                            PDEFIELD_TYPE twooverdt,
                                            PDEFIELD_TYPE dx2,
                                            PDEFIELD_TYPE *BH,
                                            PDEFIELD_TYPE *diffusioncoefficient,
                                            PDEFIELD_TYPE *alt_PDEvars);

/*! \brief  For Ax=b, this initialises the vectorb b for every column
*/

/**
 * @brief Intialises the righthandside vectors of the implicit ADI solver for
  columns.

 * For Ax=b, this initialises the vectorb b for every column.
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param twooverdt 2/dt
 * @param dx2 dx*dx
 * @param BV The vector b for the verticall ADI sweep
 * @param diffusioncoefficient Vector of diffusion coefficients
 * @param alt_PDEvars The second PDE field
 */
__global__ void InitialiseVerticalVectors(int sizex, int sizey,
                                          PDEFIELD_TYPE twooverdt,
                                          PDEFIELD_TYPE dx2, PDEFIELD_TYPE *BV,
                                          PDEFIELD_TYPE *diffusioncoefficient,
                                          PDEFIELD_TYPE *alt_PDEvars);


/**
 * @brief Copy the solution of the first PDEvar layer by the horizontal ADI
 * iteration back into PDE vars
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param BH Contains the vector x for Ax = b for the horizontal sweep
 * @param PDEvars The first PDE field
 */
__global__ void NewPDEfieldH0(
    int sizex, int sizey, PDEFIELD_TYPE *BH,
    PDEFIELD_TYPE *PDEvars);

/**
 * @brief Copy the solution of the first PDEvar layer by the vertical ADI
 * iteration back into PDE vars
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param BV Contains the vector x for Ax = b for the vertical sweep
 * @param PDEvars The first PDE field
 */
__global__ void NewPDEfieldV0(
    int sizex, int sizey, PDEFIELD_TYPE *BV,
    PDEFIELD_TYPE *PDEvars);

/*! \brief Copy all values of alt_PDEvars, except the first value after
  diffusion Only the first component of the PDEvars vector diffuses. This may be
  extended to diffuse any or all chemicals in an analogous way.
*/

/**
 * @brief Copy all values of alt_PDEvars, except the first value after
  diffusion. 
  
 * Only the first component of the PDEvars vector diffuses. This may be
  extended to diffuse any or all chemicals in an analogous way.
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param layers Bumber of PDE field layers
 * @param PDEvars First PDE field
 * @param alt_PDEvars Second PDE field
 */
__global__ void NewPDEfieldOthers(
    int sizex, int sizey, int layers, PDEFIELD_TYPE *BV, PDEFIELD_TYPE *PDEvars,
    PDEFIELD_TYPE
        *alt_PDEvars);



/**
 * @brief Perform forward Euler step for a total of dt time in steps of size
  ddt.

 * The forward Euler steps are computed with time step ddt for a total of dt
  time par.ddt must therefore divide par.dt/2. 
 * @param dt Total time for which the forward Euler steps are computed
 * @param ddt Time steps in which time steps of a total of dt are computed
 * @param thetime The current time
 * @param layers Number of PDE variables
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param PDEvars First PDE field
 * @param alt_PDEvars Second PDE field
 * @param sigmafield Current CPM field
 * @param secr_rate Secretion rates of chemicals
 * @param decay_rate Decay rate of chemicals
 */
__global__ void ODEstepFE(PDEFIELD_TYPE dt, PDEFIELD_TYPE ddt, double thetime,
                          int layers, int sizex, int sizey,
                          PDEFIELD_TYPE *PDEvars, PDEFIELD_TYPE *alt_PDEvars,
                          int *sigmafield, PDEFIELD_TYPE *secr_rate,
                          PDEFIELD_TYPE *decay_rate);

/*! \brief Utitility function that copies alt_PDEvars to PDEvars
  \param sizex Grid size in x direction
  \param sizey Grid size in y direction
  \param layers Number of PDE variables
  \param PDEsource Source vector
  \param PDEtarget Target vector
*/


/**
 * @brief Utitility function that copies alt_PDEvars to PDEvars
 * @param sizex x-dimension of grid
 * @param sizey y-dimension of grid
 * @param layers Number of PDE variables
 * @param PDEsource Source field that is used for the copy
 * @param PDEtarget Target field that is used for the copy
 */
__global__ void CopyAltToOriginalPDEvars(int sizex, int sizey, int layers,
                                         PDEFIELD_TYPE *PDEsource,
                                         PDEFIELD_TYPE *PDEtarget);


/*! \brief Buffer size required for the horizontal ADI sweep*/
size_t pbuffersizeH;
/*! \brief Location alloted to the buffer for the horizontal ADI sweep on the
 * GPU*/
void *pbufferH;
/*! \brief Status of horizontal ADI sweep*/
cusparseStatus_t statusH;
/*! \brief Handle for the  horizontal ADI sweep*/
cusparseHandle_t handleH;
/*! \brief Buffer size required for the vertical ADI sweep*/
size_t pbuffersizeV;
/*! \brief Location alloted to the buffer for the vertical ADI sweep on the
 * GPU*/
void *pbufferV;
/*! \brief Status of vertical ADI sweep*/
cusparseStatus_t statusV;
/*! \brief Handle for the  vertical ADI sweep*/
cusparseHandle_t handleV;