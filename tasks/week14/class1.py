import numpy as np
from astropy.table import Table
import random

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

# CF Write function to calculate (ln) posterior probability for a linear fit to the data

def lnlikelifunc(y, x, var, m, b):
   '''Log of the likelihood function (the probability of the data for a given model)

   y: can be a float or an array
   x: can be a float or an array
   var: variance of the y values in each bin of x
   m: slope of straight line
   b: y-intercept of straight line '''
   
   lnL = - 1 / 2 * np.sum((((y - (m * x + b)) ** 2) / var ** 2) + np.log(2 * np.pi * var ** 2))
   
   if b > 8 or b < 0:
      lnL = -np.inf

   return lnL

# CF Get x values to input in my likelihood function

xnums = np.linspace(0.5, 10, 10)

# CF Test a "flat" prior and a prior that will exceed my range for b

flatprior1 = lnlikelifunc(datafile_mean, xnums, datafile_var, 3, 5)
priorbeyondrange = lnlikelifunc(datafile_mean, xnums, datafile_var, 3, 14)

# CF Print out "flat" and "beyond range" ln likelihood function values

print(flatprior1)
print(priorbeyondrange)

# CF Print out the probabilities associated with my "flat" and "beyond range" ln likelihood function values
prob1 = np.exp(flatprior1)
probbeyond = np.exp(priorbeyondrange)

print(prob1)
print(probbeyond)

# CF Follow the Metropolis-Hastings algorithm

# CF Select initial parameter values

m_guess1 =np.array([3.0])
b_guess1 = np.array([5.0])

# CF Use a Gaussian proposal function with a step size of 0.1

proposalm1 = m_guess1 + np.random.normal(loc = 0, scale = 0.1)
proposalb1 = b_guess1 + np.random.normal(loc = 0, scale = 0.1)

# CF Determine R

def lnR(y, x, var, m, b):
   '''Function to determine lnR, which is lnPnew - lnPold, in log space'''
   lnR = lnlikelifunc(datafile_mean, xnums, datafile_var, m_guess1, b_guess1) - lnlikelifunc(datafile_mean, xnums, datafile_var, proposalm1, proposalb1)
   R = np.exp(lnR)
   return R
#   if R > 1,
      #always accept the new parameters, the 0.1 deviations
   
#   if R < 1
      #accept new parameters if random.randint(0, 1) < R


