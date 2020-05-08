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
        raise NotImplementedError('Not implemented...')
        #return pd.merge(self._X, self._y, on='ID')