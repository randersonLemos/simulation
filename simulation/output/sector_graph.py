from .graph import Graph
from dictionary.scripts.sector_keys import Sector_Keys

class Sector_Graph:
    def __init__(self, table_obj):
        self.table_obj = table_obj

    def fluids(self):
        Graph.fluid(self._df_oil(), 'Field Oil Production')
        Graph.fluid(self._df_gas(), 'Field Gas Production')
        Graph.fluid(self._df_wat(), 'Field Water Production')

    def pressure(self):
        Graph.pressure(self.table_obj.\
                field_average_pressure(), 'Field Avg. Pressure')

    def recovery_factor(self):
        Graph.percent(self.table_obj.\
                field_recovery_factor(), 'Field Recovery Factor')

    def _df_oil(self):
        tab = self.table_obj
        df = tab.get(Sector_Keys.sector()).df
        return df[Sector_Keys.cum_oil_sc()]

    def _df_gas(self):
        tab = self.table_obj
        df = tab.get(Sector_Keys.sector()).df
        return df[Sector_Keys.cum_gas_sc()]

    def _df_wat(self):
        tab = self.table_obj
        df = tab.get(Sector_Keys.sector()).df
        return df[Sector_Keys.cum_wat_sc()]

    def show(self):
        Graph.show()

