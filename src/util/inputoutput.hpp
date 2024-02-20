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

#include "ca.hpp"
#include "cell.hpp"
#include "dish.hpp"
#include "pde.hpp"

#ifndef OUTPUT_H_
#define OUTPUT_H_

#ifdef __cplusplus
extern "C" {
#endif

class IO {
public:
  IO(Dish &d);

  int OpenFileAndCheckExistence(FILE **fp, const char *fname,
                                const char *ftype);
  int YesNoP(const char *message);
  FILE *OpenWriteFile(const char *filename);
  FILE *OpenGZippedWriteFile(const char *filename);
  FILE *OpenReadFile(const char *filename);
  char *ReadLine(FILE *fp);
  void CheckFile(FILE *fp);
  int FileExistsP(const char *fname);
  char *Chext(char *filename);
  void MakeDir(const char *dirname);
  bool CanWeWriteP(char *filename);
  /*! A simple method to count all sigma's and write the output to an ostream */
  void CountSigma(std::ostream &os);
  // Write contact surfaces to a file.
  void WriteContactInterfaces(void);
  // Read and write json files
  void WriteConfiguration(char *write_loc);
  void ReadConfiguration(void);

private:
  Dish *dish;
};

#ifdef __cplusplus
}
#endif

#define MESS_BUF_SIZE 160
#ifndef FALSE
#define FALSE 0
#define TRUE 1
#endif

#endif
