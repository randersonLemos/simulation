import pathlib
import matplotlib.pyplot as plt
import seaborn as sb
from .graph import Graph
from .sector_keys import Sector_Keys

class Sector_Graph:
    _figsize = (10,5)
    _tight_layout = True

    @classmethod
    def set_figsize(cls, size):
        if isinstance(size, tuple):
            cls._figsize = size
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

    def oil_prod(self, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'FIELD OIL PRODUCTION'
        self._fluid(Sector_Keys.oil_prod_sc(), title, ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'FIELDOILPROD.png')

        return fig, ax, path

    def gas_prod(self, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'FIELD GAS PRODUCTION'
        self._gas(Sector_Keys.gas_prod_sc(), title, ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'FIELDGASPROD.png')

        return fig, ax, path

    def wat_prod(self, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'FIELD WATER PRODUCTION'
        self._fluid(Sector_Keys.wat_prod_sc(), title, ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'FIELDWATPROD.png')

        return fig, ax, path

    def gas_inje(self, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'FIELD GAS INJECTION'
        self._gas(Sector_Keys.gas_inje_sc(), title, ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'FIELDGASINJE.png')

        return fig, ax, path

    def wat_inje(self, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'FIELD WATER INJECTION'
        self._fluid(Sector_Keys.wat_inje_sc(), title, ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'FIELDWATINJE.png')

        return fig, ax, path

    def avg_pres(self, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'FIELD PRESSURE'
        legend = []
        for tables in self.tables:
            Graph.pressure(tables.get(Sector_Keys.sector()).df[Sector_Keys.avg_pressure()], title, ax)
            legend.append(tables.path_to_rwo_file.stem)
        ax.legend(legend)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'FIELDAVGPRESS.png')

        return fig, ax, path

    def _fluid(self, key, title, ax):
        lst = []
        for tables in self.tables:
            Graph.fluid(tables.get(Sector_Keys.sector()).df[key], title, ax)
            lst.append(tables.path_to_rwo_file.stem)
        ax.legend(lst)

    def _gas(self, key, title, ax):
        lst = []
        for tables in self.tables:
            Graph.gas(tables.get(Sector_Keys.sector()).df[key], title, ax)
            lst.append(tables.path_to_rwo_file.stem)
        ax.legend(lst)


