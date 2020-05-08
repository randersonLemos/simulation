import pandas as pd
import warnings
from collections.abc import Iterable
from .data import Data


class OtmManagerData:
    def __init__(self, project_names=[], OtmManagerFile_objs=[]):
        if not isinstance(project_names, Iterable): raise TypeError('Must be iterable...')
        if not isinstance(OtmManagerFile_objs, Iterable): raise TypeError('Must be iterable...')

        self._omfs = {}
        for name, obj in zip(project_names, OtmManagerFile_objs):
            self._omfs[name] = obj


    def add_omf(self, project_name, obj):
        if project_name in self._omfs:
            raise ValueError('Project name must be unique...')
        self._omfs[project_name] = obj


    def data(self, npv_sorted=True):
        X = self._inputs()
        y = self._outputs()

        del X['PROBABILITY']

        #del y['ITERATION']
        del y['OBJECTIVE FUNCTION']

        if npv_sorted:
            warnings.warn('Sorted from the worst to the best NPV value...')
            y = y.sort_values(by=['GROUP', 'NPV'], ascending=True)
            X = X.loc[y.index]
        return Data(X,y)


    def _inputs(self):
        Df = pd.DataFrame()
        for key in self._omfs:
            lst = []
            for path in self._omfs[key].hldg_sample_file_paths():
                lst.append(pd.read_csv(path, sep='\t'))

            df = pd.concat(lst)
            df = df.sort_values(by=['ID'])
            df = df.set_index('ID')
            df.index.name = 'RUN'
            df.index = pd.MultiIndex.from_product([[key], df.index], names=['GROUP', 'RUN'])

            Df = Df.append(df)
        return Df


    def _outputs(self):
        Df = pd.DataFrame()
        for key in self._omfs:
            df = pd.read_csv(self._omfs[key].result_file_path(), skiprows=2, sep=';')
            df = df.rename(columns={'VALUE':'NPV', 'MODEL':'ID'})
            df = df.set_index('ID')
            df.index.name = 'RUN'
            df.index = pd.MultiIndex.from_product([[key], df.index], names=['GROUP', 'RUN'])

            Df = Df.append(df)
        return Df