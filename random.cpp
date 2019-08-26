/* 

Copyright 1996-2006 Roeland Merks

This file is part of Tissue Simulation Toolkit.

Tissue Simulation Toolkit is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

Tissue Simulation Toolkit is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Tissue Simulation Toolkit; if not, write to the Free
Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
02110-1301 USA

*/
#include <stdio.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include <iostream>
#include "random.h"

static int idum = -1;

/*! \return A random double between 0 and 1
**/
double RANDOM(void)
/* Knuth's substrative method, see Numerical Recipes */
{
  static int inext,inextp;
  static long ma[56];
  static int iff=0;
  long mj,mk;
  int i,ii,k;

  if (idum < 0 || iff == 0) {
    iff=1;
    mj=MSEED-(idum < 0 ? -idum : idum);
    mj %= MBIG;
    ma[55]=mj;
    mk=1;
    i=1;
    do {
      ii=(21*i) % 55;
      ma[ii]=mk;
      mk=mj-mk;
      if (mk < MZ) mk += MBIG;
      mj=ma[ii];
    } while ( ++i <= 54 );
    k=1;
    do {
      i=1;
      do {
        ma[i] -= ma[1+(i+30) % 55];
        if (ma[i] < MZ) ma[i] += MBIG;
      } while ( ++i <= 55 );
    } while ( ++k <= 4 );
    inext=0;
    inextp=31;
    idum=1;
  }
  if (++inext == 56) inext=1;
  if (++inextp == 56) inextp=1;
  mj=ma[inext]-ma[inextp];
  if (mj < MZ) mj += MBIG;
  ma[inext]=mj;
  return mj*FAC;
}

/*! \param An integer random seed
  \return the random seed
**/
int Seed(int seed)
{
  if (seed < 0) {
	  std::cerr << "Randomizing random generator, seed is ";
    int rseed=Randomize();
    std::cerr << rseed << "\n";
    return rseed;
  } else {
    int i;
    idum = -seed;
    for (i=0; i <100; i++)
      RANDOM();
    return seed;
  }
}


/*! Returns a random integer value between 1 and 'max'
  \param The maximum value (long)
  \return A random integer (long)
**/
long RandomNumber(long max)
{
   return((long)(RANDOM()*max+1));
}

/*! Interactively ask for the seed
\param void
\return void
**/
void AskSeed(void)
{
  int seed;
  printf("Please enter a random seed: ");
  scanf("%d",&seed);
  printf("\n");
  Seed(seed);
}


/*! Make a random seed based on the local time
\param void
\return void
**/

int Randomize(void) {
  
  // Set the seed according to the local time
  struct timeb t;
  int seed;

  ftime(&t);
  
  seed=abs((int)((t.time*t.millitm)%655337));
  Seed(seed);
  fprintf(stderr,"Random seed is %d\n",seed);
  return seed;
}


