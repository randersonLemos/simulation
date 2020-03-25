from simulation.common.keywords import Keywords as Kw
from simulation.input.well.parts.name import Name
from simulation.input.well.parts.trigger_object import Trigger_Object

class Trigger:
    _apply_times = 0
    _test_times = 0

    @classmethod
    def set_default_apply_times(cls, apply_times):
        if apply_times > 0:
            cls._apply_times = apply_times
            return
        raise ValueError('Only positive values...')

    @classmethod
    def set_default_test_times(cls, test_times):
        if test_times > 0:
            cls._test_times = test_times
            return
        raise ValueError('Only positive values...')

    def __init__(self):
        self._name = ''
        self._stat = []
        self._act = []

    def stat(self): # statement
        return self._stat

    def add_stat(self, trigger_object):
        if isinstance(trigger_object, Trigger_Object):
            self._stat.append(trigger_object)
            return
        raise TypeError('Not allowed type...')

    def action(self):
        return self._act

    def add_action(self, action):
        self._act.append(action)

    def name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, Name):
            self._name = name
            return
        raise TypeError('Not allowed type...')

    def apply_times(self):
        return self._apply_times

    def set_apply_times(self, apply_times):
        if apply_times > 0:
            self._apply_times = apply_times
            return
        raise ValueError('Only positive values...')

    def test_times(self):
        return self._test_times

    def set_test_times(self, test_times):
        if test_times > 0:
            self._test_times = test_times
            return
        raise ValueError('Only positive values...')

    def repr(self):
        stat = ' '.join([el.repr() for el in self._stat])

        stg = ''
        stg += '{} {} {}'.format(Kw.trigger(), self._name.repr(), stat)
        if self._apply_times: stg += ' {} {}'.format(Kw.apply_times(), self._apply_times)
        if self._test_times: stg += ' {} {}'.format(Kw.test_times(), self._test_times)

        lst = []
        for el in self._act:
            el = '\n  '.join(el.repr().split('\n'))
            lst.append('\n  {}'.format(el))
        act = ''.join(lst)

        stg += '{}'.format(act)

        stg += '\n{}'.format(Kw.end_trigger())
        return stg
