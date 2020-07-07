prod_lst = []
prod_lst.append('Wildcat'); prod_lst.append('PRK014'); prod_lst.append('PRK028')
prod_lst.append('PRK045');  prod_lst.append('PRK052'); prod_lst.append('PRK060')
prod_lst.append('PRK061');  prod_lst.append('PRK083'); prod_lst.append('PRK084')
prod_lst.append('PRK085')

prod_zone_lst = ['{}_{}'.format(el,z) for el in prod_lst[1:] for z in ('Z1', 'Z2', 'Z3', )]

inje_lst = []
inje_lst.append(('IRK004',('IRK004-G','IRK004-W', ), )); inje_lst.append(('IRK028',('IRK028-G','IRK028-W', ), ))
inje_lst.append(('IRK029',('IRK029-G','IRK029-W', ), )); inje_lst.append(('IRK036',('IRK036-G','IRK036-W', ), ))
inje_lst.append(('IRK049',('IRK049-G','IRK049-W', ), )); inje_lst.append(('IRK050',('IRK050-G','IRK050-W', ), ))
inje_lst.append(('IRK056',('IRK056-G','IRK056-W', ), )); inje_lst.append(('IRK063',('IRK063-G','IRK063-W', ), ))

import os
import pathlib
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.style.use('seaborn-talk')

mpl.rcParams['axes.titlesize'] = 18.0
mpl.rcParams['axes.labelsize'] = 18.0
mpl.rcParams['xtick.labelsize'] = 18.0
mpl.rcParams['ytick.labelsize'] = 18.0

if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.table.utils import get_tables

def Get_tables(FileDotTables):
    Tables = []
    with open(FileDotTables, 'r') as fh:
        for line in fh:
            tables = get_tables(line.strip())
            for well_name, alias in inje_lst: tables.add(tables.join(well_name, *alias, dell=True)) # join xxxxxx-w and xxxxxx-g to xxxxxx
            Tables.append(tables)
    return Tables
