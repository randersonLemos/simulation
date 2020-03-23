from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Well(Agregator):
    def __init__(self, name, group):
        super().__init__()
        self.name = name
        self.group = group

        self._build()

    def _build(self):
        name = "'{}'".format(self.name)
        group = "'{}'".format(self.group)
        self.add_four(kw.well(), name, kw.attachto(), group)
