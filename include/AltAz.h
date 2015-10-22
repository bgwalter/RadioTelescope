/*
    AltAz.h
    2015 October 15
    Brendon Walter

    Classes for Altitude (Alt) and Azimuth (Az).
    
    Methods for each class are found in AltAz.cpp
*/

#ifndef ALTAZ_H
#define ALTAZ_H

/*
	Class for the Altitude (Alt) of an object
	
	The altitude of an object is defined a degree between 0 and 90
*/
class Alt: public Coordinate_Degree {
  public:
	
  	// constructor
  	Alt();
  	
  	/*
  		Parameters: float value for degrees between 0 and 90
  		Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
    		was given
  	*/
  	bool setAlt(float);
  	
  	/*
  		Parameters: None
  		Returns: The altitude of the object as a string
  	*/
  	std::string getAlt();
};

/*
  Class for the Azimuth (Az) of an object

  The azimuth of an object is defined by a degree between 0 and 360
*/
class Az: public Coordinate_Degree {
  public:
  
  	// constructor
  	Az();
  	
  	/*
	 	  Parameters: float value for degrees between 0 and 360
		  Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
  			was given
	  */
  	bool setAz(float);
  	
  	/*
		  Parameters: None
		  Returns: The azimuth of the object as a string
	  */
  	std::string getAz();
};

#endif