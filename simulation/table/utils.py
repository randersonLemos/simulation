import pathlib
import warnings
import pandas as pd
from itertools import zip_longest
from .tables import Tables
from .well_table import Well_Table
from .sector_table import Sector_Table
from .special_table import Special_Table

def is_well_table(lst):
    return 'WELL' in ''.join(lst)

def is_special_table(lst):
    return 'SPECIAL' in ''.join(lst)

def is_sector_table(lst):
    return 'SECTOR' in ''.join(lst)

def get_tables(path_to_rwo_file):
    tabs = Tables()
    tabs.path_to_rwo_file = path_to_rwo_file
    lst = []
    with pathlib.Path(path_to_rwo_file).open() as fh:
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