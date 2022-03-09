import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from numpy.random import random
# ADM additional needed modules for my updates.
import argparse
import os
from astropy.table import Table

# CF Question 1
# CF Create function to determine the area of a general field in square degrees
def area_sqdeg(ramin, ramax, decmin, decmax):
    """Enter right ascension maximum and minimum values, in degrees, as
    well as declination maximum and minimum values, also in degrees, and
    compute the area in square degrees"""
    area = (180 / np.pi) * ((ramax * u.deg) - (ramin * u.deg)) * (
        np.sin(np.radians(decmax)) - np.sin(np.radians(decmin)))

    # ADM the area needs to be in SQUARE degrees.
    return area * u.deg

# ADM these aren't needed at all.
#def ra_rad(ra):
#    """Enter RA in degrees, return RA in radians"""
#    rarad = np.radians(ra)
#    return rarad
#
#def dec_rad(dec):
#    "Enter Dec in degrees, return Dec in radians"""
#    decrad = np.radians(dec)
#    return decrad

def pop_spharea(ramin, ramax, decmin, decmax, n=1000000):
    """Function pop_spharea takes in RA min and max, in degrees, as well 
    as Declination min and max, in degrees, populates the sphere randomly
    over its area then returns the right ascensions and declinations that
    lie within my lat-long rectangular area

    ADM:
    docstrings should include info on inputs and outputs in a specific
    format. For example:

    Parameters
    ----------
    ra_min : float, lower ra bound in degrees
    ra_max : float, upper ra bound in degrees
    dec_min : numpy.float64, lower dec bound in degrees
    dec_max : numpy.float64, upper dec bound in degrees
    n : integer, number of points to generate, defaults to 1000000

    Returns
    -------
    array, RA values that are in the rectangle
    array, Dec values that are in the rectangle
    """
    # CF Compute area of lat-lon rectangle    
#    area = (180 / np.pi) * ((ramax * u.deg) - (ramin * u.deg)) * (np.sin(np.radians(decmax)) - np.sin(np.radians(decmin)))
    # ADM why do this twice? You already have a function that does exactly this!
    area = area_sqdeg(ramin, ramax, decmin, decmax)

    # CF Randomly populate area of sphere
    # ADM no need to write 10000 twice, just define n once.
    ra = 360.*(random(n))
    dec = (180/np.pi)*np.arcsin(1.-random(n)*2.)
    # CF Return set of RA and DEC coordinates that lie within the lat-lon rectangular field    
#    infield =[]
#    for i in range(len(ra)):
#        if ((ra[i] < ramax) and (ra[i] > ramin) and (dec[i] > decmin) and (dec[i] < decmax)):
#            infield.append([ra[i], dec[i]])
    # ADM better to use Boolean indexing.
    infield = (ra < ramax) & (ra > ramin) & (dec > decmin) & (dec < decmax)

# ADM unnecessary print statement.
#    print(infield)

    # ADM can now return just the RA/Dec in the field.
    return(ra[infield], dec[infield])

# ADM set up the main space and transfer everything that isn't a function
# ADM to that main space.
if __name__ == "__main__":
    # ADM use the argument parser so inputs can be passed at the command line.
    parser = argparse.ArgumentParser(description='Enter Plot directory')
    parser.add_argument('plot_dir', metavar='plot_dir')
    args = parser.parse_args()
    # ADM now we have a plot_dir directory to use for all plots.
    plot_dir = args.plot_dir

    # ADM no need to print this. You already do it elsewhere in the code.
#    print("The area of a hemisphere: {}".format(area_sqdeg(0, 360, 0 , 90)))

    # CF Returns 20,626 square degrees, the correct amount in one hemisphere!
    # CF Plot 4 lat-lon rectangles in Aitoff projection
    # CF First get the areas of the 4 lat-lon rectangles
#    area1 = area_sqdeg(30, 90, 5, 20)
#    area2 = area_sqdeg(30, 90, 20, 35)
#    area3 = area_sqdeg(30, 90, 35, 50)
#    area4 = area_sqdeg(30, 90, 50, 65)
    # ADM you use the variables, 30, 90, etc. again, below. Why repeatedly
    # ADM write them when you can just have a single array to track them?
    # ADM There are lots of array-based ways to do this, but perhaps an 
    # ADM astropy Table will be most illustrative when we start plotting.
    radec = Table([[30, 30, 30, 30],
                   [90, 90, 90, 90],
                   [5, 20, 35, 50],
                   [20, 35, 50, 65]],
                  names=('ramin', 'ramax', 'decmin', 'decmax'))

    # ADM then, with array-based arithmetic, you can calculate all 
    # ADM the areas at once!
    area = area_sqdeg(radec['ramin'], radec['ramax'],
                      radec['decmin'], radec['decmax'])

    # CF Determine RA and Dec in radians in order to plot in Aitoff projection
    # ADM This is a little convoluted, but you can also convert everything 
    # ADM to radians at once, even in Table format. Better, maybe, would be
    # ADM to have set up quantities in radians at the beginning and had a
    # ADM function to calculate areas using inputs in radians.
    radec = Table(np.radians(radec.as_array().tolist()), names=radec.columns)

    # CF Make the first lat-lon rectangle plot in Aitoff projection
    fig1 = plt.figure()
    ax = fig1.add_subplot(111, projection = "aitoff")
    # ADM Draw the BASE of the zeroth rectangle. Note that the dec
    # ADM terms are the same (radec[0]["decmin"]), because we want a
    # ADM line along decmin that epresents the base of the rectangle.
    ax.plot([radec[0]["ramin"], radec[0]["ramax"]], [radec[0]["decmin"], radec[0]["decmin"]])
    # ADM Draw the TOP of the zeroth rectangle
    ax.plot([radec[0]["ramin"], radec[0]["ramax"]], [radec[0]["decmax"], radec[0]["decmax"]])
    # ADM Draw the LEFT-HAND side.
    ax.plot([radec[0]["ramin"], radec[0]["ramin"]], [radec[0]["decmin"], radec[0]["decmax"]])
    # ADM Draw the RIGHT-HAND side.
    ax.plot([radec[0]["ramax"], radec[0]["ramax"]], [radec[0]["decmin"], radec[0]["decmax"]])
# ADM these aren't needed.
#    ax.axvline(x = ra_rad(30))
#    ax.axvline(x = ra_rad(90))
    # ADM nice use of string formatting, by the way!
    plt.annotate("{0:.2f}".format(area[0]), 
                 xy = (radec[0]["ramax"], radec[0]["decmax"]))
    # ADM xy, here, creates a label somewhere near the top-corner.
    plt.title("Aitoff {}".format(0))
    plt.grid(True)
    # ADM don't forget that we have a name for the plot_dir, now!
    plt.savefig(os.path.join(plot_dir, "HW2aitoff{}.png".format(0)))

    # ADM I hope it should be obvious from my (hopefully illustrative) use
    # ADM of a Table with named columns, that everything, above, shares the
    # ADM index 0. So, you could have just looped through all the plots
    # ADM instead of wasting time writing 4 nearly-identical blocks of code:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "aitoff")
    for i, row in enumerate(radec):
        ax.plot([row["ramin"], row["ramax"]], [row["decmin"], row["decmin"]])
        ax.plot([row["ramin"], row["ramax"]], [row["decmax"], row["decmax"]])
        ax.plot([row["ramin"], row["ramin"]], [row["decmin"], row["decmax"]])
        ax.plot([row["ramax"], row["ramax"]], [row["decmin"], row["decmax"]])
        # Add a label near the top-right corner of each rectangle.
        plt.annotate("{0:.2f}".format(area[i]), xy = (row["ramax"], row["decmax"]))
    plt.title("Rectangles in Aitoff projection")
    plt.grid(True)
    plt.savefig(os.path.join(plot_dir, "HW2aitoff.png"))

#    fig2 = plt.figure()
#    ax = fig2.add_subplot(111, projection = "aitoff")
#    ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(20), dec_rad(35)])
#    ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(35), dec_rad(50)])
#    ax.axvline(x = ra_rad(30))
#    ax.axvline(x = ra_rad(90))
#    plt.annotate("{0:.2f}".format(area2), xy = (ra_rad(40), dec_rad(32.5)))
#    plt.title("Aitoff 2")
#    plt.grid(True)
#    plt.savefig("/d/www/admyers/public_html/HW2aitoff1.png")

    # CF Make the third lat-lon rectangle plot in Aitoff projection
#    fig3 = plt.figure()
#    ax = fig3.add_subplot(111, projection = "aitoff")
#    ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(35), dec_rad(50)])
#    ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(50), dec_rad(65)])
#    ax.axvline(x = ra_rad(30))
#    ax.axvline(x = ra_rad(90))
#    plt.annotate("{0:.2f}".format(area3), xy = (ra_rad(40), dec_rad(47.5)))
#    plt.title("Aitoff 3")
#    plt.grid(True)
#    plt.savefig("/d/www/admyers/public_html/HW2aitoff2.png")

    # CF Make the fourth lat-lon rectangle plot in Aitoff projection
#    fig4 = plt.figure()
#    ax = fig4.add_subplot(111, projection = "aitoff")
#    ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(50), dec_rad(65)])
#    ax.plot([ra_rad(30), ra_rad(90)], [dec_rad(65), dec_rad(80)])
#    ax.axvline(x = ra_rad(30))
#    ax.axvline(x = ra_rad(90))
#    plt.annotate("{0:.2f}".format(area4), xy = (ra_rad(40), dec_rad(62.5)))
#    plt.title("Aitoff 4")
#    plt.grid(True)
#    plt.savefig("/d/www/admyers/public_html/HW2aitoff4.png")

# ADM this comment line is far too long.
# CF Return set of RA and DEC values for the same values of RA min and max, and DEC min and max, as in my function for Question 1
# ADM this line of code isn't needed.
#pop_spharea(0, 360, 0, 90)

    # ADM now, finally, you needed to compare your recovered density to 
    # ADM the expectation for a known area like the full sphere. For example:

    # ADM let's use 10 million points.
    n = 10000000
    hemisphere = area_sqdeg(0, 360, 0, 90)
    ra_in, dec_in = pop_spharea(0, 360, 0, 90, n)
    nhemi = len(ra_in)
    print("Area of hemisphere: {:.2f}".format(hemisphere))
    print("Density of points over hemisphere: {:.2f}".format(nhemi/hemisphere))
    full_sphere = u.deg*u.deg*4*180*180/np.pi
    print("Known area of full sphere: {:.2f}".format(full_sphere))
    print("Density of points over full sphere: {:.2f}".format(n/full_sphere))

    # ADM, or better yet, use the fraction of points to estimate the area
    # ADM (a "Monte Carlo" integration).
    print("True area: {:.2f}".format(hemisphere))
    print("Estimated (Monte Carlo) area: {:.2f}".format(full_sphere*nhemi/n))
    
    
