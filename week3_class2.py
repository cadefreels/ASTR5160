#Preliminary Tasks
from astropy.coordinates import SkyCoord
import sfdmap
import numpy as np
dustdir = '/d/scratch/ASTR5160/data/dust/v0_1/maps'
m = sfdmap.SFDMap(dustdir, scaling=1)
ra, dec = '12h42m30s', '+41d12m00s'
c = SkyCoord(ra, dec)
ebv = m.ebv(c.ra.value,c.dec.value)
ugriz = np.array([4.239 ,3.303 , 2.285 , 1.698 , 1.263])
A = ebv*ugriz
print(ebv) 
print(A)

#Task 1
import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import sfdmap
dustdir = '/d/scratch/ASTR5160/data/dust/v0_1/maps'
m = sfdmap.SFDMap(dustdir, scaling=1)
ebv = m.ebv(c.ra.value,c.dec.value)
ugriz = np.array([4.239 ,3.303 , 2.285 , 1.698 , 1.263])

q1g=18.81
q1r=18.73
q1i=18.82

q2g=19.10
q2r=18.79
q2i=18.73

gr1=q1g-q1r
ri1=q1r-q1i

gr2=q2g-q2r
ri2=q2r-q2i

plt.scatter(gr1,ri1,c="red")
plt.scatter(gr2,ri2,c="blue")
plt.xlabel("g-r")
plt.ylabel("r-i")   

plt.savefig("/d/www/cade/public_html/quasarcolor.png")
#These quasars do not have similar colors. Even though they are at a similar redshift, the dust distribution for their given RAs and Decs can difffer such that they appear different on this plot.

cq1=SkyCoord(246.933,40.795,frame='icrs',unit='deg')
cq2=SkyCoord(236.562, 2.440,frame='icrs',unit='deg')

ebvq1 = m.ebv(cq1.ra.value,cq1.dec.value)
ebvq2 = m.ebv(cq2.ra.value,cq2.dec.value)

A1=ebvq1*ugriz
A2=ebvq2*ugriz

print(A1)
print(A2)

q1ext=np.array(A1)
q2ext=np.array(A2)
print(q1ext)
print(q2ext)

q1extg=q1g-q1ext[1]
q1extr=q1r-q1ext[2]
q1exti=q1i-q1ext[3]

q2extg=q2g-q2ext[1]
q2extr=q2r-q2ext[2]
q2exti=q2i-q2ext[3]

q1extgr=q1extg-q1extr
q1extri=q1extr-q1exti

q2extgr=q2extg-q2extr
q2extri=q2extr-q2exti

plt.scatter(q1extgr,q1extri,c="black")
plt.scatter(q2extgr,q2extri,c="cyan")
plt.xlabel("g-r")
plt.ylabel("r-i")

plt.savefig("/d/www/cade/public_html/quasarcolorextinction.png")
