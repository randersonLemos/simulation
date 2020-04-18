import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.utils.otm_manager_file import OtmManagerFile
from simulation.utils.otm_manager_data import OtmManagerData

def best_solutions_distribution_values(Df, suptitle, figname):
    plt.ioff()
    fig, axs = plt.subplots(1,9, figsize=(12,4), sharey=True, gridspec_kw={'wspace':0.05})
    fig.suptitle(suptitle, fontsize=20, y=1.01)
    
    count = 1
    groups = [tuple(Df['ZONE'].unique()[i:3+i]) for i in range(0,27,3)]
    for (ax, group) in zip(axs, groups):
        mask = (Df['ZONE'] == group[0]) | (Df['ZONE'] == group[1]) | (Df['ZONE'] == group[2])
        df = Df[mask]
        df['ZONE'] = df['ZONE'].str[-2:]
        well = group[0][:-3]
        
        ax.scatter(x=df['ZONE'], y=df['GOR'], s=300)
        ax.set_title(well, fontsize=14, y=0.98)
        
        ax.margins(0.25, 0.05)
        
        if count == 1:
            ax.set_ylabel('GOR', fontsize=14, labelpad=-2.5)        
              
        if count == 5:
            ax.set_xlabel('Zones', fontsize=14, labelpad=1)
        count += 1       
        
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.tick_params(axis='both', which='major', pad=-2.5)
            
        for idx, row in df.iterrows():
            ax.annotate(int(row['COUNT']), (row['ZONE'],row['GOR']), textcoords='offset points',  xytext=(0,0), ha='center', va='center', fontsize=12)
        
        
        for label in ax.get_xticklabels():
            label.set_rotation(90)
            label.set_fontsize(12)
            
            
        for label in ax.get_yticklabels():
            label.set_fontsize(12)

            
    plt.savefig(figname, bbox_inches='tight')
    
    
if __name__ == '__main__':   
    omf = OtmManagerFile()
    omf.set_project_root('H:/OTM_ICV_01S_SSS1')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')
    
    omd = OtmManagerData(omf)
    
    data = omd.data().tail(5)    
    data.X.columns.name = 'ZONE'
    Df = data.X.apply(pd.value_counts).T.stack().reset_index()
    Df = Df.rename(columns={'level_1':'GOR', 0:'COUNT'})
    Df['ZONE'] = Df['ZONE'].str.replace('_GOR','')
    best_solutions_distribution_values(Df, 'Best solutions distribution and values', 'fig/bsol.png')
    
    data = omd.data().head(5)    
    data.X.columns.name = 'ZONE'   
    Df = data.X.apply(pd.value_counts).T.stack().reset_index()
    Df = Df.rename(columns={'level_1':'GOR', 0:'COUNT'})
    Df['ZONE'] = Df['ZONE'].str.replace('_GOR','')
    best_solutions_distribution_values(Df, 'Worst solutions distribution and values', 'fig/wsol.png')