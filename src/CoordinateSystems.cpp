/*
	CoordinateSystems.cpp
	2015 October 15
	Brendon Walter
	
	Methods for the coordinate system classes found in CoordinateSystems.h
*/

#include "CoordinateSystems.h"


/* Methods from the Coordinate_MinuteSecond class */

Coordinate_MinuteSecond::Coordinate_MinuteSecond() {
    minute = 0;
    second = 0;
}

bool Coordinate_MinuteSecond::setMinute(float m) { 
    if (m < 60 && m >= 0) {
  	    minute = m; 
  	    return 1;
    }
      
  	return 0;
}

bool Coordinate_MinuteSecond::setSecond(float s) { 
    if (s < 60 && s >= 0) {
        second = s;
        return 1;
    }
    
    return 0;
}

float Coordinate_MinuteSecond::getMinute() { return minute; }
float Coordinate_MinuteSecond::getSecond() { return second; }


  
/* Methods from the Coordinate_Hour class */

Coordinate_Hour::Coordinate_Hour() {
	hour = 0;
}

bool Coordinate_Hour::setHour(float h) {
		if (h < 24 && h >= 0) {
			hour = h;
			return 1;
		}
		
		return 0;
	}
	
	float Coordinate_Hour::getHour() { return hour; }
	

	
/* Methods from the Coordinate_Degree class */

Coordinate_Degree::Coordinate_Degree() {
	degree = 0;
	maxDegree = 180;
	minDegree = -180;
}

bool Coordinate_Degree::setDegree(float d) {
	if (d < maxDegree && d > minDegree) {
		degree = d;
		return 1;
	}
	
	return 0;
}

float Coordinate_Degree::getDegree() { return degree; }