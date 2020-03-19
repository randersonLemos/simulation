from simulation.builder.well.part.well import Well
from simulation.builder.well.part.producer import Producer
from simulation.builder.well.part.operate import Operate
from simulation.builder.well.part.monitor import Monitor
from simulation.builder.well.part.geometry import Geometry
from simulation.builder.well.part.perf_ff import Perf_ff
from simulation.builder.well.part.shutin import Shutin
from simulation.builder.well.part.ontime import Ontime
from simulation.builder.well.part.layerclumps import Layerclumps
from simulation.builder.well.part.clumpsetting import Clumpsetting
from simulation.builder.well.agregator import Agregator
from simulation.common.keywords import Keywords as kw

class Well_Producer(Agregator):
    def __init__(self, well_design):
        super().__init__()
        self.wd = well_design

        self._build()

    def _build(self):
        wd = self.wd

        self.add_one(Well(wd.name, wd.group))
        self.add_one(Producer(wd.name))
        self.add_one(Operate(wd.operate))
        self.add_one(Monitor(wd.monitor))
        self.add_one(Geometry(wd.geometry))
        self.add_one(Perf_ff(wd.name, wd.perf_ff, wd.perf_table))
        self.add_one(Shutin(wd.name))
        self.add_one(Ontime(wd.name, wd.on_time))
        layerclumps = Layerclumps('{}_Z'.format(wd.name) , wd.name, wd.layerclump)
        self.add_one(layerclumps)
        for name in layerclumps.names: self.add_one(Clumpsetting(name, 0))



        #if wd.icv_operation:
        #    Icv.deafult(agregator, well_name, wd.layerclump, wd.icv_operation, wd.icv_control_law)

        #if wd.icv_control_signal:
        #    for zone, signal in zip(wd.get_icv_zones(), wd.icv_control_signal):
        #        agregator.add_three(kw.clumpsetting(), "'"+zone+"'", signal)

