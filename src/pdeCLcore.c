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
double diff_coeff,
double secr_rate,
int boundtype )
{
  int id = get_global_id(0);
  int size = get_global_size(0);
  
  int layersize = xsize * ysize;

  int zpos = id/layersize;
  int ypos = (id - (zpos * layersize)) /xsize;
  int xpos = id - ypos * xsize - zpos * layersize; 


  double value = sigmaA[id];
   if (zpos == 0){
     if (sigmacells[id] > 0){
       value = value + secr_rate * dt;
     }
     else{
       value = value - decay_rate*dt*value;
       }
   }

    double sum =0.;


    if (xpos == 0 || ypos == 0 || xpos == xsize || ypos == ysize){
    value = .0;
    }
    else{
    sum += sigmaA[id-1];
    sum += sigmaA[id+1];
    sum += sigmaA[id-xsize];
    sum += sigmaA[id+xsize];
    sum-=4*value;
    sigmaB[id]= value+sum*dt*diff_coeff/dx2;
    }

}

