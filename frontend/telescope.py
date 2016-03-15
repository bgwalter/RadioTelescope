from datetime import datetime
from astropy.time import Time
from astropy.coordinates import SkyCoord


class Telescope:

    def __init__(self, observer):
        '''
        Initialize self with and observer object #and a park location

        Parameters
        ----------
        observer : `~astroplan.Observer`
            Information about the location of the telescope

        # park : `~astropy.coordinates.AltAz
        #    Park location for the telescope
        '''

        self.Observer = observer
        # self.park = park            # TODO: Figure this out
        self.tracking = False

    def getTime(self):
        '''
        Return a `astropy.time.Time` time object with a `datetime` format
        '''

        return Time(datetime.now())

    def printTelescope(self):
        '''
        Print information about the telescope to the screen
        '''

        print(self.Observer.name)

        print("Latitude: %s\tLongitude: %s" %
              (self.Observer.location.latitude,
               self.Observer.location.longitude))

        print("Current time is %s" % (self.getTime()))
        # print("Telescope park location: %s, %s" %
        #        (self.park.az, self.park.alt))

    def slewToCoord(self, ra, dec, time=None):
        '''
        Slew the telescope to a given AltAz

        Parameters
        ----------
        ra : float
            Right Ascension in degrees

        dec : float
            Declination in degrees

        time : `~astropy.time.Time` (optional)
            Time of the observation. If left blank, it will default to
            the current time.
        '''

        print("Slewing to RA: %s, Dec: %s..." % (ra, dec))

        # check if the coordinates are above the horizon
        if not time:
            time = self.getTime()

        coord = SkyCoord(ra, dec)
        if not self.Observer.target_is_up(time, coord):
            print("Target RA: %s, Dec: %s is below the horizon." % (ra, dec))
            return

#        call to C++ code goes here

        print("Finished slewing to RA: %s, Dec: %s." % (ra, dec))

    def slewToObject(self, obj):
        '''
        Slew the telescope to an object

        Parameters
        ----------
        obj : `~astroplan.FixedTarget`
            Object to observe
        '''

        print("Slewing to %s..." % (obj.name))
        self.slewToCoord(obj.ra, obj.dec)

    def trackObject(self, obj):
        '''
        Track an object through the sky

        Parameters
        ----------
        obj : `~astroplan.FixedTarget`
            Object to track
        '''

        self.tracking = True

        print("Slewing to %s..." % (obj.name))
        self.slewToObject(obj)

        print("Tracking %s" % (obj.name))
        while self.tracking:
            self.slewToObject(obj)

    # TODO: Figure out parking
#    def park(self, park=None):
#
#        Park the telescope at a certain location. If no location is
#        given, park at the initialized location.
#
#        Parameters
#        ----------
#        park : `~astropy.coordinates.AltAz` (optional)
#            Location to park the telescope at
#
#
#        if not park: park = self.park
#
#        print("Parking scope at %s" %park)
#
#        call to C++ code goes here
#
#        print("Finished parking")

    def record(self, outFile=None):
        '''
        Records radio signals to an outfile. If no file is specified, it
        records to a .txt file with the current date and time as the
        title.

        Parameters
        ----------
        outFile : str
            Name of the file to write to
        '''

        if not outFile:
            outFile = str(datetime.today()) + '.txt'

        print("recording to %s" % outFile)

#        call to C++ code goes here

#        with open(outFile, 'a') as f:
#            f.write(c++output)
