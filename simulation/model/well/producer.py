import re
import pathlib
from simulation.model.well import agregator
from simulation.common.keywords import Keywords as kw

class Producer:
    _builder = None

    @classmethod
    def set_builder(cls, builder):
        cls._builder = builder

    def __init__(self, well_design):
        self._wd = well_design
        self._ag = agregator.Agregator()

    def build(self):
        if self._builder:
            self._builder.build(self._ag, self._wd)
            return self
        raise NameError('Builder object not defined...')

    def write(self, path_to_folder):
        p = pathlib.Path(path_to_folder)
        p.mkdir(parents=True, exist_ok=True)
        with (p / '{}.inc'.format(self._wd.name)).open('w') as fh: fh.write(self._ag.__repr__())

    def __repr__(self):
        return self._ag.__repr__()