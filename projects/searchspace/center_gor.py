import numpy
import copy

class Interval_Handle:
    def __init__(self, ini, end, n_int):
        self.ini = ini
        self.end = end
        self.n_int = n_int

        self.lst = []
        self.lst_ext = []

        self._intervals()

    def _intervals(self):
        incr = (self.end - self.ini) / self.n_int
        curr = self.ini
        for i in range(self.n_int):
            self.lst.append(int(curr + incr/2.0))
            self.lst_ext.append(int(curr))
            self.lst_ext.append(int(curr + incr/2.0))
            curr += incr
        self.lst_ext.append(int(curr))

    def new_intervals(self, value):
        idx = self.lst_ext.index(value)
        if idx == 0:
            ini = self.lst_ext[0]
            end = self.lst_ext[1]
        elif idx == len(self.lst_ext) - 1:
            ini = self.lst_ext[-2]
            end = self.lst_ext[-1]
        else:
            ini = self.lst_ext[idx-1]
            end = self.lst_ext[idx+1]

        other = copy.deepcopy(self)
        other.__init__(ini, end, other.n_int)

        return other

    def __repr__(self):
        stg = ''
        for idx in range(len(self.lst_ext)):
            if idx%2 == 0: stg += str(self.lst_ext[idx]) + ' '
            else: stg += '(' + str(self.lst_ext[idx]) + ') '
        return stg


ih = Interval_Handle(300, 3700, 5)

