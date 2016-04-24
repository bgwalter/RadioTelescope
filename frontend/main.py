import sys

from configobj import ConfigObj
from astropy.coordinates import EarthLocation, SkyCoord
from astroplan import Observer, FixedTarget, add_site

from PyQt5 import QtGui, QtCore, QtWidgets

from telescope import Telescope
from allsky import AllSky
import gui


# parse configuration file
config = ConfigObj("config.ini")
location = config["LOCATION"]
objects = config["OBJECTS"]

# set new Observer object from config file
obsLocation = EarthLocation(location["LONGITUDE"], location["LATITUDE"],
                            float(location["ELEVATION"]))
add_site(location["SITE_NAME"], obsLocation)

# add objects to a dictionary of `astroplan.FixedTarget`s
fixed_targets = {}
for key in objects:
    coordinates = SkyCoord(objects[key]["RA"], objects[key]["DEC"])
    fixed_targets[key] = FixedTarget(name=key, coord=coordinates)


skymap = AllSky(objects=fixed_targets)
telescope = Telescope(Observer.at_site(location["SITE_NAME"]))
gui.run(telescope, skymap)

#fig = skymap.draw(telescope.Observer)
#fig.savefig("test.png")
