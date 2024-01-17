MUSCLE3_DIR = "../lib/muscle3/muscle3"

TARGET = focaladhesions
MAINFILE = "models/focaladhesions.cpp"

include(Tissue_Simulation_Toolkit.pri)

HEADERS += util/muscle3/*.hpp cpm_ecm/*.hpp
SOURCES += util/muscle3/*.cpp cpm_ecm/*.cpp

INCLUDEPATH += $$MUSCLE3_DIR/include
LIBS += -L$$MUSCLE3_DIR/lib -lmuscle -lymmsl

