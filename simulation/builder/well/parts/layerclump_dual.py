from collections.abc import Iterable
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Layerclump_Dual(Agregator):
    def __init__(self, well_name, layerclump):
        super().__init__()

        self.well_name = well_name
        self.layerclump = layerclump

        self._build()

    def _build(self):
        well_name = "'{}'".format(self.well_name())
        for name, layer in self.layerclump:
            name = "'{}'".format(name)

            stg = ''
            for el in layer:
                if isinstance(el, Iterable):
                    stg += ' {:02d}:{:02d}'.format(el[0], el[1])
                else:
                    stg += ' {:02d}'.format(el)

            stg = stg.strip()
            self.add_two(kw.layerclump(), name)
            self.add_three(well_name, stg, kw.mt())
            self.add_three(well_name, stg, kw.fr())


