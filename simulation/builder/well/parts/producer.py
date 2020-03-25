from simulation.input.well.parts.name import Name as iName
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Producer(Agregator):
    def __init__(self, well_name):
        super().__init__()

        if not isinstance(well_name, iName): raise TypeError('Not allowed type...')

        self.well_name = well_name

        self._build()

    def _build(self):
        name = "'{}'".format(self.well_name())
        self.add_two(kw.producer(), name)
