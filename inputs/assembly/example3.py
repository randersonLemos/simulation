CON_INJ01 = '''
31 06 01 1.0 *OPEN
31 06 02 1.0 *OPEN
31 06 03 1.0 *OPEN
31 06 04 1.0 *OPEN
31 06 05 1.0 *OPEN
31 06 06 1.0 *OPEN
31 06 07 1.0 *OPEN
31 06 08 1.0 *OPEN
31 06 09 1.0 *OPEN
31 06 10 1.0 *OPEN
31 06 11 1.0 *OPEN
31 06 12 1.0 *OPEN
31 06 13 1.0 *OPEN
31 06 14 1.0 *OPEN
31 06 15 1.0 *CLOSED
31 06 16 1.0 *CLOSED
31 06 17 1.0 *OPEN
31 06 18 1.0 *OPEN
31 06 19 1.0 *OPEN
31 06 20 1.0 *OPEN
31 06 21 1.0 *OPEN
31 06 22 1.0 *OPEN
31 06 23 1.0 *OPEN
31 06 24 1.0 *OPEN
31 06 25 1.0 *OPEN
31 06 26 1.0 *OPEN
31 06 27 1.0 *OPEN
31 06 28 1.0 *OPEN
31 06 29 1.0 *OPEN
31 06 30 1.0 *OPEN
'''

CON_INJ02 = '''
41 30 01 1.0 *OPEN
41 30 02 1.0 *OPEN
41 30 03 1.0 *OPEN
41 30 04 1.0 *OPEN
41 30 05 1.0 *OPEN
41 30 06 1.0 *OPEN
41 30 07 1.0 *OPEN
41 30 08 1.0 *OPEN
41 30 09 1.0 *OPEN
41 30 10 1.0 *OPEN
41 30 11 1.0 *OPEN
41 30 12 1.0 *OPEN
41 30 13 1.0 *OPEN
41 30 14 1.0 *OPEN
41 30 15 1.0 *CLOSED
41 30 16 1.0 *CLOSED
41 30 17 1.0 *OPEN
41 30 18 1.0 *OPEN
41 30 19 1.0 *OPEN
41 30 20 1.0 *OPEN
41 30 21 1.0 *OPEN
41 30 22 1.0 *OPEN
41 30 23 1.0 *OPEN
41 30 24 1.0 *OPEN
41 30 25 1.0 *OPEN
41 30 26 1.0 *OPEN
41 30 27 1.0 *OPEN
41 30 28 1.0 *OPEN
41 30 29 1.0 *OPEN
41 30 30 1.0 *OPEN
'''

WELL_LST = ['INJ01', 'INJ02']

COMPLETION_DIC = {'INJ01':CON_INJ01,'INJ02':CON_INJ02}

ON_TIME_DIC = {'INJ01':1.0,'INJ02':0.75}

OPEN_DIC = {'INJ01':('W', 100), 'INJ02': ('G',150)}

LAYERCLUMP_DIC = {}
LAYERCLUMP_DIC['INJ01'] = ['31 06 01:14','31 06 17:30']
LAYERCLUMP_DIC['INJ02'] = ['41 30 01:14','41 30 17:30']

WAG_START_DIC = {}
WAG_START_DIC['INJ01'] = ('W', 300, 25, 200)
WAG_START_DIC['INJ02'] = ('G', 300, 25, 200)

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from assembly.scripts.injector_dual_wag import injector_dual_wag
    from dictionary.scripts.dictionary import Keywords as kw

    cont_repeat = '{} {}'.format(kw.cont(), kw.repeat())

    operate = []
    operate.append(('G', kw.max(), kw.stg(), 3000000.0, cont_repeat))
    operate.append(('G', kw.max(), kw.bhp(),     540.0, cont_repeat))
    operate.append(('W', kw.max(), kw.stw(),    5000.0, cont_repeat))
    operate.append(('W', kw.max(), kw.bhp(),     470.0, cont_repeat))

    monitor = []

    geometry = (kw.k(),0.108,0.370,1.0,0.0)
    perf = kw.geoa()

    for well in WELL_LST:
        completion = [tuple(line.split()) for line in COMPLETION_DIC[well].strip().splitlines()]

        injector_dual_wag(well, 'INJECTION', operate, monitor, geometry
                , perf, completion, OPEN_DIC[well],ON_TIME_DIC[well]
                , WAG_START_DIC[well], LAYERCLUMP_DIC[well]
                , './wells/injector_dual_wag')
