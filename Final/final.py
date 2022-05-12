# CF Import modules I will need

import numpy as np
from astropy.table import Table
import random
import emcee
import matplotlib.pyplot as plt

# CF Import modules I have elsewhere if I had them

# if__name__ == "__main__"

# CF Read in the file dataxy.fits                                                                                                                                                        
data = '/d/scratch/ASTR5160/final/dataxy.fits'
data_file = Table.read(data)

# CF Print the data to see what it looks like

print(data_file)

# CF Graph data to see what it looks like

# CF Get x, y, and error bars on y data values in order to plot

xdata = data_file['x']
ydata = data_file['y']
yerr = data_file["yerr"]

# CF Plot x and y values and look at plot

plt.errorbar(xdata, ydata, yerr = yerr)

plt.savefig("/d/www/cade/public_html/dataxy.png")

# CF Bayesian Linear Fit to the data                                                                                     

def lnlikelifunc(m, b):
   '''Log of the likelihood function (the probability of the data for a given model)                                                                                                                                                                                                                                         
   m: slope of straight line                                                                                                                                                           
   b: y-intercept of straight line '''

   lnL = - 1 / 2 * np.sum((((ydata - (m * xdata + b)) ** 2) / yerr ** 2) + np.log(2 * np.pi * yerr ** 2))

   if b > 5 or b < -1:
      lnL = -np.inf

   return lnL


# CF Quadratic Fit to the data

def quadfit(a0, a1, a2):
   '''Quadratic Bayesian fit to the data (the probability of the data for a given model)                                                                                                 
   a0: y-intercept of quadratic fit

   a1: linear coefficient (a1 * x)

   a2: quadratic coefficient (a2 * x ** 2)
                                                                                                                                                                                       
   b: y-intercept of straight line '''

   quadfit = - 1 / 2 * np.sum((((ydata - (m * xdata + b)) ** 2) / yerr ** 2) + np.log(2 * np.pi * yerr ** 2))

   if b > 5 or b < -1:
      quadfit = -np.inf

   return quadfit

# CF Get fits to data

lnlikelifunc(2.5, 2.5)

quadfit(2.5, 1, 0.5)
