import pymangle
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
import matplotlib.pyplot as plt
import os

# CF Make place to easily review plots, after going to d/www/cade/public_html and making a 'week6' directory in public_html
user = os.getenv("cade")
formatter = "/d/www/cade/public_html/week6"
webdir = formatter.format(user)

# CF Use a function similar to the function I made last week, but now one that accepts inputs, to create two caps

def circle_cap(ra, dec, theta):
    """ Creates a 4-array for a spherical cap given an right ascension, declination, and a radius of the sphere """
    skycoord = SkyCoord(ra*u.degree, dec*u.degree, frame = 'icrs')
    skycoord.representation_type = 'cartesian'
    skycoord_cap = np.array([skycoord.x, skycoord.y, skycoord.z, 1 - np.cos(np.deg2rad(theta))])
    skycoord_deci = np.around(skycoord_cap, decimals = 8)
    print(skycoord_deci)
cap1 = circle_cap(76, 36, 5)
cap2 = circle_cap(75, 35, 5)

# CF Read in each of my masks

minter = pymangle.Mangle("intersection.ply")
mboth = pymangle.Mangle("bothcaps.ply")

# CF Fill each mask with 10,000 random points

ra_inter, dec_inter = minter.genrand(10000)
ra_both, dec_both = mboth.genrand(10000)

# CF Plot
figure1 = plt.figure()
ax = figure1.add_subplot(111)
ax.scatter(ra_inter, dec_inter, s = 0.8, c = 'g')
ax.scatter(ra_both, dec_both, s = 0.8, c = 'c')
ax.set_xlabel('RA')
ax.set_ylabel('Dec')
#plt.title("10,000 Random Points on Both Masks")
figure1.savefig(os.path.join(webdir, "masksplot.png"))
#plt.show()

# CF Flip sign on intersection.ply and read it in as a mask
mflip1 = pymangle.Mangle("intersection_flip.ply")

ra_mflip, dec_mflip = mflip1.genrand(10000)

# CF Plot intersection.ply and intersection_flip.ply
figure2 = plt.figure()
ax2 = figure2.add_subplot(111)
ax2.scatter(ra_inter, dec_inter, s = 0.8, c = 'g')
ax2.scatter(ra_mflip, dec_mflip, s = 0.8, c = 'k')
ax2.set_xlabel('RA')
ax2.set_ylabel('Dec')
#plt.title("10,000 Random Points on intersection.ply and intersection_flip.ply")
figure2.savefig(os.path.join(webdir, "inter_intflip.png"))
#plt.show()

