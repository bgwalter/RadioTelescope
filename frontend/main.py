from configobj import ConfigObj
from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from astropy.time import Time
from astroplan import Observer, FixedTarget, add_site
from datetime import datetime
from telescope import Telescope

# parse configuration file
config = ConfigObj("config.ini")
location = config["LOCATION"]
objects = config["OBJECTS"]

# set new Observer object from config file
add_site(location["SITE_NAME"], EarthLocation(lat=location["LATITUDE"], lon=location["LONGITUDE"]))
telescope = Telescope(Observer.at_site(location["SITE_NAME"]))

fixed_targets = {}
for key in objects:
	coordinates = SkyCoord(objects[key]["RA"], objects[key]["DEC"], frame=objects[key]["FRAME"])
	fixed_targets[key] = FixedTarget(name=key, coord=coordinates)

telescope.printTelescope()
#telescope.slewToObject(fixed_targets["ALTAIR"])
telescope.record()
telescope.slewToObject(fixed_targets["DENEB"])
