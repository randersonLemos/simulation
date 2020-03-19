from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd
from simulation.builder.well.agregator import Agregator

class Perf_ff(Agregator):
    def __init__(self, well_name, perf_ff, completions):
        super().__init__()
        self.well_name = well_name
        self.perf_ff = perf_ff
        self.completions = completions

        self._build()

    def _build(self):
        well_name = "'{}'".format(self.well_name)
        self.add_three(kw.perf(), self.perf_ff, well_name)

        for idx, completion in enumerate(self.completions):
            ff = completion[3]
            uba = ' '.join(completion[:3])
            status = completion[4]
            if idx == 0:
                self.add_seven(uba, kw.fr(), ff, status, kw.flow_to()
                        , wrd.surface(), kw.reflayer()
                        #, suf=" ** uba ff status connection"
                        )
                self.add_five(uba, kw.mt(), ff, status, kw.flow_to())
            else:
                self.add_six(uba, kw.fr(), ff, status
                        , kw.flow_to(), '{:02d}'.format(idx))
                self.add_six(uba, kw.mt(), ff, status
                        , kw.flow_to(), '{:02d}'.format(idx))
