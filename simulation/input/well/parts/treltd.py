from simulation.input.well.parts.on_elapsed_condition import On_Elapsed_Condition

class Treltd(On_Elapsed_Condition):
    def __init__(self, value):
        self_value = value

    def __call__(self):
        return self._value
