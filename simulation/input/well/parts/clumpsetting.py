class Clumpsetting:
    def __init__(self):
        self._layerclump_name = ''
        self._value = ''

    def layerclump(self):
        return self._layerclump

    def set_layerclump_name(self, name):
        self._layerclump_name = name

    def value(self):
        return self._value

    def set_value(self, value):
        self._value = value
