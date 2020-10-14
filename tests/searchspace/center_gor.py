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
            self.lst.append(curr + incr/2.0)
            self.lst_ext.append(curr)
            curr += incr
        self.lst_ext.append(curr)

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
        other.ini = ini
        other.end = end
        other._intervals()
        other._intervals_ext()

        other.lst[0] = ini; other.lst[-1] = end
        other.lst_ext[0] = ini; other.lst_ext[-1] = end
        return other

    #def __repr__(self):
    #    stg = ''
    #    for idx in range(len(self.lst_ext)):
    #        if idx%2 == 0:
    #            stg += str(self.lst_ext[idx]) + ' '
    #        else:
    #            stg += '(' + str(self.lst_ext[idx]) + ') '
    #    return stg


ih = Interval_Handle(300, 3700, 5)
