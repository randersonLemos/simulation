from simulation.dict.keywords import Keywords as Kw

class AstkClumpsetting:
    def __init__(self):
        self._layerclump_name = ''
        self._value = ''


    def set_layerclump_name(self, name):
        self._layerclump_name = "'" + name + "'"
        return self


    def set_value(self, value):
        self._value = value
        return self


    def __call__(self):
        return '{} {} {}'.format(Kw.clumpsetting(), self._layerclump_name, self._value)
