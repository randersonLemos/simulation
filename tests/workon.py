# -*- coding: utf-8 -*-
MARK_SIMTIME = '$#@SIMTIME@#$'
MARK_IRFFILE = '$#@IRFFILE@#$'

PROD_NAMES = ['PRK014', 'PRK028', 'PRK045', 'PRK052', 'PRK060', 'PRK061'
        ,'PRK083', 'PRK084', 'PRK085', 'Wildcat']

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def gaussian_kernel(size, std):
    if size % 2 == 0: raise ValueError("Just odd numbers for variable 'size'...")
    xs = np.linspace(-(size-1)/2.0, (size-1)/2.0, size)
    kernel = np.exp(-0.5 * (xs / std)**2)
    return kernel / np.sum(kernel)

import pathlib
import calendar
import datetime
import collections
import numpy as np
import matplotlib.pyplot as plt
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from simulation.common.words import Words as wrd
from simulation.input.well_design import Well_Design
from simulation.builder.well.well_producer import Well_Producer


Well_Design.set_inputRoot('./input')

wd = Well_Design(name='PRK014')
pd = Well_Producer(wd)
print(pd)