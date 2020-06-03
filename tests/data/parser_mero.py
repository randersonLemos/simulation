import os
import pathlib

if os.name == 'posix':
    root = pathlib.Path('/media/pamonha/DATA/DRIVE/OTM_20200101')
else:
    root = pathlib.Path('H:/')

path = root / 'OTM_TIME_ICV1_WIDE1_1'

#old_part = 'otm_iteration_0'
#new_part = 'otm_IT'
#
#lst = []
#for item in path.glob('{}*'.format(old_part)):
#    name = item.stem.replace(old_part, new_part)
#    item.rename(item.parent / name)

old_part = 'model'
new_part = 'run'
    
for item in path.glob('otm_IT*'):
    for itemm in item.glob('*'):
        name = itemm.stem.replace(old_part, new_part)
        itemm.rename(itemm.parent / name)
  