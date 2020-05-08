from simulation.common.keywords import Keywords as Kw
from simulation.common.words import Words as Wrd
from simulation.input.well.parts.triggerobject import TriggerObject


class OnElapsed(TriggerObject):
    def __init__(self):
        super().__init__()
        self._condition = None


    def set_condition(self, measure, operator, value):
        self._condition = (measure, operator, value)
        return self


    def __call__(self):
        stg = ''
        stg += '{} {} {}'.format(Kw.on_elapsed(), Wrd.time(), ' '.join(list(map(str, self._condition))))
        if self._increment: stg += ' {} {}'.format(Kw.increment(), self._increment)
        if self._avrgtime:  stg += ' {} {}'.format(Kw.avrgtime(), self._avrgtime)
        return stg
