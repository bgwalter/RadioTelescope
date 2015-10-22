/*
    RADec.h
    2015 October 15
    Brendon Walter

    Classes for lattitude (lat) and longitude (lon).
    
    Methods for each class are found in RADec.cpp
*/

#ifndef RADEC_H
#define RADEC_H

/*
	Class for the Right Ascension (RA) of an object
	
	The right ascension of an object is defined by hours, minutes, and seconds.
*/
class RA: public Coordinate_Hour, public Coordinate_MinuteSecond {
  public: 
  
  	/*
  		Parameters: float values for hours, minutes, and seconds (between 0 
  			and 24 and 0 and 60 respectively)
  		Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
  			was given
  	*/
  	bool setRA(float, float, float);
  	
  	/*
  		Parameters: None
  		Returns: The right ascension of the object as a string
  	*/
  	std::string getRA();

    /*
      Parameters: None
      Returns: float value of RA in either hour or degree form
    */
    float toHours();
    float toDegrees();
};

/*
	Class for the Declination (Dec) of an object
	
	The declination of an object is defined by degrees, minutes, and seconds.
*/
class Dec: public Coordinate_Degree, public Coordinate_MinuteSecond {
  public:
  
  	// constructor
  	Dec();
   
  	/*
  		Parameters: float values for degrees, minutes, and seconds (between 
  			-90 and 90 and 0 and 60 respectively)
  		Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
  			was given
  	*/
    bool setDec(float, float, float);
    
    /*
  		Parameters: None
  		Returns: The declination of the object as a string
  	*/
    std::string getDec();

    /*
      Parameters: None
      Returns: Float value of declination in degree form
    */
    float toDegrees();
};

#endif