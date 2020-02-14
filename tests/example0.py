# -*- coding: utf-8 -*-

from conf import paths

sim_folder_group = 'DEFAULT'
sim_folder = 'sim_001'

from assembly.scripts.producer_dual_icv import producer_dual_icv
from inputt.loader import prod_lst
for prod in prod_lst:
    prod.load_more_more()
    producer_dual_icv(  prod.name
                      , prod.group
                      , prod.operate
                      , prod.monitor
                      , prod.geometry
                      , prod.perf_ff
                      , prod.perf_table
                      , prod.time_open
                      , prod.time_on
                      , prod.layerclump
                      , []#prod.icv_operation
                      , []#prod.icv_control_law
                      , paths.LOCAL_ROOT / paths.SIMS_FOLDER / sim_folder_group / sim_folder / 'wells'
                      )






