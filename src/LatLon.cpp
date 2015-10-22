/*
	LatLon.cpp
	2015 October 20
	Brendon Walter
	
	Methods for the lattitude (lat) and longitude (lon) classes found in 
	CoordinateSystems.h
*/

#include "CoordinateSystems.h"
#include "LatLon.h"

/* Methods from the Lat class */

Lat::Lat() {
  	direction = 'X';
	maxDegree = 90;
	minDegree = 0;
} 

bool Lat::setDirection(char c) {
	if (c == 'N' || c == 'S') {
		direction = c;
		return 1;
	}
	return 0;
}

bool Lat::setLat(float d, char c, float m, float s) {
	if (setDegree(d) && setDirection(c) && setMinute(m) && setSecond(s)) 
		return 1;
	return 0;
}

std::string Lat::getLat() {
	std::stringstream lat;
  	lat << degree << direction << " " << minute << "m " << second << "s ";
  	return lat.str();
}
  
float Lat::toDegrees() {
  	float deg = degree + minute/60 + second/3600;
  	if (direction == 'N') return (deg);
  	if (direction == 'S') return (-deg);
  	return 0;
}

/* Methods from the Lon class */ 

Lon::Lon() {
 	direction = 'X';
	maxDegree = 180;
	minDegree = 0;
}

bool Lon::setDirection(char c) {
	if (c == 'E' || c == 'W') {
		direction = c;
		return 1;
	}
	return 0;
}

bool Lon::setLon(float d, char c, float m, float s) {
	if (setDegree(d) && setDirection(c) && setMinute(m) && setSecond(s)) 
		return 1;
	return 0;
}

std::string Lon::getLon() {
 	std::stringstream lon;
  	lon << degree << direction << " " << minute << "m " << second << "s ";
  	return lon.str();
}

float Lon::toDegrees() {
  	float deg = degree + minute/60 + second/3600;
  	if (direction == 'E') return (deg);
  	if (direction == 'W') return (-deg);
  	return 0;
}