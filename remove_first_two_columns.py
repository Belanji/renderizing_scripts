#!/usr/bin/env python

import glob
import os
import numpy as np
import sys

import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

folder = sys.argv[1]

filelist = glob.glob(folder + '/optical_*.csv')
filelist = natural_sort(filelist)

for file in filelist:
    print(file)
    g = np.loadtxt(file, delimiter=',', usecols=(2,))
    np.savetxt(file, g,fmt='%.6f')
