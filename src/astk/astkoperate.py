from simulation.dict.keywords import Keywords as Kw

class AstkOperate:
    def __init__(self):
        self._lst = []

    def add(self, measure, value, action):
        self._lst.append((measure, value, action, ))
        return self

    def __call__(self):
        lst = []
        for el in self._lst:
            lst.append('{} {}'.format(Kw.operate(), ' '.join(map(str, el))))
        return '\n'.join(lst)





