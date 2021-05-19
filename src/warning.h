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
#ifndef WARNING_H_
#define WARNING_H_

#define MEMORYCHECK(x) if ((x)==NULL) {   fprintf(stderr, "Out of Memory error in "#x" \n");  exit(0); }

#define UNIDENTIFIED 2353996
//static int last_value=UNIDENTIFIED;
/*#define WATCH(x) if (last_value==UNIDENTIFIED) {   last_value=x; 
} else { if (x!=last_value) { fprintf(stderr,"WATCH value changed. Suspending execution. \n Interrupt within debugger to examine position in program.\n"); 
				 last_value=x; 
				 while(1);
	   } else { 
		      last_value=x;
	   } 
	   }*/


/* These functions were a gift from Josh Barnes */
/* I changed the name "eprintf" to "warning" */

#ifdef __cplusplus 
extern "C" { 
#endif

void error(char *, ...);
void warning(char *, ...);

#ifdef __cplusplus
}
#endif

#endif
