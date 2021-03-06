import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
#Task 1
#CF Test to see if getting correct coordinates
#c=SkyCoord('11h00m00s','+00d00m00s',frame='icrs')
#c.representation_type='cartesian'
#print(c)

#CF Define function to create a vector 4-array for the spherical cap bounded by 5h in RA
np.set_printoptions(precision=12,suppress=True)
def sph_cap_ra():
    c=SkyCoord('11h00m00s', '+00d00m00s', frame='icrs')
    c.representation_type='cartesian'
    sphcapra=np.array([c.x, c.y, c.z, 1])
    sphcapra_deci=np.around(sphcapra,decimals=11)
    print(sphcapra_deci)
sph_cap_ra()

#Task 2
import numpy as np
from  astropy.coordinates import SkyCoord
np.set_printoptions(precision=18,suppress=True)
def sph_cap_dec():
    c_deccap=SkyCoord('00h00m00s', '+90d00m00s', frame='icrs')
    c_deccap.representation_type='cartesian'
    sphcapdec=np.array([c_deccap.x, c_deccap.y, c_deccap.z, 1-np.sin(np.deg2rad(36))])
    sphcapdec_deci=np.around(sphcapdec, decimals=17)
    print(sphcapdec_deci)
sph_cap_dec()

#Task 3
import numpy as np
from astropy.coordinates import SkyCoord
np.set_printoptions(precision=12,suppress=True)
def sph_cap_circfield():
    c_circfield=SkyCoord('05h00m00s', '+36d00m00s', frame='icrs')
    c_circfield.representation_type='cartesian'
    sphcapradeccirc=np.array([c_circfield.x, c_circfield.y, c_circfield.z, 1-np.cos(np.deg2rad(1))])
    sphcapradeccirc_deci=np.around(sphcapradeccirc, decimals=11)
    print(sphcapradeccirc_deci)
sph_cap_circfield()
