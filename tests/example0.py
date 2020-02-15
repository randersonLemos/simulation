# -*- coding: utf-8 -*-
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import setup
from simulation.model.well.producer_dual_icv import producer_dual_icv
from simulation.input.well_design import Well_Design

Well_Design.set_rootPath('./input')

prds = []
prds.append(Well_Design(name='PRK014'))
prds.append(Well_Design(name='PRK028'))
prds.append(Well_Design(name='PRK045'))
prds.append(Well_Design(name='PRK052'))
prds.append(Well_Design(name='PRK060'))
prds.append(Well_Design(name='PRK061'))
prds.append(Well_Design(name='PRK083'))
prds.append(Well_Design(name='PRK084'))
prds.append(Well_Design(name='PRK085'))
prds.append(Well_Design(name='Wildcat'))

injs = []
injs.append(Well_Design(name='IRK004',alias=['IRK004_G','IRK004_W']))
injs.append(Well_Design(name='IRK028',alias=['IRK028_G','IRK028_W']))
injs.append(Well_Design(name='IRK029',alias=['IRK029_G','IRK029_W']))
injs.append(Well_Design(name='IRK036',alias=['IRK036_G','IRK036_W']))
injs.append(Well_Design(name='IRK049',alias=['IRK049_G','IRK049_W']))
injs.append(Well_Design(name='IRK050',alias=['IRK050_G','IRK050_W']))
injs.append(Well_Design(name='IRK056',alias=['IRK056_G','IRK056_W']))
injs.append(Well_Design(name='IRK063',alias=['IRK063_G','IRK063_W']))

sim_folder_group = 'DEFAULT'
sim_folder = 'sim_001'

for well in prds:
    producer_dual_icv(  well.name
                      , well.group
                      , well.operate
                      , well.monitor
                      , well.geometry
                      , well.perf_ff
                      , well.perf_table
                      , well.time_open
                      , well.time_on
                      , well.layerclump
                      , well.icv_operation
                      , well.icv_control_law
                      , setup.LOCAL_ROOT / setup.SIMS_FOLDER / sim_folder_group / sim_folder / 'wells'
                      )
