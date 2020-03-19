from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Ontime(Agregator):
    def __init__(self, well_name, on_time):
        super().__init__()
        self.well_name = well_name
        self.on_time = on_time

        self._build()

    def _build(self):
        name = "'{}'".format(self.well_name)
        self.add_two(kw.on_time(), name)
        self.add_one(self.on_time)
