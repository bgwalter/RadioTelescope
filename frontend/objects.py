import astropy
from astroplan.coordinates import SkyCoord

class Object:

	def __init__(self, name=None, ra=None, dec=None, frame=None, kind=None):
		self.name = name
		self.ra = ra
		self.dec = dec
		self.frame = frame
		self.kind = kind
		self.SkyCoord(ra, dec, frame)
