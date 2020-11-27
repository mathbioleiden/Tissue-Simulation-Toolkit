MCDSDIR = ../MultiCellDS
XSDEDIR = $(MCDSDIR)/v1.0/v1.0.0/libMCDS/xsde/libxsde

INCLUDES += -I $(XSDEDIR)
INCLUDES += -I $(MCDSDIR)/v1.0/v1.0.0/libMCDS/mcds_api/

TARGET_NAME = libcellshape

CXX = g++
CXXFLAGS += -Wall
CXXFLAGS += -std=c++11
CXXFLAGS += -O3
CXXFLAGS += -g

LIB_NAME = $(TARGET_NAME).a
SOURCES  = $(shell find . -name *.cpp)
OBJECTS  = $(SOURCES:.cpp=.o)

all: $(LIB_NAME)

$(OBJECTS):
	$(CXX) -c $(SOURCES) -o $(OBJECTS) $(CXXFLAGS) $(INCLUDES) $(LIBS) 

$(LIB_NAME): $(OBJECTS)
	ar -rcs $(LIB_NAME) $(OBJECTS)

clean:
	rm *.o
	rm *.a
