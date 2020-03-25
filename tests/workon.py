import pathlib
import numpy as np
import matplotlib.pyplot as plt
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from simulation.input.well.parts.name import Name
from simulation.input.well.parts.group import Group
from simulation.input.well.parts.producer import Producer
from simulation.input.well.parts.operate import Operate
from simulation.input.well.parts.monitor import Monitor
from simulation.input.well.parts.geometry import Geometry
from simulation.input.well.parts.perf import Perf
from simulation.input.well.parts.on_time import On_Time
from simulation.input.well.parts.layerclump import Layerclump
from simulation.input.well.parts.trigger import Trigger
from simulation.input.well.parts.on_elapsed import On_Elapsed
from simulation.input.well.parts.andd import AND
from simulation.input.well.parts.orr import OR
from simulation.input.well.parts.treltd import Treltd
from simulation.input.well.parts.clumpsetting import Clumpsetting
from simulation.input.well.design_producer_dual_icv import Design_Producer_Dual_Icv
from simulation.builder.well.producer_dual_icv import Producer_Dual_Icv

design = Design_Producer_Dual_Icv()
name = Name('PRK014')
design.set_name(name)
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
design.set_perf(perf)
design.set_on_time(On_Time(1.0))
layerclump = Layerclump(base_name_mode=True)
layerclump.set_base_name('{}_Z'.format(name()))
layerclump.add(25, 10, ( 1,12,))
layerclump.add(25, 10, (14,19,))
layerclump.add(25, 10, (21,30,))
design.set_layerclump(layerclump)

On_Elapsed.set_default_increment(183)
on_elapsed = On_Elapsed(Treltd(999))
on_elapsed.set_avrgtime(10)

clumpsetting = Clumpsetting()
clumpsetting.set_value(0.0)
clumpsetting.set_layerclump_name('Cawesome')

Trigger.set_default_test_times(1)
Trigger.set_default_apply_times(200)

trigger = Trigger()
trigger.set_name('Tawesome')
trigger.add_stat(on_elapsed)
trigger.add_stat(OR())
trigger.add_stat(on_elapsed)
trigger.add_action(clumpsetting)
design.set_trigger(trigger)

PRK014 = Producer_Dual_Icv(design)
print(PRK014)