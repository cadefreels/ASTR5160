import matplotlib.pyplot as plt
plt.plot(objs["DEC"], objs["RA"], "bx")
plt.savefig("/d/www/cade/public_html/DEC_vs_RA_Strucc_FITS.png")

objs["EXTINCTION"][:,0]

#plot overlap of object' DEC and RA that have extinction > 0.22 
objs.as_array()
import numpy as np
import matplotlib.pyplot as plt

objsarray = np.array(objs)
col1extobjs = np.array(objs["EXTINCTION"][:,0])
extmore = objsarray[col1extobjs > 0.22]
extmoredec = extmore["DEC"]
extmorera = extmore["RA"] 
plt.plot(objs["DEC"], objs["RA"], "bx")
plt.plot(extmoredec,extmorera,"bx")
plt.savefig("/d/www/cade/public_html/struc_fits_overplot.png")
