from simulation.common.keywords import Keywords as Kw

class AstkMonitor:
    def __init__(self):
        self._lst = []

    def add(self, condition, value, action):
        self._lst.append((condition, value, action, ))
        return self

    def repr(self):
        lst = []
        for el in self._lst:
            lst.append('{} {}'.format(Kw.operate(), ' '.join(map(str, el))))
        return '\n'.join(lst)
