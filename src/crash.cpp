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
/* Contains functions for crash reports */
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#ifndef  __APPLE__
#include <malloc.h> 
#endif

//#include <unistd.h>
#include <string.h>
#include "sticky.h"
//#include "structs.h"
#include "crash.h"
#define NOPVM

/* This message will be mailed to MAILREPORT if a segmentation fault is caught.  */
static char SIGSEGVmessage[1000]; 

void StartSIGINTHandling() {
  
  void HandleSIGINT(int);
  void NiceMessage();
  (void)signal(SIGINT,HandleSIGINT);
}

void HandleSIGINT(int dummy) {
  
  Crash("Master process is killed... \n Killing all subprocesses...\n");

} 

void StartSIGSEGVHandling() {
  
  void HandleSIGSEGV(int);
  (void)signal(SIGSEGV,HandleSIGSEGV);
}



void HandleSIGSEGV(int dummy) {

#ifndef NOPVM
  if (Masterp())
    Crash("Segmentation fault caught by master...\nKilling all subprocesses.\n");
  else {
    Crash(SIGSEGVmessage);
  }
#else
    Crash(SIGSEGVmessage);
#endif
}



void NiceMessage() {
  
  fprintf(stderr,"You suspended the process, probably to put it in the background.\n");
  fprintf(stderr,"The machine wishes you a good night or a good weekend!\n");
  
} 
		    

void MemoryWarning(void)
{

  //MailReport("Allocation Problem!");
  
  Crash("Warning: not enough memory left to allocate.\n Sorry: exiting......\n");
      
}

void Crash(char *message) {
  
  
  fprintf(stderr,"%s\n",message);

#ifndef NOPVM
  if (Masterp()) 
    KillAllDishes();
#endif
  
  exit(0);
}

