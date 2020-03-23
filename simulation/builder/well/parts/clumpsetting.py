from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Clumpsetting(Agregator):
    def __init__(self, layerclump_name, value):
        super().__init__()
        self.layerclump_name = layerclump_name
        self.value = value

        self._build()

    def _build(self):
        self.add_three(kw.clumpsetting(), self.layerclump_name, self.value)
