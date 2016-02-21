from astropy.wcs import WCS
from array import array

def init():
	wcs = WCS(naxis=2)
	wcs.wcs.crpix = [0., 0.]
	wcs.wcs.cdelt = [1./3600.,1./3600.]
	wcs.wcs.crval = [23.2334, 45.2333]
	wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
	return wcs

#xp, yp = wcs.wcs_world2pix(23.32, 45.222, 0)
ras = array('f', [23.32,  32.23])
decs = array('f', [45.222, 22.254])
xp, yp = wcs.wcs_world2pix(ras, decs, 0)

print(xp)
print(yp)
