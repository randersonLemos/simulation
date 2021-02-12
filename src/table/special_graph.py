from ._graph import *

class Special_Graph(Default):
    @Preprocessing
    def oil_prod(self, zone_lst, title=None, ax=None):
        if not title: title = 'ZONE OIL PRODUCTION'
        key = 'ZOPC'
        self._fluid(zone_lst, title, key, ax)
        return ax

    @Preprocessing
    def oil_prod_dot(self, zone_lst, title=None, ax=None):
        if not title: title = 'ZONE OIL PRODUCTION RATE'
        key = 'ZOPR'
        self._fluid_dot(zone_lst, title, key, ax)
        return ax

    @Preprocessing
    def gas_prod(self, zone_lst, title=None, ax=None):
        if not title: title = 'ZONE GAS PRODUCTION'
        key = 'ZGPC'
        self._gas(zone_lst, title, key, ax)
        return ax

    @Preprocessing
    def gas_prod_dot(self, zone_lst, title=None, ax=None):
        if not title: title = 'ZONE GAS PRODUCTION RATE'
        key = 'ZGPR'
        self._gas_dot(zone_lst, title, key, ax)
        return ax

    @Preprocessing
    def wat_prod(self, zone_lst, title=None, ax=None):
        if not title: title = 'ZONE WATER PRODUCTION'
        key = 'ZWPC'
        self._fluid(zone_lst, title, key, ax)
        return ax

    @Preprocessing
    def wat_prod_dot(self, zone_lst, title=None, ax=None):
        if not title: title = 'ZONE WATER PRODUCTION RATE'
        key = 'ZWPR'
        self._fluid_dot(zone_lst, title, key, ax)
        return ax

    @Preprocessing
    def gor(self, zone_lst, title=None, ax=None):
        if not title: title = 'ZONE GOR'
        key = 'ZGOR'
        self._gor(zone_lst, title, key, ax)
        return ax

    @Preprocessing
    def wcut(self, zone_lst, tile=None, ax=None):
        title = 'ZONE WCUT'
        key = 'ZWCUT'
        self._wcut(zone_lst, title, key, ax)
        return ax

    def _fluid(self, zone_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            #import pdb; pdb.set_trace()
            df = pd.DataFrame(tables.get(key).df[zone_lst] / 1000)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='ZONE', value_name='VALUE')

        #sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='ZONE', data=Melt, ax=ax)
        sb.lineplot(x='DATE', y='VALUE', size='RUN', hue='RUN', style='ZONE', dashes=False, markers=['^', 'X', 'o'], markersize=15, mew=1.0, mec='k', alpha=0.70, data=Melt.iloc[0::5,:], ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$msm^3$')

        self._default_ax(ax)

    def _fluid_dot(self, zone_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            #import pdb; pdb.set_trace()
            df = pd.DataFrame(tables.get(key).df[zone_lst])
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='ZONE', value_name='VALUE')

        #sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='ZONE', data=Melt, ax=ax)
        sb.lineplot(x='DATE', y='VALUE', size='RUN', hue='RUN', style='ZONE', dashes=False, markers=['^', 'X', 'o'], markersize=15, mew=1.0, mec='k', alpha=0.70, data=Melt.iloc[0::5,:], ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$sm^3/d$')

        self._default_ax(ax)

    def _gas(self, zone_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.get(key).df[zone_lst] / 1000000)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='ZONE', value_name='VALUE')

        #sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='ZONE', data=Melt, ax=ax)
        sb.lineplot(x='DATE', y='VALUE', size='RUN', hue='RUN', style='ZONE', dashes=False, markers=['^', 'X', 'o'], markersize=15, mew=1.0, mec='k', alpha=0.70, data=Melt.iloc[0::5,:], ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$mmsm^3$')

        self._default_ax(ax)

    def _gas_dot(self, zone_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.get(key).df[zone_lst] / 1000)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='ZONE', value_name='VALUE')

        #sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='ZONE', data=Melt, ax=ax)
        sb.lineplot(x='DATE', y='VALUE', size='RUN', hue='RUN', style='ZONE', dashes=False, markers=['^', 'X', 'o'], markersize=15, mew=1.0, mec='k', alpha=0.70, data=Melt.iloc[0::5,:], ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$msm^3/d$')
        self._default_ax(ax)

    def _gor(self, zone_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.get(key).df[zone_lst])
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='ZONE', value_name='VALUE')

        #sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='ZONE', data=Melt, ax=ax)
        sb.lineplot(x='DATE', y='VALUE', size='RUN', hue='RUN', style='ZONE', dashes=False, markers=['^', 'X', 'o'], markersize=15, mew=1.0, mec='k', alpha=0.70, data=Melt.iloc[0::5,:], ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$sm^3/sm^3$')

        self._default_ax(ax)

    def _wcut(self, zone_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.get(key).df[zone_lst]).fillna(0)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='ZONE', value_name='VALUE')

        #sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='ZONE', data=Melt, ax=ax)
        sb.lineplot(x='DATE', y='VALUE', size='RUN', hue='RUN', style='ZONE', dashes=False, markers=['^', 'X', 'o'], markersize=15, mew=1.0, mec='k', alpha=0.70, data=Melt.iloc[0::5,:], ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$\\%$')

        self._default_ax(ax)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:0.0f}'.format(x)))
