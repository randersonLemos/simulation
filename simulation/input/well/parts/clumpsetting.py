from simulation.input.well.parts.name import Name
from simulation.common.keywords import Keywords as Kw

class Clumpsetting:
    def __init__(self):
        self._layerclump_name = ''
        self._value = ''

    def layerclump(self):
        return self._layerclump_name.strip("'")

    def set_layerclump_name(self, name):
        if isinstance(name, Name):
            self._layerclump_name = name
            return
        raise TypeError('Not allowed type...')

    def value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def repr(self):
        return '{} {} {}'.format(Kw.clumpsetting(), self._layerclump_name.repr(), self._value)
