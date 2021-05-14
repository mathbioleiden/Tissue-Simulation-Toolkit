TEMPLATE = app 
GRAPHICS = qt
CONFIG += console 
CONFIG += release
CONFIG -= app_bundle
#QMAKE_MACOSX_DEPLOYMENT_TARGET = 10.6
QT += widgets

LIBDIR = ../lib
TARGET = sorting
MAINFILE = $$join(TARGET, " ", , ".cpp" )

MCDS_DIR  = $$LIBDIR/MultiCellDS/v1.0/v1.0.0/libMCDS
XSDE_DIR  = $$MCDS_DIR/xsde/libxsde
LIBCS_DIR = $$LIBDIR/libCellShape

LIBS += -L$$LIBCS_DIR -lcellshape -L$$MCDS_DIR/mcds_api -lmcds -L$$XSDE_DIR/xsde/ -lxsde 

QMAKE_CXXFLAGS += -I$$LIBCS_DIR -I$$MCDS_DIR/mcds_api -I$$XSDE_DIR -I -m64 -std=c++11
QMAKE_LFLAGS += -m64  -std=c++11

message( $$MAINFILE )
message( $$TARGET )
# Input
HEADERS += ca.h \
	   hull.h \
           cell.h \
           conrec.h \
           dish.h \
           graph.h \
           info.h \
           misc.h \
           output.h \
           parameter.h \
           parse.h \
           pde.h \
           random.h \
           sqr.h \
           sticky.h \
       	   crash.h \
	   warning.h 
        
SOURCES += ca.cpp \
	   hull.cpp \
           cell.cpp \
           conrec.cpp \
           dish.cpp \
           info.cpp \
           misc.cpp \
           output.cpp \
           parameter.cpp \
           parse.cpp \
           pde.cpp \
           random.cpp \
           crash.cpp \
           warning.cpp 

SOURCES += $$MAINFILE
       
contains( GRAPHICS, qt ) {
   message( "Building Qt executable" )
   SOURCES += qtgraph.cpp
   HEADERS += qtgraph.h
   QMAKE_CXXFLAGS_RELEASE += -DQTGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DQTGRAPHICS 
   unix {
      system(rm $$TARGET.o)
   } 
   win32 {
     QMAKE_LFLAGS += -L "\"C:\Program Files\GnuWin32\lib\"" -lpng -lzdll
     QMAKE_CXXFLAGS += -I "\"C:\Program Files\GnuWin32\include\""
   }
}

contains( GRAPHICS, qt3 ) {
   message( "Building Qt executable" )
   SOURCES += qt3graph.cpp
   HEADERS += qt3graph.h
   QMAKE_CXXFLAGS_RELEASE += -DQTGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DQTGRAPHICS 
   unix {
      system(rm vessel.o)
   } 
   win32 {
     QMAKE_LFLAGS += -L "C:\Program Files\GnuWin32\lib" -lpng -lzdll
     QMAKE_CXXFLAGS += -I "C:\Program Files\GnuWin32\include"
   }
   LIBS += -lpng
}
contains( GRAPHICS, x11 ) {
   !unix {
     error("X11 graphics only available on Unix systems.")
   }
   message("Building X11 executable")
   SOURCES += x11graph.cpp
   HEADERS += x11graph.h
   QMAKE_CXXFLAGS_RELEASE += -DX11GRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DX11GRAPHICS 
   unix {
      system(rm vessel.o)
   }
   CONFIG -= qt
   CONFIG += x11
   unix:LIBS += -lpng
}
