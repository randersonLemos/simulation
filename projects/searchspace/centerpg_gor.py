import numpy
import copy

class Interval_Handle:
    def __init__(self, ini, end, n_int):
        self.ini = ini
        self.end = end
        self.n_int = n_int

        self._intervals()
        self._intervals_ext()

    def _intervals(self):
        q = numpy.power(self.end/self.ini, 1/self.n_int)
        self.lst = [int(self.ini*q**power) for power in range(self.n_int+1)]
        self.lst[0] = self.ini
        self.lst[-1] = self.end

    def _intervals_ext(self):
        self.lst_ext = []
        self.lst_ext.append(self.lst[0])
        for a,b in zip(self.lst[:-1], self.lst[1:]):
            self.lst_ext.append(int((a+b)/2))
            self.lst_ext.append(b)

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

    def __repr__(self):
        stg = ''
        for idx in range(len(self.lst_ext)):
            if idx%2 == 0:
                stg += str(self.lst_ext[idx]) + ' '
            else:
                stg += '(' + str(self.lst_ext[idx]) + ') '
        return stg


ih = Interval_Handle(300, 3700, 17)
