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

char *ParsePar(FILE *fp, char *parameter, bool wrapflag);
int igetpar(FILE *fp,char *parameter, bool wrapflag);
int igetpar(FILE *fp,char *parameter, int default_val, bool wrapflag);
float fgetpar(FILE *fp,char *parameter, bool wrapflag);
float fgetpar(FILE *fp,char *parameter, double default_val, bool wrapflag);

/* Get a list of n comma separated doubles */
double *dgetparlist(FILE *fp,char *parameter, int n, bool wrapflag);
char *sgetpar(FILE *fp,char *parameter, bool wrapflag);
char *sgetpar(FILE *fp,char *parameter,const char *default_val, bool wrapflag);
bool bgetpar(FILE *fp, char *parameter, bool wrapflag);
bool bgetpar(FILE *fp, char *parameter, int default_val, bool wrapflag);
char *SearchToken(FILE *fp, char *token, bool wrapflag);
int TokenInLineP(char *line,char *token);
void SkipToken(FILE *fp,char *token, bool wrapflag);
void SkipLine(FILE *fp);
char *bool_str(bool bool_var);

