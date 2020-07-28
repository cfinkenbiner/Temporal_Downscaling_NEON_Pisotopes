#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:42:44 2020

@author: catiefinkenbiner
"""
import numpy as np
import scipy as sp
from scipy import stats

## Step 4 Use prediction to create conditional copula generated values
def main(tsP,xday_stats,H_scale,O_scale):
    # Observed P statistics
    Pmu = np.mean(tsP)
    Psig = np.std(tsP)
    
    # Correlation Coefficients
    xday_rho1 = xday_stats[2,0] ; xday_rho2 = xday_stats[2,1] ; xday_rho3 = xday_stats[2,2] 
    
    # Calculate Sigma_bar
    sigma_bar = [[1 - xday_rho1*xday_rho1, xday_rho3 - xday_rho1*xday_rho2],
                 [xday_rho3 - xday_rho1*xday_rho2, 1 - xday_rho2*xday_rho2]]
    
    series = []
    for i in np.arange(len(tsP)):
        if tsP[i] > 0:
            a = (tsP[i] - Pmu) / Psig        
            H2mu_bar = xday_rho1 * a
            O18mu_bar = xday_rho2 * a
            mu_bar = np.array([H2mu_bar,O18mu_bar])

            X = sp.stats.multivariate_normal.rvs(mean= mu_bar,cov= sigma_bar) 
            X2 = sp.stats.norm.cdf(X[0],loc=0,scale=1) 
            X3 = sp.stats.norm.cdf(X[1],loc=0,scale=1)

            index = int(np.floor(X2 * len(H_scale)))
            newH = H_scale[index]

            index = int(np.floor(X3 * len(O_scale)))
            newO = O_scale[index]

            series.append([newH,newO]) 
        else:
            series.append([np.nan,np.nan])
    return series

if __name__ == '__main__':
    main(tsP,xday_stats,H_scale,O_scale)