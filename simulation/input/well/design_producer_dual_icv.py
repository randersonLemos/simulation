from simulation.input.well.parts.name import Name
from simulation.input.well.parts.group import Group
from simulation.input.well.parts.producer import Producer
from simulation.input.well.parts.operate import Operate
from simulation.input.well.parts.monitor import Monitor
from simulation.input.well.parts.geometry import Geometry
from simulation.input.well.parts.perf import Perf
from simulation.input.well.parts.on_time import On_Time
from simulation.input.well.parts.layerclump import Layerclump
from simulation.input.well.parts.trigger import Trigger

class Design_Producer_Dual_Icv:
    def __init__(self):
        self._kind = Producer()

    def kind(self):
        return self._kind

    def name(self):
        return self._name

    def set_name(self, name):
            self._name = Name(name)

    def group(self):
        return self._group

    def set_group(self, group):
        if isinstance(group, Group):
            self._group = group
            return
        raise TypeError('Not allowed type...')

    def operate(self):
        return self._operate

    def set_operate(self, operate):
        if isinstance(operate, Operate):
            self._operate = operate
            return
        raise TypeError('Not allowed type...')

    def monitor(self):
        return self._monitor

    def set_monitor(self, monitor):
        if isinstance(monitor, Monitor):
            self._monitor = monitor
            return
        raise TypeError('Not allowed type...')

    def geometry(self):
        return self._geometry

    def set_geometry(self, geometry):
        if isinstance(geometry, Geometry):
            self._geometry = geometry
            return
        raise TypeError('Not allowed type...')

    def perf(self):
        return self._perf

    def set_perf(self, perf):
        if isinstance(perf, Perf):
            self._perf = perf
            return
        raise TypeError('Not allowed type...')

    def on_time(self):
        return self._on_time

    def set_on_time(self, on_time):
        if isinstance(on_time, On_Time):
            self._on_time = on_time
            return
        raise TypeError('Not allowed type...')

    def layerclump(self):
        return self._layerclump

    def set_layerclump(self, layerclump):
        if isinstance(layerclump, Layerclump):
            self._layerclump = layerclump
            return
        raise TypeError('Not allowed type...')

    def trigger(self):
        return self._trigger

    def set_trigger(self, trigger):
        if isinstance(trigger, Trigger):
            self._trigger = trigger
            return
        raise TypeError('Not allowed type...')

    def __repr__(self):
        lst = []
        for key in self.__dict__:
            lst.append('{}:{}'.format(key[1:],self.__dict__[key]))
        return '\n'.join(map(str, lst))



