/*
    LatLon.h
    2015 October 15
    Brendon Walter

    Classes for lattitude (lat) and longitude (lon).
    
    Methods for each class are found in LatLon.cpp
*/

#ifndef LATLON_H
#define LATLON_H

/*
  Class for the Lattitude (Lat) of an object

  The lattitude of an object is defined by degrees, direction (North or South),
  minutes, and seconds.
*/
class Lat: public Coordinate_Degree, Coordinate_MinuteSecond {
  protected:
  	char direction;		// N(orth) or S(outh)
  	
  public:
  	
  	// constructor
  	Lat();
  	
  	bool setDirection(char);
  	
  	/*
		  Parameters: float value for degrees between 0 and 90, char value for 
			  direction (N/S), and float values for minutes and seconds
		  Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
  			was given
    */
  	bool setLat(float, char, float, float);
  	
  	/*
		  Parameters: None
		  Returns: The latitude of the object as a string
    */
  	std::string getLat();

    /*
      Parameters: None
      Returns: Float value of lattitude in degree form. Positive if the
        direction is North, negative if South.
    */
    float toDegrees();
};


/*
  Class for the Longitude (Lon) of an object

  The longitude of an object is defined by degrees, direction (East or West), 
  minutes, and seconds.
*/
class Lon: public Coordinate_Degree, Coordinate_MinuteSecond {
  protected:
  	char direction;		// E(ast) or W(est)
  	
  public:
  
  	// constructor
  	Lon();
  	
  	bool setDirection(char);
  	
  	/*
		  Parameters: float value for degrees between 0 and 90, char value for 
        direction (E/W), and float values for minutes and seconds
		  Returns: 1 (true) if set correctly, 0 (false) if an invalid parameter
  			was given
	  */
  	bool setLon(float, char, float, float);
  	
  	/*
		  Parameters: None
		  Returns: The longitude of the object as a string
	  */
  	std::string getLon();

    /*
      Parameters: None
      Returns: Float value of longitude in degree form. Ppstitive if the
        direction is East, negative if West.
    */
    float toDegrees();
};

#endif