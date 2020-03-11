from simulation.model.well.part.header import Header
from simulation.model.well.part.completion import Completion
from simulation.model.well.part.others import Others
from simulation.model.well.part.icv import Icv
from simulation.common.keywords import Keywords as kw

class Builder_Producer_Icv:
    @staticmethod
    def build(agregator, well_design):
        wd = well_design
        well_name = "'" + wd.name + "'"
        well_group = "'" + wd.group + "'"
        Header.default(agregator, well_name, kw.producer(), well_group,
                '', wd.operate, wd.monitor, wd.geometry, wd.perf_ff)

        if wd.perf_table:
            Completion.default(agregator, wd.perf_table)
        agregator.add_two(kw.shutin(), well_name)

        if wd.on_time:
            agregator.add_two(kw.on_time(), well_name)
            agregator.add_one(wd.on_time)

        if wd.open_time:
            Others.Open.default(agregator, well_name, wd.open_time)

        if wd.layerclump:
            Others.Layerclump.default(agregator, well_name, wd.layerclump)

        if wd.icv_operation:
            Icv.deafult(agregator, well_name, wd.layerclump, wd.icv_operation, wd.icv_control_law)

        if wd.icv_control_signal:
            for zone, signal in zip(wd.get_icv_zones(), wd.icv_control_signal):
                agregator.add_three(kw.clumpsetting(), "'"+zone+"'", signal)

