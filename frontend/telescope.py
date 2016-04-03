from datetime import datetime
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astropy import units as u


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

    def printTelescope(self, qwindow=None):
        '''
        Print information about the telescope to the screen
        '''

        name = self.Observer.name
        location = ("Latitude: %s\tLongitude: %s" %
                    (self.Observer.location.latitude,
                     self.Observer.location.longitude))
        time = "Current time is %s" % (self.getTime())
#        park = ("Telescope park location: %s, %s" %
#                (self.park.az, self.park.alt))

        if qwindow is None:
            print(name)
            print(location)
            print(time)
#            print(park)
        else:
            qwindow.printInfo(name)
            qwindow.printInfo(location)
            qwindow.printInfo(time)
#            qwindow.printInfo(park)

    def slewToCoord(self, ra, dec, time=None, qwindow=None):
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

        # make sure input coordinates are valid
        try:
            coord = SkyCoord(ra, dec)
        except u.UnitsError:
            self.slewToCoord(float(ra)*u.deg, float(dec)*u.deg, time, qwindow)
            return
        except ValueError:
            error = "Please input a valid format for RA and Dec."\
                    "\nAcceptable formats:\n"\
                    "\t'xxhxxmxxs, xxdxxmxxs'\n\t'xx.xxx, xx.xxx'"
            if qwindow is None: print(error)
            else: qwindow.printInfo(error)
            return

        if time is None:
            time = self.getTime()

        # check if the coordinates are above the horizon
        if not self.Observer.target_is_up(time, coord):
            string = "Target RA: %s, Dec: %s is below the horizon." % (ra, dec)
            if qwindow is None: print(string)
            else: qwindow.printInfo(string)

            return

        string = "Slewing to RA: %s, Dec: %s..." % (ra, dec)
        if qwindow is None: print(string)
        else: qwindow.printInfo(string)

#        call to C++ code goes here

        string = "Finished slewing to RA: %s, Dec: %s." % (ra, dec)
        if qwindow is None: print(string)
        else: qwindow.printInfo(string)

    def slewToObject(self, obj, time=None, qwindow=None):
        '''
        Slew the telescope to an object

        Parameters
        ----------
        obj : `~astroplan.FixedTarget`
            Object to observe

        time : `~astropy.time.Time` (optional)
            Time of the observation. If left blank, it will default to
            the current time.
        '''

        string = "Slewing to %s..." % (obj.name)
        if qwindow is None: print(string)
        else: qwindow.printInfo(string)

        self.slewToCoord(obj.ra, obj.dec, time, qwindow)

    def track(self, ra, dec, time=None, qwindow=None):
        '''
        Track given coordinates

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
        self.tracking = True
        self.slewToCoord(ra, dec, time, qwindow)

        string = "Tracking RA: %s, Dec: %s" % (ra, dec)
        if qwindow is None: print(string)
        else: qwindow.printInfo(string)

        # TODO: Figure out tacking (threading?)
#        while self.tracking:
#            self.slewToCoord(ra, dec, time, qwindow)

    def trackObject(self, obj, time=None, qwindow=None):
        '''
        Track an object through the sky

        Parameters
        ----------
        obj : `~astroplan.FixedTarget`
            Object to track

        time : `~astropy.time.Time` (optional)
            Time of the observation. If left blank, it will default to
            the current time.
        '''

        self.tracking = True

        self.slewToObject(obj)

        string = "Tracking %s" % (obj.name)
        if qwindow is None: print(string)
        else: qwindow.printInfo(string)

#        while self.tracking:
#            self.slewToObject(obj)

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

    def record(self, outFile=None, qwindow=None):
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

        string = "Recording to %s" % outFile
        if qwindow is None: print(string)
        else: qwindow.printInfo(string)

#        call to C++ code goes here

#        with open(outFile, 'a') as f:
#            f.write(c++output)
