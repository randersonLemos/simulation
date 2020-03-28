from simulation.common.keywords import Keywords as Kw
from simulation.common.words import Words as Wrd
from simulation.input.well.parts.trigger_object import Trigger_Object
from simulation.input.well.parts.on_elapsed_condition import On_Elapsed_Condition

class On_Elapsed(Trigger_Object):
    def __init__(self, condition):
        if isinstance(condition, On_Elapsed_Condition):
            self._condition = condition
            return
        raise TypeError('Not allowed type...')

    def repr(self):
        stg = ''
        stg += '{} {} > {}'.format(Kw.on_elapsed(), Wrd.time(), self._condition.repr())
        if self._increment: stg += ' {} {}'.format(Kw.increment(), self._increment)
        if self._avrgtime:  stg += ' {} {}'.format(Kw.avrgtime(), self._avrgtime)
        return stg
