import pathlib
import numpy as np
import matplotlib.pyplot as plt
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from simulation.input.parts.name import Name
from simulation.input.parts.group import Group
from simulation.input.parts.operate import Operate
from simulation.input.parts.monitor import Monitor
from simulation.input.parts.geometry import Geometry
from simulation.input.parts.perf import Perf
from simulation.input.design_producer_dual_icv import Design_Producer_Dual_Icv
from simulation.builder.well.producer_dual_icv import Producer_Dual_Icv

design = Design_Producer_Dual_Icv()
design.set_name(Name('PRK014'))
design.set_group(Group('PRODUCER'))
operate = Operate()
operate.add('*MAX *STL', 3000.0, '*CONT *REPEAT')
operate.add('*MIN *BHP',  295.0, '*CONT *REPEAT')
design.set_operate(operate)
monitor = Monitor()
monitor.add('*WCUT', 0.95, '*SHUTIN')
monitor.add('*GOR', 1200.0, '*SHUTIN')
design.set_monitor(monitor)
design.set_geometry(Geometry('*K', 0.108, 0.370, 1.000, 0.000))
perf = Perf('*GEOA')
perf.add(25, 10,  1, 1.0, '*OPEN')
perf.add(25, 10, 13, 1.0, '*CLOSED')
perf.add(25, 10, 20, 1.0, '*CLOSED')
perf.add(25, 10, 30, 1.0, '*OPEN')

PRK014 = Producer_Dual_Icv(design)
print(PRK014)