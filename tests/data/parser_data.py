import os
import pandas as pd
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.manager.otm_manager_file import OtmManagerFile

OtmManagerFile.set_default_simulation_folder_prefix('otm_iteration')
OtmManagerFile.set_default_simulation_file_prefix('model')
OtmManagerFile.set_default_result_file('otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

omf = OtmManagerFile('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_WIDE1_1')

def rename_rootname_simulation_folders(old_part, new_part):
    for path in omf.simulation_folder_paths():
        stem = path.stem.replace(old_part, new_part)
        path.rename(path.parent / stem)

def rename_rootname_simulation_files(old_part, new_part):
    for path in omf.simulation_file_paths():
        name = path.name.replace(old_part, new_part)
        path.rename(path.parent / name)

def update_hldg_content():
    for path in omf.hldg_sample_file_paths():
        df = pd.read_csv(path, sep='\t')
        df['ID'] = df['ID'].str.replace('model', 'run')
        df.to_csv(path, sep='\t', index=False)

def delete_rstr_simulation_files():
    for path in omf.simulation_file_paths():
        if '.rstr' in ''.join(path.parts):
            path.unlink()

def delete_unitub_simulation_files():
    for path in omf.simulation_file_paths('.unitub'):
        path.unlink()

def delete_SERIES_simulation_files():
    for path in omf.simulation_file_paths():
        if 'SERIES' in ''.join(path.parts):
            path.unlink()

