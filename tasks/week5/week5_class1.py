import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
from numpy.random import random

#CF Generate set of 1000000 random points on the surface of the sphere
ra=360.*(random(1000000))
dec=(180/np.pi)*np.arcsin(1.-random(1000000)*2.)
#CF Determine which pixels each of ra, dec points within at the nside=1 level
nside=1
hpix=(hp.ang2pix(nside,ra,dec,lonlat=True))
print(hpix)
#CF Get area of an nside=1 HEALPixel
print(hp.nside2pixarea(nside,degrees=True))
#CF Print out the number of points in each HEALPixel
histo=np.histogram(hpix,bins=hp.nside2npix(nside))
print(histo[0])
print("There are approximately the same number of points in each HEALPixel, which is consistent with pixels being equal-area")

