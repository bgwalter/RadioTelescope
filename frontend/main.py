import sys

from configobj import ConfigObj
from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from astropy.time import Time
from astroplan import Observer, FixedTarget, add_site
from datetime import datetime
from telescope import Telescope
from allsky import AllSky
import json
from astropy import units as u

from PyQt5 import QtGui, QtCore, QtWidgets
import gui


# parse configuration file
config = ConfigObj("config.ini")
location = config["LOCATION"]
objects = config["OBJECTS"]
'''
with open('catalogs/messier.json', 'r') as f:
    messier = json.load(f)


with open('catalogs/brightstars.json', 'r') as f:
    stars = json.load(f)
'''

# set new Observer object from config file
add_site(location["SITE_NAME"], EarthLocation(lat=location["LATITUDE"],
            lon=location["LONGITUDE"]))
telescope = Telescope(Observer.at_site(location["SITE_NAME"]))

fixed_targets = {}
for key in objects:
	coordinates = SkyCoord(objects[key]["RA"], objects[key]["DEC"])
	fixed_targets[key] = FixedTarget(name=key, coord=coordinates)

'''
for key in messier:
    RA = messier[key]['Coord']['RA']
    Dec = messier[key]['Coord']['Dec']
    m = messier[key]['Messier Number']
    coordinates = SkyCoord(RA*u.degree, Dec*u.degree)
    fixed_targets[key] = FixedTarget(name=m, coord=coordinates)

for key in stars:
    RA = stars[key]['Coord']['RA']
    Dec = stars[key]['Coord']['Dec']
    n = stars[key]['Proper Name']
    coordinates = SkyCoord(RA*u.degree, Dec*u.degree)
    fixed_targets[key] = FixedTarget(name=n, coord=coordinates)
'''

#telescope.printTelescope()
# telescope.slewToObject(fixed_targets["ALTAIR"])
#telescope.record()
#telescope.slewToObject(fixed_targets["DENEB"])

#allsky = AllSky(objects = fixed_targets)
#print("drawing")
#allsky.draw(telescope.Observer, telescope.getTime())

gui.run(telescope)
