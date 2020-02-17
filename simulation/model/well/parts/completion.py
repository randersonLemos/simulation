from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd

class Completion:

    @staticmethod
    def default(agr, perf_table):
        for idx, com in enumerate(perf_table):
            ff = com[3]
            uba = ' '.join(com[:3])
            status = com[4]
            if idx == 0:
                agr.add_seven(uba, kw.fr(), ff, status, kw.flow_to()
                        , wrd.surface(), kw.reflayer()
                        #, suf=" ** uba ff status connection"
                        )
                agr.add_five(uba, kw.mt(), ff, status, kw.flow_to())
            else:
                agr.add_six(uba, kw.fr(), ff, status
                        , kw.flow_to(), '{:02d}'.format(idx))
                agr.add_six(uba, kw.mt(), ff, status
                        , kw.flow_to(), '{:02d}'.format(idx))
