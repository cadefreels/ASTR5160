import argparse
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table
import os
from glob import glob
import numpy as np

# CF Comment about running this file from the command line using argparse

parser = argparse.ArgumentParser(description = 'Determine FIRST and Legacy Survey objects the astronomer wants in their survey')

# CF If I wanted to run existing functions I have somewhere else
# if __name__ == "__main__"

# CF Retrieve the FIRST sources

objs = Table.read("/d/scratch/ASTR5160/data/first/first_08jul16.fits")

# CF Set RA and DEC to coordinates chosen by astronomer

choose_ra = 163.0*u.deg
choose_dec  = 50.0*u.deg
                                                                                                                                      
# CF Find which FIRST Sources lie in astronomer's survey 

cgiven = SkyCoord([choose_ra], [choose_dec])
csfirst = SkyCoord(objs["RA"], objs["DEC"], unit = 'deg')

igiven, ifirst, d1, d2 = cgiven.search_around_sky(csfirst, 3.0*u.deg)                                                                                                                                                                 
print(objs[igiven])

# CF Cross Match with Legacy Surveys Sweeps Files (North)

# CF Read in the Legacy Surveys North File

lsnorth = Table.read("/d/scratch/ASTR5160/data/legacysurvey/dr9/north/sweep/9.0")

# CF Got help from classmates about finding out which sweeps files I will need for this astronomers survey

# CF Need to have the is_in_box and decode_sweep_name functions
def my_sweeps(RA, DEC, lsnorth):
    fitstab = np.array(glob(os.path.join(sweepdir, "*fits")))
    ii = np.array([np.any(is_in_box_coords(RA, DEC, decode_sweep_name(fn))) for fn in fitstab])
    return (fitstab[ii])

# CF Find sources using coordinates I am interested in
firstsweep = my_sweeps(160, 53, lsnorth)
secondsweep = my_sweeps(160, 47, lsnorth)


# CF Get help from classmates about finding my sources that fit the specified parameters in the sweeps files

my_obs_list = []
for lsnorth in firstsweep[0], secondsweep[0]
    sweepstable = Table.read(lsnorth)
    ii = sweepstable["TYPE"] == "PSF"
    ii &= (22.5 - 2.5 * np.log10(sweepstable['FLUX_R']) < 22)
    ii &= (((22.5 - 2.5 * np.log10(sweepstable['FLUX_W1'])) - (22.5 - 2.5 * np.log10(sweepstable['FLUX_W2']))) > 0.5)
    my_obs_list.append(sweepstable[ii])
    sweeps_table = np.vstack(my_obs_list)
