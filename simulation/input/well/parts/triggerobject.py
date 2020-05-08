class TriggerObject:
    _increment = 0
    _avrgtime = 0

    @classmethod
    def set_default_increment(cls, increment):
        if int(increment) > 0:
            cls._increment = increment
            return
        raise ValueError('Only positive values...')

    @classmethod
    def set_default_avrgtime(cls, avrgtime):
        if int(avrgtime) > 0:
            cls._avrgtime= avrgtime
            return
        raise ValueError('Only positive values...')


    def set_increment(self, increment):
        if increment > 0:
            self._increment = increment
            return
        raise ValueError('Only positive values...')


    def set_avrgtime(self, avrgtime):
        if avrgtime > 0:
            self._avrgtime = avrgtime
            return
        raise ValueError('Only positive values...')

    def __call__():
        raise NotImplementedError('Method for child class...')
