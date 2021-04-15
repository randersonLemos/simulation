from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.dict.keywords import Keywords as Kw
from src.astk.astkwell import AstkWell
from src.astk.astkproducer import AstkProducer
from src.astk.astkoperate import AstkOperate
from src.astk.astkmonitor import AstkMonitor
from src.astk.astkgeometry import AstkGeometry
from src.astk.astkperf import AstkPerf
from src.astk.astkopen import AstkOpen
from src.astk.astkshutin import AstkShutin
from src.astk.astkontime import AstkOntime
from src.astk.astklayerclump import AstkLayerclump
from src.astk.astklayerclump import AstkLayerclumps

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

astklayerclump = AstkLayerclump(dual_mode_on=True).set_name('PRK014_Z1')
astklayerclump.add_layers('PRK014', '25 10 01:12')
astklayerclump.add_layers('PRK014', '25 10 14:19')
astklayerclump.add_layers('PRK014', '25 10 21:30')

astklayerclumps = AstkLayerclumps(dual_mode_on=True).set_root_name('PRK014').set_suffix_name('_Z')
astklayerclumps.add_layers('PRK014', '25 10 01:12')
astklayerclumps.add_layers('PRK014', '25 10 14:19', new_layerclump=True)
astklayerclumps.add_layers('PRK014', '25 10 21:30', new_layerclump=True)
