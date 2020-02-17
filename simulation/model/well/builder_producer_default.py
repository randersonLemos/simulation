from simulation.model.well.parts.header import Header
from simulation.model.well.parts.completion import Completion
from simulation.model.well.parts.others import Others
from simulation.common.keywords import Keywords as kw

class Builder_Producer_Default:
    @staticmethod
    def build(agregator, well_design):
        wd = well_design
        Header.default(agregator, wd.name, kw.producer(), wd.group,
                '', wd.operate, wd.monitor, wd.geometry, wd.perf_ff)

        Completion.default(agregator, wd.perf_table)

        agregator.add_two(kw.shutin(), wd.name)

        if wd.time_on:
            agregator.add_two(kw.on_time(), wd.name)
            agregator.add_one(wd.time_on)


        if wd.time_open:
            Others.Open.default(agregator, wd.name, wd.time_open)

#        if self.layerclump:
#            from ..pieces.others import layerclump_default as layerclump
#            layerclump(agr, self.well_name, self.layerclump)
#
#        if self.icv_start:
#            from ..pieces.icvs import icv_deafult as icv
#            icv(agr, self.well_name, self.icv_start, self.layerclump, self.icv_control)
#
