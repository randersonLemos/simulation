import os
import pathlib
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib as mpl
import matplotlib.pyplot as plt
import header
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path:
    os.sys.path.insert(0 , os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.manager.otm_manager_file import OtmManagerFile
from src.manager.otm_manager_data import OtmManagerData


dirs = header.Get_dirs('./list.dirs')


omd = OtmManagerData()
for key, value in dirs:
    omd.add_omf(key, OtmManagerFile(project_root=value))
X, y = omd.data()

index = X.index.to_frame(index=False)
index['RUN'] = index['RUN'].str.replace('model', 'run')

## WIDE18_1 (Reference)
#index['GRP'] = index['GRP'].str.replace('WIDE18_1', 'WIDE18')
#
## WIDE18_VVGS_1 (Variable value geometric spaced)
#index['GRP'] = index['GRP'].str.replace('WIDE18_VVGS_1', 'WIDE18VVGS')
#
## WIDE18_SNGS_1 (Sample number geometric spaced)
#index['GRP'] = index['GRP'].str.replace('WIDE18_SNGS_1', 'WIDE18SNGS')

# USS5_1_[1,16]
index['GRP'] = index['GRP'].str.replace('USS5_1_\d*', 'USS5_1')
mask = index['GRP'] == 'USS5_1'
tmp = index.loc[ mask , 'ITE' ]
index.loc[ mask , 'ITE' ] = [int(x/100 + 1) for x in range(len(tmp))]

# USS5_2_[1,9]
index['GRP'] = index['GRP'].str.replace('USS5_2_\d*', 'USS5_2')
mask = index['GRP'] == 'USS5_2'
tmp = index.loc[ mask , 'ITE' ]
index.loc[ mask , 'ITE' ] = [int(x/100 + 1) for x in range(len(tmp))]

# USS5_3_[1,11]
index['GRP'] = index['GRP'].str.replace('USS5_3_\d*', 'USS5_3')
mask = index['GRP'] == 'USS5_3'
tmp = index.loc[ mask , 'ITE' ]
index.loc[ mask , 'ITE' ] = [int(x/100 + 1) for x in range(len(tmp))]

# USS5_4_[1,16]
index['GRP'] = index['GRP'].str.replace('USS5_4_\d*', 'USS5_4')
mask = index['GRP'] == 'USS5_4'
tmp = index.loc[ mask , 'ITE' ]
index.loc[ mask , 'ITE' ] = [int(x/100 + 1) for x in range(len(tmp))]

index['#RU'] = -1
for grp in index['GRP'].unique():
    index.loc[ index['GRP'] == grp, '#RU' ] = range(1, sum(index['GRP'] == grp) + 1 )

y.index = pd.MultiIndex.from_frame(index)
y['NPV'] = (y['NPV']/1000000).apply(int)

frame = y.reset_index()

piv = frame.pivot_table(index=['ITE'], columns=['GRP'], values='NPV', aggfunc=np.max)
piv = piv.dropna()

msk = frame.ITE <= piv.index.max()
frame = frame[msk]

frame['MNPV'] = -1
for grp in frame['GRP'].unique():
    for ite in frame[ frame['GRP'] == grp ]['ITE'].unique():
        frame.loc[ (frame['GRP'] == grp) & (frame['ITE'] == ite), 'MNPV' ] = piv.loc[ite, grp]


fig, ax = plt.subplots()
ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'WIDE18_1' ]
, c='k'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'WIDE18_2' ]
, c='k'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'WIDE18_3' ]
, c='k'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'WIDE18_4' ]
, c='k'
, alpha=1.0
)


ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'VVGS_1' ]
, c='tab:blue'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'VVGS_2' ]
, c='tab:blue'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'VVGS_3' ]
, c='tab:blue'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'VVGS_4' ]
, c='tab:blue'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'USS5_1' ]
, c='tab:green'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'USS5_2' ]
, c='tab:green'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'USS5_3' ]
, c='tab:green'
, alpha=1.0
)

ax.plot('#RU', 'MNPV', data=frame.loc[ frame['GRP'] == 'USS5_4' ]
, c='tab:green'
, alpha=1.0
)


ax.legend(['WIDE18'])
ax.set_ylabel('NPV [MM$]')
ax.set_xlabel('RUNS')

#xlabels = [1, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
#ylabels = [2402, 2425, 2450, 2475, 2493, 2496]
#ax.set_xlim(-25,2025)
#ax.set_ylim(2401,2497)
#ax.set_xticks(xlabels)
#ax.set_yticks(ylabels)
ax.set_xticklabels(ax.get_xticks().astype('int'), rotation=90)
ax.grid()
#
#plt.savefig('./fig/uss_npv.png', bbox_inches='tight')
