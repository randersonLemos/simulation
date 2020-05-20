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

def get_data(rwo_paths_lst, printColumns=False, printIndexes=False):
    from simulation.table.utils import get_tables
    from simulation.table.sector_keys import Sector_Keys

    lst = []
    models = []
    for path in rwo_paths_lst:
        #print(path)
        tables = get_tables(path)
        #tables.date_range(end='2040')

        model = path.stem; print(model)
        models.append(model)

        for well_name, alias in inje_lst:
            tables.add(tables.join(well_name, *alias, dell=True)) # join xxxxxx-w and xxxxxx-g to xxxxxx

        df = pd.DataFrame()
        df = tables.get(Sector_Keys.sector()).df

        for prod in prod_lst:
            for col in tables.get(prod).df:
                df[col.replace('WELL', prod)] = tables.get(prod).df[col]

        for inje in inje_lst:
            for col in tables.get(inje[0]).df:
                df[col.replace('WELL', inje[0])] = tables.get(inje[0]).df[col]

        for prod in prod_lst:
            for col in tables.grp_col_spe_well(prod):
                df['{} {}'.format(prod,col.replace('_', ' '))] = tables.grp_col_spe_well(prod)[col]

        for inje in inje_lst:
            for col in tables.grp_col_spe_well(inje[0]):
                df['{} {}'.format(inje[0],col.replace('_', ' '))] = tables.grp_col_spe_well(inje[0])[col]

        for col in df:
            if 'OPC' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'OIL CUMU SC')] = df[col]
                del df[col]

            if 'OPR' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'OIL RATE SC')] = df[col]
                df['{} {} {}'.format(split[0], split[2], 'STATE')] = df[col].map(lambda x: 0 if x else 1)
                del df[col]

            if 'GPC' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'GAS CUMU SC')] = df[col]
                del df[col]

            if 'GPR' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'GAS RATE SC')] = df[col]
                del df[col]

            if 'WPC' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'WATER CUMU SC')] = df[col]
                del df[col]

            if 'WPR' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'WATER RATE SC')] = df[col]
                del df[col]

            if 'GOR Z' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'GOR SC')] = df[col]
                del df[col]

            if 'WCUT Z' in col:
                split = col.split()
                df['{} {} {}'.format(split[0], split[2], 'WCUT SC')] = df[col]
                del df[col]

        del df['TIME']
        df.dropna(inplace=True)
        lst.append(df)

        if model == 'model0001': break

    if printColumns:
        with open('output/columns.txt', 'w') as fh:
            fh.write('\n'.join(df.columns))

    if printIndexes:
        with open('output/indexes.txt', 'w') as fh:
            fh.write('\n'.join(df.index))

    return lst


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData


OtmManagerFile.set_default_simulation_folder_prefix('otm_iteration')
OtmManagerFile.set_default_simulation_file_prefix('model')
OtmManagerFile.set_default_result_file('otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')


if __name__ == '__main__':
    sources = {}
    sources['SSS'] = ('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1')
    sources['SSS_RELAXED'] = ('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_SSS1_FLEX1')
    sources['WIDE'] = ('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_WIDE1')

    omd = OtmManagerData()

    omfs = {}
    for key in sources:
        omf = OtmManagerFile(sources[key])
        omd.add_omf(key, omf)
        omfs[key] = omf

    kkey, runn = omd.data().y()['NPV'].idxmax()
    path = [el for el in omfs[kkey].simulation_file_paths('.rwo') if runn in str(el)][0]

    Dfs = get_data([path], printColumns=True)
    Df = pd.concat(Dfs)#.reset_index(drop=True)


    ### FIELD ###
    fig, ax = plt.subplots(1,1, figsize=(10,5), constrained_layout=True)
    (Df.filter(like='FIELD OIL PROD CUMU')/1000).plot(ax=ax)
    ax.yaxis.set_major_locator(LinearLocator(5))
    ax.set_ylabel('$msm^3$')
    ax.set_ylim(ymin=0)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, ['OIL PRODUCTION'], loc='upper right')
    fig.subplots_adjust(top=0.92)
    fig.suptitle('FIELD')
    ax.grid()

    plt.savefig('./output/fig/FIELD1.png')

    fig, axs = plt.subplots(2,2, figsize=(10,5), sharex=True, gridspec_kw={}, constrained_layout=True)
    fig.subplots_adjust(top=0.92)
    fig.suptitle('FIELD')

    (Df.filter(like='FIELD GAS PROD CUMU')/1000000).plot(ax=axs[0,0])
    axs[0,0].set_ylabel('$mmsm^3$')
    axs[0,0].yaxis.set_major_locator(LinearLocator(5))
    axs[0,0].set_ylim(ymin=0)
    handles, labels = axs[0,0].get_legend_handles_labels()
    axs[0,0].legend(handles, ['GAS PRODUCTION'], loc='upper right')
    axs[0,0].grid()

    (Df.filter(like='FIELD WATER PROD CUMU')/1000).plot(ax=axs[1,0])
    axs[1,0].set_ylabel('$msm^3$')
    axs[1,0].yaxis.set_major_locator(LinearLocator(5))
    axs[1,0].set_ylim(ymin=0)
    handles, labels = axs[1,0].get_legend_handles_labels()
    axs[1,0].legend(handles, ['WATER PRODUCTION'], loc='upper right')
    axs[1,0].grid()

    (Df.filter(like='FIELD GAS INJE CUMU')/1000000).plot(ax=axs[0,1])
    #axs[0,1].set_ylabel('$mmsm^3$')
    axs[0,1].yaxis.set_major_locator(LinearLocator(5))
    axs[0,1].set_ylim(ymin=0)
    handles, labels = axs[0,1].get_legend_handles_labels()
    axs[0,1].legend(handles, ['GAS INJECTION'], loc='upper right')
    axs[0,1].grid()

    (Df.filter(like='FIELD WATER INJE CUMU')/1000).plot(ax=axs[1,1])
    #axs[1,1].set_ylabel('$msm^3$')
    axs[1,1].yaxis.set_major_locator(LinearLocator(5))
    axs[1,1].set_ylim(ymin=0)
    handles, labels = axs[1,1].get_legend_handles_labels()
    axs[1,1].legend(handles, ['WATER INJECTION'], loc='upper right')
    axs[1,1].grid()

    plt.savefig('./output/fig/FIELD2.png')

    ### WELL AND ZONES GOR ###
    for well in prod_lst:
        fig, ax = plt.subplots(1,1, figsize=(10,5), tight_layout=True)
        Df.filter(like='GOR').filter(like=well).plot(ax=ax)
        handles, labels = ax.get_legend_handles_labels()
        labels = ['WELL', 'ZONE 1', 'ZONE 2', 'ZONE 3']
        ax.legend(handles, labels, loc='upper right')
        ax.set_ylabel('GOR [$sm^3/sm^3$]')
        ax.set_yticks(range(0,4750,250))
        ax.set_title('{} ZONES w/ ON/OFF ICV'.format(well))
        ax.set_ylim(ymax=4500,ymin=0)
        ax.grid()
        plt.savefig('./output/fig/{}GOR.png'.format(well))

    ### WELL AND ZONES OIL RATE ###
    for well in prod_lst:
        fig, ax = plt.subplots(1,1, figsize=(10,5), tight_layout=True)
        Df.filter(like='OIL').filter(like='RATE').filter(like=well).plot(ax=ax)
        handles, labels = ax.get_legend_handles_labels()
        labels = ['WELL', 'ZONE 1', 'ZONE 2', 'ZONE 3']
        ax.legend(handles, labels, loc='upper right')
        ax.set_ylabel('OIL RATE [$msm^3/d$]')
        ax.set_yticks(range(0,3250,250))
        ax.set_title('{} ZONES w/ ON/OFF ICV'.format(well))
        ax.set_ylim(ymax=3000,ymin=0)
        ax.grid()
        plt.savefig('./output/fig/{}OIL.png'.format(well))

    ### WELL AND ZONES WATER RATE ###
    for well in prod_lst:
        fig, ax = plt.subplots(1,1, figsize=(10,5), tight_layout=True)
        Df.filter(like='WCUT').filter(like=well).plot(ax=ax)
        handles, labels = ax.get_legend_handles_labels()
        labels = ['WELL', 'ZONE 1', 'ZONE 2', 'ZONE 3']
        ax.legend(handles, labels, loc='upper right')
        ax.set_ylabel('WCUT [$100\\times sm^3/sm^3$]')
        ax.set_yticks(range(0,110,10))
        ax.set_title('{} ZONES w/ ON/OFF ICV'.format(well))
        #ax.set_ylim(ymax=2000,ymin=0)
        ax.grid()
        plt.savefig('./output/fig/{}WCUT.png'.format(well))

    ### PREVIOUS THREE ###
    for well in prod_lst:
        fig, axs = plt.subplots(3,1, figsize=(5,5), sharex=True, tight_layout=True)
        Df.filter(like='OIL').filter(like='RATE').filter(like=well).plot(ax=axs[0])
        handles, labels = ax.get_legend_handles_labels()
        labels = ['WELL', 'ZONE 1', 'ZONE 2', 'ZONE 3']
        axs[0].legend(handles, labels, loc='upper right')
        axs[0].set_ylabel('OIL RATE [$msm^3/d$]')
        axs[0].set_yticks(range(0,3250,500))
        axs[0].set_title('{} ZONES w/ ON/OFF ICV'.format(well))
        axs[0].set_ylim(ymax=3000,ymin=0)
        axs[0].grid()

        Df.filter(like='GOR').filter(like=well).plot(ax=axs[1])
        handles, labels = ax.get_legend_handles_labels()
        labels = [] #['WELL', 'ZONE 1', 'ZONE 2', 'ZONE 3']
        axs[1].legend(handles, labels, loc='upper right')
        axs[1].set_ylabel('GOR [$sm^3/sm^3$]')
        axs[1].set_yticks(range(0,4750,750))
        #axs[1].set_title('ON/OFF ICVs of well {}'.format(well))
        axs[1].set_ylim(ymax=4500,ymin=0)
        axs[1].grid()

        Df.filter(like='WCUT').filter(like=well).plot(ax=axs[2])
        handles, labels = ax.get_legend_handles_labels()
        labels = [] #['WELL', 'ZONE 1', 'ZONE 2', 'ZONE 3']
        axs[2].legend(handles, labels, loc='upper right')
        axs[2].set_ylabel('WCUT [$\\%$]')
        axs[2].set_yticks(range(0,110,25))
        #axs[2].set_title('ON/OFF ICVs of well {}'.format(well))
        axs[2].grid()

        plt.savefig('./output/fig/{}.png'.format(well))



#    ### WELL AND ZONES WATER RATE ###
#    for well in prod_lst:
#        fig, ax = plt.subplots(1,1, figsize=(10,5), tight_layout=True)
#        Df.filter(like='').filter(like='RATE').filter(like=well).plot(ax=ax)
#        handles, labels = ax.get_legend_handles_labels()
#        labels = ['WELL', 'ZONE 1', 'ZONE 2', 'ZONE 3']
#        ax.legend(handles, labels)
#        ax.set_ylabel('WATER RATE [$msm^3/d$]')
#        ax.set_yticks(range(0,2250,250))
#        ax.set_title('ON/OFF ICVs of well {}'.format(well))
#        ax.set_ylim(ymax=2000,ymin=0)
#        ax.grid()
#        plt.savefig('./output/fig/{}WATER.png'.format(well))





    plt.clf()

    #omf.simulation_file_paths('.rwo')
    #omf = OtmManagerFile('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_ICV1_WIDE1')
    #Dfs = get_data(omf, printColumns=True)

    #Df = pd.concat(Dfs)#.reset_index(drop=True)
    #Df.index = Df.index.map(lambda x: str(x).split()[0])
    #Df[sorted(Df.filter(like='STATE').columns)].T.to_excel('output/wide_state.xlsx')
    #Df.to_excel('output/wide.xlsx')