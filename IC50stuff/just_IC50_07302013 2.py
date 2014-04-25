#!/usr/bin/env python
# shebang so you can run it from command line with just name of file
# Shane Neeley 07-30-2013

import matplotlib.pyplot as plt
import scipy.misc
import numpy as np
import scipy.optimize
import os
from os.path import join as join2
np.set_printoptions(threshold=np.nan) # remove the limit for size of array to print
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

user_concentrations = '10 5 2.5 1.25 .625 .0625 .00625 pbs' 

# Enter the data to be used
data = np.array([0.227,0.718,0.773,1.064,1.256,1.437,1.614,1.411])

# user_concentrations = names for plots. concs_nums is their numerical values
concs_nums = []
for i in user_concentrations.split():
    try:
        num = eval(i)
    except:
        num = 0
    concs_nums.append(num)

# Trying is awesome
# In [12]: try:
#    ....:     print cow
#    ....: except:    
#    ....:     print 'cow is not real'
#    ....: print 5*5      

####################################################
# Make all the necessary directories
save_dir = os.getcwd()
os.chdir(save_dir)

##############################################################
# EC50 Calculations 
##############################################################

ec50s_file = open('IC50s.txt', 'w')


rangeconc = np.arange(0, np.max(concs_nums), 0.1)

def x_for_known_y_sig( sigmoid, p ):
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

def Plot_dose_response_sig(data, save_fig, save_data, namedata):
    '''This function normalizes a set of data points for plotting on a dose response curve.
       They are normalized so that the highest drug concentration's data = 0, lowest = 1.
       A sigmoidal is fit to the data, and we measure where 0.5 (50% effect) crosses on that line.'''

    normalized = (data - data[0]) / (data[-1] - data[0])
    normalized = np.absolute(normalized)
    np.savetxt( join2(save_dir, save_data), normalized, delimiter=',')
    
    p_guess = ( np.median( concs_nums ),np.median( normalized ),1.0,1.0 )
    p, cov, infodict, mesg, ier = scipy.optimize.leastsq(residuals, p_guess, args=(concs_nums, normalized), full_output=1)  

    x0,y0,c,k = p
    pxp = sigmoid(p, rangeconc)

    ss_err =(infodict['fvec']**2).sum()
    ss_tot =((normalized - normalized.mean())**2).sum()
    r_squared = 1- (ss_err / ss_tot)

    EC50 = x_for_known_y_sig( sigmoid, p )
    ec50s_file.write(('%s Endpoint\t EC50 = ' %namedata + '%.3f' %EC50 + '\tR-squared = ' + '%.3f' %r_squared + '\n'))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xscale('log')
    plt.scatter(concs_nums, normalized, s=75, color='#756E71')
    plt.ylabel('effect (0 to 1)')
    plt.xlabel('concentration')
    plt.plot(rangeconc, pxp, 'k', EC50, sigmoid(p, EC50), 'r<', ms=9)
    ax.tick_params(axis='x') 
    ax.xaxis.tick_bottom()
    ax.tick_params(axis='y')
    ax.yaxis.tick_left()
    plt.grid(True)
    plt.savefig( join2(save_dir, save_fig))
    plt.close()

def x_for_known_y_poly(f):
    '''Get the value of x, based on known y by choosing an average of the x's near that y'''
    fit = [ (x, f(x)) for x in rangeconc ]  # list of tuples containing x and f(x) values
    near50 = []
    for tup in fit:
        if tup[1] > 0.48 and tup[1] < 0.52:  # get x values near f(x) = 0.5
            x = tup[0]
            near50.append(x)
    EC50 = np.mean(np.array(near50))
    return EC50

def Plot_dose_response_poly(data, save_fig, save_data, ec50_poly, save_poly_coeffs, namedata):
    '''This function normalizes a set of data points for plotting on a dose response curve.
       They are normalized so that the highest drug concentration's data = 0, lowest = 1.
       A polynomial is fit to the data, and we measure where 0.5 (50% effect) crosses on that line.'''
    normalized = (data - data[0]) / (data[-1] - data[0])
    normalized = np.absolute(normalized)
    np.savetxt( join2(save_dir, save_data), normalized, delimiter=',')
    # fit a 3 degree polynomial. nm is the ranks and other crap
    poly_coeffs, residual, nm1, nm2, nm3 = np.polyfit(concs_nums, normalized, ec50_poly, full=True)
    r_squared = 1 - residual / (len(normalized) * normalized.var())
    # make a function out of it
    f = np.poly1d(poly_coeffs)
    np.savetxt( join2(save_dir, save_poly_coeffs), f)
    EC50 = x_for_known_y_poly(f)
    ec50s_file.write(('%s Endpoint\t EC50 = ' %namedata + '%.3f' %EC50 + '\tR-squared = ' + '%.3f' %r_squared + '\n'))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xscale('log')
    plt.scatter(concs_nums, normalized, s=75, color='#756E71')
    plt.ylabel('effect (0 to 1)')
    plt.xlabel('concentration')
    plt.plot(rangeconc, f(rangeconc),'k', EC50, f(EC50),'r<', ms=8)
    plt.grid(True)
    ax.tick_params(axis='x') 
    ax.xaxis.tick_bottom()
    ax.tick_params(axis='y')
    ax.yaxis.tick_left()
    plt.savefig( join2(save_dir, save_fig))
    plt.close() 

def Run_ec50_plotting():
    Plot_dose_response_sig(data, 'dose_response_sig.png', 'normalized_for_EC50_sig.csv', 'Sigmoidal')
    Plot_dose_response_poly(data, 'dose_response_poly.png', 'normalized_for_EC50_poly.csv', 2, 'polynomial_coeffs.txt', 'Polynomal')


Run_ec50_plotting()

ec50s_file.close()









