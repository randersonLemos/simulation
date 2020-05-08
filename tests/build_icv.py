import os
os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.input.well.parts.astktrigger import AstkTrigger
from simulation.input.well.parts.triggerobject_onctrllump import OnCtrllump
from simulation.input.well.parts.triggerobject_onelapsed import OnElapsed
from simulation.input.well.parts.clumpsetting import Clumpsetting

AstkTrigger.set_default_test_times(1)
astktrigger = AstkTrigger()
astktrigger.set_name('ICV_PRK014_Z1')

OnCtrllump.set_default_increment('100')
OnCtrllump.set_default_avrgtime('180')

onctrllump = OnCtrllump()
onctrllump.set_layerclump_name('PRK014_Z1').set_condition('*GOR', '>', 1000)

astktrigger.add_trigger_obj(onctrllump)
astktrigger.add_action('Hello World')

astktrigger2 = AstkTrigger()
astktrigger2.set_name('CLOSE_IN_TIME')

OnElapsed.set_default_increment('100')
OnElapsed.set_default_avrgtime('180')

onelapsed = OnElapsed()
onelapsed.set_condition('*TIMSIM', '>', '1000')

astktrigger2.add_trigger_obj(onelapsed)
astktrigger2.add_action(astktrigger)
