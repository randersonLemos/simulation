from simulation.common.keywords import Keywords as Kw

class AstkWell:
    def __init__(self):
        self._name = ''
        self._group = ''

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = "'" + name + "'"
        return self

    def group(self):
        return self._group

    def set_group(self, group):
        self._group = "'" + group + "'"
        return self

    def repr(self):
        return '{} {} {} {}'.format(Kw.well(), self._name, Kw.attachto(), self._group)
