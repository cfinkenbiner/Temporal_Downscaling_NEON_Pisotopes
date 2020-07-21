#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:29:01 2020

@author: catiefinkenbiner
"""
from datetime import datetime

### Read time and calculate fractional days
def change_Pdata(siteDF):
    timeStrs = siteDF['endDateTime']
    newTimes = [] ; fracyr = []
  
    for t in timeStrs:
        cTime = datetime.strptime(str(t),"%Y-%m-%d %H:%M:%S")
        newTimes.append(cTime)
        fracyr.append(float(cTime.strftime('%j'))/365.25) # day of year
    siteDF['DateTime'] = newTimes
    siteDF['FracYear'] = fracyr
    return siteDF

if __name__ == '__main__':
    change_Pdata(siteDF)
    
    
    
def change_ISOdata(siteDF):
    timeStrs = siteDF['collectDate']
    newTimes = [] ; fracyr = []
  
    for t in timeStrs:
        cTime = datetime.strptime(str(t),"%Y-%m-%d %H:%M:%S")
        newTimes.append(cTime)
        fracyr.append(float(cTime.strftime('%j'))/365.25) # day of year
    siteDF['DateTime'] = newTimes
    siteDF['FracYear'] = fracyr
    return siteDF

if __name__ == '__main__':
    change_ISOdata(siteDF)