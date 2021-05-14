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
SOURCES  = $(wildcard *.cpp)
OBJECTS  = $(SOURCES:.cpp=.o)

all: $(LIB_NAME)

%.o : %.cpp
	$(CXX) $< -o $@ $(CXXFLAGS) $(INCLUDES) $(LIBS) -c 

$(LIB_NAME): $(OBJECTS)
	ar -rcs $(LIB_NAME) $(OBJECTS)

clean:
	rm -f *.o
	rm -f *.a
