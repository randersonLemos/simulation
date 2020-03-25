from simulation.input.well.parts.trigger_object import Trigger_Object
from simulation.input.well.parts.on_ctrllump_condition import On_Ctrllump_Condition

class On_Ctrllump(Trigger_Object):
    def __init__(self, condition):
        if isinstance(condition, On_Ctrllump_Condition):
            self._condition = condition
            return
        raise TypeError('Not allowed type...')
