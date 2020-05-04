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
        return pd.merge(self._X, self._y, on='ID')

    #def head(self, num):
    #    other = copy.deepcopy(self)
    #    other.X = self._X.iloc[:num,:]
    #    other.y = self._y.iloc[:num,:]
    #    return other

    #def tail(self, num):
    #    other = copy.deepcopy(self)
    #    other.X = self._X.iloc[-num:,:]
    #    other.y = self._y.iloc[-num:,:]
    #    return other