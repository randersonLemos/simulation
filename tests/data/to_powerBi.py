import os
import pathlib
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

if os.name == 'posix':
    root = pathlib.Path('/media/pamonha/DATA/DRIVE/OTM_20200101')
else:
    root = pathlib.Path('H:/')
    
pathprojects = {}
pathprojects['SSS1'] = root / 'OTM_GOR_ICV1_SSS1_1'
pathprojects['SSS2'] = root / 'OTM_GOR_ICV1_SSS2_1'
pathprojects['WIDE'] = root / 'OTM_GOR_ICV1_WIDE1_1'
pathprojects['TIM1'] = root / 'OTM_TIME_ICV1_RANGE1_1'
pathprojects['TIM2'] = root / 'OTM_TIME_ICV1_RANGE2_1'
pathprojects['TIM3'] = root / 'OTM_TIME_ICV1_RANGE3_1'
pathprojects['TIM4'] = root / 'OTM_TIME_ICV1_RANGE4_1'

from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

OtmManagerFile.set_default_simulation_folder_prefix('otm_IT')
OtmManagerFile.set_default_simulation_file_prefix('run')
OtmManagerFile.set_default_result_file('otm.otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

omd = OtmManagerData()
for key, value in pathprojects.items(): omd.add_omf(key, OtmManagerFile(project_root=value))
X, y = omd.data().X(), omd.data().y()
y['NPV'] = (y['NPV'] / 1000000).astype('int')
y = y.sort_values(by='NPV', ascending=False)
y['GLOBAL RANK'] = y['NPV'].rank(method='first', ascending=False).astype('int')
y['RANK'] = y.groupby('GROUP')['NPV'].rank(method='first', ascending=False).astype('int')
y = y.reset_index()
y['DOMAIN'] = y['GROUP'].apply(lambda x: 'TIME' if 'TIM' in x else 'GOR')
y = y.set_index(['GROUP', 'RUN'])
Merge = pd.merge(X, y, on=['GROUP', 'RUN']).reset_index()
for group in Merge['GROUP'].unique():
    Merge.loc[Merge['GROUP'] == group, 'RUN'] = Merge.loc[Merge['GROUP'] == group, 'RUN'].str.replace('run', group.lower())
Melt = Merge.melt(id_vars=['GROUP', 'RUN', 'ITERATION', 'NPV' , 'GLOBAL RANK', 'RANK', 'DOMAIN']).dropna()
Melt.columns = Melt.columns.str.upper()
Melt = Melt.sort_values('NPV', ascending=False)

for domain in Melt['DOMAIN'].unique():
    if domain == 'TIME':
        Melt.loc[Melt['DOMAIN'] == domain, 'VARIABLE'] =  Melt.loc[Melt['DOMAIN'] == domain, 'VARIABLE'].str.replace('CLOSETIME_PRK0', 'P')
    else:
        Melt.loc[Melt['DOMAIN'] == domain, 'VARIABLE'] =  Melt.loc[Melt['DOMAIN'] == domain, 'VARIABLE'].str.replace('_GOR', '')
        Melt.loc[Melt['DOMAIN'] == domain, 'VARIABLE'] =  Melt.loc[Melt['DOMAIN'] == domain, 'VARIABLE'].str.replace('PRK0', 'P')

def melt_to_csv():
    Melt.to_csv('melt.csv', index=False, sep=';')
