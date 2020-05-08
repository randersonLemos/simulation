import os
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

sources = {}
sources['SSS'] = ('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1')
sources['SSS_RELAXED'] = ('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1_FLEX1')
sources['WIDE'] = ('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_WIDE1')

OtmManagerFile.set_default_simulation_folder_prefix('otm_iteration')
OtmManagerFile.set_default_simulation_file_prefix('model')
OtmManagerFile.set_default_result_file('otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

omd = OtmManagerData()

for key in sources:
    OtmManagerFile(sources[key])
    omd.add_omf(key, OtmManagerFile(sources[key]))

X = omd.data().X();
y = omd.data().y();
y['NPV'] = y['NPV']/1000000

with sb.plotting_context('talk'):
    xLabel = []
    for group in y.index.get_level_values(0).unique():
        for el in range(len(y.loc[group])):
            xLabel.append(el)

    fig, ax = plt.subplots(1,1, figsize=(10,5), tight_layout=True)

    sb.lineplot(x=xLabel, y='NPV', hue='GROUP', data=y.reset_index())

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:])

    ax.set_xticks(np.linspace(1, len(y.loc['SSS_RELAXED']), 10).astype(int))

    ax.set_yticks(np.linspace(y['NPV'].min(), y['NPV'].max(), 10).astype('int'))

    ax.set_title('IDHLC (n_samples=100, cut_value=0.2)')
    ax.set_xlabel('RUN')
    ax.set_ylabel('NPV [$MM]')

    ax.relim()      # make sure all the data fits
    ax.autoscale()

plt.savefig('output/line_group_npvs.png')
