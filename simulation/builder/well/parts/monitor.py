from simulation.input.parts.monitor import Monitor as iMonitor
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Monitor(Agregator):
    def __init__(self, monitor):
        super().__init__()

        if not isinstance(monitor, iMonitor): raise TypeError('Not allowed type...')

        self.mon = monitor

        self._build()

    def _build(self):
        for el in self.mon:
            self.add_two(kw.monitor(), ' '.join(map(str, el)))
