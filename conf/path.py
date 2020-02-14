# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:04:54 2019

@author: randerson
"""


from pathlib import Path, PurePosixPath


LOCAL_ROOT     = Path('U:/simulation')
LOCAL_IMEX_EXE = Path('C:/\"Program Files (x86)"/CMG/IMEX/2017.10/Win_x64/EXE/mx201710.exe')
LOCAL_REPO_EXE = Path('C:/\"Program Files (x86)"/CMG/BR/2017.10/Win_x64/EXE/report.exe')
LOCAL_PUTT_EXE = Path('C:/\"Program Files (x86)"/PuTTY/plink.exe')

REMOTE_ROOT     = PurePosixPath('/home/randerson/simulation')
REMOTE_IMEX_EXE = PurePosixPath('/mnt/software/CMG/imex/2017.10/linux_x64/exe/mx201710.exe')

SIMS_FOLDER = Path('SIMS')