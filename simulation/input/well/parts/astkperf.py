from simulation.common.words import Words as Wd
from simulation.common.keywords import Keywords as Kw
import numpy as np

class AstkPerf:
    def __init__(self):
        self._well_name = ''
        self._connection = ''
        self._index_keys = []
        self._lst = []
        self._dual_mode = False

    def set_dual_mode(self):
        self._dual_mode = True
        return self

    def set_well_name(self, name):
        self._well_name = "'" + name + "'"
        return self

    def set_index_keys(self, *args):
        self._index_keys = args
        return self

    def set_connection(self, connection):
        self._connection = connection
        return self

    def add(self, location, index_values, more):
        if not isinstance(location, tuple) \
            or not isinstance(index_values, tuple):
            raise TypeError('Not allowed type...')
        self._lst.append((location, index_values, more, ))

    def fill(self):
        lst = []
        for tail, head in zip(self._lst[:-1], self._lst[1:]):

            init = np.array(tail[0])
            goal = np.array(head[0])

            vec = ((goal - init) / np.linalg.norm(goal - init)).astype(int)

            lst.append(tail)
            init += vec
            while (init != goal).any():
                lst.append((tuple(init), tail[1], '*OPEN', ))
                init += vec
        lst.append(head)
        self._lst = lst

    def repr(self):
        if self._dual_mode:
            return self._repr_dual_mode()
        return self._repr()

    def _repr(self):
        pass

    def _repr_dual_mode(self):
        lst = []
        lst.append('{} {} {}'.format(Kw.perf(), ' '.join(self._index_keys), self._well_name))

        for idx, line in enumerate(self._lst):
            uba = '{:02d} {:02d} {:02d}'.format(*line[0])
            index_values = ' '.join(map(str, line[1]))
            status = line[2]

            if idx == 0:
                stg ='{} {} {} {} {} {} {}'.format(uba, Kw.mt(), index_values, status, self._connection , Wd.surface(), Kw.reflayer())
                lst.append(stg)
                stg = '{} {} {} {} {}'.format(uba, Kw.fr(), index_values, status, self._connection)
                lst.append(stg)
            else:
                stg = '{} {} {} {} {} {}'.format(uba, Kw.mt(), index_values, status, self._connection, '{:02d}'.format(idx))
                lst.append(stg)
                stg = '{} {} {} {} {} {}'.format(uba, Kw.fr(), index_values, status, self._connection, '{:02d}'.format(idx))
                lst.append(stg)
        return '\n'.join(lst)

