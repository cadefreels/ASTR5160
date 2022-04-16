import numpy as np
from astropy.table import Table

# CF Read in the file line.data                                                                                                                                                         
linedata = '/d/scratch/ASTR5160/week13/line.data'
linedata = np.loadtxt(linedata)
print(linedata)

# CF Calculate the covariance matrix

covmatrix = np.cov(linedata)
print(covmatrix)

# CF The covariance matrix should be a 10x10 matrix

# CF Use np.var to confirm that the diagonals of the covariance matrix contains the data variances

variance = np.var(linedata, ddof = 1)
print(variance)
