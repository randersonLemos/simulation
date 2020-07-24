from ._graph import *
from .well_keys import Well_Keys

class Well_Graph(Default):
    @Preprocessing
    def oil_prod(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL OIL PRODUCTION'
        self._fluid(well_lst, title, Well_Keys.oil_prod_sc(), ax)
        return ax

    @Preprocessing
    def oil_prod_dot(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL OIL PRODUCTION RATE'
        self._fluid_dot(well_lst, title, Well_Keys.oil_prod_dot_sc(), ax)
        return ax

    @Preprocessing
    def gas_prod(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL GAS PRODUCTION'
        self._gas(well_lst, title, Well_Keys.gas_prod_sc(), ax)
        return ax

    @Preprocessing
    def gas_prod_dot(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL GAS PRODUCTION RATE'
        self._gas_dot(well_lst, title, Well_Keys.gas_prod_dot_sc(), ax)
        return ax

    @Preprocessing
    def wat_prod(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL WATER PRODUCTION'
        self._fluid(well_lst, title, Well_Keys.wat_prod_sc(), ax)
        return ax

    @Preprocessing
    def wat_prod_dot(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL WATER PRODUCTION RATE'
        self._fluid_dot(well_lst, title, Well_Keys.wat_prod_dot_sc(), ax)
        return ax

    @Preprocessing
    def gor(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL GOR'
        self._gor(well_lst, title, Well_Keys.gor_sc(), ax)
        return ax

    @Preprocessing
    def wcut(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL WCUT'
        self._wcut(well_lst, title, Well_Keys.wat_cut_sc(), ax)
        return ax

    @Preprocessing
    def bhp(self, well_lst, title=None, ax=None):
        if not title: title = 'WELL BHP'
        self._bhp(well_lst, title, Well_Keys.bhp(), ax)
        return ax

    def _fluid(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst] / 1000)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        if len(well_lst) == 1 or isinstance(well_lst, str):
            sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='RUN', data=Melt, ax=ax)
        else:
            sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$msm^3$')

        self._default_ax(ax)

    def _fluid_dot(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst])
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        if len(well_lst) == 1 or isinstance(well_lst, str):
            sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='RUN', data=Melt, ax=ax)
        else:
            sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$sm^3/d$')
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

        if len(well_lst) == 1 or isinstance(well_lst, str):
            sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='RUN', data=Melt, ax=ax)
        else:
            sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$mmsm^3$')

        self._default_ax(ax)

    def _gas_dot(self, well_lst, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = pd.DataFrame(tables.grp_col(key)[well_lst] / 1000)
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='WELL', value_name='VALUE')

        if len(well_lst) == 1 or isinstance(well_lst, str):
            sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='RUN', data=Melt, ax=ax)
        else:
            sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$msm^3/d$')

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

        if len(well_lst) == 1 or isinstance(well_lst, str):
            sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='RUN', data=Melt, ax=ax)
        else:
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

        if len(well_lst) == 1 or isinstance(well_lst, str):
            sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='RUN', data=Melt, ax=ax)
        else:
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

        if len(well_lst) == 1 or isinstance(well_lst, str):
            sb.lineplot(x='DATE', y='VALUE', hue='RUN', style='RUN', data=Melt, ax=ax)
        else:
            sb.lineplot(x='DATE', y='VALUE', hue='WELL', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$kg/cm^2$')

        self._default_ax(ax)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:0.0f}'.format(x)))
        ax.set_ylim(ymin=Melt['VALUE'].min()-10)
