class Trigger_Object:
    _increment = -1
    _avrgtime = -1

    @classmethod
    def set_default_increment(cls, increment):
        cls._increment = increment

    @classmethod
    def set_default_avrgtime(cls, avrgtime):
        cls._avrgtime= avgrtime

    def __init__(self):
        pass

    def increment(self):
        return self._increment

    def set_increment(self, increment):
        self._increment = increment

    def avrgtime(self):
        return self._avgrtime

    def set_avrgtime(self, avgrtime):
        self._avgrtime = avgrtime
