TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle

#CONFIG += release
CONFIG += debug
CONFIG += c++17

# Select the graphics backend by uncommenting it.
# - GL graphics requires the GLUT and GLEW libraries.
#     It should be the fastest but does not
#     implement image writing yet.
# - Qt graphics requires Qt 5 or Qt 6.
#     Use this for MacOS.
#     It implements image writing.
# - QtGL graphics requires Qt 5 or Qt 6.
#     It is unfinished.
# - X11 graphics (no longer supported) requires X11 development libraries
#     Old graphics backend, Qt can also use X11.
#     Generally only works on unix systems.
GRAPHICS = qt
#GRAPHICS = gl
#GRAPHICS = qtgl

# Enable or disable the profiling macros
# defined in util/profiler.h.
#PROFILING = enabled
PROFILING = disabled

#USECUDA = enabled
USECUDA = disabled

LIBDIR = ../lib
DESTDIR = ../bin
OBJECTS_DIR = ../build_files
MOC_DIR= ../build_files

MCDS_DIR  = $$LIBDIR/MultiCellDS/v1.0/v1.0.0/libMCDS
XSDE_DIR  = $$MCDS_DIR/xsde/libxsde
LIBCS_DIR = $$LIBDIR/libCellShape

LIBS += -L$$LIBCS_DIR -lcellshape
# LIBS += -L$$MCDS_DIR/mcds_api -lmcds
LIBS += -L$$XSDE_DIR/xsde/ -lxsde

macx {
  QMAKE_LFLAGS += -framework OpenCL
}
unix:!macx {
  LIBS += -lOpenCL
}

QMAKE_CXXFLAGS += -I$$LIBCS_DIR
QMAKE_CXXFLAGS += -I$$MCDS_DIR/mcds_api
QMAKE_CXXFLAGS += -I$$XSDE_DIR
QMAKE_LFLAGS += -m64 -std=c++11 -O3
QMAKE_CXXFLAGS += -Wno-unused-parameter



message("Building model:" $$MODEL )

HEADERS += adhesions/*.hpp \
           cellular_potts/*.hpp \
           parameters/*.hpp \
           plotting/*.hpp \
           reaction_diffusion/*.hpp \
           reaction_diffusion/*.h \
           util/*.hpp \
           compute/*.hpp \
           spatial/*.hpp


SOURCES += adhesions/*.cpp \
           cellular_potts/*.cpp \
           parameters/*.cpp \
           plotting/*.cpp \
           util/*.cpp \
           compute/*.cpp \
           spatial/*.cpp \
           graphics/graph.cpp

SOURCES += $$MAINFILE

contains ( USECUDA, disabled ){
   SOURCES += reaction_diffusion/*.cpp
}


INCLUDEPATH += adhesions/ \
               cellular_potts/ \
               graphics/ \
               models/ \
               parameters/ \
               plotting/ \
               reaction_diffusion/ \
               util/ \
               xpm/ \
               compute/ \
               spatial/ \
               ./


contains( USECUDA, enabled ){
   # File(s) containing CUDA code
   CUDA_SOURCES = reaction_diffusion/pde_cuda.cu
   CUDA_HEADERS = reaction_diffusion/pde_cuda.cuh

   # Location of CUDA on system
   CUDA_DIR = $$system(which nvcc | sed 's,/bin/nvcc$,,')
   INCLUDEPATH += ${CUDA_DIR/include}
   INCLUDEPATH += $$QT.includePath/QtWidgets
   QMAKE_LIBDIR += $$CUDA_DIR/lib
   LIBS += -L$$CUDA_DIR/lib64 -lcuda -lcudart -lcusparse


   cuda.input = CUDA_SOURCES
   cuda.headers = CUDA_HEADERS
   cuda.output = ${OBJECTS_DIR}${QMAKE_FILE_BASE}.o
   cuda.commands = nvcc -c -Xcompiler $$join(QMAKE_CXXFLAGS,",") $$join(INCLUDEPATH,'" -I "','-I "','"') ${QMAKE_FILE_NAME} -o ${QMAKE_FILE_OUT}
   cuda.dependcy_type = TYPE_C
   cuda.depend_command = nvcc -M -Xcompiler $$join(QMAKE_CXXFLAGS,",") $$join(INCLUDEPATH,'" -I "','-I "','"') ${QMAKE_FILE_NAME} | sed "s,^.*: ,," | sed "s,^ *,," | tr -d '\\n'
   QMAKE_EXTRA_COMPILERS += cuda

   QMAKE_CXXFLAGS_RELEASE += -DCUDA_ENABLED
   QMAKE_CXXFLAGS_DEBUG += -DCUDA_ENABLED
}


contains( GRAPHICS, qt ) {
   message("Using QT graphics")
   SOURCES += graphics/qtgraph.cpp
   HEADERS += graphics/qtgraph.hpp
   QMAKE_CXXFLAGS_RELEASE += -DQTGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DQTGRAPHICS 
   QT += widgets
}

contains( GRAPHICS, gl ) {
   message("Using OpenGL graphics")
   SOURCES += graphics/glgraph.cpp
   HEADERS += graphics/glgraph.hpp
   LIBS += -lglut -lGLU -lGL -lGLEW 
   QMAKE_CXXFLAGS_RELEASE += -DGLGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DGLGRAPHICS 
}

contains( GRAPHICS, qtgl ) {
   message("Using Qt based OpenGL graphics")
   SOURCES += graphics/qtglgraph.cpp
   HEADERS += graphics/qtglgraph.hpp
   QT += opengl
   QMAKE_CXXFLAGS_RELEASE += -DQTGLGRAPHICS
   QMAKE_CXXFLAGS_DEBUG += -DQTGLGRAPHICS
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

contains( PROFILING, enabled ) {
  QMAKE_CXXFLAGS_RELEASE += -DPROFILING_ENABLED
  QMAKE_CXXFLAGS_DEBUG += -DPROFILING_ENABLED
}
