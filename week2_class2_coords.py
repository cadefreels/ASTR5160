#Convert DEC and RA to decimal and check
from astropy import units as u
from astropy.coordinates import SkyCoord
c=SkyCoord('00h52m17s', '+45d18m00s', frame='icrs') 
print(c.ra)
print(c.dec)
print(c)
 
checkra = 15*(0+(52/60)+17/3600)
checkdec = 1*(45+(18/60)+(0/3600))
print(checkra)
print(checkdec)

#Use Time.now() to obtain today's MJD and today's JD
from astropy.time import Time
import numpy as np
timenow=Time.now()
print(timenow.mjd)
print(timenow.jd)
 
checktime = timenow.jd-2400000.5
print(checktime)

#Use np.arange to get a few days around today's MJD
import numpy as np
from astropy.time import Time
tn=Time.now()
tn.mjd
aroundmjd = np.arange(tn.mjd, tn.mjd+5, 1)
print(aroundmjd)
