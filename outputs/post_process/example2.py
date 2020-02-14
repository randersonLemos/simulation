# -*- coding: utf-8 -*-
"""
From .rep to .csv over all simulation groups (sim_group_folder) organized
under the simulation directory (SIMS_FOLDER)

@author: randerson
"""

import os
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from config import settings as sett
from post_process.scripts import utils


sim_group_folders = os.listdir(sett.REP_ROOT / sett.SIMS_FOLDER)
for sim_group_folder in sim_group_folders:
    sim_folders = []
    for content in os.listdir(sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder):
        if os.path.isdir(sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / content):
            sim_folders.append(content)
    for sim_folder in sim_folders:
        try:
            path_to_rep_file = sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / sim_folder / sett.REP_NAME
            tables = utils.get_tables(path_to_rep_file)
            print(path_to_rep_file)

            from inputt import loader
            for well in loader.inje_lst:
                als1, als2 = well.alias_lst
                tables.add(tables.join(well.name, als1, als2, dell=True))
            path_to_csv_folder = sett.CSV_ROOT / sett.SIMS_FOLDER / sim_group_folder / sim_folder
            tables.to_csv(path_to_csv_folder)

        except KeyError:
            print("Error with rep file from:")
            print("  ", path_to_rep_file)
            print(str(path_to_rep_file), file=open("log.txt", "a"))
