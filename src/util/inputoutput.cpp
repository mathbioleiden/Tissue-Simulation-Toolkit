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
#include "inputoutput.hpp"
#include "cell.hpp"
#include "dish.hpp"
#include "parameter.hpp"
#include "pde.hpp"
#include "warning.hpp"
#include <errno.h>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#include "../lib/json/json.hpp"
using json = nlohmann::json_abi_v3_11_2::json;

#define FNAMESIZE 100

extern Parameter par;

using namespace std;

IO::IO(Dish &d) { dish = &d; }

int IO::OpenFileAndCheckExistence(FILE **fp, const char *fname,
                                  const char *ftype) {

  *fp = fopen(fname, ftype);
  if (*fp == NULL)
    return FALSE;

  if (!strncmp(ftype, "a", 1)) {
    if (ftell(*fp) > 0L)
      return TRUE;
    else
      return FALSE;
  } else
    return TRUE;
}

int IO::FileExistsP(const char *fname) {

  FILE *fp;
  fp = fopen(fname, "r");
  if (fp == NULL)
    return FALSE;

  fclose(fp);
  return TRUE;
}

int IO::YesNoP(const char *message) {

  char answer[100];
  int res;
  fprintf(stderr, "%s (y/n) ", message);
  fflush(stderr);

  res = scanf("%s", answer);
  while ((strcmp(answer, "y") && strcmp(answer, "n")) || res == EOF) {
    fprintf(stderr, "\n\bPlease answer 'y' or 'n'. ");
    fflush(stderr);
    res = scanf("%s", answer);
  }

  if (!strcmp(answer, "y"))
    return TRUE;

  return FALSE;
}

FILE *IO::OpenWriteFile(const char *filename) {

  char fname[FNAMESIZE];

  FILE *fp;

  fprintf(stderr, "Opening %s for writing\n", filename);

  if (FileExistsP(filename) == TRUE) {

    /* Rename old file */
    sprintf(fname, "%s~", filename);
    rename(filename, fname);

    //}
  }

  strncpy(fname, filename, FNAMESIZE - 1);

  if ((fp = fopen(fname, "w")) == NULL) {
    char *message = (char *)malloc(2000 * sizeof(char));
    sprintf(message, " Could not open file %s for writing: ", fname);
    perror("");
    throw(message);
  }

  return fp;
}

FILE *IO::OpenReadFile(const char *filename) {
  FILE *fp;

  fprintf(stderr, "Opening %s for reading\n", filename);

  if ((OpenFileAndCheckExistence(&fp, filename, "r")) == FALSE) {
    char *message = (char *)malloc(2000 * sizeof(char));
    sprintf(message, " File %s not found or empty, exiting... \n", filename);
    throw(message);
  }
  return fp;
}

char *IO::ReadLine(FILE *fp) {
  /* does almost the same as fgetln(), but DEC Unix doesn't understand
         fgetln(). Also I want my function to return a real C string,
         terminated by a \0. */

  /* The function reads a line from file *fp, and returns a pointer to the
         line read, which can be freed with a normal free(). The length of the
         string is written in *len */

#define INITIAL_BUFSIZE 100

  char *tmpstring;
  int character;
  long bufsize;
  char *line;
  int pos;

  CheckFile(fp);

  /* first allocate a string with a standard length */
  bufsize = INITIAL_BUFSIZE;
  MEMORYCHECK(tmpstring = (char *)malloc(bufsize * sizeof(char)));

  pos = 0;

  while ((character = getc(fp)) != EOF && /* read a character and check */
         character != '\n') {

    tmpstring[pos] = (char)character;
    (pos)++;

    if (pos >= bufsize) {
      /* line is longer than initial_bufsize, reallocate space */
      bufsize += INITIAL_BUFSIZE;
      MEMORYCHECK(tmpstring =
                      (char *)realloc(tmpstring, bufsize * sizeof(char)));
    }
  }

  if (character == EOF) {

    if (pos == 0) {
      /* EOF was reached, while no characters were read */
      free(tmpstring);
      return NULL;
    }
    if (ferror(fp)) {
      error("I/O error in ReadLine(%ld): %s\n", (long)fp, strerror(errno));
    }
  }

  /* Allocate enough memory for the line */
  MEMORYCHECK(line = (char *)malloc((++(pos)) * sizeof(char)));

  strncpy(line, tmpstring, (pos)-1);
  free(tmpstring);

  line[pos - 1] = '\0';
  return line;
}

void IO::CheckFile(FILE *fp) {
  if (ftell(fp) < 0) {
    /* file is probably not open, or another error occured */
    error("File error (fp=%ld): %d %s\n", fp, errno, strerror(errno));
  }
  /* File pointer is ok */
}

char *IO::Chext(char *filename) {

  /* Chop the extension from a filename */

  /* Search backwards until a dot */

  /* Remember to free the memory allocated by this function */
  /* ( free(result) ) */

  /* not yet tested */

  int i;
  char *result;

  for (i = strlen(filename) - 1; i >= 0; i--) {
    if (filename[i] == '.')
      break;
  }

  /* No . found */
  if (i == 0) {

    result = strdup(filename);
  } else {

    /* . found */
    result = (char *)malloc((i + 1) * sizeof(char));
    strncpy(result, filename, i);
  }
  return result;
}

/** A simple method to count all sigma's and write the output to an ostream */
void IO::CountSigma(std::ostream &os) {
  int *sum_sigma = new int[Cell::MaxSigma()];
  for (int i = 0; i < Cell::MaxSigma(); i++) {
    sum_sigma[i] = 0;
  }
  for (int x = 1; x < par.sizex - 1; x++) {
    for (int y = 1; y < par.sizey - 1; y++) {
      sum_sigma[dish->CPM->getSigma()[x][y]]++;
    }
  }
  for (int i = 0; i < Cell::MaxSigma(); i++) {
    os << i << " " << sum_sigma[i] << endl;
  }
  delete[] sum_sigma;
}

void IO::WriteContactInterfaces(void) {
  int RedRedSurface = 0;
  int RedYellowSurface = 0;
  int YellowYellowSurface = 0;
  for (int x = 1; x < par.sizex - 1; x++)
    for (int y = 1; y < par.sizey - 1; y++) {
      for (int i = 1; i <= 4; i++) {
        int x2, y2;
        x2 = x + dish->CPM->getNbhx(i);
        y2 = y + dish->CPM->getNbhy(i);
        if (dish->CPM->getSigma()[x][y] != dish->CPM->getSigma()[x2][y2]) {
          // dish->CPM->getCell())[dish->CPM->getSigma()[x][y]] returns the cell
          // corresponding to the sigma found on position (x,y)
          if ((dish->CPM->getCell(dish->CPM->getSigma()[x][y])).getTau() == 1 &&
              (dish->CPM->getCell(dish->CPM->getSigma()[x2][y2])).getTau() == 1)
            RedRedSurface++;
          if ((dish->CPM->getCell(dish->CPM->getSigma()[x][y])).getTau() == 2 &&
              (dish->CPM->getCell(dish->CPM->getSigma()[x2][y2])).getTau() == 1)
            RedYellowSurface++;
          if ((dish->CPM->getCell(dish->CPM->getSigma()[x][y])).getTau() == 1 &&
              (dish->CPM->getCell(dish->CPM->getSigma()[x2][y2])).getTau() == 2)
            RedYellowSurface++;
          if ((dish->CPM->getCell(dish->CPM->getSigma()[x][y])).getTau() == 2 &&
              (dish->CPM->getCell(dish->CPM->getSigma()[x2][y2])).getTau() == 2)
            YellowYellowSurface++;
        }
      }
    }
  // cout << "Red-red surface = " << RedRedSurface << endl;
  // cout << "Red-yellow surface = " << RedYellowSurface << endl;
  // cout << "Yellow-yellow surface = " << YellowYellowSurface << endl;

  ofstream myfile;
  myfile.open("Data_original.txt", std::ofstream::out | std::ofstream::app);
  myfile << RedYellowSurface << endl;
  myfile.close();
}

void IO::WriteConfiguration(char *write_loc) {
  // Write the current configuration in json format
  json Configuration;
  // Convert sigmafield to vector
  int *sigmafieldarray = dish->CPM->getSigma()[0];
  int size = par.sizex * par.sizey;
  vector<int> sigmafieldvector(sigmafieldarray, sigmafieldarray + size);
  // Write sigmafield to json
  Configuration["sigma"] = sigmafieldvector;

  // Construct a cell types matrix
  vector<int> celltypes;
  vector<Cell>::iterator c = dish->CPM->getCellArray()->begin();
  ++c;
  for (; c != dish->CPM->getCellArray()->end(); c++) {
    celltypes.push_back(c->getTau());
  }
  // Write celltypes to json
  Configuration["tau"] = celltypes;

  // Write configuration to file
  ofstream myfile;
  myfile.open(write_loc, std::ofstream::out);
  myfile << Configuration;
  myfile.close();
}

void IO::ReadConfiguration(void) {
  ifstream f(par.initial_configuration_file);
  json Configuration = json::parse(f);

  /* Fill CA plane with imported configuration */
  {
    for (int i = 0; i < par.sizex * par.sizey; i++)
      dish->CPM->getSigma()[0][i] = Configuration["sigma"][i];
  }

  // Construct the cells
  dish->CPM->ConstructInitCells(*dish);

  // Assign celltypes
  vector<Cell>::iterator c = dish->CPM->getCellArray()->begin();
  ++c;
  for (; c != dish->CPM->getCellArray()->end(); c++) {
    c->setTau(Configuration["tau"][c->sigma - 1]);
  }
}
