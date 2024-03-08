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
#include "random.hpp"
#include <chrono>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdio.h>
#include <stdlib.h>

static long idum = -1;

/*! \return A random double between 0 and 1
 **/
double RANDOM(void) {
  /* Knuth's substractive method, see Numerical Recipes */
  static int inext, inextp;
  static long ma[56];
  static int iff = 0;
  long mj, mk;
  int i, ii, k;

  if (idum < 0 || iff == 0) {
    iff = 1;
    mj = labs(MSEED - labs(idum));
    mj %= MBIG;
    ma[55] = mj;
    mk = 1;
    i = 1;
    do {
      ii = (21 * i) % 55;
      ma[ii] = mk;
      mk = mj - mk;
      if (mk < MZ)
        mk += MBIG;
      mj = ma[ii];
    } while (++i <= 54);
    k = 1;
    do {
      i = 1;
      do {
        ma[i] -= ma[1 + (i + 30) % 55];
        if (ma[i] < MZ)
          ma[i] += MBIG;
      } while (++i <= 55);
    } while (++k <= 4);
    inext = 0;
    inextp = 31;
    idum = 1;
  }
  if (++inext == 56)
    inext = 1;
  if (++inextp == 56)
    inextp = 1;
  mj = ma[inext] - ma[inextp];
  if (mj < MZ)
    mj += MBIG;
  ma[inext] = mj;
  return mj * FAC;
}

/*! \param An integer random seed
  \return the random seed
**/
long Seed(long seed) {
  if (seed < 0) {
    std::cerr << "Randomizing random generator, seed is ";
    long rseed = Randomize();
    std::cerr << rseed << "\n";
    return rseed;
  } else {
    int rseed = (seed % (MBIG - 1));
    int i;
    idum = -rseed;
    for (i = 0; i < 100; i++)
      RANDOM();
    return seed;
  }
}

/*! Returns a random integer value between 1 and 'max'
  \param The maximum value (long)
  \return A random integer (long)
**/
long RandomNumber(long max) { return ((long)(RANDOM() * max + 1)); }

/*! Interactively ask for the seed
\param void
\return void
**/
void AskSeed(void) {
  int seed;
  int res = EOF;
  while (res == EOF) {
    printf("Please enter a random seed: ");
    res = scanf("%d", &seed);
    printf("\n");
  }
  Seed(seed);
}

/*! Make a random seed based on the local time
\param void
\return void
**/

long Randomize(void) {
  // Set the seed according to the local time
  int seed;

  auto timepoint = std::chrono::system_clock::now();
  auto since_epoch = timepoint.time_since_epoch();
  auto seconds = std::chrono::duration_cast<std::chrono::seconds>(since_epoch);
  auto milliseconds =
      std::chrono::duration_cast<std::chrono::milliseconds>(since_epoch);

  seed = abs((int)((seconds.count() * milliseconds.count()) % 655337));
  Seed(seed);
  fprintf(stderr, "Random seed is %d\n", seed);
  return seed;
}

double generateGaussianNoise(double mu, double sigma) {
  static const double epsilon = std::numeric_limits<double>::min();
  static const double two_pi = 2.0 * 3.14159265358979323846;

  thread_local double z1;
  thread_local bool generate;
  generate = !generate;

  if (!generate)
    return z1 * sigma + mu;

  double u1, u2;
  do {
    u1 = RANDOM();
    u2 = RANDOM();
  } while (u1 <= epsilon);

  double z0;
  z0 = sqrt(-2.0 * log(u1)) * cos(two_pi * u2);
  z1 = sqrt(-2.0 * log(u1)) * sin(two_pi * u2);
  return z0 * sigma + mu;
}
