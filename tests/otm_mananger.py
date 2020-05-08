import os
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

SOURCES = []
SOURCES.append('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1')
SOURCES.append('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1_FLEX1')
SOURCES.append('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_WIDE1')

GROUPS = []
GROUPS.append('SSS')
GROUPS.append('SSS_RELAXED')
GROUPS.append('WIDE')

Xs = pd.DataFrame()
ys = pd.DataFrame()

for source, group in zip(SOURCES, GROUPS):
    omf = OtmManagerFile()
    omf.set_project_root(source)
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')

    omd = OtmManagerData(omf)
    X = omd.data(npv_sorted=False).X()
    X.index = pd.MultiIndex.from_product([[group], X.index] , names=['REGION', 'RUN'])
    Xs = Xs.append(X)

    y = omd.data(npv_sorted=False).y()
    y['NPV'] = y['NPV'] / 1000000
    y['ITERATION'] = y['ITERATION'].apply(str)
    y.index = pd.MultiIndex.from_product([[group], y.index] , names=['REGION', 'RUN'])
    ys = ys.append(y)


with sb.plotting_context('talk'):
    fig, ax = plt.subplots(1,1, figsize=(10,5), tight_layout=True)

    sb.scatterplot(x='RUN', y='NPV', hue='REGION',  data=ys.reset_index() , legend='brief', ax=ax)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles[1:], labels=labels[1:])

    ax.set_xticks(np.linspace(1, len(ys.loc['SSS_RELAXED']), 10).astype(int))
    ax.xaxis.set_ticklabels(np.linspace(1, len(ys.loc['SSS_RELAXED']), 10).astype(int), rotation=90)

    ax.set_yticks(np.linspace(ys['NPV'].min(), ys['NPV'].max(), 10).astype('int'))

    ax.set_title('IDHLC (n_samples=100, cut_value=0.2)')
    ax.set_ylabel('NPV [$MM]')

    ax.relim()      # make sure all the data fits
    ax.autoscale()

    plt.savefig('output/scatter_regions_npv.png')
