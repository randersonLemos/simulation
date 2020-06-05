import os
import pandas as pd
import re
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.manager.otm_manager_file import OtmManagerFile

OtmManagerFile.set_default_simulation_folder_prefix('otm_IT')
OtmManagerFile.set_default_simulation_file_prefix('run')
OtmManagerFile.set_default_result_file('otm.otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

omf = OtmManagerFile('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_TIME_ICV1_RANGE4_1')

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

def shift_number_simulation_file(first_itFolder, shift):
    for path in omf.simulation_file_paths():
        split = path.name.split('.')
        name, ext = split[0], split[1:]
        folder = path.parent.name
        if int(re.findall(r'\d+', folder)[0]) >= first_itFolder:

            num = '{:04d}'.format(int(name[3:7]))
            nnum = '{:04d}'.format(int(name[3:7]) + shift)
            nname = name.replace(num, nnum)
            #print('{} --> {}'.format(
            #    path,
            #    path.parent / '{}.{}'.format(nname, '.'.join(ext))
            #    ))
            path.rename(path.parent / '{}.{}'.format(nname, '.'.join(ext)))



def hide_hldg_files():
    for path in omf.hldg_sample_file_paths():
        if path.exists():
            path.rename(path.parent / '{}.txt.bkp'.format(path.stem))

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

