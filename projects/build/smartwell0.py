import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.misc.icv import Icv


SMART_WELLS = [  'PRK014'
               , 'PRK028'
               , 'PRK045'
               , 'PRK052'
               , 'PRK060'
               , 'PRK061'
               , 'PRK083'
               , 'PRK084'
               , 'PRK085'
              ]


ZONES = ['Z1', 'Z2', 'Z3']


def Icv2OnElapsedTime():
    lst = []
    wildcards = []
    for well in SMART_WELLS:
        for zone in ZONES:
            icv = Icv()
            icv.set_layer('{}_{}'.format(well, zone))
            icv.add_stage('ICV_{}_{}_S0'.format(well, zone), 0.0)

            from src.astk.triggerobject_onelapsed import OnElapsed
            trigger_obj = OnElapsed()
            wildcard = '#CLOSETIME_{}_{}#'.format(well, zone)
            trigger_obj.set_condition('*TIMSIM', '>', wildcard)
            wildcards.append(wildcard)

            icv.add_trigger_rule('ICV_{}_{}_S0'.format(well, zone), trigger_obj)
            lst.append(icv())

    with open('output/ICV2ONELAPSEDTIMETRIGGERS.txt', 'w') as fh:
        fh.write('\n'.join(lst))

    with open('output/ICV2ONELAPSEDTIMEWILDCARDS.txt', 'w') as fh:
        fh.write('\n'.join(wildcards))



def MultiPositIcvOnCrtllump(positions, tracked_measure):
    lst = []
    wildcards = []
    for well in SMART_WELLS:
        for zone in ZONES:
            icv = Icv()
            layer = '{}_{}'.format(well, zone)
            icv.set_layer(layer)
            for idx, position in enumerate(reversed(positions)):
                position_name = 'ICV_{}_{}_S{}'.format(well, zone, idx+1)
                icv.add_stage(position_name, position)

                from src.astk.triggerobject_onctrllump import OnCtrllump
                trigger_obj = OnCtrllump().set_layerclump_name(layer)
                wildcard = '#CLOSE_{}_{}_{}_S{}#'.format(tracked_measure.strip('*') ,well, zone, idx+1)
                trigger_obj.set_condition(tracked_measure, '>', wildcard)
                wildcards.append(wildcard)

                icv.add_trigger_rule(position_name, trigger_obj)
            lst.append(icv())


    with open('./output/ICV{}ONCRTLLUMP{}TRIGGERS.txt'.format(len(positions), tracked_measure.strip('*')), 'w') as fh:
        fh.write('\n'.join(lst))

    with open('./output/ICV{}ONCRTLLUMP{}WILDCARDS.txt'.format(len(positions), tracked_measure.strip('*')), 'w') as fh:
        fh.write('\n'.join(wildcards))
 

if __name__ == '__main__':
    positions = [0.0, 0.25, 0.50, 0.75, 1.0]

    MultiPositIcvOnCrtllump(positions=positions, tracked_measure='*GOR')
