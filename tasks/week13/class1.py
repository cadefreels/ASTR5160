import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt

# CF Read in the file line.data

linedata = '/d/scratch/ASTR5160/week13/line.data'
line_data = Table.read(linedata, format = "ascii")
print(line_data)

# CF Determine the mean of the y values in each bin of x

linedata = np.loadtxt(linedata)
#print(linedata)
means = np.mean(linedata, 0)
print(means)

# CF Determine the variance of the y values in each bin of x

variances = np.var(linedata, 0, ddof = 1)
print(variances)

# CF Guess at some m and b values that could fit the data

# CF Plot the observed ("O") y values

xvals = np.linspace(0.5, 10, 10)

#saveplots = "/d/www/cade/public_html"

plt.scatter(xvals, means)
plt.savefig("/d/www/cade/public_html/mbguess.png")

#plt.savefig(saveplots + "guessvals.png")

# CF Get a straight line to get "E" values and plot models to data

def line(m, x, b):
    """Make a Straight Line to get expected "E" values for y"""
    """ m is the slope, x is an array of x points, b is the y-intercept"""
    y = m * x + b
    return y

# CF Guess some m and b values by looking at "mbguess.png" plot and return the associated expected y-values

xdata = np.linspace(0.5, 10, 100)

guess1 = line(2.90, xvals, 5.35)
guess2 = line(2.80, xvals, 5.25)
guess3 = line(2.70, xvals, 5.5)

print(guess1)
print(guess2)
print(guess3)

plt.scatter(xvals, means)
plt.plot(xvals, guess1, label = "Guess 1")
plt.plot(xvals, guess2, label = "Guess 2")
plt.plot(xvals, guess3, label = "Guess 3")
plt.legend()
plt.savefig("/d/www/cade/public_html/modelfits.png")

# CF Calculate X^2

def chi_squared(o, e, var):
    chisq = np.sum(((o - e) ** 2) / var)
    return chisq

# CF Get my grid of m and b that corresponds to my range of values from step 2

guess4 = line(2.90, xvals, 5.25)
guess5 = line(2.90, xvals, 5.5)
guess6 = line(2.80, xvals, 5.35)
guess7 = line(2.80, xvals, 5.5)
guess8 = line(2.70, xvals, 5.35)
guess9 = line(2.70, xvals, 5.25)

# CF Print X^2 values

chisq1 = chi_squared(means, guess1, variances)
chisq2 = chi_squared(means, guess2, variances)
chisq3 = chi_squared(means, guess3, variances)
chisq4 = chi_squared(means, guess4, variances)
chisq5 = chi_squared(means, guess5, variances)
chisq6 = chi_squared(means, guess6, variances)
chisq7 = chi_squared(means, guess7, variances)
chisq8 = chi_squared(means, guess8, variances)
chisq9 = chi_squared(means, guess9, variances)

print(chisq1)
print(chisq2)
print(chisq3)
print(chisq4)
print(chisq5)
print(chisq6)
print(chisq7)
print(chisq8)
print(chisq9)
