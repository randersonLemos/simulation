import numpy as np

class Perf:
    def __init__(self, *args):
        self._args = args
        self._lst = []

    def add(self, *args):
        self._lst.append(args)

    def fill(self):
        lst = []
        for tail, head in zip(self._lst[:-1], self._lst[1:]):

            init = np.array(tail[:3])
            goal = np.array(head[:3])
            vec = ((goal - init) / np.linalg.norm(goal - init)).astype(int)

            middle = list(tail[3:-1])

            body = []
            body.append(list(tail))
            init += vec
            while (init != goal).any():
                body.append(init.tolist() + middle + ['*OPEN'])
                init += vec
            lst += body
        lst.append(list(head))
        self._lst = lst

