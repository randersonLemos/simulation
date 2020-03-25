from simulation.common.keywords import Keywords as Kw
from simulation.input.well.parts.on_elapsed_condition import On_Elapsed_Condition

class Treltd(On_Elapsed_Condition):
    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value

    def repr(self):
        return '{} {}'.format(Kw.treltd(), self._value)
