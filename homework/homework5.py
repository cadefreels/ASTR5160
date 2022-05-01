import argparse
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table
import os

# CF Use ArgumentParser to provide a message about running this code at the command line

parser = argparse.ArgumentParser(description = 'Enter a Table into function in order to better determine which objects in the larger spectroscopic survey should be targeted as quasars')

# CF If I wanted to run existing functions I have somewhere else                                                                                                                          
# if __name__ == "__main__"

#CF Read in file that has definitive list of quasars

qsos = Table.read("/d/scratch/ASTR5160/week10/qsos-ra180-dec30-rad3.fits")

print(qsos)

# CF Look at sweeps files to help classify objects as quasars

classify_qsos1 = Table.read("/d/scratch/ASTR5160/data/legacysurvey/dr9/north/sweep/9.0/sweep-180p030-190p035.fits")

classify_qsos2 = Table.read("/d/scratch/ASTR5160/data/legacysurvey/dr9/north/sweep/9.0/sweep-170p025-180p030.fits")

# CF Could look at sweeps files I read in to get various parameters of the objects

#print(classify_qsos1)
#print(classify_qsos2)

# Look at r-flux, as we only want r-magnitudes < 19 in larger survey

rflux1 = classify_qsos1["FLUX_R"]
rflux2 = classify_qsos2["FLUX_R"]

# CF Return r fluxes from sweeps files

print(rlux1)
print(rflux2)

# CF Write a function that converts fluxes from sweeps files in nanomaggies into magnitudes

def flux_to_mag(flux):
    '''Returns the magnitude value from a flux value in a sweeps file'''
    '''input: float or array'''
    '''output: float or array'''
    mag = 22.5 - 2.5 * np.log10(flux)
    return mag

# CF Return r-magnitudes from sweeps file

rmag1 = flux_to_mag(rflux1)
rmag2 = flux_to_mag(rflux2)

print(rmag1)
print(rmag2)


# CF 

def splendid_function(table):
    '''Accepts an astropy table as input to determine which sources in the table are quasars'''
    
