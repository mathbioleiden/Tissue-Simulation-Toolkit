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
#define GRIDX 100
#define GRIDY 100
#define MAXCELLS 1024 /*  beware  */
#define MAXNEIGH  2054
#define FALSE    0
#define TRUE     1
#define OK 1
#define TESTCELLS 1
#define BOLTZMANN 1024 


#define MAXSEED 65531349

/* #define SAMPLE POPSIZE/2 */

//#define DEBUG 0
#define MAXHIST 4096
#define MAXTYPE 256
#define WHITE 0
#define BLACK 1
#define RED 2
#define BLUE 3
#define GREEN 4
#define MEDIUM 0
#define EMPTY -1
#define DIV 1   /* DIV 2^(# of divbit) */
#define REMARK 56
#define HASHCOLPRIME 255
#define PLOTPERIODFREQUENCY 25
#define HOSTDEAD -20
#define NULL_BEAST -10
#define OK_BEAST -5

/* the number of external connections per genome
   of random DNA's */
/* "parameters" */

#define PMUT 0.009
#define PMUT2 .1
#define DMUT 0.0021
#define PCO 0.
#define NETSIZE 29 
#define INETSIZE 16 
#define INP_PROT 16 /* number of negative inputs (connectivity) */
#define POTPROT 16 /* number of potential proteins */
//#define EXTCONNECTIONS 0
#define COMMUNICATION 2
#define ENERGYOFFSET 8
#define NHHIST 10
#define NH_TH 0.5
#define ENDOFSTATES 1<<(NETSIZE+2)
/* function definitions */

double RANDOM();












