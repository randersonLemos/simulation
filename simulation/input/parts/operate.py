class Operate:
    def __init__(self):
        self._lst = []

    def add(self, tracked_measure, value, action):
        self._lst.append([tracked_measure, value, action])

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, idx):
        return self._lst[idx]

    def __call__(self):
        return self._lst
