from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Incomp(Agregator):
    def __init__(self, fluid):
        super().__init__()
        self.fluid = fluid

        self._build()

    def _build(self):
       self.add_two(kw.incomp(), self.fluid)
