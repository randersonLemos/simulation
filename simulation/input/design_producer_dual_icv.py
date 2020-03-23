from simulation.input.parts.name import Name
from simulation.input.parts.group import Group
from simulation.input.parts.operate import Operate
from simulation.input.parts.monitor import Monitor
from simulation.input.parts.geometry import Geometry

class Design_Producer_Dual_Icv:
    def __init__(self):
        self._name = None
        self._group = None
        self._operate = None
        self._monitor = None
        self._geometry = None

    def name(self):
        return self._name()

    def set_name(self, name):
        if isinstance(name, Name):
            self._name = name
            return
        raise TypeError('Not allowed type...')

    def group(self):
        return self._group()

    def set_group(self, group):
        if isinstance(group, Group):
            self._group = group
            return
        raise TypeError('Not allowed type...')

    def operate(self):
        return self._operate()

    def set_operate(self, operate):
        if isinstance(operate, Operate):
            self._operate = operate
            return
        raise TypeError('Not allowed type...')

    def monitor(self):
        return self._monitor()

    def set_monitor(self, monitor):
        if isinstance(monitor, Monitor):
            self._monitor = monitor
            return
        raise TypeError('Not allowed type...')

    def geometry(self):
        return self._geometry()

    def set_geometry(self, geometry):
        if isinstance(geometry, Geometry):
            self._geometry = geometry
            return
        raise TypeError('Not allowed type...')


    def __repr__(self):
        lst = []
        for key in self.__dict__:
            lst.append('{}:{}'.format(key[1:],self.__dict__[key]))
        return '\n'.join(map(str, lst))



