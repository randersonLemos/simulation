from simulation.input.well.parts.trigger import Trigger as iTrigger
from simulation.input.well.parts.on_elapsed import On_Elapsed as iOn_Elapsed
from simulation.input.well.parts.on_ctrllump import On_Ctrllump as iOn_Ctrllump
from simulation.common.keywords import Keywords as kw
from simulation.builder.well.agregator import Agregator

class Trigger(Agregator):
    def __init__(self, trigger):
        super().__init__()

        if not isinstance(trigger, iTrigger): raise TypeError('Not allowed type...')

        self.trigger = trigger

        self._build()

    def _build(self):
        name = "'{}'".format(self.trigger.name())
        self.add_two(kw.trigger(), name)

