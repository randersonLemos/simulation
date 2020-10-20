import copy
import matplotlib.pyplot as plt
from collections.abc import Iterable
import numpy as np
import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.misc.icv import Icv

SMART_WELLS = \
[
'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18'
]

ZONES = ['Z1', 'Z2', 'Z3']

class Exp:
    def __init__(self, xi, xf, scaler=1.0):
        self.xi = xi
        self.xf = xf
        self.scaler = scaler

    def rate(self):
        return np.exp((np.log(0.01))/((self.xf-self.xi))) - 1.0

    def comp(self, arr):
        y =  (1 + self.rate())**((arr-self.xi)/self.scaler)
        idx, _ = self.find_nearest(arr, self.xi)
        y[:idx+1] = 1.0
        idx, _ = self.find_nearest(arr, self.xf)
        y[idx:] = 0.0
        return y

    def comp_inv(self, ys):
        if not isinstance(ys, Iterable):
            ys = np.asarray(y)

        lst = []
        for y in ys:
            arr = np.linspace(self.xi, self.xf, 1000)
            yys = self.comp(arr)
            idx, _ = self.find_nearest(yys, y)
            lst.append(arr[idx])
        return np.asarray(lst)

    def find_nearest(self, arr, value):
        arr = np.asarray(arr)
        idx = (np.abs(arr - value)).argmin()
        return idx, arr[idx]

def plot():
    COLORS = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', ]


    N_POSITIONS = [3, 4, 5, 6]

    exp250 = Exp(250, 1000, 1.0)
    exp500 = Exp(500, 1000, 1.0)
    exp750 = Exp(750, 1000, 1.0)
    EXP = [exp250, exp500, exp750]

    arr = np.linspace(200,1050,50)

    plot = []

    for n_positions in N_POSITIONS:
        fig, ax = plt.subplots(1,1,figsize=(10,5), tight_layout=True)
        plot.append((fig, ax, ))
        positions = np.linspace(0.0, 1.0, n_positions)
        lst = []
        for exp in EXP:
            for position in positions:
                lst.append((int(exp.comp_inv(position)), position, ))
            ys = exp.comp(arr)
            ax.plot(arr, ys)
        xs, ys = zip(*lst)
        ax.set_xticks(xs)
        ax.set_yticks(ys)
        ax.tick_params(axis='x', rotation=90)
        ax.grid()
        ax.set_xlabel('GOR')
        ax.set_ylabel('Opening degree')
        ax.set_title('Multi-position ICV w/ {} stages'.format(n_positions))

        lst = list(reversed(lst))
        rg = list(reversed(range(len(lst))))
        colors = list(reversed(copy.copy(COLORS)))
        while rg:
            idx = rg.pop()
            if idx%n_positions == 0:
                color = colors.pop()
            ax.get_xticklabels()[idx].set_color(color)
        ax.get_xticklabels()[idx-n_positions+1].set_color('black')

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

                from simulation.astk.triggerobject_onctrllump import OnCtrllump
                trigger_obj = OnCtrllump().set_layerclump_name(layer)
                wildcard = '#CLOSE{}_{}_{}_S{}#'.format(tracked_measure.strip('*') ,well, zone, idx+1)
                trigger_obj.set_condition(tracked_measure, '>', wildcard)
                wildcards.append(wildcard)

                icv.add_trigger_rule(position_name, trigger_obj)
            lst.append(icv())


    with open('./output/ICV{}ONCRTLLUMP{}TRIGGERS.txt'.format(len(positions), tracked_measure.strip('*')), 'w') as fh:
        fh.write('\n'.join(lst))

    with open('./output/ICV{}ONCRTLLUMP{}WILDCARDS.txt'.format(len(positions), tracked_measure.strip('*')), 'w') as fh:
        fh.write('\n'.join(wildcards))



if __name__ == '__main__':
    positions = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

    MultiPositIcvOnCrtllump(positions=positions, tracked_measure='*GOR')

    #exps = {}
    #exps['exp500'] = Exp(500, 1000, 1.0)
    #exps['exp750'] = Exp(750, 1000, 1.0)

    #dic = {}
    #n_positions = 6
    #positions = np.linspace(0.0, 1.0, n_positions)
    #for key in exps:
    #    lst = []
    #    for position in positions:
    #        lst.append((int(exps[key].comp_inv(position)), position, ))
    #    dic[key] = lst


    gorfs = {}
    with open('/media/pamonha/DATA/DRIVE/simulation/tests/smartwell/output/ICV_GOR.txt', 'r') as fh:
        fh.readline()
        for line in fh:
            zone, gor = line.strip().split('\t')
            gorfs[zone] = int(gor)

    gors = {}
    with open('/media/pamonha/DATA/DRIVE/simulation/tests/smartwell/output/ICV6ONCRTLLUMPGORWILDCARDS.txt', 'r') as fh:
        for key, gorf in gorfs.items():
            gori = 0.5*gorf
            exp = Exp(gori, gorf)
            _gors = exp.comp_inv(positions)
            wildcards = []
            for _ in enumerate(_gors):
                wildcards.append('{}'.format(fh.readline().strip()))

            wildcards = reversed(wildcards)
            gors[key] = list(reversed(list(zip(wildcards, positions, _gors))))


    with open('/media/pamonha/DATA/DRIVE/simulation/tests/smartwell/output/ICV6ONCRTLLUMPGORTRIGGERS.txt', 'r') as fh:
        document = fh.read()

    for key, lst in gors.items():
        for wildcard, openn, gor in lst:
            document = document.replace(wildcard, str(gor))

    with open('./output/EXP50%ClOSE.txt', 'w') as fh:
        fh.write(document)


    with open('./output/EXP50%ClOSEVALUES.txt', 'w') as fh:
        for key, lst in gors.items():
            fh.write(key); fh.write('\n')
            for tup in lst:
                fh.write(str(tup)), fh.write('\n')
