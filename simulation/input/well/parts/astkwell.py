from simulation.common.keywords import Keywords as Kw

class AstkWell:
    def __init__(self):
        self._name = ''
        self._group = ''

    def set_name(self, name):
        self._name = "'" + name + "'"
        return self

    def set_group(self, group):
        self._group = "'" + group + "'"
        return self

    def __call__(self):
        return '{} {} {} {}'.format(Kw.well(), self._name, Kw.attachto(), self._group)
