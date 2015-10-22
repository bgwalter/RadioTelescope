/*
	RADec.cpp
	2015 October 20
	Brendon Walter
	
	Methods for the right ascenscion (RA) and declination (dec) classes found in 
	CoordinateSystems.h
*/

#include "CoordinateSystems.h"
#include "RADec.h"

/* Methods from the RA class */	
bool RA::setRA(float h, float m, float s) {
	if (setHour(h) && setMinute(m) && setSecond(s))
		return 1;
	
	return 0;
}

std::string RA::getRA() {
	std::stringstream ra;
	ra << hour << "h " << minute << "m " << second << "s";
	return ra.str();
}

float RA::toHours() {
  return (hour + minute/60 + second/3600);
}
	
float RA::toDegrees() {
  return (hour*15 + minute/60 + second/3600);
}

	
/* Methods from the Dec class */	
Dec::Dec() {
	maxDegree = 90;
	minDegree = -90;
}

bool Dec::setDec(float d, float m, float s) {
	if (setDegree(d) && setMinute(m) && setSecond(s))
		return 1;
	
	return 0;
}

std::string Dec::getDec() {
	std::stringstream dec;
	dec << degree << "deg " << minute << "m " << second << "s";
	return dec.str();
}

float Dec::toDegrees() {
  return (degree + minute/60 + second/3600);
}