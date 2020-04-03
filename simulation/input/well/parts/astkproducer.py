from simulation.common.keywords import Keywords as Kw

class AstkProducer():
    def __init__(self):
        self._name = ''

    def name(self):
        return self._name

    def set_well_name(self, name):
        self._name = "'" + name + "'"
        return self

    def repr(self):
        return '{} {}'.format(Kw.producer(), self._name)
