import pathlib
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import FuncFormatter

locator = mdates.MonthLocator(bymonth=[1])
formatter = mdates.DateFormatter('%Y')

import functools

class Default:
    _figsize = (10,5)
    _tight_layout = True

    @classmethod
    def set_figsize(cls, size):
        if isinstance(size, tuple):
            cls._figsize = size
            return
        raise TypeError('Not allowed type...')

    @classmethod
    def set_tight_layout(cls, bbool):
        cls._tight_layout = bboll

    def __init__(self, tables):
        if not isinstance(tables, list):
            lst = []
            lst.append(tables)
            self.tables = lst
            return
        self.tables = tables

    def _default_ax(self, ax):
        ax.xaxis.set_ticklabels(ax.xaxis.get_ticklabels(), rotation=90, horizontalalignment='center')
        ax.xaxis.set_major_locator(LinearLocator(10))
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_locator(LinearLocator(5))
        ax.set_ylim(ymin=0)
        ax.grid()

class Preprocessing(Default):
    def __init__(self, func):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        functools.update_wrapper(self, func)
        self.func = func

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

    def __call__(self, obj, *args, **kwargs):
        if not 'ax' in kwargs:
            fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
            kwargs['ax'] = ax

        value = self.func(obj, *args, **kwargs)
        return value
