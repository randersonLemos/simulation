def handle_df(df_obj):
    df_obj = df.sort_values(by=['MODEL']).reset_index(drop=True)
    df_obj.index.name = 'Index'
    df_obj['Sim Group'] = sim_group_folder
    df_obj['MODEL'] = df_obj['MODEL'].str[:-5]
    df_obj = df_obj.rename(columns={'MODEL': 'Sim'})
    df_obj = df_obj.rename(columns={'NPVF': 'Npv'})
    df_obj['Close Condition'] = 'none'
    path_to_npv_file_dest = sett.CSV_ROOT / sett.CSV_FOLD / sett.SIMS_FOLDER / sim_group_folder / 'Sims.npv'
    path_to_npv_file_dest.parent.mkdir(parents=True, exist_ok=True)
    df_obj.to_csv(path_to_npv_file_dest, index=True)


from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


import pandas
from config import settings as sett


sim_group_folder = 'REFERENCE'
path_to_npv_file = sett.NPV_ROOT / sett.SIMS_FOLDER / sim_group_folder / sett.NPV_NAME
df = pandas.read_csv(path_to_npv_file, sep=';')[['MODEL', 'NPVF']]
handle_df(df)