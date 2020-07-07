from header import *
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

OtmManagerFile.set_default_simulation_folder_prefix('otm_IT')
OtmManagerFile.set_default_simulation_file_prefix('run')
OtmManagerFile.set_default_result_file('otm.otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

Group = '18WIDE'
omf = OtmManagerFile('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_18WIDE1_1')
omd = OtmManagerData([Group] ,[omf])
Xy = omd.data().Xy()
Xy['NPV'] = (Xy['NPV']/1000000).astype('int')

Xy.columns = Xy.columns.str.replace(r'(\D)\D\D\d(\d\d)\D(\D\d)\D*',r'\1\2\3',regex=True)

def heatmap(df, title, do_annot, do_cbar, fname):
    fig, ax = plt.subplots(figsize=(16,6), tight_layout=True)
    sb.heatmap(df, fmt='d', annot=do_annot, annot_kws={'size':14}, cbar=do_cbar, square=False, ax=ax)
    ax.set_ylabel('NPV [MM$]')

    from itertools import cycle
    colors = ['b', 'g', 'r']
    pool = cycle(colors)
    for xtick in ax.get_xticklabels():
        xtick.set_color(next(pool))

    plt.title(title)

    root = pathlib.Path('./fig/solution')
    root.mkdir(parents=True, exist_ok=True)
    plt.savefig(root / fname); plt.close()

heatmap(Xy.set_index('NPV').sort_values(by='NPV').iloc[-15:,:], 'BEST {} STRATEGIES'.format(Group), True, False, 'best-solutions-{}'.format(Group))
heatmap(Xy.set_index('NPV').sort_values(by='NPV'), '{} STRATEGIES'.format(Group), False, True, 'solutions-{}'.format(Group))