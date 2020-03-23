from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Layerclump(Agregator):
    def __init__(self, name, well_name, layer):
        super().__init__()
        self.name = name
        self.well_name = well_name
        self.layer = layer

        self._build()

    def _build(self):
        name = "'{}'".format(self.name)
        self.add_two(kw.layerclump(), name)
        well_name = "'{}'".format(self.well_name)
        self.add_three(well_name, ' '.join(self.layer), kw.mt())
        self.add_three(well_name, ' '.join(self.layer), kw.fr())


