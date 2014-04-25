import matplotlib.pyplot as plt
import scipy.misc
import numpy as np
import scipy.optimize
import os
from os.path import join as join2
np.set_printoptions(threshold=np.nan) # remove the limit for size of array to print
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

# Say you have protein expression data, you gathered from western blots.
# This drug increases protein expression.
# A very common measurement for drug effectiveness is the EC50, or half maximal effect.

user_concentrations = '10 5 2.5 1.25 .625 .0625 .00625 pbs' 

# Enter the data to be used
data = np.array([0.227,0.718,0.773,1.064,1.256,1.437,1.614,1.411])

def x_for_known_y( sigmoid, p ):
    '''Get the value of x, based on known y by choosing an average of the x's near that y'''
    fit = [ (x, sigmoid(p, x)) for x in rangeconc ]  # list of tuples containing x and f(x) values
    near50 = []
    for tup in fit:
        if tup[1] > 0.48 and tup[1] < 0.52:  # get x values near f(x) = 0.5
            x = tup[0]
            near50.append(x)
    EC50 = np.mean(np.array(near50))
    return EC50

def sigmoid(p,x):
    x0,y0,c,k=p
    y = c / (1 + np.exp(-k*(x-x0))) + y0
    return y

def residuals(p,x,y):
    return y - sigmoid(p,x)


p_guess = ( np.median( concentrations ), np.median( data ), 1.0, 1.0 )
p, cov, infodict, mesg, ier = scipy.optimize.leastsq(residuals, p_guess, args=(concentrations, data), full_output=1)  
# leastsq Minimize the sum of squares of a set of equations.
# Fitting data to a model

# Don't worry about it. One of the most important things I can teach you is to look at other people's work.
x0,y0,c,k = p  # parametersof the sigmoid
sigmoid_curve = sigmoid(p, rangeconc)

EC50 = x_for_known_y( sigmoid, p )

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xscale('log')

plt.scatter(concentrations, data, s=75, color='#756E71')

plt.ylabel('effect (0 to 1)')
plt.xlabel('concentration (%s)' %units)

plt.plot(rangeconc, sigmoid_curve, 'k', EC50, sigmoid(p, EC50), 'r<', ms=9)

ax.tick_params(axis='x') 
ax.xaxis.tick_bottom()
ax.tick_params(axis='y')
ax.yaxis.tick_left()

plt.grid(True)













