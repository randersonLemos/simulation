# -*- coding: utf-8 -*-
MARK_SIMTIME = '$#@SIMTIME@#$'
MARK_IRFFILE = '$#@IRFFILE@#$'

import pathlib
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from simulation import setup
from simulation.common.words import Words as wrd
from simulation.input.well_design import Well_Design
from simulation.model.well.producer import Producer
from simulation.model.well.injector import Injector
from simulation.model.well.builder.builder_producer_icv import Builder_Producer_Icv
from simulation.model.well.builder.builder_injector_wag import Builder_Injector_Wag
from simulation.model.dat.builder_dat import Builder_Dat
from simulation.model.rwd.builder_rwd import Builder_Rwd
from simulation.model.dat.simtime import Simtime
from simulation.run.imex import Imex_Remote
from simulation.run.report import Report

Well_Design.set_inputRoot('./input')
Producer.set_builder(Builder_Producer_Icv)
Injector.set_builder(Builder_Injector_Wag)
Imex_Remote.set_exe(setup.REMOT_IMEX_EXE)
Imex_Remote.set_exe_putty(setup.LOCAL_PUTT_EXE)
Imex_Remote.set_dic_remote_root({'U:': '/home/randerson'})
Imex_Remote.set_user(setup.USER)
Imex_Remote.set_cluster_name(setup.CLUSTER_NAME)
Imex_Remote.set_queue_kind(setup.QUEUE_KIND)
Report.set_exe(setup.LOCAL_REPO_EXE)

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
for wd in prds: Producer(wd).write('./remote/sim/wells')

injs = []
injs.append(Well_Design(name='IRK004',alias={'G': 'IRK004-G', 'W': 'IRK004-W'}))
injs.append(Well_Design(name='IRK028',alias={'G': 'IRK028-G', 'W': 'IRK028-W'}))
injs.append(Well_Design(name='IRK029',alias={'G': 'IRK029-G', 'W': 'IRK029-W'}))
injs.append(Well_Design(name='IRK036',alias={'G': 'IRK036-G', 'W': 'IRK036-W'}))
injs.append(Well_Design(name='IRK049',alias={'G': 'IRK049-G', 'W': 'IRK049-W'}))
injs.append(Well_Design(name='IRK050',alias={'G': 'IRK050-G', 'W': 'IRK050-W'}))
injs.append(Well_Design(name='IRK056',alias={'G': 'IRK056-G', 'W': 'IRK056-W'}))
injs.append(Well_Design(name='IRK063',alias={'G': 'IRK063-G', 'W': 'IRK063-W'}))
for wd in injs: Injector(wd).write('./remote/sim/wells')

st = Simtime((2022, 4, 30), (2023, 12, 31), 2038)

bd = Builder_Dat(frameRoot='./frame', frameFile='main.dat.frame', frameIncludeFolder='include')
bd.replace_mark(MARK_SIMTIME, st.simtime())
bd.write(datRoot='./remote/sim', datFile='main.dat')

imexx = Imex_Remote(
      path_to_dat='U:/simulation/tests/remote/sim/main.dat' 
    , folder_to_output='U:/simulation/tests/remote/sim'                        
    , nr_processors=setup.NR_PROCESSORS            
    , see_log=True
    , verbose=True
    , run=True
)