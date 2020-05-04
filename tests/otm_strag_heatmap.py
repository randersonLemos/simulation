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


if __name__ == '__main__':
    omf = OtmManagerFile()

    omf.set_project_root('/media/pamonha/DATA/DRIVE/IDLHC_20200101/OTM_ICV_01S_WIDE')

    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')

    omd = OtmManagerData(omf)

    X = omd.data().X()
    y = omd.data().y()

    X.columns = X.columns.str[:-4]
    X.index = X.index.str[-4:]

    sb.palplot(sb.color_palette("coolwarm", 7))

    fig, ax = plt.subplots(figsize=(10,5), tight_layout=True)
    sb_heatmap = sb.heatmap(X, annot=False, fmt='d', xticklabels=X.columns, cbar=True, square=False, ax=ax, cbar_kws={'pad':0.01})
    sb.set_context('talk')
    plt.title('SOLUTIONS (WIDE)', fontsize=20)
    plt.ylabel('runs')
    sb_heatmap.get_figure().savefig('out/heatmap_sols_wide.png')
    X.to_csv('out/heatmap_sols_wide.csv')

    X = X[sorted(X.columns, key= lambda x: x[-2:])]
    fig, ax = plt.subplots(figsize=(10,5), tight_layout=True)
    sb_heatmap = sb.heatmap(X, annot=False, fmt='d', xticklabels=X.columns, cbar=True, square=False, ax=ax, cbar_kws={'pad':0.01})
    sb.set_context('talk')
    plt.title('SOLUTIONS (WIDE) (SORTED)', fontsize=20)
    plt.ylabel('runs')
    sb_heatmap.get_figure().savefig('out/heatmap_sols_wide_sorted.png')
    X.to_csv('out/heatmap_sols_wide_sorted.csv')


    #X = omd.data().X().tail(10)
    #y = omd.data().y().tail(10)

    #fig, ax = plt.subplots(figsize=(10,5))
    #sb_heatmap = sb.heatmap(X, annot=False, fmt='d', xticklabels=X.columns.str[:-4], cbar=True, square=True, ax=ax)
    #sb.set_context('talk')
    #plt.title('10 BEST SOLUTIONS (WIDE)', fontsize=20)
    #plt.ylabel('runs')
    #sb_heatmap.get_figure().savefig('out/heatmap_10_bsols_wide.png')
    #X.to_csv('out/heatmap_10_bsol_wide.csv')

    #X = X[sorted(X.columns, key= lambda x: x[-6:])]
    #fig, ax = plt.subplots(figsize=(10,5), tight_layout=True)
    #sb_heatmap = sb.heatmap(X, annot=False, fmt='d', xticklabels=X.columns.str[:-4], cbar=True, square=True, ax=ax)
    #sb.set_context('talk')
    #plt.title('10 BEST SOLUTIONS (WIDE) (SORTED)', fontsize=20)
    #plt.ylabel('runs')
    #sb_heatmap.get_figure().savefig('out/heatmap_10_bsols_wide_sorted.png')
    #X.to_csv('out/heatmap_10_bsols_wide_sorted.csv')
