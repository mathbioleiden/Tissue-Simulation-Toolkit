void kernel SecreteAndDiffuse(
global const int* sigmacells, 
global const double* sigmaA,  
global double* sigmaB, 
int xsize, 
int ysize,
int layers,
double decay_rate, 
double dt, 
double dx2, 
global const double* diff_coeff,
double secr_rate,
int btype )
{
  //ID is used for position in array
  int id = get_global_id(0); 
  
  //Calculate position in aray
  int layersize = xsize * ysize;
  int zpos = id/layersize;
  int ypos = (id - (zpos * layersize)) /xsize;
  int xpos = id - ypos * xsize - zpos * layersize; 

  
  btype = 1;
  //Boundaries
  double sum =0.;
  if (xpos == 0 || ypos == 0 || xpos == xsize || ypos == ysize){
    switch(btype){
    case 1:
    //Noflux
    if (ypos == ysize) sigmaB[id] = 1.;
    if (ypos == 0) sigmaB[id] = 0.;
    if (xpos == xsize) sigmaB[id] = sigmaA[id-1];
    if (xsize == 0) sigmaB[id] = sigmaB[id+1];
    break;
    //Periodic
    case 2:
    if (ypos == ysize) sigmaB[id] = sigmaA[id-layersize+xsize];
    if (ypos == 0) sigmaB[id] = sigmaA[id+layersize-xsize];
    if (xpos == xsize) sigmaB[id] = sigmaA[id-xsize+1];
    if (xsize == 0) sigmaB[id] = sigmaB[id+xsize-1]; 
    break;
    //Absorbing
    case 3:
    sigmaB[id] = 0.;
    break;

    } 
  }
  else{
  //Retrieve current value in array
  double value = sigmaA[id];
  
 //Secretion
  if (zpos == 0){
    if (sigmacells[id] > 0){
      value = value + secr_rate * dt;
    }
    else{
       value = value - decay_rate*dt*value;
    }
  }

    //Diffusion
    sum += sigmaA[id-1];
    sum += sigmaA[id+1];
    sum += sigmaA[id-xsize];
    sum += sigmaA[id+xsize];
    sum-=4*value;
    sigmaB[id]= value+sum*dt*diff_coeff[zpos]/dx2;
  }
}

