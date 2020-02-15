# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:30:09 2020

@author: randerson
"""

import pathlib

USER = 'randerson'
CLUSTER_NAME = 'hpc02'
QUEUE_KIND = 'longas'
NR_PROCESSORS = 12

SIMS_FOLDER = 'SIMS'

LOCAL_ROOT     = pathlib.Path('')
REMOT_ROOT     = pathlib.PurePosixPath('')
LOCAL_PUTT_EXE = pathlib.Path('C:/\"Program Files (x86)"/PuTTY/plink.exe')
LOCAL_IMEX_EXE = pathlib.Path('C:/\"Program Files (x86)"/CMG/IMEX/2017.10/Win_x64/EXE/mx201710.exe')
REMOT_IMEX_EXE = pathlib.PurePosixPath('/mnt/software/CMG/imex/2017.10/linux_x64/exe/mx201710.exe')
LOCAL_REPO_EXE = pathlib.Path('C:/\"Program Files (x86)"/CMG/BR/2017.10/Win_x64/EXE/report.exe')
