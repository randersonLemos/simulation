from .graph import Graph
import matplotlib.pyplot as plt


class Special_Graph:
    def __init__(self, well_lst, table_obj):
        self.well_lst = well_lst
        self.table_obj = table_obj

    def essential_prod(self, well_lst=[]):
        fig, axs = plt.subplots(2, 2, sharex=True, sharey=False)
        self.opr(axs[0,0], well_lst)
        self.wcut(axs[0,1], well_lst)
        self.gor(axs[1,1], well_lst)

    def essential_inje(self, well_lst=[]):
        fig, axs = plt.subplots(2, sharex=True, sharey=False)
        self.wpr(axs[0], well_lst)
        self.gpr(axs[1], well_lst)

    def opc(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='OPC', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.fluid_dot(ax, df, well)

    def opr(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='OPR', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.fluid_dot(ax, df, well)

    def gpc(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='GPC', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.fluid_dot(ax, df, well)

    def wpr(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='WPR', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.fluid_dot(ax, df, well)

    def wpc(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='WPC', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.fluid_dot(ax, df, well)

    def gpr(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='GPR', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.fluid_dot(ax, df, well)

    def wcut(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='WCUT', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.percent(ax, df, well)

    def gor(self, ax=None, well_lst=[]):
        tab = self.table_obj
        if not well_lst: well_lst = self.well_lst

        for well in well_lst:
            df = tab.grp_col_spe_well(well)
            df = df.filter(like='GOR', axis=1)
            if ax is None: fig, ax = plt.subplots()
            if not df.empty: Graph.fluid_ratio(ax, df, well)

    def show(self):
        Graph.show()
