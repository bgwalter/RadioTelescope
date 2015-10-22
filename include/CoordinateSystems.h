/*
    CoordinateSystems.h
    2015 October 15
    Brendon Walter

    Classes for Right Ascension (RA), declination (Dec), Altitude (Alt),
    Azimuth (Az), Lattitude (Lat), and Longitude (Long).
    
    Methods for each class are found in CoordinateSystems.cpp
*/

#ifndef COORDINATESYSTEMS_H
#define COORDINATESYSTEMS_H

#include <iostream>
#include <string>
#include <sstream>

/*
	Base class for all coordinate systems which use minutes and seconds.
	
	Coordinate systems which use hours should also inherit from Coordinate_Hour, 
	and sysetems which use degrees should also inherit from Coordinat_Degree.
*/
class Coordinate_MinuteSecond {
  protected:
    float minute, second;

  public:
  
  	// constructor
  	Coordinate_MinuteSecond();
  
    /*
        Parametes: float values for the minutes and seconds between 0 and 60
        Returns: 1 (true) if set correctly or 0 (false) if an invalid parameter
            was given
    */
    bool setMinute(float);
    bool setSecond(float);
    
    /*
        Parameters: None
        Returns: float value for the minute or second of the object
    */
    float getMinute();
    float getSecond();
};

/*
	Base class for all coordinate systems which use hours. Classes should also
	inherit from Coordinate_MinuteSecond if the system uses minutes and seconds
	as well.
*/
class Coordinate_Hour {
  protected:
  	float hour;
  	
  public:
  
  	// constructor
  	Coordinate_Hour();
  
  	/*
  		Parameters: float value for hours between 0 and 24
  		Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
  			was given
  	*/
  	bool setHour(float);
  	
  	/*	
  		Parameters: None
  		Returns: float value for the hours of the object
  	*/
  	float getHour();
};

/*
	Base class for all coordinate systems which use degrees. Classes should also
	inherit from Coordinate_MinuteSecond if the system uses minutes and seconds
	as well.
*/
class Coordinate_Degree {
  protected:
  	float degree;
  	int minDegree, maxDegree;	// values between which an angle can exist
  	
  public:
  	
  	// constructor
  	Coordinate_Degree();
  
  	/*
  		Parameters: float value for degrees between -180 and 180
  		Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
  			was given
  	*/
  	bool setDegree(float);
  	
  	/*
  		Parameters: None
  		Returns: float value for the degrees of the object
  	*/
  	float getDegree();
};

#endif