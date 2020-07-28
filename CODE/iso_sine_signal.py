#!/usr/bin/env python
# coding: utf-8

import scipy as sp
from scipy import stats
from scipy import optimize
import numpy as np

def sine_func(t, amplitude, phase, offset):
    return amplitude * np.sin(2*np.pi*t - phase) + offset  # assume phase is decimal year/year

if __name__ == '__main__':
    sine_func(t, amplitude, phase, offset)
    
def sine_params(name,agglevel,frac_yr,P,H,O):   
    param_bounds=([0,-np.pi,-np.inf],[np.inf,np.pi,np.inf])               
    
    # d2H - find parameters for sine function based on frac year 
    params1, params_covariance = optimize.curve_fit(sine_func, frac_yr, H, p0 = [np.std(H)*(2*np.sqrt(2)),np.pi/2,np.mean(H)], bounds = param_bounds)
    # d18O - find parameters for sine function based on frac year 
    params2, params_covariance = optimize.curve_fit(sine_func, frac_yr, O, p0 = [np.std(O)*(2*np.sqrt(2)),np.pi/2,np.mean(O)], bounds = param_bounds)
      
    return params1, params2

if __name__ == '__main__':
    sine_params(t, amplitude, phase, offset)

