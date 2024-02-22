#define ARRAY_SIZE 33

#define gpuErrchk(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true)

void PDE::InitialiseCuda(CellularPotts *cpm){
  cout << "Start cuda init" << endl;
  //AllocateTridiagonalvars(sizex, sizey);

  cudaMalloc((void**) &d_couplingcoefficient, sizex*sizey*sizeof(PDEFIELD_TYPE));
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
  gpuErrchk(cudaMallocManaged(&next_stepsize, sizey*sizex*sizeof(PDEFIELD_TYPE)));

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


__global__ void InitializeDiagonals(int sizex, int sizey, PDEFIELD_TYPE twooverdt, PDEFIELD_TYPE dx2, PDEFIELD_TYPE* lowerH, PDEFIELD_TYPE* upperH, PDEFIELD_TYPE* diagH, PDEFIELD_TYPE* lowerV, PDEFIELD_TYPE* upperV, PDEFIELD_TYPE* diagV, PDEFIELD_TYPE* couplingcoefficient){
  //This function could in theory be parellelized further, split into 6 (each part only assigning 1 value.), but this is probably slower
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  int xloc; //position we currently want to assign to
  int yloc;
  int idcc; //id corresponding to the couplingcoefficient (+sizey to get the value right, +1 to get the value above)
  for (int id = index; id < sizex*sizey; id += stride){
    xloc = id/sizey; //needed to obtain interleaved format
    yloc = id%sizey;
    idcc = xloc*sizey + yloc;
    if(xloc == 0){
      lowerH[id] = 0;
      diagH[id] = couplingcoefficient[idcc+sizey]/dx2 + twooverdt;
      upperH[id] = -couplingcoefficient[idcc+sizey]/dx2;  
    }
    else if(xloc == sizex -1){
      lowerH[id] = -couplingcoefficient[idcc-sizey]/dx2;
      diagH[id] = couplingcoefficient[idcc-sizey]/dx2 + twooverdt;
      upperH[id] = 0;
    }
    else{
      lowerH[id] = -couplingcoefficient[idcc-sizey]/dx2;
      diagH[id] = (couplingcoefficient[idcc+sizey]+couplingcoefficient[idcc-sizey])/dx2 + twooverdt;
      upperH[id] = -couplingcoefficient[idcc+sizey]/dx2;
    }

    xloc = id%sizex; //needed to obtain interleaved format
    yloc = id/sizex;
    idcc = xloc*sizey + yloc;
    if(yloc == 0){
      lowerV[id] = 0;
      diagV[id] = couplingcoefficient[idcc+1]/dx2 + twooverdt;
      upperV[id] = -couplingcoefficient[idcc+1]/dx2;
    }
    else if(yloc == sizey -1){
      lowerV[id] = -couplingcoefficient[idcc-1]/dx2;
      diagV[id] = couplingcoefficient[idcc-1]/dx2 + twooverdt;
      upperV[id] = 0;
    }
    else{
      lowerV[id] = -couplingcoefficient[idcc-1]/dx2;
      diagV[id] = (couplingcoefficient[idcc+1]+couplingcoefficient[idcc-1])/dx2 + twooverdt;
      upperV[id] = -couplingcoefficient[idcc+1]/dx2;
      
    }
  }
}

__global__ void InitializeHorizontalVectors(int sizex, int sizey, PDEFIELD_TYPE twooverdt, PDEFIELD_TYPE dx2, PDEFIELD_TYPE* BH, PDEFIELD_TYPE* couplingcoefficient, PDEFIELD_TYPE* alt_PDEvars){
  
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  int xloc;
  int yloc;
  int idcc; //id corresponding to the couplingcoefficient and alt_PDEvars(+sizey to get the value right, +1 to get the value above)
  for (int id = index; id < sizex*sizey; id += stride){
    xloc = id/sizey; //needed to obtain interleaved format
    yloc = id%sizey;
    idcc = xloc*sizey + yloc;

    if (yloc == 0)
      BH[id] = twooverdt*alt_PDEvars[idcc] + (couplingcoefficient[idcc+1]*(alt_PDEvars[idcc+1] - alt_PDEvars[idcc]))/dx2; 
    else if (yloc == sizey-1)
      BH[id] = twooverdt*alt_PDEvars[idcc] + (couplingcoefficient[idcc-1]*(alt_PDEvars[idcc-1] - alt_PDEvars[idcc]))/dx2;  
    else 
      BH[id] = twooverdt*alt_PDEvars[idcc] + (couplingcoefficient[idcc+1]*(alt_PDEvars[idcc+1] - alt_PDEvars[idcc]) + couplingcoefficient[idcc-1]*(alt_PDEvars[idcc-1] - alt_PDEvars[idcc]))/dx2;
  }
}

__global__ void InitializeVerticalVectors(int sizex, int sizey, PDEFIELD_TYPE twooverdt, PDEFIELD_TYPE dx2, PDEFIELD_TYPE* BV, PDEFIELD_TYPE* couplingcoefficient, PDEFIELD_TYPE* alt_PDEvars){

  //This function could in theory be parellelized further, split into 6 (each part only assigning 1 value.), but this is probably slower
  
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  int xloc;
  int yloc;
  int idcc; //id corresponding to the couplingcoefficient and alt_PDEvars(+sizey to get the value right, +1 to get the value above)
  for (int id = index; id < sizex*sizey; id += stride){
    xloc = id%sizex;
    yloc = id/sizex;
    idcc = xloc*sizey + yloc;

    if (xloc == 0)
      BV[id] = twooverdt*alt_PDEvars[idcc] + (couplingcoefficient[idcc+sizey]*(alt_PDEvars[idcc+sizey] - alt_PDEvars[idcc]))/dx2; 
    else if (xloc == sizex-1)
      BV[id] = twooverdt*alt_PDEvars[idcc] + (couplingcoefficient[idcc-sizey]*(alt_PDEvars[idcc-sizey] - alt_PDEvars[idcc]))/dx2;  
    else 
      BV[id] = twooverdt*alt_PDEvars[idcc] + (couplingcoefficient[idcc+sizey]*(alt_PDEvars[idcc+sizey] - alt_PDEvars[idcc]) + couplingcoefficient[idcc-sizey]*(alt_PDEvars[idcc-sizey] - alt_PDEvars[idcc]))/dx2;
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

__device__ void derivsFitzHughNagumo(PDEFIELD_TYPE current_time, PDEFIELD_TYPE* y, PDEFIELD_TYPE* dydt, bool celltype2, int* sigmafield, PDEFIELD_TYPE pacing_interval, PDEFIELD_TYPE pacing_duration, PDEFIELD_TYPE pacing_strength, int id, PDEFIELD_TYPE interval_beats, PDEFIELD_TYPE pulse_duration, PDEFIELD_TYPE pulse_strength,  PDEFIELD_TYPE a, PDEFIELD_TYPE b, PDEFIELD_TYPE tau, PDEFIELD_TYPE* FHN_a, PDEFIELD_TYPE* FHN_b, PDEFIELD_TYPE* FHN_tau ){
  
    a = 0.1;
    PDEFIELD_TYPE epsilon = 10;
    PDEFIELD_TYPE beta = -1.0;
    PDEFIELD_TYPE RIext = 0;
    PDEFIELD_TYPE c = 0.191;
    PDEFIELD_TYPE timescale = 40;
  
  int sigma = sigmafield[id];
  if (fmod(current_time, interval_beats) < pulse_duration && celltype2)
    RIext = pulse_strength;


  dydt[0] = timescale*(epsilon*(y[0]*(1-y[0])*(y[0]-beta)) - y[1] + RIext);
  dydt[1] = timescale*((y[0] -a*y[1]+c));      

}

__global__ void ODEstepFE(PDEFIELD_TYPE dt, PDEFIELD_TYPE ddt, double thetime, int layers, int sizex, int sizey, PDEFIELD_TYPE* PDEvars, PDEFIELD_TYPE* alt_PDEvars, int* celltype, int* sigmafield, PDEFIELD_TYPE* next_stepsize, PDEFIELD_TYPE stepsize_min, PDEFIELD_TYPE pacing_interval, PDEFIELD_TYPE I_Na_factor, PDEFIELD_TYPE I_f_factor, PDEFIELD_TYPE I_Kr_factor){
  //PDEFIELD_TYPE ddt = 2e-7; //for couplingcoefficient 1e-4 
  //PDEFIELD_TYPE ddt = 1e-6; //for couplingcoefficient 1e-5
  int nr_of_iterations = round(dt/ddt);
  if (fabs(dt/ddt - nr_of_iterations) > 0.001)
    printf("dt and ddt do not divide properly!");
  PDEFIELD_TYPE begin_time,stepsize_next,stepsize_did,stepsize, end_time;
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
      stepsize=next_stepsize[id];
      for (i=0;i<layers;i++)
        y[i]=PDEvars[i*sizex*sizey + id];
      for (int it = 0; it < nr_of_iterations; it++){

        overshot = false;
        if (celltype2)
          derivsFabbriSeveri(current_time,y,dydt,pacing_interval, I_f_factor, I_Kr_factor, id);
        else{
          derivsMaleckar(current_time,y,dydt,pacing_interval, I_Na_factor, id, 0);
        }
        //derivsFitzHughNagumo(current_time,y,dydt,celltype2, sigmafield, pacing_interval,pacing_duration,pacing_strength, id, FHN_interval_beats, FHN_pulse_duration, FHN_pulse_strength,  a, b, tau, FHN_a, FHN_b, FHN_tau);
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
  if (thetime == 0 && par.SF_all)
    InitializeSFComputation(cpm);
  //copy current couplingcoefficient matrix and celltype matrix from host to device
  couplingcoefficient = cpm->getCouplingCoefficient();
  //couplingcoefficient = cpm->getCouplingCoefficient_Gradient();

  //int** cellnumber = cpm -> getSigma(); 
  cudaError_t errSync;
  cudaError_t errAsync;
  celltype = cpm->getTau();
  sigmafield = cpm->getSigma(); 
  cudaMemcpy(d_couplingcoefficient, couplingcoefficient[0], sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyHostToDevice); 
  cudaMemcpy(d_celltype, celltype[0], sizex*sizey*sizeof(int), cudaMemcpyHostToDevice); 
  cudaMemcpy(d_sigmafield, sigmafield[0], sizex*sizey*sizeof(int), cudaMemcpyHostToDevice); 
  cudaMemcpy(d_PDEvars, PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyHostToDevice); 

  
  int nr_blocks = sizex*sizey/par.threads_per_core + 1;
  PDEFIELD_TYPE Cm_maleckar = 50; //in nF
  PDEFIELD_TYPE I_m;
  bool afterdiffusion;

  for (int iteration = 0; iteration < repeat; iteration++){
    if (par.SF_all){
      cuSFChecker();
    }
      //cout << "Iteration = " << iteration << endl;

      //setup matrices for upperdiagonal, diagonal and lower diagonal for both the horizontal and vertical direction, since these remain the same during once MCS
    InitializeDiagonals<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, 2/dt, dx2, lowerH, upperH, diagH, lowerV, upperV, diagV, d_couplingcoefficient);
    cudaDeviceSynchronize();
    errSync  = cudaGetLastError();
    errAsync = cudaDeviceSynchronize();
    if (errSync != cudaSuccess) 
      printf("Sync kernel error: %s\n", cudaGetErrorString(errSync));
    if (errAsync != cudaSuccess)
      printf("Async kernel error: %s\n", cudaGetErrorString(errAsync));


    cuODEstep();
    afterdiffusion = false;
    if (par.SF_all){
      cuCopyVoltageForSF(afterdiffusion);
    }
  
    cuHorizontalADIstep();
    afterdiffusion = true;
    if (par.SF_all){
      cuCopyVoltageForSF(afterdiffusion);
    }

    //increase time by dt/2
    thetime = thetime + dt/2;  
    cuODEstep();
    afterdiffusion = false;
    if (par.SF_all){
      cuCopyVoltageForSF(afterdiffusion);
      cout << "This shouldn't happen!";
    }


    cuVerticalADIstep();
    afterdiffusion = true;
    if (par.SF_all){
      cuCopyVoltageForSF(afterdiffusion);
      cout << "This shouldn't happen!";
    }
      
    //cudaMemcpy(alt_PDEvars, d_alt_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
    //cout << "After second FE step, alt_PDEvars[23885] = " << alt_PDEvars[23885] << endl;
    if (par.SF_all){
      cout << "This shouldn't happen!";
      if (SF_start_one && !SF_end_one && par.SF_one_pixel)
        cuComputeSFOne();
      
      if (SF_in_progress && !SF_all_done && par.SF_all)
        cuWriteSFData();
    }
    

    
    //increase time by dt/2
    thetime = thetime + dt/2; 

    if (par.activation_times){    
      CheckActivationTimes<<<par.number_of_cores, par.threads_per_core>>>(thetime, d_Activation_times_array, d_sigmafield,  d_PDEvars, sizex, sizey);
    }   
  }
  cudaMemcpy(PDEvars, d_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
  cudaDeviceSynchronize();
  cuPDEVarsToFiles();
  if (par.activation_times){ 
    cudaMemcpy(Activation_times_array, d_Activation_times_array, sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);   
    cuWriteActivationTimes();
  }
}

void PDE::cuODEstep(){
  //Do an ODE step of size dt/2
  cudaError_t errSync;
  cudaError_t errAsync;
  //ODEstepRL_Paci<<<nr_blocks, par.threads_per_core>>>(dt/2, ddt, thetime, layers, sizex, sizey, d_PDEvars, d_alt_PDEvars, d_celltype, next_stepsize, min_stepsize, par.eps, pacing_interval, par.pacing_duration, par.pacing_strength);
  //ODEstepRKA<<<par.number_of_cores, par.threads_per_core>>>(dt/2, thetime, layers, sizex, sizey, d_PDEvars, d_alt_PDEvars, d_celltype, next_stepsize, min_stepsize, par.eps, pacing_interval, par.pacing_duration, par.pacing_strength);
  ODEstepFE<<<par.number_of_cores, par.threads_per_core>>>(dt/2, ddt, thetime, layers, sizex, sizey, d_PDEvars, d_alt_PDEvars, d_celltype, d_sigmafield, next_stepsize, min_stepsize, pacing_interval, par.I_f_factor, par.I_Kr_factor, par.I_Na_factor);
  //CopyOriginalToAltPDEvars<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, layers, d_PDEvars, d_alt_PDEvars);

  //cudaMemcpy(alt_PDEvars, d_alt_PDEvars, layers*sizex*sizey*sizeof(PDEFIELD_TYPE), cudaMemcpyDeviceToHost);
  //cout << "After second FE step, alt_PDEvars[4305] = " << alt_PDEvars[4305] << endl;
  cuErrorChecker(errSync, errAsync);
}

void PDE::cuHorizontalADIstep(){
  //Do a horizontal ADI sweep of size dt/2
  cudaError_t errSync;
  cudaError_t errAsync;
  InitializeHorizontalVectors<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, 2/dt, dx2, BH, d_couplingcoefficient, d_alt_PDEvars);
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
  InitializeVerticalVectors<<<par.number_of_cores, par.threads_per_core>>>(sizex, sizey, 2/dt, dx2, BV, d_couplingcoefficient, d_alt_PDEvars);
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

void PDE::cuErrorChecker(cudaError_t errSync, cudaError_t errAsync){
  errSync  = cudaGetLastError();
  errAsync = cudaDeviceSynchronize();
  if (errSync != cudaSuccess) 
    printf("Sync kernel error: %s\n", cudaGetErrorString(errSync));
  if (errAsync != cudaSuccess)
    printf("Async kernel error: %s\n", cudaGetErrorString(errAsync));
}