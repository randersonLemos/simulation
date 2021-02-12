import pathlib
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import FuncFormatter


import functools

class Default:
    _figsize = (10,6)
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
        #xlocator = mdates.MonthLocator(bymonth=[1])
        xformatter = mdates.DateFormatter('%Y')
        ax.xaxis.set_ticklabels(ax.xaxis.get_ticklabels(), rotation=0, horizontalalignment='center')
        ax.xaxis.set_major_locator(LinearLocator(5))
        ax.xaxis.set_major_formatter(xformatter)

        def myround(x, base=5):
            return int(base * round(x/base))

        @FuncFormatter
        def yformatter(value, pos):
            if len(str(int(value)))    < 3:
                stg =  '{}'.format(myround(value, base=10))

            elif len(str(int(value))) == 3:
                stg =  '{}'.format(myround(value, base=10))

            elif len(str(int(value)))  > 3 and len(str(int(value))) <= 5:
                stg =  '{}'.format(myround(value, base=100))

            elif len(str(int(value))) >= 6:
                stg =  '{}'.format(myround(value, base=1000))

            return stg

        ax.yaxis.set_major_locator(LinearLocator(5))
        ax.yaxis.set_major_formatter(yformatter)

        ax.set_ylim(ymin=0)
        #ax.xaxis.set_label_coords(-0.120, -0.045)
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
