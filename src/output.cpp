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
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include "warning.h"
#include "parameter.h"
#include "output.h"

#define FNAMESIZE 100

int OpenFileAndCheckExistance(FILE **fp, const char *fname, const char *ftype) {
  
  *fp=fopen(fname,ftype);
  if (*fp==NULL) 
    return FALSE;
  
  if (!strncmp(ftype,"a",1)) {
    if (ftell(*fp)>0L) return TRUE;
    else return FALSE;
  } else return TRUE;
}

int FileExistsP(const char *fname) {
  
  FILE *fp;
  fp=fopen(fname,"r");
  if (fp==NULL)
    return FALSE;
  
  fclose(fp);
  return TRUE;

}
		       
int YesNoP(const char *message) {
  
  char answer[100];

  fprintf(stderr,"%s (y/n) ",message);
  fflush(stderr);
  
  scanf("%s",answer);
  while (strcmp(answer,"y") && strcmp(answer,"n")) {
    fprintf(stderr,"\n\bPlease answer 'y' or 'n'. ");
    fflush(stderr);
    scanf("%s",answer);
  }
  
  if (!strcmp(answer,"y")) return TRUE;
  
  return FALSE;
    
}


FILE *OpenWriteFile(const char *filename) 
{

  char fname[FNAMESIZE];

  FILE *fp;

  fprintf(stderr,"Opening %s for writing\n",filename);
	
  if(FileExistsP(filename)==TRUE) {
  
 
      /* Rename old file */
    sprintf(fname, "%s~",filename);
    rename(filename, fname);
      
    //}
  }
  
  strncpy(fname, filename, FNAMESIZE-1);
  
  if ((fp=fopen(fname,"w"))==NULL) {
    char *message=(char *)malloc(2000*sizeof(char));
    sprintf(message," Could not open file %s for writing: "
	    ,fname);
    perror("");
    throw(message);
  }
	
  return fp;
}



FILE *OpenReadFile(const char *filename) 
{
  FILE *fp;

  fprintf(stderr,"Opening %s for reading\n",filename);
  
  if((OpenFileAndCheckExistance(&fp,filename,"r"))==FALSE) {	
    char *message=(char *)malloc(2000*sizeof(char));
    sprintf(message," File %s not found or empty, exiting... \n"
			,filename);
    throw(message);
	  
  }
  return fp;
}


char *ReadLine(FILE *fp) 
{
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
  bufsize=INITIAL_BUFSIZE;
  MEMORYCHECK(tmpstring=(char *)malloc(bufsize*sizeof(char)));

  pos=0;
  
  while ((character=getc(fp))!=EOF && /* read a character and check */
		 character!='\n') {
	
	tmpstring[pos]=(char)character;
	(pos)++;

	if (pos >= bufsize) {
	  /* line is longer than initial_bufsize, reallocate space */
	  bufsize+=INITIAL_BUFSIZE;
	  MEMORYCHECK(tmpstring=(char *)realloc(tmpstring,bufsize*sizeof(char)));
	  
	}
		   
  }


  if (character==EOF) {
	
	if (pos==0) {
	  /* EOF was reached, while no characters were read */
	  free(tmpstring);
	  return NULL;

	}
	if (ferror(fp)) {
	  error("I/O error in ReadLine(%ld): %s\n",(long)fp, strerror(errno));
	}
	

  }
  
  /* Allocate enough memory for the line */
  MEMORYCHECK(line=(char *)malloc((++(pos))*sizeof(char)));

  strncpy(line,tmpstring,(pos)-1);
  free(tmpstring);
  
  line[pos-1]='\0';
  return line;
    
}


void CheckFile(FILE *fp) 
{
  if (ftell(fp)<0) {
	/* file is probably not open, or another error occured */
	error("File error (fp=%ld): %d %s\n",fp,errno,strerror(errno));
  }
  /* File pointer is ok */
}

char *Chext(char *filename) {

  /* Chop the extension from a filename */
  
  /* Search backwards until a dot */
  
  /* Remember to free the memory allocated by this function */
  /* ( free(result) ) */
  
  /* not yet tested */

  int i;
  char *result;

  for (i=strlen(filename)-1;i>=0;i--) {
    if (filename[i]=='.') 
      break;
    
  }
  
  /* No . found */
  if (i==0) {
    
    result=strdup(filename);
  } else {
   
    /* . found */
    result=(char *)malloc((i+1)*sizeof(char));
    strncpy(result, filename, i);
  }
  return result;
  
  
}
