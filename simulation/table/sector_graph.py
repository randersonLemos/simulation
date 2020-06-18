from ._graph import *
from .sector_keys import Sector_Keys

class Sector_Graph(Default):
    @Preprocessing
    def oil_prod(self, title=None, ax=None):
        if not title: title = 'FIELD OIL PRODUCTION'
        self._fluid(title, Sector_Keys.oil_prod_sc(), ax)
        return ax

    @Preprocessing
    def gas_prod(self, title=None, ax=None):
        if not title: title = 'FIELD GAS PRODUCTION'
        self._gas(title, Sector_Keys.gas_prod_sc(), ax)
        return ax

    @Preprocessing
    def wat_prod(self, title=None, ax=None):
        if not title: title = 'FIELD WATER PRODUCTION'
        self._fluid(title, Sector_Keys.wat_prod_sc(), ax)
        return ax

    @Preprocessing
    def gas_inje(self, title=None, ax=None):
        if not title: title = 'FIELD GAS INJECTION'
        self._gas(title, Sector_Keys.gas_inje_sc(), ax)
        return ax

    @Preprocessing
    def wat_inje(self, title=None, ax=None):
        if not title: title = 'FIELD WATER INJECTION'
        self._fluid(title, Sector_Keys.wat_inje_sc(), ax)
        return ax

    @Preprocessing
    def avg_pres(self, title=None, ax=None):
        if not title: title = 'FIELD AVG. PRESSURE'
        self._avg_pres(title, Sector_Keys.avg_pressure(), ax)
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


    def _gas(self, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = tables.get(Sector_Keys.sector()).df[key].to_frame() / 1000000
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='VAR', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$mmsm^3$')
        self._default_ax(ax)

    def _avg_pres(self, title, key, ax):
        Df = pd.DataFrame()
        lst = []
        for tables in self.tables:
            df = tables.get(Sector_Keys.sector()).df[key].to_frame()
            df['RUN'] = tables.path_to_rwo_file.stem
            lst.append(df)
        Df = pd.concat(lst).reset_index()
        Melt = Df.melt(id_vars=['DATE', 'RUN'], var_name='VAR', value_name='VALUE')

        sb.lineplot(x='DATE', y='VALUE', style='RUN', data=Melt, ax=ax)

        ax.set_title(title)
        ax.set_ylabel('$kg/cm^2$')

        self._default_ax(ax)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{:0.0f}'.format(x)))
        ax.set_ylim(ymin=Melt['VALUE'].min()-10)
