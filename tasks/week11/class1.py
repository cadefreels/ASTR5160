from astropy.table import Table
from astropy import units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

# CF Read in the sweep files

objs = Table.read("/d/scratch/ASTR5160/data/legacysurvey/dr9/south/sweep/9.0/sweep-180p020-190p025.fits")
#print(objs)

# CF RA and DEC coordinates for my location

my_ra = 188.53667*u.deg
my_dec = 21.04572*u.deg

# CF Match the given RA and DEC with the sweeps file                                                    
cgiven = SkyCoord([my_ra], [my_dec])
csweeps = SkyCoord(objs["RA"], objs["DEC"], unit = 'deg')

# CF Decrease radius that I am searching around to hone in on the object in the sweeps file that matches my given RA and DEC
igiven, isweeps, d1, d2 = csweeps.search_around_sky(cgiven, 0.05*u.arcsec)
#igiven, isweeps, d1, d2 = csweeps.search_around_sky(cgiven, 1.0*u.arcsec)
#igiven, isweeps, d1, d2 = csweeps.search_around_sky(cgiven, 10.0*u.arcsec) 

#print(csweeps[isweeps])
print(objs[isweeps])

plt.figure(figsize = (8, 8))
plt.axis([187, 189, 20.5, 21.5])
plt.plot(objs["RA"], objs["DEC"], "g,")
plt.plot(objs[isweeps]["RA"], objs[isweeps]["DEC"],"kx")
plt.savefig("/d/www/cade/public_html/w11c1.png")

# CF Get TYPE of object

print("TYPE of object is EXP, which from the sweeps files documentation means 'exponential'")
print("Light profile is extended like a galaxy")

# CF Check ALLMASK_G, _R, and _Z for this object

print(objs[isweeps]["ALLMASK_G"])
print(objs[isweeps]["ALLMASK_R"])
print(objs[isweeps]["ALLMASK_Z"])

print("All these values are 2, which from looking at the legacypipe bitmask definitions link, correspond to objects that are saturated. So all three bands [g, r, z] are saturated.")

print("Yes, it appears to be saturated from the Legacy Survey Sky Viewer. Difficult to tell if it is a galaxy, but by clicking on the 'Look up in SIMBAD' link, it states it is a possible blazar, so it possibly is a galaxy.")
