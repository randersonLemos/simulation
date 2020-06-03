import os
import pathlib
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from collections import OrderedDict
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

_Order = OrderedDict()
_Order['SSS1'] = 0
_Order['SSS2'] = 1
_Order['WIDE'] = 2
_Order['TIM1'] = 3
_Order['TIM2'] = 4
_Order['TIM3'] = 5

root = pathlib.Path('/media/pamonha/DATA/DRIVE/OTM_20200101')
pathprojects = {}
pathprojects['SSS1'] = root / 'OTM_GOR_ICV1_SSS1_1'
pathprojects['SSS2'] = root / 'OTM_GOR_ICV1_SSS2_1'
pathprojects['WIDE'] = root / 'OTM_GOR_ICV1_WIDE1_1'
pathprojects['TIM1'] = root / 'OTM_TIME_ICV1_RANGE1_1'
pathprojects['TIM2'] = root / 'OTM_TIME_ICV1_RANGE2_1'
pathprojects['TIM3'] = root / 'OTM_TIME_ICV1_RANGE3_1'
pathprojects['TIM3'] = root / 'OTM_TIME_ICV1_RANGE4_1'

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

piv = y.pivot_table(y, index=['ITERATION'], columns=['GROUP'], aggfunc={'NPV': [max, np.mean, min, len]}, fill_value=0).astype('int')
piv = piv.loc[piv.index <= 15]
piv.columns = piv.columns.rename('FUNC', level=1)
pivs = piv.stack(level=[1,2]).reset_index()
pivs['FUNC'] = pivs['FUNC'].str.upper()

pivs['GROUP'] = pd.Categorical(pivs['GROUP'], _Order.keys())
pivs = pivs.sort_values('GROUP')

plt.style.use('seaborn-talk')

fig, axs = plt.subplots(2, 1, figsize=(10,5), sharex=True, tight_layout=True)

sb.barplot(x='GROUP', y='NPV', hue='FUNC', data=pivs[pivs['FUNC'] == 'MAX'], dodge=False, ci=None, estimator=np.max, alpha=0.50, linewidth=1, edgecolor='black', ax=axs[0])
axs[0].set_ylabel('NPV [MM$]')
axs[0].set_yticks([])
axs[0].set_ylim(bottom=2200, top=2525)
axs[0].set_xlabel('')
axs[0].get_legend().remove()

sb.barplot(x='GROUP', y='NPV', hue='FUNC', data=pivs[pivs['FUNC'] == 'LEN'], dodge=False, ci=None, estimator=np.sum, alpha=0.50, linewidth=1, edgecolor='black', ax=axs[1])
axs[1].set_ylabel('ITERATION')
axs[1].set_yticks([])
axs[1].set_ylim(top=1750)
axs[1].get_legend().remove()

for index, row in pivs[pivs['FUNC'] == 'MAX'].groupby('GROUP').max().iterrows():
    axs[0].text(_Order[index], row['NPV']+1, row['NPV'], color='black', ha="center", fontsize='x-large')

for index, row in pivs[pivs['FUNC'] == 'LEN'].groupby('GROUP').sum().iterrows():
    axs[1].text(_Order[index], row['NPV']+1, row['NPV'], color='black', ha="center", fontsize='x-large')