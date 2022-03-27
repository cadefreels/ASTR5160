import numpy as np
import pymangle

# CF Functions to create spherical caps                                                                                                                                                   

# CF Create the RA Bounds of the spherical caps for the spectroscopic survey the astronomer conducts                                                                                                                                

def sph_cap_ra(ra):
    """Enter ra in hours"""
    c = SkyCoord(ra*15*u.deg + 90*u.deg, 0*u.deg, frame='icrs')
    c.representation_type='cartesian'
    sphcapra=np.array([c.x, c.y, c.z, 1])
    return sphcapra
print(sph_cap_ra(10.25))
print(sph_cap_ra(11.25))

# CF Create the Dec Bounds of the spherical caps for the  spectroscopic survey the astronomer conducts                                                                                                                                               

def sph_dec(dec):
    """Enter the dec in degrees"""
    cdec = SkyCoord(0*u.deg, 90*u.deg, frame = 'icrs')
    cdec.representation_type = 'cartesian'
    dec_cap = np.array([cdec.x, cdec.y, cdec.z, 1 - np.sin(np.deg2rad(dec))])
    return dec_cap
print(sph_dec(30))
print(sph_dec(40))

# CF Function to write mask polygons out to a .ply file in standard Mangle format

def mask_poly(namefile, numcaps, weight, pixel, strarea):
    """Function that accepts the name of the file, the numner of caps in the polygon, the weight of polygons, the number of pixels, and the area of the polygon in steradians"""
# CF Make the output a .ply file
    filename = open(namefile + '.ply', 'w')
    numcaps = len(numcaps)



# CF Get the mask file

mask = pymangle.Mangle("namefile")

# CF Create catalog of random points over some of the sphere  

ra_min = 10.25
ra_max = 11.25
dec_min = 30.0
dec_max = 40.0

ra_rand = mask.genrand_range(10000, ra_min, ra_max)
dec_rand = mask.genrand_range(10000, dec_min, dec_max)
