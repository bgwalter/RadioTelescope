IDIR=include
SDIR=src
CC=g++
CFLAGS=-Wall -I$(IDIR)
OUT=main

_SRC = CoordinateSystems.cpp AltAz.cpp LatLon.cpp RADec.cpp DateAndTime.cpp
SRC = $(patsubst %,$(SDIR)/%,$(_SRC))

all:
	g++ $(SDIR)/main.cc $(SRC) $(CFLAGS) -o $(OUT)
