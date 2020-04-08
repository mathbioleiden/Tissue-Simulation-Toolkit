void kernel SecreteAndDiffuse(
global const int* sigmacells, 
global const double* sigma,  
global double* sigmaout, 
int xsize, 
int ysize,
int layers,
double decay_rate, 
double dt, 
double dx2, 
double diff_coeff,
double secr_rate,
int step )
{
  int id = get_global_id(0);
  int size = get_global_size(0);
  
  int layersize = xsize * ysize;

  int zpos = id/layersize;
  int ypos = (id - (zpos * layersize)) /xsize;
  int xpos = id - ypos * xsize - zpos * layersize; 
//Secrete
   if (step == 0){
     if (sigmacells[id] > 0){
       sigmaout[id] = sigma[id] + secr_rate * dt;
     }
   else{
       sigmaout[id] = sigma[id] - decay_rate*dt*sigma[id];
       }
   }
   else{   
  //Diffuse
    double sum =0.;


    if (xpos == 0 || ypos == 0 || xpos == xsize || ypos == ysize){
    sigmaout[id] = .0;
    }
    else{
    sum += sigma[id-1];
    sum += sigma[id+1];
    sum += sigma[id-xsize];
    sum += sigma[id+xsize];
    sum-=4*sigma[id];
    //sum *= 20;
    //if (sigma[id] > 0.)
    //printf("sigma:%f n: %f xpos: %d ypos: %d, zpos: %d\n", sigma[id], sum, xpos, ypos, zpos);//}
    sigmaout[id]= sigma[id]+sum*dt*diff_coeff/dx2;
    }
    }

}

