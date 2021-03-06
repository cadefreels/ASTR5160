import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
#CF Input Coordinates in SKyCoord
c1=SkyCoord(263.75*u.degree,-17.9*u.degree,frame='icrs')
c2=SkyCoord('20h24m59.9s','10d6m0s',frame='icrs')

#CF Put coordinates in Cartesian
c1.representation_type = 'cartesian'
c2.representation_type = 'cartesian'

print(c1)
print(c2)

#CF Put coordinates in an array
c1cart=np.array([c1.x,c1.y,c1.z])
c2cart=np.array([c2.x,c2.y,c2.z])

#CF Solve for the angle
dot=np.dot(c1cart,c2cart)
arccos=np.arccos(dot)
angle=np.rad2deg(arccos)
print(angle)

#CF Check with SkyCoord Separartion
SkyCoordSep=c1.separation(c2)*u.degree
print(SkyCoordSep)

#Populate area of the Sky
c3=SkyCoord('2h00m00s','-2d00m00s',frame='icrs')
c4=SkyCoord('3h00m00s','+2d00m00s',frame='icrs')

pts1=(np.random.random(100)+2)*u.hour
pts2=(np.random.random(100)*4-2)*u.degree

coords1=SkyCoord(pts1,pts2,frame='icrs')

pts3=(np.random.random(100)+2)*u.hour
pts4=(np.random.random(100)*4-2)*u.degree

coords2=SkyCoord(pts3,pts4,frame='icrs')

plt.scatter(coords1.ra.degree,coords1.dec.degree,c='blue',marker='o')
plt.scatter(coords2.ra.degree,coords2.dec.degree,c='red',marker='^')
plt.xlabel("RA(Degrees)")
plt.ylabel("Dec(Degrees)")
plt.savefig("/d/www/cade/public_html/randomradec.png")

#CF Use seaerch_around_sky
id1,id2,d2,d3 = coords2.search_around_sky(coords1,(10*u.degree)/60)

coords3=SkyCoord(pts1[id1],pts2[id1],frame='icrs')
coords4=SkyCoord(pts3[id2],pts4[id2],frame='icrs')

plt.scatter(coords1.ra.degree,coords1.dec.degree,c='blue',marker='o')
plt.scatter(coords2.ra.degree,coords2.dec.degree,c='red',marker='^')
plt.scatter(coords3.ra.degree,coords3.dec.degree,c='c',marker='>')
plt.scatter(coords4.ra.degree,coords4.dec.degree,c='k',marker='<')
plt.xlabel("RA(Degrees)")
plt.ylabel("Dec(Degrees)")
plt.savefig("/d/www/cade/public_html/randomradecin10.png")
