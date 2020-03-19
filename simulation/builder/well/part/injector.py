from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Injector(Agregator):
    def __init__(self, well_name):
        super().__init__()
        self.well_name = well_name

        self._build()

    def _build(self):
        name = "'{}'".format(self.well_name)
        self.add_two(kw.injector(), name)
