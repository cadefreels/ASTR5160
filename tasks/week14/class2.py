import numpy as np
from astropy.table import Table

# CF Read in the file line.data                                                                                                                 
datafile = '/d/scratch/ASTR5160/week13/line.data'
data_file = Table.read(datafile, format = "ascii")
print(data_file)

# CF Determine the variance of the y data in each bin of x                                                                                      
datafiletxt = np.loadtxt(datafile)

datafile_var = np.var(datafiletxt, 0, ddof = 1)
print(datafile_var)

# CF Determine the mean of the y deata in each bin of x                                                                                        

datafile_mean = np.mean(datafiletxt, 0)
print(datafile_mean)

# CF Follow the emcee tutorial

# CF Make the log likelhihood function

def lnlikelifunc(y, x, var, m, b):
   '''Log of the likelihood function (the probability of the data for a given model)                                            
                                                                                                                                
   y: can be a float or an array                                                                                                
   x: can be a float or an array                                                                                                
   var: variance of the y values in each bin of x                                                                               
   m: slope of straight line                                                                                                    
   b: y-intercept of straight line '''

   lnL = - 1 / 2 * np.sum((((y - (m * x + b)) ** 2) / var ** 2) + np.log(2 * np.pi * var ** 2))

   return lnL

# CF Make the log prior

def ln_prior(y, x, var, m, b):
    '''Prior function'''
    if b > 8 or b < 0
       return 0.0
    return -np.inf

def log_probability(y, x, var, m, b):
    lp


