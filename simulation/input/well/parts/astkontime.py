from simulation.common.keywords import Keywords as Kw

class AstkOntime:
    def set_well_name(self, name):
        self._well_name = "'" + name + "'"
        return self

    def set_on_time(self, value):
        self._value = value
        return self

    def __call__(self):
        return '{} {}\n{}'.format(Kw.on_time(), self._well_name, self._value)
