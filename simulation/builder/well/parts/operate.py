from simulation.input.well.parts.operate import Operate as iOperate
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Operate(Agregator):
    def __init__(self, operate):
        super().__init__()

        if not isinstance(operate, iOperate): raise TypeError('Not allowed type...')

        self.ope = operate

        self._build()

    def _build(self):
        for el in self.ope:
            self.add_two(kw.operate(), ' '.join(map(str, el)))
