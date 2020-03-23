from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Operate(Agregator):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst

        self._build()

    def _build(self):
        for el in self.lst:
            self.add_two(kw.operate(), el)
