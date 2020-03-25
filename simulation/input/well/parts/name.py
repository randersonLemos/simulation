class Name:
    def __init__(self, stg):
        self._stg = stg

    def __call__(self):
        return self._stg
