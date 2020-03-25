from simulation.input.well.parts.on_ctrllump_condition import On_Ctrllump_Condition

class GOR(On_Ctrllump_Condition):
    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value
