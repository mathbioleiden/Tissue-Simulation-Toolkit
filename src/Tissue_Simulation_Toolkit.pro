TEMPLATE = app 
GRAPHICS = qt
CONFIG += console 
CONFIG += release
#CONFIG += debug
CONFIG -= app_bundle
#QMAKE_MACOSX_DEPLOYMENT_TARGET = 10.6
QT += widgets

MODEL = vessel

LIBDIR = ../lib
DESTDIR = ../bin
TARGET = $$MODEL
MAINFILE = "models/"$$TARGET".cpp"

MCDS_DIR  = $$LIBDIR/MultiCellDS/v1.0/v1.0.0/libMCDS
XSDE_DIR  = $$MCDS_DIR/xsde/libxsde
LIBCS_DIR = $$LIBDIR/libCellShape

LIBS += -L$$LIBCS_DIR -lcellshape 
LIBS += -L$$MCDS_DIR/mcds_api -lmcds 
LIBS += -L$$XSDE_DIR/xsde/ -lxsde 
LIBS += -lOpenCL

QMAKE_CXXFLAGS += -I$$LIBCS_DIR 
QMAKE_CXXFLAGS += -I$$MCDS_DIR/mcds_api 
QMAKE_CXXFLAGS += -I$$XSDE_DIR 
QMAKE_LFLAGS += -m64 -std=c++11

QMAKE_CXXFLAGS += -Wno-unused-parameter

message("Building model:" $$MODEL )

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
   message("Using QT graphics")
   SOURCES += qtgraph.cpp
   HEADERS += qtgraph.h
   QMAKE_CXXFLAGS_RELEASE += -DQTGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DQTGRAPHICS 
}

contains( GRAPHICS, x11 ) {
   !unix {
     error("X11 graphics only available on Unix systems.")
   }
   message("Using X11 graphics")
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

