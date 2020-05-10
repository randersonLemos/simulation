from simulation.builder.well.parts.well import Well
from simulation.builder.well.parts.producer import Producer
from simulation.builder.well.parts.operate import Operate
from simulation.builder.well.parts.monitor import Monitor
from simulation.builder.well.parts.geometry import Geometry
from simulation.builder.well.parts.perf_dual import Perf_Dual
from simulation.builder.well.parts.shutin import Shutin
from simulation.builder.well.parts.on_time import On_Time
from simulation.builder.well.parts.layerclump_dual import Layerclump_Dual
from simulation.builder.well.parts.clumpsetting import Clumpsetting
from simulation.builder.well.parts.trigger import Trigger
from simulation.builder.well.agregator import Agregator
from simulation.common.keywords import Keywords as kw

from simulation.input.well.design_producer_dual_icv import Design_Producer_Dual_Icv

class Producer_Dual_Icv(Agregator):
    def __init__(self, design):
        if isinstance(design, Design_Producer_Dual_Icv):
            super().__init__()
            self.design = design
            self._build()
            return
        raise TypeError('Argument "design" must be from type Design_Producer_Dual_Icv')

    def _build(self):
        de = self.design
        self.add_one(Well(de.name(), de.group()))
        self.add_one(Producer(de.name()))
        self.add_one(Operate(de.operate()))
        self.add_one(Monitor(de.monitor()))
        self.add_one(Geometry(de.geometry()))
        self.add_one(Perf_Dual(de.name(), de.perf(), de.kind()))
        self.add_one(Shutin(de.name()))
        self.add_one(On_Time(de.name(), de.on_time()))
