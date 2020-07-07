import copy
import pandas as pd

class Data:
    def __init__(self, X, y):
        self._X = X
        self._y = y

    def X(self):
        return self._X.copy()

    def y(self):
        return self._y.copy()

    def Xy(self):
        Xy = self._X.copy()
        Xy.loc[:, 'NPV'] = self._y['NPV']
        return Xy