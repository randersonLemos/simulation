from simulation.dict.keywords import Keywords as Kw
from simulation.astk.triggerobject import TriggerObject

class AstkTrigger:
    _apply_times = 0
    _test_times = 0

    @classmethod
    def set_default_apply_times(cls, apply_times):
        if apply_times > 0:
            cls._apply_times = apply_times
            return
        raise ValueError('Only positive values...')

    @classmethod
    def set_default_test_times(cls, test_times):
        if test_times > 0:
            cls._test_times = test_times
            return
        raise ValueError('Only positive values...')

    def __init__(self):
        self._name = ''
        self._stat = []
        self._act = []


    def add_trigger_obj(self, obj): # statement
        if isinstance(obj, TriggerObject):
            self._stat.append(obj)
            return
        raise TypeError('Not allowed type...')


    def add_action(self, action):
        self._act.append(action)


    def set_name(self, name):
        self._name = "'" + name + "'"


    def set_apply_times(self, apply_times):
        '''
        Optional subkeyword used to specify the maximum number of times
        that the actions specified with the trigger can be taken. An
        integer number (napt) must immediately follow this subkeyword.
        If no value is entered, then the default is 1 and the trigger
        condition is tested at the end of every timestep. As soon as
        the trigger condition is satisfied the list of actions is
        implemented and the trigger is removed from the list of active
        triggers. If more than 1 (say "n" times) is selected then the
        trigger remains active until the trigger condition is satisfied
        ("n") times.
        '''
        if apply_times > 0:
            self._apply_times = apply_times
            return
        raise ValueError('Only positive values...')


    def set_test_times(self, test_times):
        '''
        Optional subkeywordused to specify the maximum number of
        times that the trigger can be tested to ascertain if the
        trigger condition is satisfied. A single integer number (ntestt)
        must follow this subkeyword. If no value is entered, then the
        default is to test the trigger every timestep. If a value of
        1 is entered then the trigger condition is tested only once at
        the end of the timestep during which the trigger is defined.
        The trigger is then removed from the active trigger list
        whether or not the trigger condition itself is satisfied.
        If more than 1 (say "n" times) is selected then the trigger
        condition is tested for "n" timesteps after the trigger is
        defined.
        '''
        if test_times > 0:
            self._test_times = test_times
            return
        raise ValueError('Only positive values...')


    def __call__(self):
        stat = ' '.join([el() for el in self._stat])

        stg = ''
        stg += '{} {} {}'.format(Kw.trigger(), self._name, stat)
        if self._apply_times: stg += ' {} {}'.format(Kw.apply_times(), self._apply_times)
        if self._test_times: stg += ' {} {}'.format(Kw.test_times(), self._test_times)

        lst = []
        for el in self._act:
            if isinstance(el, str):
                el = '\n  '.join(el.split('\n'))
            else:
                el = '\n  '.join(el().split('\n'))
            lst.append('\n  {}'.format(el))
        act = ''.join(lst)

        stg += '{}'.format(act)

        stg += '\n{}'.format(Kw.end_trigger())
        return stg
