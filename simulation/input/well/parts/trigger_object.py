class Trigger_Object:
    _increment = 0
    _avrgtime = 0

    @classmethod
    def set_default_increment(cls, increment):
        if increment > 0:
            cls._increment = increment
            return
        raise ValueError('Only positive values...')

    @classmethod
    def set_default_avrgtime(cls, avrgtime):
        if avrgtime > 0:
            cls._avrgtime= avgrtime
            return
        raise ValueError('Only positive values...')

    def __init__(self):
        pass

    def increment(self):
        return self._increment

    def set_increment(self, increment):
        if increment > 0:
            self._increment = increment
            return
        raise ValueError('Only positive values...')

    def avrgtime(self):
        return self._avgrtime

    def set_avrgtime(self, avgrtime):
        if avgrtime > 0:
            self._avgrtime = avgrtime
            return
        raise ValueError('Only positive values...')

    def repr():
        raise NotImplementedError('Method for child class...')
