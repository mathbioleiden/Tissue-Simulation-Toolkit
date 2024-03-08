// This file allows choosing wether the pdefield uses float
// or double values. The OpenCL core should automatically
// adopt this setting as well.

#define PDEFIELD_FLOAT
//#define PDEFIELD_DOUBLE

#ifdef PDEFIELD_FLOAT
#define PDEFIELD_TYPE float
#define OPENCL_PDE_TYPE "#define PDEFIELD_TYPE float\n"
#endif
#ifdef PDEFIELD_DOUBLE
#define PDEFIELD_TYPE double
#define OPENCL_PDE_TYPE "#define PDEFIELD_TYPE double\n"
#endif
