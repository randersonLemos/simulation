from simulation.input.well.parts.geometry import Geometry as iGeometry
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Geometry(Agregator):
    def __init__(self, geometry):
        super().__init__()

        if not isinstance(geometry, iGeometry): raise TypeError('Not allowed type...')

        self.geometry = geometry

        self._build()

    def _build(self):
        self.add_two(kw.geometry(), self.geometry())
