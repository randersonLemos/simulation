prod_lst = []
prod_lst.append('Wildcat'); prod_lst.append('PRK014'); prod_lst.append('PRK028')
prod_lst.append('PRK045');  prod_lst.append('PRK052'); prod_lst.append('PRK060')
prod_lst.append('PRK061');  prod_lst.append('PRK083'); prod_lst.append('PRK084')
prod_lst.append('PRK085')

inje_lst = []
inje_lst.append(('IRK004',('IRK004-G','IRK004-W', ), )); inje_lst.append(('IRK028',('IRK028-G','IRK028-W', ), ))
inje_lst.append(('IRK029',('IRK029-G','IRK029-W', ), )); inje_lst.append(('IRK036',('IRK036-G','IRK036-W', ), ))
inje_lst.append(('IRK049',('IRK049-G','IRK049-W', ), )); inje_lst.append(('IRK050',('IRK050-G','IRK050-W', ), ))
inje_lst.append(('IRK056',('IRK056-G','IRK056-W', ), )); inje_lst.append(('IRK063',('IRK063-G','IRK063-W', ), ))

import matplotlib.pyplot as plt
plt.style.use('seaborn-talk')

import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.table.utils import get_tables

Tables = []
Tables.append(get_tables('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_SSS2_1/otm_IT020/run1996.rwo'))
Tables.append(get_tables('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_TIME_ICV1_RANGE5_1/otm_IT006/run0540.rwo'))

for tables in Tables:
    tables.date_range(ini='2020')
    for well_name, alias in inje_lst: tables.add(tables.join(well_name, *alias, dell=True)) # join xxxxxx-w and xxxxxx-g to xxxxxx

from simulation.table.sector_graph import Sector_Graph

sg = Sector_Graph(Tables)
sg.oil_prod();# plt.savefig(path)

# sg.gas_prod(savefig_rootpath='./fig'); plt.savefig(path)
#
# sg.wat_prod(savefig_rootpath='./fig'); plt.savefig(path)
#
# sg.gas_inje(savefig_rootpath='./fig'); plt.savefig(path)
#
# sg.wat_inje(savefig_rootpath='./fig'); plt.savefig(path)
#
# sg.avg_pres(savefig_rootpath='./fig'); plt.savefig(path)
