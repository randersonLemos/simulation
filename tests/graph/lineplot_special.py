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

import copy
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.table.utils import get_tables

Tables = []
Tables.append(get_tables('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_SSS2_1/otm_IT020/run1996.rwo'))

for tables in Tables:
    tables.date_range(ini='2020')
    for well_name, alias in inje_lst: tables.add(tables.join(well_name, *alias, dell=True)) # join xxxxxx-w and xxxxxx-g to xxxxxx

from simulation.table.special_graph import Special_Graph

sg = Special_Graph(Tables)
wells = copy.copy(prod_lst[1:])
wells.reverse()
for i in range(0, len(prod_zone_lst), 3):
    well = wells.pop()
    root = pathlib.Path('./fig/{}'.format(well))
    root.mkdir(parents=True, exist_ok=True)

    sg.oil_prod(prod_zone_lst[i:i+3]); plt.savefig(root / 'ZONEOILPROD.png')
    sg.gas_prod(prod_zone_lst[i:i+3]); plt.savefig(root / 'ZONEGASPROD.png')
    sg.wat_prod(prod_zone_lst[i:i+3]); plt.savefig(root / 'ZONEWATPROD.png')
    sg.gor(prod_zone_lst[i:i+3]); plt.savefig(root / 'ZONEGOR.png')
    sg.wcut(prod_zone_lst[i:i+3]); plt.savefig(root / 'ZONEWCUT.png')
