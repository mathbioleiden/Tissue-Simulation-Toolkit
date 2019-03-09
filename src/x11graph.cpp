/* 

Copyright 1995-2006 Roeland Merks, Maarten Boerlijst (probably)

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

// This graphics code derives from C code circulating in Utrecht
// University´s Theoretical Biology group around 1995, which was
// (probably) written by Maarten Boerlijst

#include <stdio.h>
#include <unistd.h>
#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <X11/keysym.h>
#include <X11/cursorfont.h>
#include <math.h>
#include <malloc.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <cstring>
#include <errno.h>
#include <png.h>
#include "sticky.h"
#include "x11graph.h"
#include "parameter.h"
#include "output.h"
#include <iostream>
#include <string>

extern Parameter par;
extern int errno;

using namespace std;

X11Graphics::X11Graphics(int xsize, int ysize, const char *movie_file) : Graphics() {
  
  // initialisation of data members
  count=0;
  title=strdup("Cellular Potts");
  server = 0;
  display = 0;
  visual_list = 0;
  colors = 0;
  xfield=xsize;
  yfield=ysize;

  pseudoCol8=1;
  
  old_window_name=0;

  // X11Graphics Initialisation
  // Open window, etc.
  if (par.graphics)
    InitGraphics(xfield, yfield);
  
  if (par.store) {
    if (movie_file) {
      movie_file_name=strdup(movie_file);
      store=true;
      InitStore();
    }
    else       
      store=false;
    // NB dropped default movie name "showbeast.mov"
    // No movie name given, no movie written.
  } else {
    store=false;
  }

  // movie data will also be used for writing images
  movie_data=(unsigned char *)malloc(xfield*yfield*sizeof(unsigned char));

}

X11Graphics::~X11Graphics(void) {

  CloseGraphics();
  free(title);

  if (store) {
    free(film); 
  }
  if (store) 
    if (compressed_movie_p)
      pclose(movie_fp);
    else
      fclose(movie_fp);
    
}

void X11Graphics::BeginScene(void) {
  // nothing
}

void X11Graphics::EndScene(void)
{ 
  if (par.graphics) {
#ifdef USE_XSHM
    if (shm) {// shared memory extension available?
       XShmPutImage(display,window,windowGC,image,0,0,0,0,image->width,image->height,0);
    }
    else
#endif 
      XPutImage(display,window,windowGC,image,0,0,0,0,image->width,image->height);
    }
  
  static int thetime=0;
  if (store && !(thetime++ % par.storage_stride) )
    StoreCompPict();

}

#define NOPVM
#ifndef NOPVM
void X11Graphics::SendScene() {
  
  SendPicture(image_data,xfield,yfield);
}

void X11Graphics::ReceiveScene(int machineindex, int beastindex, int ndish) {
  
  int sizex,sizey;
  char *picture;
  int xpos,ypos;
  int i,j;
  int xdim;
  
 /*  ComputeDimensions(&xdim,&ydim); */
  xdim=(int)(sqrt((float)(ndish)-1.))+1;
 
  /* Receive the picture */
  picture=ReceivePicture(&sizex,&sizey,machineindex);
  
  /* position of this scene in the big picture */
  xpos=(beastindex%xdim)*sizex;
  ypos=(beastindex/xdim)*sizey;

  printf("xp: %d, yp: %d\n",xpos,ypos);
    
  /* Copy the picture in the display window */
  for (i=0;i<sizex;i++)
    for (j=0;j<sizey;j++) {
      if (pseudoCol8) 
	image_data[xpos+i+xdim*sizey*(ypos+j)]=picture[j+ i*sizex ];
      else
	XPutPixel(image,xpos+i,ypos+j,colors[picture[j+i*sizex]].pixel);
      }
  /* And redraw the window .... */
  DrawScene();
}




void X11Graphics::ReceiveScene1(int machineindex, int beastindex, int ndish) {
  
  int sizex,sizey;
  char *picture;
  int xpos,ypos;
  int i,j;
  
 
 
  /* Receive the picture */
  picture=ReceivePicture(&sizex,&sizey,machineindex);
  
  /* position of this scene in the big picture */
  xpos=0;
  ypos=0;
    
  /* Copy the picture in the display window */
  for (i=0;i<sizex;i++)
    for (j=0;j<sizey;j++)
      image_data[xpos+i+sizey*(ypos+j)]=picture[j+ i*sizex ];
  
  /* And redraw the window .... */
  DrawScene();
  
}
#endif

void X11Graphics::ReadColorTable(XColor *cols)
{
   int i;
   int p,q,r;
   char name[50];
   FILE *fpc;

   sprintf(name,"default.ctb");
   if ((fpc = fopen(name,"r")) == NULL) {
     char *message=(char *)malloc(200*sizeof(char));
     if (message==0) {
       throw "Memory panic in X11Graphics::ReadColorTable\n";
     }
     snprintf(message,199,"X11Graphics::ReadColorTable: Colormap '%s' not found.",name);
     //cerr << message << endl;
     throw(message);
     
   }
   while (fscanf(fpc,"%d",&i) != EOF) {
         fscanf(fpc,"%d %d %d\n",&p,&q,&r);
         cols[i].red=p*255;
         cols[i].green=q*255;
         cols[i].blue=r*255;
   }
   fclose(fpc);

}

void X11Graphics::MakeColorMap()
{
  int i,colormap_size;

  //colormap_size = DisplayCells(display, screen);
  colormap_size=256;
  
  if ((colors = (XColor *)malloc(colormap_size*sizeof(XColor))) == NULL) {
    fprintf(stderr, "No memory for setting up colormap\n");
    exit(1);
  }
  for (i=0; i < colormap_size; i++) {
    colors[i].pixel = i;
    colors[i].flags = DoRed | DoGreen | DoBlue;
  }
  XQueryColors(display,DefaultColormap(display,screen),
	       colors,colormap_size);
  ReadColorTable(colors);
  if (pseudoCol8) {
    new_colormap = XCreateColormap(display,
				   RootWindow(display,screen),
				   DefaultVisual(display,screen),
				   AllocAll);
    XStoreColors(display,new_colormap,colors,colormap_size);
    //free(colors);
  } else {
    new_colormap = XDefaultColormap(display,screen);
    for (i=0; i <= 255 && i < colormap_size; i++)
      XAllocColor(display,new_colormap,&colors[i]);
  }
}  

 
int X11Graphics::GetXYCoo(int *X, int *Y)
{
#define KEYBUFSIZE 10
  char keybuffer[KEYBUFSIZE];
  int bufsize=KEYBUFSIZE;
  static unsigned int oldwidth=0,oldheight=0;
  
  KeySym key;
  XComposeStatus cs;
  
  

  if (par.graphics) {
    
    /* initialise oldwidth and oldheight */
    if (oldwidth==0 && oldheight==0) {
      int di;
      unsigned int dui;
      Window dw;
      XGetGeometry(display,window,&dw,&di,&di,&oldwidth,&oldheight,&dui,&dui);
    }
    
    while (XEventsQueued(display,QueuedAfterFlush) > 0) {
      XNextEvent(display, &event);
      if (event.xany.window == window)
	switch (event.type) {
	case Expose:
	  EndScene();
	  return 0;
	  break;
	case KeyPress:
	  XLookupString(&event.xkey,keybuffer,bufsize,&key,&cs);
	  return (int)keybuffer[0];
	  break;
	case MotionNotify:
	  *X = event.xmotion.x;
	  *Y = event.xmotion.y;
	  return MOTION;
	case ButtonPress:
	  *X = event.xbutton.x;
	  *Y = event.xbutton.y;
	  switch (event.xbutton.button) {
	  case Button1:
	    return 1;
	    break;
	  case Button2:
	    return 2;
	    break;
	  case Button3:
	    return 3;
	    break;
	  }
	  break;
	case ConfigureNotify:
	  if ((unsigned int)event.xconfigure.width != oldwidth || 
	      (unsigned int)event.xconfigure.height != oldheight) {
	    *X=event.xconfigure.width;
	    *Y=event.xconfigure.height;
	    oldwidth=*X;
	    oldheight=*Y;
	    Resize();
	    return RESIZE;
	  }
	  break;
	default:
	  return 0;
	  break;
	}
    }
  } else return 0;
  return 0;
}




int X11Graphics::XExposep() {
  
  if (par.graphics) 
    
    if (event.xany.window == window) 
      
      switch (event.type) {
      case Expose:
	if (event.xexpose.count == 0)
	  return TRUE;
	
	/* else: go on and return FALSE */
	
      default:
	return FALSE;
	break;
      }
    
  return FALSE;
  
}



int X11Graphics::GetHeight(Window w) {
  int di;
  unsigned int dui;
  Window dw;
  unsigned int height;
  XGetGeometry(display,w,&dw,&di,&di,&dui,&height,&dui,&dui);
  return (int)height;
}


char *X11Graphics::ChangeTitle (const char *message) {
  
  /* Change name of window: */
  if (!XFetchName(display, window, &old_window_name)) {
    
    /* Window's name fetch unsuccessful, write message to terminal. */
    fprintf(stdout,"%s\n",message);
    
  } else {
    
    /* Write message in window title */
    XStoreName(display,window,message);
        
  }
  
  XFlush(display);
  return old_window_name;
  
}

void X11Graphics::RecoverTitle(void) {

  if (old_window_name) {
    ChangeTitle(old_window_name);
    free(old_window_name);
    old_window_name=0;
  }
  
}


void X11Graphics::InitGraphics(int xsize, int ysize)
{ 
  char **argv=0;
  int i;
  hsize=xfield=xsize;
  vsize=yfield=ysize;
  

  if (par.graphics) { 
    if (!display)
      display = XOpenDisplay(server);
    if (!display) {
      printf("Failed to open display connection to %s\n",
	     XDisplayName(server));
      exit(0);
    }
    screen = DefaultScreen(display);
    visual_info.screen = screen;
    if (!visual_list)
      visual_list = XGetVisualInfo(display,VisualScreenMask,&visual_info,&i);
    
    if (pseudoCol8 && XMatchVisualInfo(display,screen,8,PseudoColor,&visual_info)) {
      visual = visual_info.visual;
      depth = visual_info.depth;
      if (VERBOSE) printf("Got PseudoColor with Depth %d\n",depth);
    }else{
      pseudoCol8 = 0;
      visual = XDefaultVisual(display, screen);
      depth = XDefaultDepth(display, screen);
      if (VERBOSE) printf("Got default Visual with Depth %d\n",depth);
    }
    colourclass = visual->c_class;
    if (depth == 1) color_screen = 0;
    else if (colourclass == GrayScale) color_screen = 0;
    else if (colourclass == PseudoColor) color_screen = 1;
    else if (colourclass == DirectColor) color_screen = 1;
    else if (colourclass == TrueColor) color_screen = 1;
    else if (colourclass == StaticColor) color_screen = 1;
    else if (colourclass == StaticGray) color_screen = 1;
    hint.x = 0; hint.y = 0;
    hint.width = hsize; hint.height = vsize;
    hint.min_width=xfield;
    hint.min_height=yfield;
    hint.flags = PPosition | PSize | PMinSize;

    if (!colors)
      MakeColorMap();
    black = BlackPixel(display, screen);
    white = WhitePixel(display, screen);
    background = white;
    foreground = black;
  
    setattributes.colormap = new_colormap;
    setattributes.background_pixel = WhitePixel(display,screen);
    background=0;
 
    setattributes.border_pixel = BlackPixel(display,screen);
    
    window = XCreateWindow(display,
			   DefaultRootWindow(display), hint.x, hint.y,
			   hint.width, hint.height, 5 , depth,
			   InputOutput, visual,
			   CWColormap | CWBackPixel | CWBorderPixel,
			   &setattributes);
    XSetStandardProperties(display, window, title, title,
			   None, argv, 0, &hint);
    XGetWindowAttributes(display,window,&attributes);

    if (DoesBackingStore(DefaultScreenOfDisplay(display))) {
      setattributes.backing_store = WhenMapped;
      XChangeWindowAttributes(display,window,CWBackingStore,&setattributes);
    
    }
    
    windowGC = XCreateGC(display, window, 0, 0);
    XSetBackground(display, windowGC, background);
    XSetForeground(display, windowGC, foreground);
    XSetLineAttributes(display,windowGC,1,LineSolid,CapRound,JoinRound);

    XSelectInput(display, window, ButtonPressMask | ExposureMask | KeyPressMask | StructureNotifyMask);
 
    XMapRaised(display, window);
    XNextEvent(display, &event);
  }  

  // Try to attach to shared memory

#ifdef USE_XSHM
  if (XShmQueryExtension(display)) {
    printf("Shared memory extension will be used\n");
    shm=1;
  }
#endif
  //shm=0;
  printf("store %d, graphics %d\n",store,par.graphics);
  printf("depth/8 = %d\n",depth/8);
  if (pseudoCol8) {
    image_data = (char *)malloc(xfield*yfield*sizeof(char));
    for (int i=0;i<xfield*yfield;i++) {
      image_data[i]=1;
    }
  } else {
    // True color visuals
    image_data = (char *)malloc(xfield*yfield*sizeof(char)*6);
    for (int i=0;i<xfield*yfield*6;i++) {
      image_data[i]=1;
    }
  }
  //  if (pseudoCol8) {
  //  movie_data=image_data;
  //} else {
  //}
  if (image_data == NULL) printf("Error in memory allocation\n"); 

#ifdef USE_XSHM
  if (graphics && shm) { 
    
    image = XShmCreateImage(display, visual, depth, ZPixmap, NULL, &shminfo,  xfield, yfield);
    // Allocate shared memory
    shminfo.shmid = shmget (IPC_PRIVATE,
			    image->bytes_per_line *image->height, 
			    IPC_CREAT|0777);
    
    // Attach the shared memory segment to the process
    shminfo.shmaddr = image->data = shmat (shminfo.shmid, 0, 0);
    
    
    // Reading and writing to the shm will be made possible
    shminfo.readOnly = False;
    
    if (!XShmAttach (display, &shminfo)) {
      printf("Warning: shared memory extension is available, but allocation of \n shared memory segment failed... Reverting to private memory. \n This is not problematic, but it will be a bit slower.\n");
      shm=0;
      
    } else {

      printf("Successfully prepared for using shared memory.\n");
    }
    
    
  } else { // Shared memory is unavailable
#endif 

    if (pseudoCol8) {
      image_data = (char *)malloc(xfield*yfield*sizeof(char));
    } else {
      // True color visuals
      image_data = (char *)malloc(xfield*yfield*sizeof(char)*6);
    }
    if (image_data == NULL) {

      printf("Error in memory allocation\n"); 
      exit (1);
    }
    
    // Create XImage structure
    if (par.graphics) {
      image = XCreateImage(display, visual, depth, ZPixmap,
			   0, image_data, xfield, yfield, 8, 0);
      // Clear image
      for (int x=0;x<xfield;x++) {
	for (int y=0;y<yfield;y++) {
	XPutPixel(image,x,y,colors[0].pixel);
	}
      }
    }
    

#ifdef USE_XSHM
  }
#endif

  // Wait for MapNotify event

  for(;;) {
    XEvent e;
    XNextEvent(display, &e);
    if (e.type == MapNotify)
      break;
  }

  printf("MapNotify Event passed\n");
}

void X11Graphics::CloseGraphics()
{
/* Free the memory that was allocated in InitGraphics */
  if (par.graphics) {
    XClearWindow(display,window);
    XDestroyImage(image);
  }

  if (par.graphics) {
    XFreeGC(display,windowGC); 
    XDestroyWindow(display,window); 
    XCloseDisplay(display);   
  }
} 




void X11Graphics::Point( int color, int x, int y)
{
  // The following is not necessary for 8-bits graphics
  // therefore I commented it out.
  // if (pseudoCol8) {
    
  //  (image_data)[i+j*xfield] = (char)color;
  //} else {
  if (color<0) color=0;
  if (par.graphics)
    XPutPixel(image,x,y,colors[color].pixel);
  movie_data[x+y*xfield]=(unsigned char)color;
  //}
}

/*void X11Graphics::Line ( int x1, int y1,int x2,int y2,int colour )
{
  // Usage of Lines in movies is not (yet) implemented
  if (par.graphics) {
    XSetForeground(display, windowGC, colour);
    XDrawLine(display,window,windowGC,x1,y1,x2,y2);
    XSetForeground(display, windowGC, foreground);
  }
  }*/

void X11Graphics::Line(  int x0, int y0,int x1,int y1,int color ) {
  
  // Bresenham's line algorithm
  // See http://www.fact-index.com/b/br/bresenham_s_line_algorithm_c_code.html

  // Provided to supply a line drawing algorithm that allows
  // for writing the lines to a picture or a movie
  
  // (and I need Bresenham for the Lacunae measurement algorithm, and
  // want to see whether it works correctly :-) and it does :-)!
  int i;
  int steep = 1;
  int sx, sy;  /* step positive or negative (1 or -1) */
  int dx, dy;  /* delta (difference in X and Y between points) */
  int e;

  /* * inline swap. On some architectures, the XOR trick may be faster */ 
  int tmpswap; 
#define SWAP(a,b) tmpswap = a; a = b; b = tmpswap;

  /* * optimize for vertical and horizontal lines here */ 
  dx = abs(x1 - x0); 
  sx = ((x1 - x0) > 0) ? 1 : -1; 
  dy = abs(y1 - y0); 
  sy = ((y1 - y0) > 0) ? 1 : -1; 
  if (dy > dx) { 
    steep = 0; 
    SWAP(x0, y0); 
    SWAP(dx, dy); 
    SWAP(sx, sy); 
  } 
  e = (dy << 1) - dx; 
  for (i = 0; i < dx; i++) { 
    if (steep) { 
      Point(color,x0,y0); 
    } else { 
      Point(color,y0,x0); 
    } 
    while (e >= 0) { 
      y0 += sy; e -= (dx << 1); 
    } 
    x0 += sx; e += (dy << 1); 
  } 
}

// Plot a field of values in this window,
// assuming they have the same dimensions
void X11Graphics::Field (const int **r, int mag) {
  for (int x=0;x<xfield;x++) {
    for (int y=0;y<yfield;y++) {
      Point(r[x/mag][y/mag],x,y);
      
    }
  }
  if (par.graphics)
    EndScene();
}



void X11Graphics::InitStore(void)
{
  //  short col[256*3];
  int pars[3];
  //FILE *fpc;
  //  if (!par.graphics) 
  //  InitGraphics(xfield, yfield); 
  // NB: movie data is always allocated in constructor, so we can write images
  film = (unsigned char *)malloc(2*xfield*yfield*sizeof(unsigned char));

  if (FileExistsP(movie_file_name)) {
    std::cerr << "Refusing to overwrite movies. \n Please remove or rename file " 
	 << movie_file_name << " and try again.\n";
    exit(1);
  }

  // check if user wants a compressed movie
  if (strstr(movie_file_name,".gz")) {
    // yes, found ".gz", open a pipe to gzip
    fprintf(stderr,"Writing compressed movie\n");
    char *command=(char *)malloc(1000*sizeof(char));
    snprintf(command,1000,"gzip -c > %s",movie_file_name);
    movie_fp=popen(command,"w");
    free(command);
    compressed_movie_p=true;
  } else {
    fprintf(stderr,"Writing uncompressed movie\n");
    movie_fp=fopen(movie_file_name,"w"); 
    compressed_movie_p=false;
  }
  
  if (movie_fp==NULL) {
    char *error_message=(char *)malloc(200*sizeof(char));
    snprintf(error_message,199,"In X11Graphics::InitStore, %s\n",
	     movie_file_name);
    perror(error_message);
    free(error_message);
    exit(1);
  }
  
  pars[0] = (int)yfield;
  pars[1] = (int)xfield;
  printf("%d %d\n",yfield,xfield); 
  fwrite(pars,sizeof(int),2,movie_fp); 

}



int X11Graphics::DetectControl()
{
  int mouse = 0;
  if (par.graphics) {
    while (XEventsQueued(display,QueuedAfterFlush) > 0) {
      XNextEvent(display, &event);
      switch (event.type) {
      case Expose:
	EndScene();
	break;
      case VisibilityNotify:
	EndScene();
	break;
      case ButtonPress:
        mouse   = 1;
	break;
      default:
	break;
      }
    }
  }
  return (mouse);
 
}

void X11Graphics::StoreCompPict(void)
{
  int dist;
  long k,t=0,params[5];
  
  if ( store ) {
    
    dist=1;t=0;
    
    for (k=1;k<xfield*yfield;k++) {
      if (dist == 255 || (movie_data)[k] != (movie_data)[k-1]) {
	film[t++] = (unsigned char)dist;
	film[t++] = (movie_data)[k-1];
	dist =1;
      }
      else 
	++dist;
    }
    film[t++] = (unsigned char)dist;
    film[t++] = (movie_data)[k-1];
    params[0]=yfield;
    params[1]=xfield;
    params[2]=0;
    params[3]=0;
    params[4]=(long)(t/2);

    // Appending to a file using open is very unsafe
    // over NFS. Indeed the files are corrupted.
    // It is safer to open the file only once and to keep the 
    // file descriptor in a static int.
    
    // RM. 14/05/03

    // AND, from now on we will be using fread and fwrite. Much
    // safer. (Less efficient?) 
    
    // RM. 14/05/03

    //lseek(fps,0L,2);
    
    fwrite(params,sizeof(long),5,movie_fp); 
    fwrite(film,sizeof(unsigned char),t,movie_fp);
    fflush(movie_fp);
    //close(fps);
    ++count;
  }
}


// testbed
/*
  int main(int argc, char *argv[]) {
  
  int s=50;
  X11Graphics *g=new X11Graphics[100](s,s);
  
  sleep(2);
  for (int c=0; c<100;c++) {
    for (int i=0;i<s*s;i++) {
      //g.Point((int)(sin(((double)i)/5000.)*127)+127, i%s, i/s);
      g[c].Point(c, i%s, i/s);
    }
    g[c].EndScene();
  }
  
  while(1);

  delete[] g;

  }*/


int X11Graphics::LineClearP(char direction,int pos, int cropcol) {

  /* returns TRUE if no pixels of this line are occupied by a cell */
  int x,y;

  if (direction=='x') {
    for (y=1;y<yfield-1;y++) 
      if (XGetPixel(image, pos, y)!=colors[cropcol].pixel) 
	return false;
  } else 
    if (direction=='y') {
      for (x=1;x<xfield-1;x++)
	if (XGetPixel(image, x, pos)!=colors[cropcol].pixel)
	  return false;
    } else {
      char *error=(char *)malloc(200*sizeof(char));
      snprintf(error,199,"LineClearP error: %c is an unknown option.",direction);
      throw (error);
      exit(1);
    }
  
  return true;

}

LineType X11Graphics::CropSize(void) {

  /* Returns the upper left and the lower right coordinates 
     of the beast */
  
  LineType CropSize;
  int x,y;
  
  for (x=1;x<xfield-1;x++) 
    if (!LineClearP('x',x)) {
      CropSize.x1=x;
      break;
    }
  
  for (y=1;y<yfield-1;y++) 
    if (!LineClearP('y',y)) {
      CropSize.y1=y;
      break;
    }

  for (x=xfield-1;x>0;x--) 
    if (!LineClearP('x',x)) {
      CropSize.x2=x;
      break;
    }
  
  for (y=yfield-1;y>0;y--) 
    if (!LineClearP('y',y)) {
      CropSize.y2=y;
      break;
    }

  return CropSize;

}

Coordinate X11Graphics::ReplaceBeast(Coordinate old_size,Coordinate new_size) {
  
  Coordinate offset;
  int x,y,button;
  Cursor hand;
  
  offset.x=0;
  offset.y=0;
  
  /* Change name of window: */
  ChangeTitle("Replace beast, please.");

  XSetBackground(display, windowGC, WhitePixel(display, screen));
  XSetForeground(display, windowGC, BlackPixel(display, screen));
  XClearWindow(display,window);
  XDrawRectangle(display,window,windowGC,offset.x,offset.y,old_size.x,old_size.y);  
  XFlush(display);
  
  XSelectInput(display, window, ButtonPressMask | PointerMotionMask);
  
  hand=XCreateFontCursor(display, XC_hand1);
  
  XGrabPointer(display,window,TRUE,ButtonPressMask | PointerMotionMask, GrabModeAsync,GrabModeAsync,window, hand,CurrentTime);
      
  while ((button=GetXYCoo(&x,&y))!=1) {
    if (button==MOTION) {

      if (x+old_size.x < new_size.x)
	offset.x=x;
      if (y+old_size.y < new_size.y)
	offset.y=y;
      
      XClearWindow(display, window);
      XDrawRectangle(display,window,windowGC,offset.x,offset.y,old_size.x,old_size.y); 
      XFlush(display);



    }
  }

  XUngrabPointer(display,CurrentTime);
  RecoverTitle();

  XSelectInput(display, window, ButtonPressMask | KeyPressMask | 
		 ExposureMask | StructureNotifyMask);
  
  return offset;
} 
  

void X11Graphics::Resize(void) {
  
#ifdef USE_XSHM
  extern int shm;
  extern XShmSegmentInfo shminfo;
#endif
  unsigned int newheight, newwidth;

  // some dummy variables:
  int di;
  unsigned int dui;
  Window dw;
  

  // Get rid of pending events 
  // many resize events are generated during a resize
  sleep(1);

  while (XEventsQueued(display,QueuedAfterFlush) > 0) {
    XNextEvent(display, &event);
  }

  //  do  {
  //  sleep(1);
  //} while (GetXYCoo(&x,&y)==RESIZE);

  // Get the geometry
  XGetGeometry(display,window,&dw,&di,&di,&newwidth,&newheight,&dui,&dui);
  printf("%d %d\n",newwidth, newheight);

  int old_xfield=xfield;
  int old_yfield=yfield;
  xfield=newwidth;
  yfield=newheight;
      
  printf("New xfield: %d, yfield: %d\n",xfield,yfield);
  
#ifdef USE_XSHM
  if (!shm) {
#endif
  
    
#ifdef USE_XSHM
  } else {
    
    // Shared memory was used
    // Destroy memory segment and XImage
    
    XShmDetach(display, &shminfo);
    XDestroyImage(image);
    shmdt(shminfo.shmaddr);
    shmctl(shminfo.shmid, IPC_RMID, 0);
    
    // Generate new segment and attach to it
    shminfo.shmid = shmget (IPC_PRIVATE,
			    image->bytes_per_line * image->height, IPC_CREAT|0777);
    
    
  }
#endif
  
  if (
#ifdef USE_XSHM
      shm || 
#endif 
      image_data != NULL) {
    
    // New Image 
#ifdef USE_XSHM
    if (!shm) {
#endif
      char *new_image_data = (char *)malloc(xfield*yfield*sizeof(char)*depth);
      XImage *new_image = XCreateImage(display, visual, depth, ZPixmap, 
			   0, new_image_data, xfield, yfield, 8, 0);
      // Clear new image
      for (int x=0;x<xfield;x++) {
	for (int y=0;y<yfield;y++) {
	  XPutPixel(new_image, x, y, colors[0].pixel);
	}
      }
      
      // Copy old image into new image
      for (int x=0;x<old_xfield;x++) {
	for (int y=0;y<old_yfield;y++) {
	  XPutPixel(new_image, x, y, 
		    XGetPixel(image, x, y) );
	}
      }

      // Destroy old image, let image point to new image
      XDestroyImage(image);
      image=new_image;
      image_data=new_image_data;
      EndScene();
      
#ifdef USE_XSHM
    } else {
      image_data = (char *)malloc(xfield*yfield*sizeof(char)*depth);
      
      image = XShmCreateImage(display, visual, depth, ZPixmap, 
			      NULL, &shminfo,  xfield, yfield);
      
      // Allocate shared memory
      shminfo.shmid = shmget (IPC_PRIVATE,
			      image->bytes_per_line *image->height, 
			      IPC_CREAT|0777);
      
      // Attach the shared memory segment to the process
      shminfo.shmaddr = image->data = shmat (shminfo.shmid, 0, 0);
      
      
      // Reading and writing to the shm will be made possible
      shminfo.readOnly = False;
      
      if (!XShmAttach (display, &shminfo)) {
	printf("Warning: shared memory extension is available, but allocation of \n shared memory segment failed... Reverting to private memory. \n This is not problematic, but it will be a bit slower.\n");
	shm=0;
	
      } else {
	
	printf("Successfully prepared for using shared memory.\n");
      }
      
    }
#endif
    
    
  }
  if (movie_data) {
    // reallocate moviedata
    free(movie_data);
    movie_data=(unsigned char *)malloc(xfield*yfield*sizeof(unsigned char));
  }
}

void X11Graphics::Write(char *fname, int quality) {

  // NB quality is dummy parameter for compatibility with
  // QtGraphics. No need to supply it. This method can only write PNG.

  // based on code borrowed from Cash2003, png.c

  string name(fname);
  if (name.find("png")==string::npos) {
    throw("X11Graphics::Write: Sorry, only PNG writing is implemented");
  }
  
  cerr << "Writing a PNG picture\n";

  
  int i,j;

  FILE *fp;
  fp = fopen(fname,"wb");
  if (fp==0) {
    perror(fname);
    throw("X11Graphics::Write: File error\n");
  }
  png_structp png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING,
						(png_voidp)NULL, 
						(png_error_ptr)NULL, 
						(png_error_ptr)NULL);
  png_infop info_ptr = png_create_info_struct (png_ptr);
  png_init_io(png_ptr, fp);
  png_set_IHDR(png_ptr, info_ptr, xfield, yfield,
	       8, PNG_COLOR_TYPE_RGB, PNG_INTERLACE_NONE,
	       PNG_COMPRESSION_TYPE_BASE, PNG_FILTER_TYPE_BASE);
  png_write_info(png_ptr,info_ptr);

  // data to hold true colour image
  unsigned char *png_image = 
    (unsigned char *)malloc(3*xfield*yfield*sizeof(unsigned char));

  int colormap_size=256;
  static XColor *png_colors=0;
  if (!png_colors) {
    // We allocate colors upon the first call only
    // so do not free png_colors!
    if ((png_colors = (XColor *)malloc(colormap_size*sizeof(XColor))) == NULL) {
      throw("X11Graphics::Write: No memory for setting up colormap");
    }
    for (i=0; i < colormap_size; i++) {
      png_colors[i].pixel = i;
      png_colors[i].flags = DoRed | DoGreen | DoBlue;
    }
    ReadColorTable(png_colors);
   
    
  }
    for (j=0; j < yfield; j++) {
      for (i=0; i < xfield; i++) {
	XColor col;
	col=png_colors[movie_data[i+j*xfield]];
	
	png_image[j*3*xfield + i*3] = col.red/256;
	png_image[j*3*xfield + i*3 + 1] = col.green/256;
	png_image[j*3*xfield + i*3 + 2] = col.blue/256;
    }
    png_bytep ptr = png_image + j*3*xfield;
    png_write_rows(png_ptr, &ptr, 1);
    }
    png_write_end(png_ptr, info_ptr);
    png_destroy_write_struct(&png_ptr,(png_infopp)NULL);
    free(png_image);
    fclose(fp);
}



