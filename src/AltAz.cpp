/*
	AltAz.cpp
	2015 October 20
	Brendon Walter
	
	Methods for the altitude (alt) and azimuth (az) classes found in 
	CoordinateSystems.h
*/

#include "CoordinateSystems.h"
#include "AltAz.h"

/* Methods from the Alt class */  

Alt::Alt() {
	maxDegree = 90;
	minDegree = 0;
}

bool Alt::setAlt(float d) {
	if (setDegree(d)) return 1;
	return 0;
}

std::string Alt::getAlt() {
	std::stringstream alt;
	alt << degree << "deg";
	return alt.str();
}
  


/* Methods from the Az class */ 

Az::Az() {
	maxDegree = 360;
	minDegree = 0;
}
  
bool Az::setAz(float d) {
	if (setDegree(d)) return 1;
	return 0;
}

std::string Az::getAz() {
	std::stringstream az;
	az << degree << "deg";
	return az.str();
}