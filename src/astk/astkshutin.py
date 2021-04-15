from src.dict.keywords import Keywords as Kw

class AstkShutin:
    def __init__(self):
        self._well_name = ''

    def set_well_name(self, name):
        self._well_name = "'" + name + "'"
        return self

    def __call__(self):
        return '{} {}'.format(Kw.shutin(), self._well_name)
