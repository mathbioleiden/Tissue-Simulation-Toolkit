#include "pde.cpp"
//Allow the CPU implementation for the PDE solver when CUDA is enabled.
#include <cusparse.h>
#include <cuda_profiler_api.h>


#define ARRAY_SIZE 2
#define gpuErrchk(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true)
{
   if (code != cudaSuccess) 
   {
      fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
      if (abort) exit(code);
   }
}

void cuErrorChecker(cudaError_t errSync, cudaError_t errAsync){
  errSync  = cudaGetLastError();
  errAsync = cudaDeviceSynchronize();
  if (errSync != cudaSuccess) 
    printf("Sync kernel error: %s\n", cudaGetErrorString(errSync));
  if (errAsync != cudaSuccess)
    printf("Async kernel error: %s\n", cudaGetErrorString(errAsync));
}


size_t pbuffersizeH; 
void *pbufferH;
//Needed for cuSparse horizontal and vertical sweeps of ADI
cusparseStatus_t statusH; 
cusparseHandle_t handleH;
size_t pbuffersizeV; 
void *pbufferV;
//Needed for cuSparse horizontal and vertical sweeps of ADI
cusparseStatus_t statusV; 
cusparseHandle_t handleV;


void PDE::InitialiseCuda(CellularPotts *cpm){
  cout << "Start cuda init" << endl;
  //AllocateTridiagonalvars(sizex, sizey);

  cudaMalloc((void**) &d_diffusioncoefficient, sizex*sizey*sizeof(PDEFIELD_TYPE));
  cudaMalloc((void**) &d_celltype, sizex*sizey*sizeof(int));
  cudaMalloc((void**) &d_sigmafield, sizex*sizey*sizeof(int));

  cudaMalloc((void**) &d_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE));
  cudaMemcpy(d_PDEvars, PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyHostToDevice);
  cudaMalloc((void**) &d_alt_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE));
  cudaMemcpy(d_alt_PDEvars, alt_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyHostToDevice);


  //Needed for ADI steps
  gpuErrchk(cudaMallocManaged(&upperH, sizex*sizey*sizeof(PDEFIELD_TYPE)));
  gpuErrchk(cudaMallocManaged(&diagH, sizex*sizey*sizeof(PDEFIELD_TYPE)));
  gpuErrchk(cudaMallocManaged(&lowerH, sizex*sizey*sizeof(PDEFIELD_TYPE)));
  gpuErrchk(cudaMallocManaged(&BH, sizex*sizey*sizeof(PDEFIELD_TYPE)));
  gpuErrchk(cudaMallocManaged(&upperV, sizey*sizex*sizeof(PDEFIELD_TYPE)));
  gpuErrchk(cudaMallocManaged(&diagV, sizey*sizex*sizeof(PDEFIELD_TYPE)));
  gpuErrchk(cudaMallocManaged(&lowerV, sizey*sizex*sizeof(PDEFIELD_TYPE)));
  gpuErrchk(cudaMallocManaged(&BV, sizey*sizex*sizeof(PDEFIELD_TYPE)));

  handleH = 0;
  pbuffersizeH = 0;
  pbufferH = NULL;
  statusH=cusparseCreate(&handleH);
  #ifdef PDEFIELD_DOUBLE
    cusparseDgtsvInterleavedBatch_bufferSizeExt(handleH, 0, sizex, lowerH, diagH, upperH, BH, sizey, &pbuffersizeH); //Compute required buffersize for horizontal sweep
  #else
    cusparseSgtsvInterleavedBatch_bufferSizeExt(handleH, 0, sizex, lowerH, diagH, upperH, BH, sizey, &pbuffersizeH); //Compute required buffersize for horizontal sweep
  #endif
  gpuErrchk(cudaMalloc( &pbufferH, sizeof(char)* pbuffersizeH));
  

  handleV = 0;
  pbuffersizeV = 0;
  pbufferV = NULL;
  statusV=cusparseCreate(&handleV);
  #ifdef PDEFIELD_DOUBLE
    cusparseDgtsvInterleavedBatch_bufferSizeExt(handleV, 0, sizey, lowerV, diagV, upperV, BV, sizex, &pbuffersizeV); //Compute required buffersize for vertical sweep
  #else
    cusparseSgtsvInterleavedBatch_bufferSizeExt(handleV, 0, sizey, lowerV, diagV, upperV, BV, sizex, &pbuffersizeV); //Compute required buffersize for vertical sweep
  #endif
  gpuErrchk(cudaMalloc( &pbufferV, sizeof(char)* pbuffersizeV));

  cout << "End cuda init" << endl;
}


__global__ void InitialiseDiagonals(int sizex, int sizey, PDEFIELD_TYPE twooverdt, PDEFIELD_TYPE dx2, PDEFIELD_TYPE* lowerH, PDEFIELD_TYPE* upperH, PDEFIELD_TYPE* diagH, PDEFIELD_TYPE* lowerV, PDEFIELD_TYPE* upperV, PDEFIELD_TYPE* diagV, PDEFIELD_TYPE* diffusioncoefficient){
  //This function could in theory be parellelized further, split into 6 (each part only assigning 1 value.), but this is probably slower
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  int xloc; //position we currently want to assign to
  int yloc;
  int idcc; //id corresponding to the diffusioncoefficient (+sizey to get the value right, +1 to get the value above)
  for (int id = index; id < sizex*sizey; id += stride){
    xloc = id/sizey; //needed to obtain interleaved format
    yloc = id%sizey;
    idcc = xloc*sizey + yloc;
    if(xloc == 0){
      lowerH[id] = 0;
      diagH[id] = diffusioncoefficient[idcc+sizey]/dx2 + twooverdt;
      upperH[id] = -diffusioncoefficient[idcc+sizey]/dx2;  
    }
    else if(xloc == sizex -1){
      lowerH[id] = -diffusioncoefficient[idcc-sizey]/dx2;
      diagH[id] = diffusioncoefficient[idcc-sizey]/dx2 + twooverdt;
      upperH[id] = 0;
    }
    else{
      lowerH[id] = -diffusioncoefficient[idcc-sizey]/dx2;
      diagH[id] = (diffusioncoefficient[idcc+sizey]+diffusioncoefficient[idcc-sizey])/dx2 + twooverdt;
      upperH[id] = -diffusioncoefficient[idcc+sizey]/dx2;
    }

    xloc = id%sizex; //needed to obtain interleaved format
    yloc = id/sizex;
    idcc = xloc*sizey + yloc;
    if(yloc == 0){
      lowerV[id] = 0;
      diagV[id] = diffusioncoefficient[idcc+1]/dx2 + twooverdt;
      upperV[id] = -diffusioncoefficient[idcc+1]/dx2;
    }
    else if(yloc == sizey -1){
      lowerV[id] = -diffusioncoefficient[idcc-1]/dx2;
      diagV[id] = diffusioncoefficient[idcc-1]/dx2 + twooverdt;
      upperV[id] = 0;
    }
    else{
      lowerV[id] = -diffusioncoefficient[idcc-1]/dx2;
      diagV[id] = (diffusioncoefficient[idcc+1]+diffusioncoefficient[idcc-1])/dx2 + twooverdt;
      upperV[id] = -diffusioncoefficient[idcc+1]/dx2;
      
    }
  }
}

__global__ void InitialiseHorizontalVectors(int sizex, int sizey, PDEFIELD_TYPE twooverdt, PDEFIELD_TYPE dx2, PDEFIELD_TYPE* BH, PDEFIELD_TYPE* diffusioncoefficient, PDEFIELD_TYPE* alt_PDEvars){
  
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  int xloc;
  int yloc;
  int idcc; //id corresponding to the diffusioncoefficient and alt_PDEvars(+sizey to get the value right, +1 to get the value above)
  for (int id = index; id < sizex*sizey; id += stride){
    xloc = id/sizey; //needed to obtain interleaved format
    yloc = id%sizey;
    idcc = xloc*sizey + yloc;

    if (yloc == 0)
      BH[id] = twooverdt*alt_PDEvars[idcc] + (diffusioncoefficient[idcc+1]*(alt_PDEvars[idcc+1] - alt_PDEvars[idcc]))/dx2; 
    else if (yloc == sizey-1)
      BH[id] = twooverdt*alt_PDEvars[idcc] + (diffusioncoefficient[idcc-1]*(alt_PDEvars[idcc-1] - alt_PDEvars[idcc]))/dx2;  
    else 
      BH[id] = twooverdt*alt_PDEvars[idcc] + (diffusioncoefficient[idcc+1]*(alt_PDEvars[idcc+1] - alt_PDEvars[idcc]) + diffusioncoefficient[idcc-1]*(alt_PDEvars[idcc-1] - alt_PDEvars[idcc]))/dx2;
  }
}

__global__ void InitialiseVerticalVectors(int sizex, int sizey, PDEFIELD_TYPE twooverdt, PDEFIELD_TYPE dx2, PDEFIELD_TYPE* BV, PDEFIELD_TYPE* diffusioncoefficient, PDEFIELD_TYPE* alt_PDEvars){

  //This function could in theory be parellelized further, split into 6 (each part only assigning 1 value.), but this is probably slower
  
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  int xloc;
  int yloc;
  int idcc; //id corresponding to the diffusioncoefficient and alt_PDEvars(+sizey to get the value right, +1 to get the value above)
  for (int id = index; id < sizex*sizey; id += stride){
    xloc = id%sizex;
    yloc = id/sizex;
    idcc = xloc*sizey + yloc;

    if (xloc == 0)
      BV[id] = twooverdt*alt_PDEvars[idcc] + (diffusioncoefficient[idcc+sizey]*(alt_PDEvars[idcc+sizey] - alt_PDEvars[idcc]))/dx2; 
    else if (xloc == sizex-1)
      BV[id] = twooverdt*alt_PDEvars[idcc] + (diffusioncoefficient[idcc-sizey]*(alt_PDEvars[idcc-sizey] - alt_PDEvars[idcc]))/dx2;  
    else 
      BV[id] = twooverdt*alt_PDEvars[idcc] + (diffusioncoefficient[idcc+sizey]*(alt_PDEvars[idcc+sizey] - alt_PDEvars[idcc]) + diffusioncoefficient[idcc-sizey]*(alt_PDEvars[idcc-sizey] - alt_PDEvars[idcc]))/dx2;
  }

}



__global__ void NewPDEfieldH0(int sizex, int sizey, PDEFIELD_TYPE* BH, PDEFIELD_TYPE* PDEvars){ //Take the values from BH and assign the new values of the first layers of PDEvars
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int id = index; id < sizex*sizey; id += stride)
    PDEvars[id] = BH[id];      
}


__global__ void NewPDEfieldV0(int sizex, int sizey, PDEFIELD_TYPE* BV, PDEFIELD_TYPE* PDEvars){ //Take the values from BV and assign the new values of the first layers of PDEvars
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int id = index; id < sizex*sizey; id += stride){
    PDEvars[sizey*(id%sizex)+id/sizex] = BV[id]; //Conversion is needed because PDEvars iterates over columns first and then rows, while BV does the opposite 
  }
}


__global__ void NewPDEfieldOthers(int sizex, int sizey, int layers, PDEFIELD_TYPE* BH, PDEFIELD_TYPE* PDEvars, PDEFIELD_TYPE* alt_PDEvars){ //copy the other values from alt_PDEvars to PDEvars
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int id = index+sizex*sizey; id < layers*sizex*sizey; id += stride)
    PDEvars[id] = alt_PDEvars[id]; 
}

__device__ void derivsFitzHughNagumo(PDEFIELD_TYPE current_time, PDEFIELD_TYPE* y, PDEFIELD_TYPE* dydt, bool celltype2, int* sigmafield, int id ){
  
    PDEFIELD_TYPE a = 0.1;
    PDEFIELD_TYPE epsilon = 10;
    PDEFIELD_TYPE beta = -1.0;
    PDEFIELD_TYPE RIext = 0;
    PDEFIELD_TYPE c = 0.191;
    PDEFIELD_TYPE timescale = 40;
  
  dydt[0] = timescale*(epsilon*(y[0]*(1-y[0])*(y[0]-beta)) - y[1] + RIext);
  dydt[1] = timescale*((y[0] -a*y[1]+c));      

}

__global__ void ODEstepFE(PDEFIELD_TYPE dt, PDEFIELD_TYPE ddt, double thetime, int layers, int sizex, int sizey, PDEFIELD_TYPE* PDEvars, PDEFIELD_TYPE* alt_PDEvars, int* celltype, int* sigmafield){
  
  int nr_of_iterations = round(dt/ddt);
  if (fabs(dt/ddt - nr_of_iterations) > 0.001)
    printf("dt and ddt do not divide properly!");
  PDEFIELD_TYPE begin_time,stepsize_did,stepsize, end_time;
  PDEFIELD_TYPE yscal[ARRAY_SIZE];
  PDEFIELD_TYPE y[ARRAY_SIZE];
  PDEFIELD_TYPE y_new[ARRAY_SIZE];
  PDEFIELD_TYPE dydt[ARRAY_SIZE];
  PDEFIELD_TYPE current_time;
  PDEFIELD_TYPE MaxTimeError = 5e-7;
  PDEFIELD_TYPE stepsize_overshot;
  bool overshot = false;
  bool celltype2 = false;
  int i;

  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int id = index; id < sizex*sizey; id += stride){
    if (celltype[id] < 1){
      for (i = 0; i < layers; i++) //fill with current PDE values
        alt_PDEvars[i*sizex*sizey + id]= PDEvars[i*sizex*sizey + id];
    }
    
    else{
      celltype2 = false; 
      if (celltype[id] == 2)
        celltype2 = true;
      begin_time = thetime;
      current_time = thetime;
      end_time = thetime + dt;
      for (i=0;i<layers;i++)
        y[i]=PDEvars[i*sizex*sizey + id];
      for (int it = 0; it < nr_of_iterations; it++){
        derivsFitzHughNagumo(current_time,y,dydt,celltype2, sigmafield,  id);
        current_time += ddt;
        if (it == nr_of_iterations-1) { //Are we done?
          for (i=0;i<layers;i++) {
            alt_PDEvars[i*sizex*sizey + id] = y[i]+ddt*dydt[i];
          }
        }
        else{  
          for (i=0;i<layers;i++) {
            y[i]=y[i]+ddt*dydt[i];  
          }
        }
      }
    }
  }
}



__global__ void CopyAltToOriginalPDEvars(int sizex, int sizey, int layers, PDEFIELD_TYPE* PDEvars, PDEFIELD_TYPE* alt_PDEvars){
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int id = index; id < layers*sizex*sizey; id += stride){
    PDEvars[id] = alt_PDEvars[id]; 
  }
}

__global__ void CopyOriginalToAltPDEvars(int sizex, int sizey, int layers, PDEFIELD_TYPE* PDEvars, PDEFIELD_TYPE* alt_PDEvars){
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int id = index; id < layers*sizex*sizey; id += stride){
    alt_PDEvars[id] = PDEvars[id]; 
  }
}

void PDE::cuPDEsteps(CellularPotts * cpm, int repeat){
  //copy current diffusioncoefficient matrix and celltype matrix from host to device

  cudaError_t errSync;
  cudaError_t errAsync;
  sigmafield = cpm->getSigma(); 
  cudaMemcpy(d_diffusioncoefficient, DiffCoeffs[0][0], sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyHostToDevice); 
  cudaMemcpy(d_celltype, celltype[0], sizex*sizey*sizeof(int), cudaMemcpyHostToDevice); 
  cudaMemcpy(d_sigmafield, sigmafield[0], sizex*sizey*sizeof(int), cudaMemcpyHostToDevice); 
  cudaMemcpy(d_PDEvars, PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyHostToDevice); 

  
  int nr_blocks = sizex*sizey/par.threads_per_core + 1;
  PDEFIELD_TYPE Cm_maleckar = 50; //in nF
  PDEFIELD_TYPE I_m;
  bool afterdiffusion;

  for (int iteration = 0; iteration < repeat; iteration++){
      //cout << "Iteration = " << iteration << endl;

      //setup matrices for upperdiagonal, diagonal and lower diagonal for both the horizontal and vertical direction, since these remain the same during once MCS
    InitialiseDiagonals<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, 2/dt, dx2, lowerH, upperH, diagH, lowerV, upperV, diagV, d_diffusioncoefficient);
    cudaDeviceSynchronize();
    errSync  = cudaGetLastError();
    errAsync = cudaDeviceSynchronize();
    if (errSync != cudaSuccess) 
      printf("Sync kernel error: %s\n", cudaGetErrorString(errSync));
    if (errAsync != cudaSuccess)
      printf("Async kernel error: %s\n", cudaGetErrorString(errAsync));


    cuODEstep();
  
    cuHorizontalADIstep();

    //increase time by dt/2
    thetime = thetime + dt/2;  
    cuODEstep();


    cuVerticalADIstep();
      
    //cudaMemcpy(alt_PDEvars, d_alt_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
    //cout << "After second FE step, alt_PDEvars[23885] = " << alt_PDEvars[23885] << endl;
    

    
    //increase time by dt/2
    thetime = thetime + dt/2; 
 
  }
  cudaMemcpy(PDEvars, d_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
  cudaDeviceSynchronize();
}

void PDE::cuODEstep(){
  //Do an ODE step of size dt/2
  cudaError_t errSync;
  cudaError_t errAsync;
  ODEstepFE<<<par.number_of_cores, par.threads_per_core>>>(dt/2, ddt, thetime, layers, sizex, sizey, d_PDEvars, d_alt_PDEvars, d_celltype, d_sigmafield);
  //CopyOriginalToAltPDEvars<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, layers, d_PDEvars, d_alt_PDEvars);

  //cudaMemcpy(alt_PDEvars, d_alt_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
  //cout << "After second FE step, alt_PDEvars[4305] = " << alt_PDEvars[4305] << endl;
  cuErrorChecker(errSync, errAsync);
}

void PDE::cuHorizontalADIstep(){
  //Do a horizontal ADI sweep of size dt/2
  cudaError_t errSync;
  cudaError_t errAsync;
  InitialiseHorizontalVectors<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, 2/dt, dx2, BH, d_diffusioncoefficient, d_alt_PDEvars);
  cuErrorChecker(errSync, errAsync);
  #ifdef PDEFIELD_DOUBLE
    statusH = cusparseDgtsvInterleavedBatch(handleH, 0, sizex, lowerH, diagH, upperH, BH, sizey, pbufferH);
  #else
    statusH = cusparseSgtsvInterleavedBatch(handleH, 0, sizex, lowerH, diagH, upperH, BH, sizey, pbufferH);
  #endif
  if (statusH != CUSPARSE_STATUS_SUCCESS)
  {
    cout << statusH << endl;
  }
  NewPDEfieldH0<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, BH, d_PDEvars);    
  cuErrorChecker(errSync, errAsync);
  NewPDEfieldOthers<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, layers, BV, d_PDEvars, d_alt_PDEvars); //////
  cuErrorChecker(errSync, errAsync);

  //cudaMemcpy(PDEvars, d_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
  //cout << "After second FE step, PDEvars[4305] = " << PDEvars[4305] << endl;

}

void PDE::cuVerticalADIstep(){
  //Do a vertical ADI sweep of size dt/2
  cudaError_t errSync;
  cudaError_t errAsync;
  InitialiseVerticalVectors<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, 2/dt, dx2, BV, d_diffusioncoefficient, d_alt_PDEvars);
  cuErrorChecker(errSync, errAsync);
  #ifdef PDEFIELD_DOUBLE
    statusV = cusparseDgtsvInterleavedBatch(handleV, 0, sizey, lowerV, diagV, upperV, BV, sizex, pbufferV);
  #else
    statusV = cusparseSgtsvInterleavedBatch(handleV, 0, sizey, lowerV, diagV, upperV, BV, sizex, pbufferV);
  #endif
  if (statusV != CUSPARSE_STATUS_SUCCESS)
  {
    cout << statusV << endl;
  }
  cudaDeviceSynchronize();
  NewPDEfieldV0<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, BV, d_PDEvars); //////
  errSync  = cudaGetLastError();
  errAsync = cudaDeviceSynchronize();
  if (errSync != cudaSuccess) 
    printf("Sync kernel error: %s\n", cudaGetErrorString(errSync));
  if (errAsync != cudaSuccess)
    printf("Async kernel error: %s\n", cudaGetErrorString(errAsync));
  NewPDEfieldOthers<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, layers, BV, d_PDEvars, d_alt_PDEvars); //////
  cuErrorChecker(errSync, errAsync);

  //cudaMemcpy(PDEvars, d_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
  //cout << "After second FE step, PDEvars[4305] = " << PDEvars[4305] << endl;

}

