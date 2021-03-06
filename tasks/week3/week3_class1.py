#Task 1
import numpy as np
from astropy.coordinates import SkyCoord
#Input RA and DEC
c=SkyCoord('02h03m50s', '+41d25m14s', frame='icrs')
#Change RA and DEC to cartesian coordinates
c.representation_type = 'cartesian'
print(c)
#Convert RA and DEC to decimal degrees
radec=(15*2)+3/60+50/3600
decdec=41+25/60+14/3600
#Convert decimal degrees to radians for use in numpy trig functions for checking with equations in lecture notes
x=np.cos(np.deg2rad(radec))*np.cos(np.deg2rad(decdec))
y=np.sin(np.deg2rad(radec))*np.cos(np.deg2rad(decdec))
z=np.sin(np.deg2rad(decdec))
print(x)
print(y)
print(z)

#Task 2
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord, get_constellation
#Enter in galactic coordinates for the galactic center
gc=SkyCoord(l=0*u.degree,b=0*u.degree,frame='galactic')
#Convert the galactic coordinates into RA and DEC in decimal degrees
radecgc=gc.icrs
print(radecgc)
#Determine which constellation the RA and DEC of the galactic center correspond to
const=get_constellation(radecgc)
print(const)
#From the "RA/Dec of the constellations" link on the "Useful links" page, Sagittarius is located at an RA of +19 05.94, Dec -28 28.61.
#The calculated RA of the galactic center corresponds to an RA of +17 45.6m, so the galactic center is located roughly near the edge of Sagittarius.


#Task 3
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
plt.figure()
dec=40
for ra in np.linspace(0,360,365):
    c_icrs=SkyCoord(ra*u.degree,dec*u.degree,frame='icrs')
    c_gal=c_icrs.transform_to("galactic")
    l=c_gal.l
    b=c_gal.b
    plt.scatter(l,b,c="red")
    plt.title("How (l,b) change through the year directly above your head from Laramie")
    plt.xlabel("l")
    plt.ylabel("b")
plt.savefig("/d/www/cade/public_html/Gal_lb_year1.png")
