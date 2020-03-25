from simulation.input.well.parts.trigger_object import Trigger_Object

class Trigger:
    _apply_times = -1
    _test_times = -1

    @classmethod
    def set_default_apply_times(cls, apply_times):
        cls._apply_times = apply_times

    @classmethod
    def set_default_test_times(cls, test_times):
        cls._test_times = test_times

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
        return self._action

    def add_action(self, action):
        self._act.append(action)

    def name(self):
        return self._name

    def set_name(self, name):
        self.name = name

    def apply_times(self):
        return self._apply_times

    def set_apply_times(self, apply_times):
        self._apply_times = apply_times

    def test_times(self):
        return self._test_times

    def set_test_times(self, test_times):
        self._test_times = test_times
