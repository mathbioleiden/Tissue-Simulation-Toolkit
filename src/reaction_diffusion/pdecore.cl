void kernel SecreteAndDiffuse(global const int *sigmacells,
                              global const PDEFIELD_TYPE *sigmaA,
                              global PDEFIELD_TYPE *sigmaB, int xsize,
                              int ysize, int layers, PDEFIELD_TYPE decay_rate,
                              PDEFIELD_TYPE dt, PDEFIELD_TYPE dx2,
                              global const PDEFIELD_TYPE *diff_coeff,
                              PDEFIELD_TYPE secr_rate, int btype) {
  // ID is used for position in array
  int id = get_global_id(0);
  // test b
  // Calculate position in aray
  int layersize = xsize * ysize;
  int zpos = id / layersize;
  int xpos = (id - (zpos * layersize)) / ysize;
  int ypos = id - xpos * ysize - zpos * layersize;

  // printf("id: %i x: %i y: %i\n", id, xpos, ypos);

  // Boundaries
  PDEFIELD_TYPE sum = 0.;
  if (xpos == 0 || ypos == 0 || xpos == xsize - 1 || ypos == ysize - 1) {
    switch (btype) {
    case 1:
      // Noflux gradient
      if (ypos == ysize - 1) {
        sigmaB[id] = 1.;
      }
      if (ypos == 0)
        sigmaB[id] = 0.;
      if (xpos == xsize - 1)
        sigmaB[id] = sigmaA[id - ysize];
      if (xpos == 0)
        sigmaB[id] = sigmaA[id + ysize];
      break;
    // Periodic
    case 2:
      if (xpos == xsize - 1)
        sigmaB[id] = sigmaA[id - layersize + ysize];
      if (xpos == 0)
        sigmaB[id] = sigmaA[id + layersize - ysize];
      if (ypos == ysize - 1)
        sigmaB[id] = sigmaA[id - ysize + 1];
      if (ysize == 0)
        sigmaB[id] = sigmaB[id + ysize - 1];
      break;
    // Absorbing
    case 3:
      sigmaB[id] = 0.;
      break;
    }
  } else {
    // Retrieve current value in array
    PDEFIELD_TYPE value = sigmaA[id];
    // Secretion
    if (btype != 1) {
      if (zpos == 0) {
        if (sigmacells[id] > 0) {
          value = value + secr_rate * dt;
        } else {
          value = value - decay_rate * dt * value;
        }
      }
    }
    // Diffusion
    sum += sigmaA[id - 1];
    sum += sigmaA[id + 1];
    sum += sigmaA[id - ysize];
    sum += sigmaA[id + ysize];
    sum -= 4 * value;
    sigmaB[id] = value + sum * dt * diff_coeff[zpos] / dx2;
    // sigmaB[id] =  value;
  }
}
