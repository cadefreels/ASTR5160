import numpy as np
from astropy.table import Table
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
from astropy import units as u
from astropy.io import ascii
from datetime import datetime

# CF Import the table of 18th mag quasars
data=ascii.read('HW1quasarfile.txt', format='no_header')

# CF Make a list of RA and DEC for all quasars
ra = []
dec = []
for i in range(len(data)):
    x = (data[i][0][:9]) 
    y = (data[i][0][9:])    
    ra.append(x)
    dec.append(y)
    print(x, y)

# CF Put RA and DEC into SkyCoord
# CF Need in hms.ss, deg'" format, and each value of RA and DEC
coords = SkyCoord(x*u.degree, y*u.degree, frame = 'icrs')

# CF Set observing location to Kitt Peak National Observatory
kpno = EarthLocation.of_site('kpno')
print(kpno)

# CF Set Time to Mountain Standard Time
utcoffset = -7*u.hour

# CF Want to get a range of times of this year at 11:00 pm MST
# CF Want this to loop over each month, and every day in each month ??
time = Time('2022-1-01 23:00:00') - utcoffset

# CF Iterate over month and day attempt
#times = Time(datetime(2022,m,d).strftime('%B') for m in range(1, 13) & d in range(1,32)
#for month in times & day in times
#    print(month, day)

# CF Want to find airmass of quasars
quasaltaz = AltAz(location=kpno, obstime=time)
loc_obs = coords.transform.to(quasaltaz) 

# CF Want to find the minimum airmass above 0
loc_obs_airmass = loc.obs.secz
min_airmass = min(lob.obs.secz)
for x in xrange(len(min_airmass)):
    if x < len(min_airmass) and min_airmass[x] < 0:
        mi_airmasss.remove(min_airmass[x])
