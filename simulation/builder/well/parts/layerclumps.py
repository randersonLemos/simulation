from simulation.common.keywords import Keywords as kw
from simulation.builder.well.parts.layerclump import Layerclump
from simulation.builder.well.agregator import Agregator

class Layerclumps(Agregator):
    def __init__(self, base_name, well_name, layers):
        super().__init__()
        self.base_name = base_name
        self.well_name = well_name
        self.layers = layers

        self.names = []

        self._build()

    def _build(self):
        for idx, layer in enumerate(self.layers):
            name = '{}{}'.format(self.base_name, idx+1)
            self.add_one(Layerclump(name, self.well_name, layer).to_string())
            self.names.append(name)
