prod_lst = []
prod_lst.append('Wildcat')
prod_lst.append('PRK014')
prod_lst.append('PRK028')
prod_lst.append('PRK045')
prod_lst.append('PRK052')
prod_lst.append('PRK060')
prod_lst.append('PRK061')
prod_lst.append('PRK083')
prod_lst.append('PRK084')
prod_lst.append('PRK085')

inje_lst = []
inje_lst.append(('IRK004',('IRK004-G','IRK004-W', ), ))
inje_lst.append(('IRK028',('IRK028-G','IRK028-W', ), ))
inje_lst.append(('IRK029',('IRK029-G','IRK029-W', ), ))
inje_lst.append(('IRK036',('IRK036-G','IRK036-W', ), ))
inje_lst.append(('IRK049',('IRK049-G','IRK049-W', ), ))
inje_lst.append(('IRK050',('IRK050-G','IRK050-W', ), ))
inje_lst.append(('IRK056',('IRK056-G','IRK056-W', ), ))
inje_lst.append(('IRK063',('IRK063-G','IRK063-W', ), ))


import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.output.utils import get_tables
from simulation.output.sector_graph import Sector_Graph
from simulation.output.sector_keys import Sector_Keys
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

SOURCES = []
SOURCES.append('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1')
SOURCES.append('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1_FLEX1')
SOURCES.append('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_WIDE1')

GROUPS = []
GROUPS.append('sss')
GROUPS.append('sss_relaxed')
GROUPS.append('wide')

if __name__ == '__main__':
    #Xs = pd.DataFrame()
    #ys = pd.DataFrame()

    for source, group in zip(SOURCES, GROUPS):
        omf = OtmManagerFile()
        omf.set_project_root(source)
        omf.set_simulation_folder_prefix('otm_iteration')
        omf.set_simulation_file_prefix('model')
        omf.set_result_file('otm.csv')
        omf.set_hldg_sample_file('hldg.txt')

        omd = OtmManagerData(omf)
        X = omd.data(npv_sorted=False).X()
        #X.index = pd.MultiIndex.from_product([[group], X.index] , names=['REGION', 'RUN'])
        #Xs = Xs.append(X)

        y = omd.data(npv_sorted=False).y()
        y['NPV'] = y['NPV'] / 1000000
        y['ITERATION'] = y['ITERATION'].apply(str)
        #y.index = pd.MultiIndex.from_product([[group], y.index] , names=['REGION', 'RUN'])
        #ys = ys.append(y)

        X.columns = X.columns.str[:-4]
        X.index = X.index.str[-4:]


        with sb.plotting_context('talk'):
            fig, ax = plt.subplots(figsize=(10,5), tight_layout=True)
            sb_heatmap = sb.heatmap(X, annot=False, fmt='d', xticklabels=X.columns, cbar=True, square=False, ax=ax, cbar_kws={'pad':0.01})
            plt.title('STRATEGIES OVERVIEW ({})'.format(group.upper()), fontsize=20)
            plt.ylabel('RUNS')
            sb_heatmap.get_figure().savefig('strategies_{}.png'.format(group))

            X = X.tail(5)

            fig, ax = plt.subplots(figsize=(10,5), tight_layout=True)
            sb_heatmap = sb.heatmap(X, annot=False, fmt='d', xticklabels=X.columns, cbar=True, square=False, ax=ax, cbar_kws={'pad':0.01}, linewidths=0.75)
            plt.title('5 BEST STRATEGIES ({})'.format(group.upper()), fontsize=20)
            plt.ylabel('RUNS')
            ax.yaxis.set_ticklabels(ax.yaxis.get_ticklabels(), rotation=0)
            sb_heatmap.get_figure().savefig('strategies_best_{}.png'.format(group))

            X = X[sorted(X.columns, key= lambda x: x[-2:])]

            fig, ax = plt.subplots(figsize=(10,5), tight_layout=True)
            sb_heatmap = sb.heatmap(X, annot=False, fmt='d', xticklabels=X.columns, cbar=True, square=False, ax=ax, cbar_kws={'pad':0.01}, linewidths=0.75)
            plt.title('5 BEST STRATEGIES (SORTED BY ZONES) ({})'.format(group.upper()), fontsize=20)
            plt.ylabel('RUNS')
            ax.yaxis.set_ticklabels(ax.yaxis.get_ticklabels(), rotation=0)
            sb_heatmap.get_figure().savefig('strategies_best_sorted_{}.png'.format(group))
