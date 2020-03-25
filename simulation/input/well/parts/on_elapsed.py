from simulation.input.well.parts.trigger_object import Trigger_Object
from simulation.input.well.parts.on_elapsed_condition import On_Elapsed_Condition

class On_Elapsed(Trigger_Object):
    def __init__(self, condition):
        if isinstance(condition, On_Elapsed_Condition):
            self._condition = condition
            return
        raise TypeError('Not allowed type...')
