from simulation.input.parts.name import Name as iName
from simulation.input.parts.perf import Perf as iPerf
from simulation.input.parts.kind import Kind as iKind
from simulation.input.parts.producer import Producer as iProducer
from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd
from simulation.builder.well.agregator import Agregator

class Perf_Dual(Agregator):
    def __init__(self, well_name, perf, kind):
        super().__init__()

        if not isinstance(well_name, iName): raise TypeError('Not allowed type...')
        if not isinstance(perf, iPerf): raise TypeError('Not allowed type...')
        if not isinstance(kind, iKind): raise TypeError('Not allowed type...')

        self.well_name = well_name
        self.perf = perf
        self.kind = kind

        self._build()

    def _build(self):
        well_name = "'{}'".format(self.well_name())
        self.add_three(kw.perf(), ' '.join(self.perf.keys()), well_name)

        for idx, line in enumerate(self.perf.table()):
            uba = '{:02d} {:02d} {:02d}'.format(line[0], line[1], line[2])
            keys_values = ' '.join(map(str, line[3:-1]))
            status = ' '.join(map(str, line[-1:-2:-1]))

            flow_dir = kw.flow_to() if isinstance(self.kind, iProducer) else kw.flow_from()

            if idx == 0:
                self.add_seven(uba, kw.fr(), keys_values, status, flow_dir
                        , wrd.surface(), kw.reflayer()
                        )
                self.add_five(uba, kw.mt(), keys_values, status, flow_dir)
            else:
                self.add_six(uba, kw.fr(), keys_values, status
                        , flow_dir, '{:02d}'.format(idx))
                self.add_six(uba, kw.mt(), keys_values, status
                        , flow_dir, '{:02d}'.format(idx))
