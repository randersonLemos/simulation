from simulation.input.well.parts.name import Name as iName
from simulation.input.well.parts.on_time import On_Time as iOn_Time
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class On_Time(Agregator):
    def __init__(self, well_name, on_time):
        super().__init__()

        if not isinstance(well_name, iName): raise TypeError('Not allowed type...')
        if not isinstance(on_time, iOn_Time): raise TypeError('Not allowed type...')

        self.well_name = well_name
        self.on_time = on_time

        self._build()

    def _build(self):
        name = "'{}'".format(self.well_name())
        self.add_two(kw.on_time(), name)
        self.add_one(self.on_time())
