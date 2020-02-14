from .graph import Graph
from dictionary.scripts.well_keys import Well_Keys
import matplotlib.pyplot as plt


params = {'legend.fontsize': 8,
          'legend.handlelength': 2,
          'legend.loc' : 'upper left'
         }
plt.rcParams.update(params)


class Well_Graph:
    def __init__(self, well_lst, table_obj):
        self.well_lst = well_lst
        self.table_obj = table_obj

    def fluids(self, well_lst=[]):
        fig, axs = plt.subplots(3, sharex=True, sharey=False)
        self.oil  (axs[0], well_lst)
        self.gas  (axs[1], well_lst)
        self.water(axs[2], well_lst)

    def fluids_dot(self, well_lst=[]):
        fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)
        self.oil_dot  (axs[0,0], well_lst)
        self.gas_dot  (axs[0,1], well_lst)
        self.water_dot(axs[1,1], well_lst)

    def essential_prod(self, well_lst=[]):
        fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)
        self.oil_dot  (axs[0,0], well_lst)
        self.gor  (axs[0,1], well_lst)
        self.wcut (axs[1,0], well_lst)
        self.bhp  (axs[1,1], well_lst)

    def essential_inje(self, well_lst=[]):
        fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)
        self.gas  (axs[0,0], well_lst)
        self.water(axs[0,1], well_lst)
        #self.wcut (axs[1,0], well_lst)
        self.bhp  (axs[1,1], well_lst)

    def oil(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.fluid(ax, self._df_oil(well_lst), 'Cumulative Oil SC')

    def gas(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.gas(ax, self._df_gas(well_lst), 'Cumulative Gas SC')

    def water(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.fluid(ax, self._df_wat(well_lst), 'Cumulative Water SC')

    def oil_dot(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.fluid_dot(ax, self._df_oil_dot(well_lst), 'Oil Rate SC')

    def gas_dot(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.gas_dot(ax, self._df_gas_dot(well_lst), 'Gas Rate SC')

    def water_dot(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.fluid_dot(ax, self._df_wat_dot(well_lst), 'Water Rate SC')

    def gor(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.fluid_ratio(ax, self._df_gor(well_lst), 'Gas Oil Ratio SC')

    def wcut(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.percent(ax, self._df_wcut(well_lst)*100, 'Water Cut SC')

    def bhp(self, ax=None, well_lst=[]):
        if ax is None: fig, ax = plt.subplots()
        Graph.pressure(ax, self._df_bhp(well_lst), 'Bottom Hole Pressure')

    def _df_oil(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.cum_oil_sc()).dropna()[well_lst]

    def _df_gas(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.cum_gas_sc()).dropna()[well_lst]

    def _df_wat(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.cum_wat_sc()).dropna()[well_lst]

    def _df_oil_dot(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.oil_rate_sc()).dropna()[well_lst]

    def _df_gas_dot(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.gas_rate_sc()).dropna()[well_lst]

    def _df_wat_dot(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.wat_rate_sc()).dropna()[well_lst]

    def _df_gor(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.gor_sc()).dropna()[well_lst]

    def _df_wcut(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.wat_cut_sc()).dropna()[well_lst]

    def _df_bhp(self, well_lst=[]):
        tab = self.table_obj
        if not well_lst:
            well_lst = self.well_lst
        return tab.grp_col(Well_Keys.well_bhp()).dropna()[well_lst]

    def show(self):
        Graph.show()
