from simulation.input.well.parts.trigger_object import Trigger_Object

class OR(Trigger_Object):
    @classmethod
    def set_default_increment(cls, increment):
        raise AttributeError("Not allowed attribute...")

    @classmethod
    def set_default_avrgtime(cls, avrgtime):
        raise AttributeError("Not allowed attribute...")

    def __init__(self):
        pass

    def repr(self):
        return 'OR'

    def increment(self):
        raise AttributeError("Not allowed attribute...")

    def set_increment(self, increment):
        raise AttributeError("Not allowed attribute...")

    def avrgtime(self):
        raise AttributeError("Not allowed attribute...")

    def set_avrgtime(self, avgrtime):
        raise AttributeError("Not allowed attribute...")
