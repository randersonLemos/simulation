class On_Time:
    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value
