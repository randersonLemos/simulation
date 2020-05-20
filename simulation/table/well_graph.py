import pathlib
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import FuncFormatter

locator = mdates.MonthLocator(bymonth=[1])
formatter = mdates.DateFormatter('%Y')

from .graph import Graph
from .well_keys import Well_Keys
import matplotlib.pyplot as plt

class Well_Graph:
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

    def oil_prod(self, well_lst, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'WELL OIL PRODUCTION'
        self._fluid(well_lst, title, Well_Keys.oil_prod_sc(), ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'WELLOILPROD.png')

        return fig, ax, path

    def gas_prod(self, well_lst, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'WELL GAS PRODUCTION'
        self._gas(well_lst, title, Well_Keys.gas_prod_sc(), ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'WELLGASPROD.png')

        return fig, ax, path

    def wat_prod(self, well_lst, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'WELL WATER PRODUCTION'
        self._fluid(well_lst, title, Well_Keys.wat_prod_sc(), ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'WELLWATPROD.png')

        return fig, ax, path

    def gor(self, well_lst, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'WELL GOR'
        self._gor(well_lst, title, Well_Keys.gor_sc(), ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'WELLGOR.png')

        return fig, ax, path

    def wcut(self, well_lst, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'WELL WCUT'
        self._wcut(well_lst, title, Well_Keys.wat_cut_sc(), ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'WELLWCUT.png')

        return fig, ax, path

    def bhp(self, well_lst, custom_ax=None, savefig_rootpath=''):
        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
        if custom_ax:
            ax = custom_ax

        title = 'WELL BHP'
        self._bhp(well_lst, title, Well_Keys.bhp(), ax)

        path = ''
        if savefig_rootpath:
            path = str(pathlib.Path(savefig_rootpath) / 'WELLBHP.png')

        return fig, ax, path


    def _fluid(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst] / 1000)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$msm^3$')

        self._default_ax(ax)

    def _gas(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst] / 1000000)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$mmsm^3$')

        self._default_ax(ax)

    def _gor(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst])
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$sm^3/sm^3$')

        self._default_ax(ax)

    def _wcut(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst]*100).fillna(0)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$\\%$')

        self._default_ax(ax)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:0.0f}'.format(x)))

    def _bhp(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst])
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$kg/cm^2$')

        self._default_ax(ax)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:0.0f}'.format(x)))
        ax.set_ylim(ymin=Melt['VALUE'].min()-10)






    def _default_ax(self, ax):
        ax.xaxis.set_ticklabels(ax.xaxis.get_ticklabels(), rotation=90, horizontalalignment='center')
        ax.xaxis.set_major_locator(LinearLocator(10))
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_locator(LinearLocator(5))
        ax.set_ylim(ymin=0)
        ax.grid()











    #def fluids(self, well_lst=[]):
    #    fig, axs = plt.subplots(3, sharex=True, sharey=False)
    #    self.oil  (axs[0], well_lst)
    #    self.gas  (axs[1], well_lst)
    #    self.water(axs[2], well_lst)

    #def fluids_dot(self, well_lst=[]):
    #    fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)
    #    self.oil_dot  (axs[0,0], well_lst)
    #    self.gas_dot  (axs[0,1], well_lst)
    #    self.water_dot(axs[1,1], well_lst)

    #def essential_prod(self, well_lst=[]):
    #    fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)
    #    self.oil_dot  (axs[0,0], well_lst)
    #    self.gor  (axs[0,1], well_lst)
    #    self.wcut (axs[1,0], well_lst)
    #    self.bhp  (axs[1,1], well_lst)

    #def essential_inje(self, well_lst=[]):
    #    fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)
    #    self.gas  (axs[0,0], well_lst)
    #    self.water(axs[0,1], well_lst)
    #    #self.wcut (axs[1,0], well_lst)
    #    self.bhp  (axs[1,1], well_lst)


    #def gas(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.gas(ax, self._df_gas(well_lst), 'Cumulative Gas SC')

    #def water(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.fluid(ax, self._df_wat(well_lst), 'Cumulative Water SC')

    #def oil_dot(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.fluid_dot(ax, self._df_oil_dot(well_lst), 'Oil Rate SC')

    #def gas_dot(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.gas_dot(ax, self._df_gas_dot(well_lst), 'Gas Rate SC')

    #def water_dot(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.fluid_dot(ax, self._df_wat_dot(well_lst), 'Water Rate SC')

    #def gor(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.fluid_ratio(ax, self._df_gor(well_lst), 'Gas Oil Ratio SC')

    #def wcut(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.percent(ax, self._df_wcut(well_lst)*100, 'Water Cut SC')

    #def bhp(self, ax=None, well_lst=[]):
    #    if ax is None: fig, ax = plt.subplots()
    #    Graph.pressure(ax, self._df_bhp(well_lst), 'Bottom Hole Pressure')

    def _df_oil(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.cum_oil_sc()).dropna()[well_lst]

    #def _df_gas(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.cum_gas_sc()).dropna()[well_lst]

    #def _df_wat(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.cum_wat_sc()).dropna()[well_lst]

    #def _df_oil_dot(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.oil_rate_sc()).dropna()[well_lst]

    #def _df_gas_dot(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.gas_rate_sc()).dropna()[well_lst]

    #def _df_wat_dot(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.wat_rate_sc()).dropna()[well_lst]

    #def _df_gor(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.gor_sc()).dropna()[well_lst]

    #def _df_wcut(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.wat_cut_sc()).dropna()[well_lst]

    #def _df_bhp(self, well_lst=[]):
    #    tab = self.table_obj
    #    if not well_lst:
    #        well_lst = self.well_lst
    #    return tab.grp_col(Well_Keys.well_bhp()).dropna()[well_lst]
