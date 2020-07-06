import os
import re
import pathlib
import pandas as pd
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.manager.otm_manager_file import OtmManagerFile

OtmManagerFile.set_default_simulation_folder_prefix('otm_IT')
OtmManagerFile.set_default_simulation_file_prefix('model')
OtmManagerFile.set_default_result_file('otm.otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

omf = OtmManagerFile('/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_18WIDE1_1')

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

def update_content(old_root, new_root):
    ree = re.compile(r'{}\d\d\d\d'.format(old_root))

    for path in omf.project_root().glob('**/*'):
        if path.is_file():
            try:
                fh = path.open('r')
                content = fh.read()
                fh.close()
            except UnicodeDecodeError:
                pass
            if ree.findall(content):
                print(path)
                content = re.sub(r'{}(\d\d\d\d)'.format(old_root), r'{}\1'.format(new_root), content)
                fh = path.open('w')
                fh.write(content)
                fh.close()

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

def fix_name_numbering():
    def find(path):
        ree = re.compile(r'\D\d\d\d\d\.')
        lst = ree.findall(str(path))
        if len(lst) > 1:
            raise ValueError('At most size 1 for lst variable')
        if len(lst) == 1:
            return lst[0][1:-1]
        if len(lst) == 0:
            return lst

    new = 1
    is_first_time = True

    try:
        pathlib.Path('fix_name_log.txt').unlink()
    except FileNotFoundError:
        pass

    for folder in omf.simulation_folder_paths():
        print('{}'.format(folder.name), file=open('fix_name_log.txt', 'a'))

        paths = sorted(list(folder.glob('*')))
        for path in paths:
            if omf.simulation_file_prefix() in str(path.name):
                if is_first_time:
                    old = find(path.name)
                    is_first_time = False

                if old in str(path.name):
                    new_path = path.parent / path.name.replace(old, '{:04d}'.format(new))
                else:
                    old = find(path.name)
                    new += 1
                    new_path = path.parent / path.name.replace(old, '{:04d}'.format(new))

                print('{} -> {}'.format(path, new_path), file=open('fix_name_log.txt', 'a'))

def hide_hldg_files():
    for path in omf.hldg_sample_file_paths():
        if path.exists():
            path.rename(path.parent / '{}.txt.bkp'.format(path.stem))

def delete_rstr_simulation_files():
    for path in omf.simulation_file_paths():
        if '.rstr' in ''.join(path.parts):
            path.unlink()

def delete_log_simulation_files():
    for path in omf.simulation_file_paths():
        if '.log' in ''.join(path.parts):
            path.unlink()

def delete_sr3_simulation_files():
    for path in omf.simulation_file_paths('.sr3'):
        path.unlink()

def delete_unitub_simulation_files():
    for path in omf.simulation_file_paths('.unitub'):
        path.unlink()

def delete_unievent_simulation_files():
    for path in omf.simulation_file_paths('.unievent'):
        path.unlink()

def delete_unipro_simulation_files():
    for path in omf.simulation_file_paths('.unipro'):
        path.unlink()

def delete_SERIES_simulation_files():
    for path in omf.simulation_file_paths():
        if 'SERIES' in ''.join(path.parts):
            path.unlink()

def delete_CONCENSSION_simulation_files():
    for folder in omf.simulation_folder_paths():
        for path in folder.glob('*'):
            if 'CONCESSION' in ''.join(path.parts):
                path.unlink()

def delete_not_essential_simulation_files():
    delete_rstr_simulation_files()
    delete_sr3_simulation_files()
    delete_unitub_simulation_files()
    delete_unievent_simulation_files()
    delete_unipro_simulation_files()
    delete_SERIES_simulation_files()
    delete_CONCENSSION_simulation_files()
    delete_log_simulation_files()
