import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt

#CF Generate random set of 10000 points in radians
ra=2*np.pi*(random(10000)-0.5)
dec=np.arcsin(1.-random(10000)*2.)

#CF Plot points on standeard (x,y) grid
#CF Change dot size to 2 (s=2)
plt.scatter(ra,dec,s=2)
plt.title("Standard (x,y) grid")
plt.savefig("/d/www/cade/public_html/radecsphereplot.png")

print("In the projection on the standard (x,y) grid, there appears to be more points near the equator than near the poles.")

#CF Plot Aitoff projection
fig=plt.figure()
ax=fig.add_subplot(111,projection="aitoff")
ax.scatter(ra,dec,s=2)
#CF Change x-labels to hours instead of degrees
xlab=['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h']
ax.set_xticklabels(xlab,weight=800)
#Add a thick, blue, dashed axis grid grid using "grid"
ax.grid(color='blue',linestyle='--',linewidth='3')
plt.title("Aitoff")
plt.savefig("/d/www/cade/public_html/radecaitoff.png")

#CF Plot Lambert projection
#CF Define fig1 so Aitoff projection does not plot on same page as Lambert projection
fig1=plt.figure()
ax1=fig1.add_subplot(111,projection="lambert")
ax1.scatter(ra,dec,s=2)
#CF Change x-labels to hours instead of degrees                                
xlab=['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h']
ax1.set_xticklabels(xlab,weight=800)
#Add a thick, blue, dashed axis grid grid using "grid"                          
ax1.grid(color='blue',linestyle='--',linewidth='3')
plt.title("Lambert")
plt.savefig("/d/www/cade/public_html/radeclambert.png")
