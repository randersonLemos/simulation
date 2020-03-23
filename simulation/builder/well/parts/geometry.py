from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Geometry(Agregator):
    def __init__(self, geometry):
        super().__init__()
        self.geometry = geometry

        self._build()

    def _build(self):
        self.add_two(kw.geometry(), self.geometry)
