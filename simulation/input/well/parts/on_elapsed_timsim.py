from simulation.common.keywords import Keywords as Kw
from simulation.input.well.parts.on_elapsed_condition import On_Elapsed_Condition

class Timsim(On_Elapsed_Condition):
    def __int__(self, value):
        self_value = value

    def __call__(self):
        return self._value

    def repr(self):
        return '{} {}'.format(Kw.timsim(), self._value)
