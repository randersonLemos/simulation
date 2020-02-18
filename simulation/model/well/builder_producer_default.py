from simulation.model.well.parts.header import Header
from simulation.model.well.parts.completion import Completion
from simulation.model.well.parts.others import Others
from simulation.model.well.parts.icv import ICV
from simulation.common.keywords import Keywords as kw

class Builder_Producer_Default:
    @staticmethod
    def build(agregator, well_design):
        wd = well_design
        Header.default(agregator, wd.name, kw.producer(), wd.group,
                '', wd.operate, wd.monitor, wd.geometry, wd.perf_ff)

        Completion.default(agregator, wd.perf_table)

        agregator.add_two(kw.shutin(), wd.name)
        if wd.on_time:
            agregator.add_two(kw.on_time(), wd.name)
            agregator.add_one(wd.on_time)


        if wd.open_time: Others.Open.default(agregator, wd.name, wd.open_time)

        if wd.layerclump: Others.Layerclump.default(agregator, wd.name, wd.layerclump)

        if wd.icv_operation: ICV.deafult(agregator, wd.name, wd.layerclump, wd.icv_operation, wd.icv_control_law)

