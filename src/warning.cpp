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

// Code is a gift from Josh Barnes:
/* Return-Path: barnes@grape.c.u-tokyo.ac.jp
Received: from complex.c.u-tokyo.ac.jp (complex.kaneko-ken [192.168.1.1])
	by cyber.kaneko-ken (8.8.8/3.7W) with ESMTP id QAA21783
	for <roel@cyber.kaneko-ken>; Wed, 21 Oct 1998 16:55:49 +0900 (JST)
Received: from provence.c.u-tokyo.ac.jp (provence.c.u-tokyo.ac.jp [157.82.63.122])
	by complex.c.u-tokyo.ac.jp (8.8.8/3.7W) with ESMTP id QAA21031
	for <roel@cyber.c.u-tokyo.ac.jp>; Wed, 21 Oct 1998 16:56:06 +0900 (JST)
Received: from grape.c.u-tokyo.ac.jp (grape [157.82.60.48])
	by provence.c.u-tokyo.ac.jp (8.8.8/3.6W-980505) with ESMTP id QAA21212
	for <roel@cyber.c.u-tokyo.ac.jp>; Wed, 21 Oct 1998 16:52:47 +0900 (JST)
Received: (from barnes@localhost)
	by grape.c.u-tokyo.ac.jp (8.8.8/3.6W-980917) id QAA26932
	for roel@cyber.c.u-tokyo.ac.jp; Wed, 21 Oct 1998 16:55:45 +0900 (JST)
Date: Wed, 21 Oct 1998 16:55:45 +0900 (JST)
From: Josh Barnes <barnes@grape.c.u-tokyo.ac.jp>
Message-Id: <199810210755.QAA26932@grape.c.u-tokyo.ac.jp>
To: roel@cyber.c.u-tokyo.ac.jp
Subject: error.c
*/

/* Roeland changed "eprintf" to "warning" */

/*
 * ERROR.C: routines to report errors, etc.
 */

#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include "warning.h"

int Quiet=0;

/*
 * ERROR: scream and die quickly.
 */

void error(char * fmt, ...)
{
    va_list ap;

    va_start(ap, fmt);
    vfprintf(stderr, fmt, ap);		/* invoke interface to printf       */
    fprintf(stderr,"\n");     /* automatic \n by Roeland */
    fflush(stderr);			/* drain std error buffer 	    */
    va_end(ap);
    exit(1);				/* quit with error status	    */
}

/*
 * EPRINTF: scream, but don't die yet.
 * Roeland changed this to "warning" (21/10/1998)
 * and added an automatic "\n"
 */

void warning(char * fmt, ...)
{
  va_list ap;
  if (Quiet) return;
  
  va_start(ap, fmt);
  vfprintf(stderr, fmt, ap);		/* invoke interface to printf       */
  fprintf(stderr,"\n");     /* automatic \n by Roeland */
  fflush(stderr);			/* drain std error buffer 	    */
  va_end(ap);
}

#ifdef TESTBED

main(int argc, char * argv[])
{
    eprintf("warning: foo=%f\tbar=%d\tfum=\"%s\"\n", 3.1415, 32768, "waldo");
    error("error: foo=%f\tbar=%d\tfum=\"%s\"\n", 3.1415, 32768, "waldo");
}

#endif
