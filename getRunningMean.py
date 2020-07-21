#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:11:59 2020

@author: catiefinkenbiner
"""

import numpy as np

## Calculate weighed running mean time series
def main(daylist,tsY,tsP,year_frac,w):
    tsYm = [] ; tsPm = [] ; tsXm = [] ; dl = []
    numList = np.arange(np.min(daylist),np.max(daylist)+w,w) # 'w' day agg. ts
    
    for i in np.arange(len(numList)-1):
        new_iso = [] ; new_p = []  ; fracyr = []     
        
        for z in np.arange(len(daylist)):
            
            if (daylist[z] >= numList[i]) & (daylist[z] < numList[i+1]):
                new_iso.append(tsY[z])
                new_p.append(tsP[z])
                fracyr.append(year_frac[z])
        
        new_iso = np.array(new_iso)
        new_p = np.array(new_p)
        
        if new_p.size > 0:
            if np.nanmean(new_p) > 0:
                tsPm.append(np.nanmean(new_p)) # calc n-day total
                ts = (np.nansum(new_iso*new_p)/np.nansum(new_p)) # P weighed total
                tsYm.append(ts)   
                tsXm.append(np.max(fracyr))
                dl.append(numList[i])
    
    return tsYm,tsPm,tsXm,dl

if __name__ == '__main__':
    main(daylist,tsY,tsP,year_frac,w)