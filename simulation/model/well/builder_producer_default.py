from simulation.model.well.parts.header import Header
from simulation.common.keywords import Keywords as kw

class Builder_Producer_Default:
    @staticmethod
    def build(agregator, well_design):
        wd = well_design
        Header.default(agregator,
                wd.name,
                kw.producer(),
                wd.group,
                '',
                wd.operate,
                wd.monitor,
                wd.geometry,
                wd.perf_ff
                )
