MUSCLE3_DIR = "../lib/muscle3/muscle3"

TARGET = adhesions
MAINFILE = "models/adhesions.cpp"

include(Tissue_Simulation_Toolkit.pri)

HEADERS += adhesions/muscle3/*.hpp
SOURCES += adhesions/muscle3/*.cpp

INCLUDEPATH += $$MUSCLE3_DIR/include
LIBS += -L$$MUSCLE3_DIR/lib -lmuscle -lymmsl

