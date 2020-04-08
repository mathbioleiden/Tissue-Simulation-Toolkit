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
  int xpos = (id - (zpos * layersize)) /ysize;
  int ypos = id - xpos * ysize - zpos * layersize; 
  btype = 2;
  //Boundaries
  double sum =0.;
  if (xpos == 0 || ypos == 0 || xpos == xsize-1 || ypos == ysize-1){
    switch(btype){
    case 1:
    //Noflux gradient
    if (ypos == ysize-1){ sigmaB[id] = 1.;} 
    if (ypos == 0) sigmaB[id] = 0.;
    if (xpos == xsize-1) sigmaB[id] = sigmaA[id-ysize];
    if (xpos == 0) sigmaB[id] = sigmaA[id+ysize];
    break;
    //Periodic
    case 2:
    if (xpos == xsize-1) sigmaB[id] = sigmaA[id-layersize+ysize];
    if (xpos == 0) sigmaB[id] = sigmaA[id+layersize-ysize];
    if (ypos == ysize-1) sigmaB[id] = sigmaA[id-ysize+1];
    if (ysize == 0) sigmaB[id] = sigmaB[id+ysize-1]; 
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
  if (btype != 1){
    if (zpos == 0){
      if (sigmacells[id] > 0){
        value = value + secr_rate * dt;
      }
      else{
         value = value - decay_rate*dt*value;
      }
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
//if (xpos == xsize -1 && ypos == ysize-1){sigmaB[id] = 1.;}

}

