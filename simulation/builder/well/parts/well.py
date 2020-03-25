from simulation.input.well.parts.name import Name as iName
from simulation.input.well.parts.group import Group as iGroup
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Well(Agregator):
    def __init__(self, name, group):
        super().__init__()

        if not isinstance(name, iName): raise TypeError('Not allowed type...')
        if not isinstance(group, iGroup): raise TypeError('Not allowed type...')

        self.name = name
        self.group = group

        self._build()

    def _build(self):
        name = "'{}'".format(self.name())
        group = "'{}'".format(self.group())
        self.add_four(kw.well(), name, kw.attachto(), group)
