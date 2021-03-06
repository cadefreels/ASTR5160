import numpy as np
#HW 0 Q1
#help(np.random.uniform)

#CF Generate 10 floating point numbers randomly in the range 0-10 along the x-axis
x=np.random.uniform(0,10,10)

#CF Define a function for a straight line
def y(x,m,b):
    return m*x+b 

#CF Draw from a Gaussian of standard deviation 0.5 centered on y values    
err=np.random.normal(loc=y(x,3,9),scale=0.5)
print(x)
print(y(x,3,9))
#CF This error is very large, not sure why?
print(err)
#CF Print difference between the y-values with error and initially generated y-values
print(y(x,3,9)-err)


#Q2
#CF Import curve_fit
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#help(curve_fit)

#CF Define function I want to use as my curve_fit
def fit(x,m2,b2):
    return m2*x+b2

#CF Generate x-values and y-values to use in curve_fit 
xdata=np.linspace(0,10,50)
ydata=y(xdata,3,9)
#CF Plot line from which data was drawn
plt.plot(xdata,ydata,'b',marker="^",label='data')
plt.plot(x,y(x,3,9),'m',marker="o",label='line')

#CF Fit curve to the data
popt,pcov=curve_fit(fit,x,y(x,3,9))

#CF Recover best fitting values for m2 and b2
mfit=popt[0]
bfit=popt[1]
print(popt)
print(mfit)
print(bfit)
#CF Plot best-fit curve 
plt.plot(xdata,y(xdata,*popt),'r',marker="s",label='fit')
#CF Not sure where error bars are to plot?

plt.title("Data Fitting")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.savefig("/d/www/cade/public_html/astr5160hw0plot.png")
