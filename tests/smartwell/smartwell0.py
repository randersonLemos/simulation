import os
os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.misc.icv import Icv


SMART_WELLS = ['PRK014', 'PRK028', 'PRK045', 'PRK052', 'PRK060', 'PRK061', 'PRK083',
        'PRK084', 'PRK085']


ZONES = ['Z1', 'Z2', 'Z3']


def Icv2OnElapsedTime():
    lst = []
    wildcards = []
    for well in SMART_WELLS:
        for zone in ZONES:
            icv = Icv()
            icv.set_layer('{}_{}'.format(well, zone))
            icv.add_stage('ICV_{}_{}_S0'.format(well, zone), 0.0)

            from simulation.astk.triggerobject_onelapsed import OnElapsed
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



