from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from simulation.common.keywords import Keywords as Kw
from simulation.input.well.parts.astkwell import AstkWell
from simulation.input.well.parts.astkproducer import AstkProducer
from simulation.input.well.parts.astkoperate import AstkOperate
from simulation.input.well.parts.astkmonitor import AstkMonitor
from simulation.input.well.parts.astkgeometry import AstkGeometry
from simulation.input.well.parts.astkperf import AstkPerf
from simulation.input.well.parts.astkopen import AstkOpen
from simulation.input.well.parts.astkshutin import AstkShutin
from simulation.input.well.parts.astkontime import AstkOntime

astkwell = AstkWell().set_name('PRK014').set_group('PRODUCTION')
astkproducer = AstkProducer().set_well_name('PRK014')
astkoperate = AstkOperate().add('*MAX *STL', 3000.0, '*CONT *REPEAT').add('*MIN *BHP',  295.0, '*CONT *REPEAT')
astkmonitor = AstkMonitor().add('*WCUT', 0.95, '*SHUTIN').add('*GOR', 1200.0, '*SHUTIN')
astkgeometry = AstkGeometry().set_dir('*K').set_rw(0.108).set_geofac(0.370).set_wfrac(1.0).set_skin(0.0)
astkperf = AstkPerf(dual_mode_on=True).set_well_name('PRK014').set_index_keys('*GEOA')
astkperf.set_default_status('*OPEN')
astkperf.set_default_connection('*FLOW-TO')
astkperf.set_default_index_values((1.0, ))
astkperf.add_completion((25, 10,  1, ))
astkperf.add_completion((25, 10, 13, ), status='*CLOSED')
astkperf.add_completion((25, 10, 20, ), status='*CLOSED')
astkperf.add_completion((25, 10, 30, ))
astkperf.fill()
astkopen = AstkOpen().set_well_name('PRK014')
astkshutin = AstkShutin().set_well_name('PRK014')
astkontime = AstkOntime().set_well_name('PRK014').set_on_time(1.0)



#from simulation.input.well.parts.name import Name
#from simulation.input.well.parts.group import Group
#from simulation.input.well.parts.producer import Producer
#from simulation.input.well.parts.operate import Operate
#from simulation.input.well.parts.monitor import Monitor
#from simulation.input.well.parts.geometry import Geometry
#from simulation.input.well.parts.perf import Perf
#from simulation.input.well.parts.on_time import On_Time
#from simulation.input.well.parts.layerclump import Layerclump
#from simulation.input.well.parts.trigger import Trigger
#from simulation.input.well.parts.on_elapsed import On_Elapsed
#from simulation.input.well.parts.on_ctrllump import On_Ctrllump
#from simulation.input.well.parts.andd import AND
#from simulation.input.well.parts.orr import OR
#from simulation.input.well.parts.on_elapsed_treltd import Treltd
#from simulation.input.well.parts.clumpsetting import Clumpsetting
#from simulation.input.well.design_producer_dual_icv import Design_Producer_Dual_Icv
#from simulation.builder.well.producer_dual_icv import Producer_Dual_Icv

#design = Design_Producer_Dual_Icv()
#name = 'PRK014'
#design.set_name(name)
#design.set_group(Group('PRODUCER'))
#operate = Operate()
#operate.add('*MAX *STL', 3000.0, '*CONT *REPEAT')
#operate.add('*MIN *BHP',  295.0, '*CONT *REPEAT')
#design.set_operate(operate)
#monitor = Monitor()
#monitor.add('*WCUT', 0.95, '*SHUTIN')
#monitor.add('*GOR', 1200.0, '*SHUTIN')
#design.set_monitor(monitor)
#design.set_geometry(Geometry('*K', 0.108, 0.370, 1.000, 0.000))
#perf = Perf('*GEOA')
#perf.add(25, 10,  1, 1.0, '*OPEN')
#perf.add(25, 10, 13, 1.0, '*CLOSED')
#perf.add(25, 10, 20, 1.0, '*CLOSED')
#perf.add(25, 10, 30, 1.0, '*OPEN')
#design.set_perf(perf)
#design.set_on_time(On_Time(1.0))
#layerclump = Layerclump(base_name_mode=True)
#layerclump.set_base_name('{}_Z'.format(name))
#layerclump.add(25, 10, ( 1,12,))
#layerclump.add(25, 10, (14,19,))
#layerclump.add(25, 10, (21,30,))
#design.set_layerclump(layerclump)

#On_Elapsed.set_default_increment(183)
#on_elapsed = On_Elapsed(Treltd(999))
#on_elapsed.set_avrgtime(10)
#
#clumpsetting = Clumpsetting()
#clumpsetting.set_value(0.0)
#clumpsetting.set_layerclump_name(Name('Cawesome'))
#
#Trigger.set_default_test_times(1)
#Trigger.set_default_apply_times(200)
#
#trigger = Trigger()
#trigger.set_name(Name('Tawesome'))
#trigger.add_stat(on_elapsed)
#trigger.add_stat(OR())
#trigger.add_stat(on_elapsed)
#trigger.add_action(clumpsetting)
#trigger.add_action(clumpsetting)
#trigger.add_action(clumpsetting)
#
#trigger2 = Trigger()
#trigger2.set_name(Name('T2awesome'))
#trigger2.add_stat(on_elapsed)
#trigger2.add_stat(OR())
#trigger2.add_stat(on_elapsed)
#trigger2.add_action(trigger)
#
#print(trigger.repr())
#print(trigger2.repr())

#design.set_trigger(trigger)
#PRK014 = Producer_Dual_Icv(design)