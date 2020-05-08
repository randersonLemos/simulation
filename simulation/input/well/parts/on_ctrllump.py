from simulation.common.keywords import Keywords as Kw
from simulation.common.words import Words as Wrd
from simulation.input.well.parts.name import Name
from simulation.input.well.parts.trigger_object import Trigger_Object
from simulation.input.well.parts.on_ctrllump_condition import On_Ctrllump_Condition

class Trigger_Object_On_Ctrllump(Trigger_Object):
    def set_condition(self, condition):
        if isinstance(condition, On_Ctrllump_Condition):
            self._condition = condition
            return
        raise TypeError('Not allowed type...')

    def set_layerclump_name(self, layerclump_name):
        self._layerclump_name = Name(layerclump_name)

    def repr(self):
        stg = ''
        stg += '{} {} {}'.format(Kw.on_ctrllump(), self._layerclump_name.repr(), self._condition.repr())
        if self._increment: stg += ' {} {}'.format(Kw.increment(), self._increment)
        if self._avrgtime:  stg += ' {} {}'.format(Kw.avrgtime(), self._avrgtime)
        return stg

