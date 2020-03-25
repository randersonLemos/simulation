from simulation.input.well.parts.on_ctrllump_wcut import On_Cltrlump_Condition

class WCUT(On_Ctrllump_Condition):
    def __init__(self, valeu):
        self._value = value

    def __call__(self):
        return self._value
