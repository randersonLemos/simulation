# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:06:08 2019

@author: randerson
"""

import pathlib
import warnings
import pandas as pd
from .tables import Tables
from .well_table import Well_Table
from .sector_table import Sector_Table
from .special_table import Special_Table
from itertools import zip_longest

def is_well_table(lst):
    return 'WELL' in ''.join(lst)

def is_special_table(lst):
    return 'SPECIAL' in ''.join(lst)

def is_sector_table(lst):
    return 'SECTOR' in ''.join(lst)

def get_tables(path_to_rep_file):
    tabs = Tables()
    lst = []
    with pathlib.Path(path_to_rep_file).open() as fh:
        for raw_line in reversed(list(fh)):
            line = raw_line.strip('\n').strip()
            if 'TABLE' in line:
                lst = list(reversed(lst))
                if is_well_table(lst):
                    tabs.add(Well_Table(lst))
                elif is_sector_table(lst):
                    tabs.add(Sector_Table(lst))
                elif is_special_table(lst):
                    tabs.add(Special_Table(lst))
                else:
                    warnings.warn('{} pattern not mapped. Just ignoring it...'.format(line))
                lst = []
            else:
                lst.append(line)
    return tabs