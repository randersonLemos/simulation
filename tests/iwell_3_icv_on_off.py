import os
os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.input.well.parts.name import Name
from simulation.input.well.parts.trigger import Trigger
from simulation.input.well.parts.on_ctrllump_gor import GOR
from simulation.input.well.parts.on_ctrllump import On_Ctrllump
from simulation.input.well.parts.clumpsetting import Clumpsetting

class OTMIW3ICV:
    def __init__(self, name):

        self.name = name
        self.Layerclump_name = []
        self.Otm_wildcat = []
        self.Trigger = []

        for layerclump_name in ['{}_Z{}'.format(self.name, i+1) for i in range(3)]:
            self.Layerclump_name.append(layerclump_name)
            on_ctrllump = On_Ctrllump()
            wildcat = '#{}_GOR#'.format(layerclump_name)
            self.Otm_wildcat.append(wildcat)
            on_ctrllump.set_condition(GOR(wildcat))
            on_ctrllump.set_layerclump_name(layerclump_name)


            clumpsetting = Clumpsetting()
            clumpsetting.set_layerclump_name(layerclump_name)
            clumpsetting.set_value(0.0)

            Trigger.set_default_test_times(1)
            trigger = Trigger()
            trigger.set_name('ICV_{}'.format(layerclump_name))
            trigger.add_stat(on_ctrllump)
            trigger.add_action(clumpsetting)

            self.Trigger.append(trigger)

    def repr(self):
        return '\n'.join([trigger.repr() for trigger in self.Trigger])


Name = ['PRK014', 'PRK028', 'PRK045', 'PRK052', 'PRK060', 'PRK061', 'PRK083',
        'PRK084', 'PRK085']
Iw = []
for name in Name:
    Iw.append(OTMIW3ICV(name))

Wildcat = []
for iw in Iw:
    for wildcat in iw.Otm_wildcat:
        Wildcat.append('{} INT [1500]'.format(wildcat.strip('#')))

with open('OTMWILDCAT.txt', 'w') as fh:
    for wildcat in Wildcat:
        fh.write(wildcat)
        fh.write('\n')

with open('OTMIW3IV2.txt', 'w') as fh:
    for iw in Iw:
        fh.write('** '+ '*'*5 + iw.name + '*'*5 + '\n')
        fh.write(iw.repr())
        fh.write('\n')
