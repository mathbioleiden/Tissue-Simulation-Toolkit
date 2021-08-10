TEMPLATE = app 
CONFIG += console 
#CONFIG += release
CONFIG += debug
CONFIG -= app_bundle
#QMAKE_MACOSX_DEPLOYMENT_TARGET = 10.6
QT += widgets

#GRAPHICS = qt
GRAPHICS = gl

MODEL = vessel


LIBDIR = ../lib
DESTDIR = ../bin
OBJECTS_DIR = ../build_files
MOC_DIR= ../build_files
TARGET = $$MODEL
MAINFILE = "models/"$$TARGET".cpp"

MCDS_DIR  = $$LIBDIR/MultiCellDS/v1.0/v1.0.0/libMCDS
XSDE_DIR  = $$MCDS_DIR/xsde/libxsde
LIBCS_DIR = $$LIBDIR/libCellShape

LIBS += -L$$LIBCS_DIR -lcellshape 
LIBS += -L$$MCDS_DIR/mcds_api -lmcds 
LIBS += -L$$XSDE_DIR/xsde/ -lxsde 

macx {
  message("Detected MacOS")
  QMAKE_LFLAGS += -framework OpenCL
}

unix:!macx{
  message("Detected Unix") 
  LIBS += -lOpenCL
}

QMAKE_CXXFLAGS += -I$$LIBCS_DIR 
QMAKE_CXXFLAGS += -I$$MCDS_DIR/mcds_api 
QMAKE_CXXFLAGS += -I$$XSDE_DIR 
QMAKE_LFLAGS += -m64 -std=c++11 -O3

QMAKE_CXXFLAGS += -Wno-unused-parameter  

message("Building model:" $$MODEL )

HEADERS += cellular_potts/*.hpp \
           parameters/*.hpp \
           plotting/*.hpp \
           reaction_diffusion/*.hpp \
	   reaction_diffusion/*.h \
           util/*.hpp \
	   compute/*.hpp

 
SOURCES += cellular_potts/*.cpp \
           parameters/*.cpp \
           plotting/*.cpp \
           reaction_diffusion/*.cpp \
           util/*.cpp \
	   compute/*.cpp 

SOURCES += $$MAINFILE

INCLUDEPATH += cellular_potts/ \
               graphics/ \
               models/ \
               parameters/ \
               plotting/ \
               reaction_diffusion/ \
               util/ \
               xpm/ \
	       compute/

       
contains( GRAPHICS, qt ) {
   message("Using QT graphics")
   SOURCES += graphics/qtgraph.cpp
   HEADERS += graphics/qtgraph.hpp
   QMAKE_CXXFLAGS_RELEASE += -DQTGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DQTGRAPHICS 
}

contains( GRAPHICS, gl ) {
   message("Using OpenGL graphics")
   SOURCES += graphics/glgraph.cpp
   HEADERS += graphics/glgraph.hpp
   LIBS += -lglut -lGLU -lGL -lGLEW 
   QMAKE_CXXFLAGS_RELEASE += -DGLGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DGLGRAPHICS 
}

contains( GRAPHICS, x11 ) {
   !unix {
     error("X11 graphics only available on Unix systems.")
   }
   message("Using X11 graphics")
   SOURCES += graphics/x11graph.cpp
   HEADERS += graphics/x11graph.hpp
   QMAKE_CXXFLAGS_RELEASE += -DX11GRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DX11GRAPHICS 
   unix {
      system(rm vessel.o)
   }
   CONFIG -= qt
   CONFIG += x11
   unix:LIBS += -lpng
}

