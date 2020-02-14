CON_INJ01 = '''
25 10 01 1.0 *OPEN
25 10 02 1.0 *OPEN
25 10 03 1.0 *OPEN
25 10 04 1.0 *OPEN
25 10 05 1.0 *OPEN
25 10 06 1.0 *OPEN
25 10 07 1.0 *OPEN
25 10 08 1.0 *OPEN
25 10 09 1.0 *OPEN
25 10 10 1.0 *OPEN
25 10 11 1.0 *OPEN
25 10 12 1.0 *CLOSED
25 10 13 1.0 *CLOSED
25 10 14 1.0 *OPEN
25 10 15 1.0 *OPEN
25 10 16 1.0 *OPEN
25 10 17 1.0 *OPEN
25 10 18 1.0 *OPEN
25 10 19 1.0 *OPEN
25 10 20 1.0 *CLOSED
25 10 21 1.0 *CLOSED
25 10 22 1.0 *OPEN
25 10 23 1.0 *OPEN
25 10 24 1.0 *OPEN
25 10 25 1.0 *OPEN
25 10 26 1.0 *OPEN
25 10 27 1.0 *OPEN
25 10 28 1.0 *OPEN
25 10 29 1.0 *OPEN
25 10 30 1.0 *OPEN
'''

CON_INJ02 = '''
23 17 01 1.0 *OPEN
23 17 02 1.0 *OPEN
23 17 03 1.0 *OPEN
23 17 04 1.0 *OPEN
23 17 05 1.0 *OPEN
23 17 06 1.0 *OPEN
23 17 07 1.0 *OPEN
23 17 08 1.0 *OPEN
23 17 09 1.0 *OPEN
23 17 10 1.0 *OPEN
23 17 11 1.0 *OPEN
23 17 12 1.0 *OPEN
23 17 13 1.0 *OPEN
23 17 14 1.0 *OPEN
23 17 15 1.0 *OPEN
23 17 16 1.0 *OPEN
23 17 17 1.0 *OPEN
23 17 18 1.0 *OPEN
23 17 19 1.0 *CLOSED
23 17 20 1.0 *CLOSED
23 17 21 1.0 *OPEN
23 17 22 1.0 *OPEN
23 17 23 1.0 *OPEN
23 17 24 1.0 *OPEN
23 17 25 1.0 *OPEN
23 17 26 1.0 *OPEN
23 17 27 1.0 *OPEN
23 17 28 1.0 *OPEN
23 17 29 1.0 *OPEN
23 17 30 1.0 *OPEN
'''

WELL_LST = ['INJ01', 'INJ02']

COMPLETION_DIC = {'INJ01':CON_INJ01,'INJ02':CON_INJ02}

ON_TIME_DIC = {'INJ01':1.0,'INJ02':0.75}

OPEN_DIC = {'INJ01':100, 'INJ02': 150}

LAYERCLUMP_DIC = {}
LAYERCLUMP_DIC['INJ01'] = ['25 10 01:11','25 10 14:19','25 10 22:30']
LAYERCLUMP_DIC['INJ02'] = ['23 17 01:18','23 17 21:30']

ICV_NR_DIC = {'INJ01':3,'INJ02':2}

ICV_START_DIC = {}
ICV_START_DIC['INJ01'] = (300, 25, 200)
ICV_START_DIC['INJ02'] = (300, 25, 200)

ICV_CONTROL_DIC = {}
ICV_CONTROL_DIC['INJ01'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*ICV_NR_DIC['INJ01']
ICV_CONTROL_DIC['INJ02'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.70',0.0))]*ICV_NR_DIC['INJ02']

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from assembly.scripts.injector_dual_icv import injector_dual_icv
    from dictionary.scripts.dictionary import Keywords as kw

    cont_repeat = '{} {}'.format(kw.cont(), kw.repeat())

    operate = []
    operate.append((kw.max(), kw.stw(), 5000.0, cont_repeat))
    operate.append((kw.max(), kw.bhp(),  470.0, cont_repeat))

    monitor = []

    geometry = (kw.k(),0.108,0.370,1.0,0.0)
    perf = kw.geoa()

    for well in WELL_LST:
        completion = [tuple(line.split()) for line in COMPLETION_DIC[well].strip().splitlines()]

        injector_dual_icv(well, 'INJECTION', kw.water(), operate, monitor,
                geometry, perf, completion, OPEN_DIC[well],
                ON_TIME_DIC[well], LAYERCLUMP_DIC[well], ICV_START_DIC[well],
                ICV_CONTROL_DIC[well], './wells/injector_dual_icv')
