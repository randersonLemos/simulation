from collections.abc import Iterable
from simulation.common.words import Words as Wd
from simulation.common.keywords import Keywords as Kw
import numpy as np

class AstkPerf:
    def __init__(self, dual_mode_on=False):
        self._dual_mode = dual_mode_on
        self._well_name = ''
        self._connection = ''
        self._index_keys = []
        self._lst = []

        self._default_rel_perm = -1
        self._default_status = ''
        self._default_connection = ''
        self._default_index_values = []

    def set_well_name(self, name):
        self._well_name = "'" + name + "'"
        return self

    def set_index_keys(self, *args):
        self._index_keys = args
        return self

    def set_default_connection(self, default):
        self._default_connection = default

    def set_default_status(self, default):
        self._default_status = default

    def set_default_rel_perm(self, default):
        self._default_rel_perm = default

    def set_default_index_values(self, default):
        if not isinstance(default, Iterable):
            raise TypeError('Not allowed type...')

        if len(default) != len(self._index_keys):
            raise ValueError('Must be of same size...')

        self._default_index_values = default

    def add_completion(self, location, index_values = [], rel_perm=-1, status='', connection=''):
        if index_values == []:
            index_values = self._default_index_values

        if rel_perm == -1:
            rel_perm = self._default_rel_perm

        if status == '':
            status = self._default_status

        if connection == '':
            connection = self._default_connection

        if not isinstance(location, Iterable):
            raise TypeError('Not allowed type...')

        if not isinstance(index_values, Iterable):
            raise TypeError('Not allowed type...')

        if len(index_values) != len(self._index_keys):
            raise ValueError('Must be of same size...')

        self._lst.append((location, index_values, rel_perm, status, connection, ))

    def fill(self):
        lst = []
        for tail, head in zip(self._lst[:-1], self._lst[1:]):

            init = np.array(tail[0])
            goal = np.array(head[0])

            vec = ((goal - init) / np.linalg.norm(goal - init)).astype(int)

            lst.append((tuple(init), tail[1], tail[2], tail[3], tail[4], ))
            init += vec
            while (init != goal).any():
                lst.append((tuple(init), self._default_index_values, self._default_rel_perm, self._default_status, self._default_connection, ))
                init += vec
        lst.append(head)
        self._lst = lst

    def __call__(self):
        if self._dual_mode:
            return self._repr_dual_mode()
        return self._repr_single_mode()

    def _repr_single_mode(self):
        raise NotImplementedError('Not implemented...')

    def _repr_dual_mode(self):
        lst = []
        lst.append('{} {} {}'.format(Kw.perf(), ' '.join(self._index_keys), self._well_name))

        for idx, completion in enumerate(self._lst):
            stg = ''
            uba = '{:02d} {:02d} {:02d}'.format(*completion[0])
            stg += uba

            stg += ' {}'.format(Kw.mt())

            index_values = []
            for index_value in completion[1]:
                index_values.append('{:.4f}'.format(index_value))
            index_values = ' '.join(index_values)
            if index_values:
                stg += ' {}'.format(index_values)

            rel_perm = completion[2]
            if rel_perm != -1:
                stg += ' {:.4f}'.format(rel_perm)

            status = completion[3]
            if status:
                stg += ' {}'.format(status)

            connection = completion[4]
            if connection:
                stg += ' {}'.format(connection)

            if idx == 0:
                stg += ' {} {}'.format(Wd.surface(), Kw.reflayer())
                lst.append(stg)
                stg = stg.replace(Kw.mt(), Kw.fr())
                stg = stg.replace('{} {}'.format(Wd.surface(), Kw.reflayer()), '')
                lst.append(stg)
            else:
                stg += ' {:02d}'.format(idx)
                lst.append(stg)
                stg = stg.replace(Kw.mt(), Kw.fr())
                lst.append(stg)
        return '\n'.join(lst)

