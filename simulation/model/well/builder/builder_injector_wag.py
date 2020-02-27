from simulation.model.well.part.header import Header
from simulation.model.well.part.completion import Completion
from simulation.model.well.part.others import Others
from simulation.common.keywords import Keywords as kw

class Builder_Injector_Wag:
    @staticmethod
    def build(agregator, well_design):
        wd = well_design

        well_name = {}
        well_name['G'] = "'"+wd.alias['G']+"'"
        well_name['W'] = "'"+wd.alias['W']+"'"
        
        well_group = "'" + wd.group + "'"

        operate = [lst[1:] for lst in wd.operate if 'G' == lst[0]]
        monitor = [lst[1:] for lst in wd.monitor if 'G' == lst[0]]

        Header.default(agregator, well_name['G'], kw.injector(), well_group,
                kw.gas(), operate, monitor, wd.geometry, wd.perf_ff)
        if wd.perf_table:
            Completion.default(agregator, wd.perf_table)
        agregator.add_two(kw.shutin(), well_name['G'])

        operate = [lst[1:] for lst in wd.operate if 'W' == lst[0]]
        monitor = [lst[1:] for lst in wd.monitor if 'W' == lst[0]]

        Header.default(agregator, well_name['W'], kw.injector(), well_group,
                kw.water(), operate, monitor, wd.geometry, wd.perf_ff)
        if wd.perf_table:
            Completion.default(agregator, wd.perf_table)
        agregator.add_two(kw.shutin(), well_name['W'])

        if wd.on_time:
            agregator.add_two(kw.on_time(), well_name['G'])
            agregator.add_one(wd.on_time)
            agregator.add_two(kw.on_time(), well_name['W'])
            agregator.add_one(wd.on_time)

        if wd.open_time:
            mode, open_time = wd.open_time
            Others.Open.default(agregator, well_name[mode], open_time)

        if wd.wag_operation:
            Others.Wag.default(agregator, well_name, wd.wag_operation)

        if wd.layerclump:
            Others.Layerclump.wag(agregator, well_name, wd.layerclump)
