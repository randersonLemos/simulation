from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Operate(Agregator):
    def __init__(self, conditions):
        super().__init__()
        self.conditions = conditions

        self._build()

    def _build(self):
        for condition in self.conditions:
            self.add_five(kw.operate(), *condition)
