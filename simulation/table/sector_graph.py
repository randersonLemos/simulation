import matplotlib.pyplot as plt
from .graph import Graph
from .sector_keys import Sector_Keys as SK

class Sector_Graph:
    def __init__(self, tables):
        if not isinstance(tables, list):
            lst = []
            lst.append(tables)
            self.tables = lst
            return

        self.tables = tables

    def _fluid(self, SK_key, title):
        fig, ax = plt.subplots()
        legend = []
        for tables in self.tables:
            Graph.fluid(ax, tables.get(SK.sector()).df[SK_key], title)
            legend.append(tables.path_to_rwo_file.stem)
        ax.legend(legend)

    def _gas(self, SK_key, title):
        fig, ax = plt.subplots()
        legend = []
        for tables in self.tables:
            Graph.gas(ax, tables.get(SK.sector()).df[SK_key], title)
            legend.append(tables.path_to_rwo_file.stem)
        ax.legend(legend)

    def oil_prod(self, custom_title=''):
        title = 'Field oil production'
        if custom_title:
            title = custom_title
        self._fluid(SK.oil_prod_sc(), title)

    def wat_prod(self, custom_title=''):
        title = 'Field water production'
        if custom_title:
            title = custom_title
        self._fluid(SK.wat_prod_sc(), title)

    def gas_prod(self, custom_title=''):
        title = 'Field gas production'
        if custom_title:
            title = custom_title
        self._gas(SK.gas_prod_sc(), title)

    def oil_inje(self, custom_title=''):
        title = 'Field oil injection'
        if custom_title:
            title = custom_title
        self._fluid(SK.oil_inje_sc(), title)

    def wat_inje(self, custom_title=''):
        title = 'Field water injection'
        if custom_title:
            title = custom_title
        self._fluid(SK.wat_inje_sc(), title)

    def gas_inje(self, custom_title=''):
        title = 'Field gas injection'
        if custom_title:
            title = custom_title
        self._gas(SK.gas_inje_sc(), title)

    def avg_pres(self, custom_title=''):
        title = 'Field pressure'
        if custom_title:
            title = custom_title

        fig, ax = plt.subplots()
        legend = []
        for tables in self.tables:
            Graph.pressure(ax, tables.get(SK.sector()).df[SK.avg_pressure()], title)
            legend.append(tables.path_to_rwo_file.stem)
        ax.legend(legend)

    def recovery_factor(self):
        Graph.percent(self.table_obj.\
                field_recovery_factor(), 'Field Recovery Factor')

    def tight_layout(self):
        plt.tight_layout()

    def show(self):
        Graph.show()

