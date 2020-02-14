def handle_df(df_obj):
    df_obj = df.sort_values(by=['MODEL']).reset_index(drop=True)
    df_obj.index.name = 'Index'
    df_obj['Sim Group'] = sim_group_folder
    df_obj['MODEL'] = df_obj['MODEL'].str[:-5]
    df_obj = df_obj.rename(columns={'MODEL': 'Sim'})
    df_obj = df_obj.rename(columns={'NPVF': 'Npv'})

    for idi, i in enumerate(range(250, 5250, 250)):
        df_obj.loc[idi, 'Close Condition'] = '{}'.format(i)

    path_to_npv_file_dest = sett.CSV_ROOT / sett.CSV_FOLD / sett.SIMS_FOLDER / sim_group_folder / 'Sims.npv'
    path_to_npv_file_dest.parent.mkdir(parents=True, exist_ok=True)
    df_obj.to_csv(path_to_npv_file_dest, index=True)


from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


import pandas
from config import settings as sett


sim_group_folders = []
sim_group_folders.append('WELL')
sim_group_folders.append('ICV_01S')
sim_group_folders.append('ICV_02S')
sim_group_folders.append('ICV_02S_SHP')
sim_group_folders.append('ICV_02S_SMT')
sim_group_folders.append('ICV_03S')
sim_group_folders.append('ICV_03S_SHP')
sim_group_folders.append('ICV_03S_SMT')
sim_group_folders.append('ICV_04S')
sim_group_folders.append('ICV_04S_SHP')
sim_group_folders.append('ICV_04S_SMT')
sim_group_folders.append('ICV_05S')
sim_group_folders.append('ICV_05S_SHP')
sim_group_folders.append('ICV_05S_SMT')


for sim_group_folder in sim_group_folders:
    path_to_npv_file = sett.NPV_ROOT / sett.SIMS_FOLDER / sim_group_folder / sett.NPV_NAME
    df = pandas.read_csv(path_to_npv_file, sep=';')[['MODEL', 'NPVF']]
    handle_df(df)