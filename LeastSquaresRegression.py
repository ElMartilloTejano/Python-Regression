#!/usr/bin/env python
# coding: utf-8

# In[99]:


import numpy as np
import matplotlib.pyplot as mpl
x = np.array([4.51,3.58,4.31,5.06,5.64,4.99,5.29,5.83,4.70,5.61,4.90,4.20])
y = np.array([2.48,2.26,2.47,2.77,2.99,3.05,3.18,3.46,3.03,3.26,2.67,2.57])

#calculate and print the regression coefficients
betaone = (sum(x * y) - ((sum(y) * sum(x))/len(x)))/(sum(x * x) - (pow(sum(x),2) / len(x)))
betazero = np.average(y) - betaone * np.average(x)
print("Slope: ", betaone, "\nIntercept: ", betazero)

#calculate corrected sums of squares and corrected slope
correctedSxx = sum(pow(x - np.average(x),2))
correctedSxy = sum((x - np.average(x)) * (y - np.average(y)))
correctedSyy = sum(pow(y - np.average(y),2))
correctedBetaone = correctedSxy/correctedSxx
print("Corrected Slope: ", correctedBetaone)

#calculate and print residuals
residuals = np.empty(x.size, float)
i = 0
while i < x.size:
    residuals[i] = y[i] - (betaone * x[i] + betazero)
    i+=1
print("Residuals: " ,residuals)

#create arrays for graphing out regression line
xreg = np.array([np.amin(x), np.amax(x)])
yreg = np.array([np.amin(x) * betaone + betazero, np.amax(x) * betaone + betazero])

mpl.plot(xreg,yreg)
mpl.plot(x,y, 'ro')
mpl.xlim(0, np.amax(x) + np.amax(x) * .1)
mpl.ylim(0, np.amax(y) + np.amax(y) * .1)


# In[ ]:




