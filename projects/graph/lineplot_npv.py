import os
import pathlib
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib as mpl
import matplotlib.pyplot as plt
import header
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData


dirs = header.Get_dirs('./list.dirs')


omd = OtmManagerData()
for key, value in dirs:
    omd.add_omf(key, OtmManagerFile(project_root=value))
X, y = omd.data()

index = X.index.to_frame(index=False)
index['RUN'] = index['RUN'].str.replace('model', 'run')

# WIDE18_1 (Reference)
index['GRP'] = index['GRP'].str.replace('WIDE18_1', 'WIDE18')

# WIDE18_VVGS_1 (Variable value geometric spaced)
index['GRP'] = index['GRP'].str.replace('WIDE18_VVGS_1', 'WIDE18VVGS')

# WIDE18_SNGS_1 (Sample number geometric spaced)
index['GRP'] = index['GRP'].str.replace('WIDE18_SNGS_1', 'WIDE18SNGS')

# USS2U1_[1,14] (Two parts uptadable search space at each 1 iteration)
index['GRP'] = index['GRP'].str.replace('USS2U1_\d*', 'USS2U1')
mask = index['GRP'] == 'USS2U1'
tmp = index.loc[ mask , 'ITE' ]
index.loc[ mask , 'ITE' ] = [int(x/100 + 1) for x in range(len(tmp))]

# USS2U1_[1,3] (Two parts uptadable search space at each 5 iteration)
index['GRP'] = index['GRP'].str.replace('USS2U5_\d*', 'USS2U5')
mask = index['GRP'] == 'USS2U5'
tmp = index.loc[ mask , 'ITE' ]
index.loc[ mask , 'ITE' ] = [int(x/100 + 1) for x in range(len(tmp))]

# USS2U1_[1, 16] (Five parts uptadable search space at each 1 iteration)
index['GRP'] = index['GRP'].str.replace('USS5U1_\d*', 'USS5U1')
mask = index['GRP'] == 'USS5U1'
tmp = index.loc[ mask , 'ITE' ]
index.loc[ mask , 'ITE' ] = [int(x/100 + 1) for x in range(len(tmp))]

index['#RU'] = -1
for grp in index['GRP'].unique():
    index.loc[ index['GRP'] == grp, '#RU' ] = range(1, sum(index['GRP'] == grp) + 1 )

y.index = pd.MultiIndex.from_frame(index)
y['NPV'] = (y['NPV']/1000000).apply(int)

frame = y.reset_index()

piv = frame.pivot_table(index=['ITE'], columns=['GRP'], values='NPV', aggfunc=np.max)

frame['MNPV'] = -1
for grp in frame['GRP'].unique():
    for ite in frame[ frame['GRP'] == grp ]['ITE'].unique():
        frame.loc[ (frame['GRP'] == grp) & (frame['ITE'] == ite), 'MNPV' ] = piv.loc[ite, grp]


fig, ax = plt.subplots()
ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'WIDE18' ]
, c='k'
, alpha=1.0,
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'WIDE18SNGS' ]
, c='tab:blue'
, alpha=1.0,
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'WIDE18VVGS' ]
, c='tab:orange'
, alpha=1.0,
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'USS2U5' ]
, c='tab:green'
, linestyle='dashed'
, alpha=1.0,
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'USS2U1' ]
, c='tab:purple'
, linestyle='dashed'
, alpha=1.0,
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'USS5U1' ]
, c='tab:brown'
, linestyle='dashed'
, alpha=1.0,
)

ax.legend(['WIDE18', 'WIDE18SNGS', 'WIDE18VVGS', 'USS2U5', 'USS2U1', 'USS5U1'])
ax.set_ylabel('NPV [MM$]')
ax.set_xlabel('RUNS')

xlabels = [1, 500, 1000, 1500, 2000]

ylabels = [2402, 2425, 2450, 2475, 2493, 2496]
ax.set_xlim(-25,2025)
ax.set_ylim(2401,2497)
ax.set_yticks(ylabels)
ax.set_xticks(xlabels)
#ax.set_xticklabels(ax.get_xticks().astype('int'), rotation=90)
ax.grid()

plt.savefig('./fig/uss_npv.png', bbox_inches='tight')