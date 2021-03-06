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

# CF Create the 4 caps

# CF Create the RA Bounds

def sph_cap_ra(ra):
    """Enter ra in hours"""
    c = SkyCoord(ra*15*u.deg + 90*u.deg, 0*u.deg, frame='icrs')
    c.representation_type='cartesian'
    sphcapra=np.array([c.x, c.y, c.z, 1])
    return sphcapra
print(sph_cap_ra(5))
print(sph_cap_ra(6))

# CF Create the Dec Bounds

def sph_dec(dec):
    """Enter the dec in degrees"""
    cdec = SkyCoord(0*u.deg, 90*u.deg, frame = 'icrs')
    cdec.representation_type = 'cartesian'
    dec_cap = np.array([cdec.x, cdec.y, cdec.z, 1 - np.sin(np.deg2rad(dec))])
    return dec_cap
print(sph_dec(30))
print(sph_dec(40))

def ster_area(ra1, ra2, dec1, dec2):
    """Enter ra's in hours, enter dec's in degrees"""
    area = (np.radians(ra2*15*u.deg) - np.radians(ra1*15*u.deg))*(np.sin(np.radians(dec2)) - np.sin(np.radians(dec1)))
    return area                                                                  
print(ster_area(5, 6, 30, 40))

# CF Added this ster_area(5, 6, 30, 40) to the value for str in the header for the Mangle file (latlongrect.ply), as well as changed the weight to 0.9

# CF Create new bounds and calculate str area
print(sph_cap_ra(10))
print(sph_cap_ra(12))

print(sph_dec(60))
print(sph_dec(70))

print(ster_area(10, 12, 60, 70))

# CF Add this second polygon, as well as this ster_area, to my Mangle file (latlongrect.ply)
