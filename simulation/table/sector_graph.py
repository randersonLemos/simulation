from ._graph import *
from .sector_keys import Sector_Keys

class Sector_Graph(Default):
    @Preprocessing
    def oil_prod(self, title=None, ax=None):
        if not title: title = 'FIELD OIL PRODUCTION'
        self._fluid(title, Sector_Keys.oil_prod_sc(), ax)
        return ax

    def _fluid(self, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = tables.get(Sector_Keys.sector()).df[key].to_frame() / 1000
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='VAR', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$msm^3$')
        self._default_ax(ax)



#    def gas_prod(self, custom_ax=None, savefig_rootpath=''):
#        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
#        if custom_ax:
#            ax = custom_ax
#
#        title = 'FIELD GAS PRODUCTION'
#        self._gas(Sector_Keys.gas_prod_sc(), title, ax)
#
#        path = ''
#        if savefig_rootpath:
#            path = str(pathlib.Path(savefig_rootpath) / 'FIELDGASPROD.png')
#
#        return fig, ax, path
#
#    def wat_prod(self, custom_ax=None, savefig_rootpath=''):
#        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
#        if custom_ax:
#            ax = custom_ax
#
#        title = 'FIELD WATER PRODUCTION'
#        self._fluid(Sector_Keys.wat_prod_sc(), title, ax)
#
#        path = ''
#        if savefig_rootpath:
#            path = str(pathlib.Path(savefig_rootpath) / 'FIELDWATPROD.png')
#
#        return fig, ax, path
#
#    def gas_inje(self, custom_ax=None, savefig_rootpath=''):
#        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
#        if custom_ax:
#            ax = custom_ax
#
#        title = 'FIELD GAS INJECTION'
#        self._gas(Sector_Keys.gas_inje_sc(), title, ax)
#
#        path = ''
#        if savefig_rootpath:
#            path = str(pathlib.Path(savefig_rootpath) / 'FIELDGASINJE.png')
#
#        return fig, ax, path
#
#    def wat_inje(self, custom_ax=None, savefig_rootpath=''):
#        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
#        if custom_ax:
#            ax = custom_ax
#
#        title = 'FIELD WATER INJECTION'
#        self._fluid(Sector_Keys.wat_inje_sc(), title, ax)
#
#        path = ''
#        if savefig_rootpath:
#            path = str(pathlib.Path(savefig_rootpath) / 'FIELDWATINJE.png')
#
#        return fig, ax, path
#
#    def avg_pres(self, custom_ax=None, savefig_rootpath=''):
#        fig, ax = plt.subplots(figsize=self._figsize, tight_layout=self._tight_layout)
#        if custom_ax:
#            ax = custom_ax
#
#        title = 'FIELD PRESSURE'
#        legend = []
#        for tables in self.tables:
#            Graph.pressure(tables.get(Sector_Keys.sector()).df[Sector_Keys.avg_pressure()], title, ax)
#            legend.append(tables.path_to_rwo_file.stem)
#        ax.legend(legend)
#
#        path = ''
#        if savefig_rootpath:
#            path = str(pathlib.Path(savefig_rootpath) / 'FIELDAVGPRESS.png')
#
#        return fig, ax, path
#
#    def _fluid(self, key, title, ax):
#        lst = []
#        for tables in self.tables:
#            Graph.fluid(tables.get(Sector_Keys.sector()).df[key], title, ax)
#            lst.append(tables.path_to_rwo_file.stem)
#        ax.legend(lst)
#
#    def _gas(self, key, title, ax):
#        lst = []
#        for tables in self.tables:
#            Graph.gas(tables.get(Sector_Keys.sector()).df[key], title, ax)
#            lst.append(tables.path_to_rwo_file.stem)
#        ax.legend(lst)
#
#
