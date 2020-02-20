# -*- coding: utf-8 -*-
import pathlib
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import setup
from simulation.common.words import Words as wrd
from simulation.input.well_design import Well_Design
from simulation.model.well.producer import Producer
from simulation.model.well.injector import Injector
from simulation.model.well.builder.builder_producer_icv import Builder_Producer_Icv
from simulation.model.well.builder.builder_injector_wag import Builder_Injector_Wag
from simulation.model.dat.builder_dat import Builder_Dat

MARK_SIMTIME  = '$#@SIMTIME@#$'

Builder_Dat.set_frameRoot('./frame')

Well_Design.set_inputRoot('./input')
Producer.set_builder(Builder_Producer_Icv)
Injector.set_builder(Builder_Injector_Wag)

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
for wd in prds: Producer(wd).write('./out/wells')

injs = []
injs.append(Well_Design(name='IRK004',alias={'G': 'IRK004_G', 'W': 'IRK004_W'}))
injs.append(Well_Design(name='IRK028',alias={'G': 'IRK028_G', 'W': 'IRK028_W'}))
injs.append(Well_Design(name='IRK029',alias={'G': 'IRK029_G', 'W': 'IRK029_W'}))
injs.append(Well_Design(name='IRK036',alias={'G': 'IRK036_G', 'W': 'IRK036_W'}))
injs.append(Well_Design(name='IRK049',alias={'G': 'IRK049_G', 'W': 'IRK049_W'}))
injs.append(Well_Design(name='IRK050',alias={'G': 'IRK050_G', 'W': 'IRK050_W'}))
injs.append(Well_Design(name='IRK056',alias={'G': 'IRK056_G', 'W': 'IRK056_W'}))
injs.append(Well_Design(name='IRK063',alias={'G': 'IRK063_G', 'W': 'IRK063_W'}))
for wd in injs: Injector(wd).write('./out/wells')

bd = Builder_Dat()
bd.replace_mark(MARK_SIMTIME, 'I am here!!!')
bd.write('./out')
