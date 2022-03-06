import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

# CF Question 1
# CF Create function to determine the area of a general field in square degrees
def area_sqdeg(ramin, ramax, decmin, decmax):
    """Enter right ascension maximum and minimum values, in degrees, as well as declination maximum and minimum values, also in degrees, and compute the area in square degrees"""
    area = (180 / np.pi) * ((ramax * u.deg) - (ramin * u.deg)) * (np.sin(np.radians(decmax)) - np.sin(np.radians(decmin)))
    return area
print(area_sqdeg(0, 360, 0 , 90))

# CF Returns 20,626 square degrees, the correct amount in one hemisphere!

# CF Plot 4 lat-lon rectangles in Aitoff projection

# CF First get the areas of the 4 lat-lon rectangles

area1 = area_sqdeg(30, 90, 5, 20)
area2 = area_sqdeg(30, 90, 20, 35)
area3 = area_sqdeg(30, 90, 35, 50)
area4 = area_sqdeg(30, 90, 50, 65)

# CF Determine RA and Dec in radians in order to plot in Aitoff projection

def ra_rad(ra):
    """Enter RA in degrees, return RA in radians"""
    rarad = np.radians(ra)
    return rarad

def dec_rad(dec):
    "Enter Dec in degrees, return Dec in radians"""
    decrad = np.radians(dec)
    return decrad

# CF Make the first lat-lon rectangle plot in Aintoff projection
fig1 = plt.figure()
ax = fig1.add_subplot(111, projection = "aitoff")
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(5), dec_rad(20)])
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(20), dec_rad(35)])
ax.axvline(x = ra_rad(30))
ax.axvline(x = ra_rad(90))
plt.annotate("{0:.2f}".format(area1), xy = (ra_rad(40), dec_rad(17.5)))
plt.title("Aitoff 1")
plt.grid(True)
plt.savefig("/d/www/cade/public_html/HW2aitoff1.png")

# CF Make the second lat-lon rectangle plot in Aintoff projection
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection = "aitoff")
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(20), dec_rad(35)])
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(35), dec_rad(50)])
ax.axvline(x = ra_rad(30))
ax.axvline(x = ra_rad(90))
plt.annotate("{0:.2f}".format(area2), xy = (ra_rad(40), dec_rad(32.5)))
plt.title("Aitoff 2")
plt.grid(True)
plt.savefig("/d/www/cade/public_html/HW2aitoff2.png")

# CF Make the third lat-lon rectangle plot in Aintoff projection
fig3 = plt.figure()
ax = fig3.add_subplot(111, projection = "aitoff")
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(35), dec_rad(50)])
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(50), dec_rad(65)])
ax.axvline(x = ra_rad(30))
ax.axvline(x = ra_rad(90))
plt.annotate("{0:.2f}".format(area3), xy = (ra_rad(40), dec_rad(47.5)))
plt.title("Aitoff 3")
plt.grid(True)
plt.savefig("/d/www/cade/public_html/HW2aitoff3.png")

# CF Make the fourth lat-lon rectangle plot in Aintoff projection
fig4 = plt.figure()
ax = fig4.add_subplot(111, projection = "aitoff")
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(50), dec_rad(65)])
ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(65), dec_rad(80)])
ax.axvline(x = ra_rad(30))
ax.axvline(x = ra_rad(90))
plt.annotate("{0:.2f}".format(area4), xy = (ra_rad(40), dec_rad(62.5)))
plt.title("Aitoff 4")
plt.grid(True)
plt.savefig("/d/www/cade/public_html/HW2aitoff4.png")

# CF Question 2

from numpy.random import random

def pop_spharea(ramin, ramax, decmin, decmax):
    """Function pop_spharea takes in RA min and max, in degrees, as well as Declination min and max, in degrees, populates the sphere randomly over its area"""
    """Then returns the right ascensions and declinations that lie within my lat-long rectangular area"""

# CF Compute area of lat-lon rectangle    
    area = (180 / np.pi) * ((ramax * u.deg) - (ramin * u.deg)) * (np.sin(np.radians(decmax)) - np.sin(np.radians(decmin)))
# CF Randomly populate area of sphere
    ra = 360.*(random(10000))
    dec = (180/np.pi)*np.arcsin(1.-random(10000)*2.)
# CF Return set of RA and DEC coordinates that lie within the lat-lon rectangular field    
    infield =[]
    for i in range(len(ra)):
        if ((ra[i] < ramax) and (ra[i] > ramin) and (dec[i] > decmin) and (dec[i] < decmax)):
            infield.append([ra[i], dec[i]])
    print(infield)
    return(infield)

# CF Return set of RA and DEC values for the same values of RA min and max, and DEC min and max, as in my function for Question 1

pop_spharea(0, 360, 0, 90)
print(area_sqdeg(0, 360, 0, 90))
print(len(pop_spharea(0, 360, 0, 90)) / area_sqdeg(0, 360, 0, 90))
