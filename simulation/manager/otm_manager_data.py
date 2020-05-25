import pandas as pd
import warnings
from collections.abc import Iterable
from .data import Data


class OtmManagerData:
    def __init__(self, project_names=[], OtmManagerFile_objs=[]):
        if not isinstance(project_names, Iterable): raise TypeError('Must be iterable...')
        if not isinstance(OtmManagerFile_objs, Iterable): raise TypeError('Must be iterable...')

        self.omfs = {}
        for name, obj in zip(project_names, OtmManagerFile_objs):
            self.omfs[name] = obj


    def add_omf(self, project_name, obj):
        if project_name in self.omfs:
            raise ValueError('Project name must be unique...')
        self.omfs[project_name] = obj


    def data(self, npv_sorted=True):
        X = self._inputs()
        y = self._outputs()

        X = X.loc[y.index]

        if npv_sorted:
            warnings.warn('Sorted from the worst to the best NPV value...')
            y = y.sort_values(by=['GROUP', 'NPV'], ascending=True)
            X = X.loc[y.index]
        return Data(X,y)


    def _inputs(self):
        Df = pd.DataFrame()
        for key in self.omfs:
            lst = []
            for path in self.omfs[key].hldg_sample_file_paths():
                try:
                    lst.append(pd.read_csv(path, sep='\t'))
                except FileNotFoundError:
                    path = self.omfs[key].result_file_path()
                    _df = pd.read_csv(path, sep=';', skiprows=2)
                    _df = _df.rename(columns={'MODEL': 'ID'})
                    del _df['TEMPLATE']
                    del _df['ITERATION']
                    del _df['NPVM']
                    _df['PROBABILITY'] = -1
                    lst.append(_df)
                    break

            df = pd.concat(lst)
            df = df.sort_values(by=['ID'])
            df = df.set_index('ID')
            df.index.name = 'RUN'
            df.index = pd.MultiIndex.from_product([[key], df.index], names=['GROUP', 'RUN'])
            del df['PROBABILITY']

            Df = Df.append(df)

        return Df


    def _outputs(self):
        Df = pd.DataFrame()
        for key in self.omfs:
            df = pd.read_csv(self.omfs[key].result_file_path(), skiprows=2, sep=';')
            if 'VALUE' in df:
                df = df.rename(columns={'VALUE':'NPV', 'MODEL':'ID'})
                del df['OBJECTIVE FUNCTION']
            else: # For MERO 2020.04
                df = df[['ITERATION', 'MODEL', 'NPVM']]
                df = df.rename(columns={'MODEL':'ID', 'NPVM': 'NPV'})
            df = df.set_index('ID')
            df.index.name = 'RUN'
            df.index = pd.MultiIndex.from_product([[key], df.index], names=['GROUP', 'RUN'])

            Df = Df.append(df)
        return Df

    def __repr__(self):
        stg = '##### OtmManagerFiles loaded #####'
        lst = []
        for key, val in self.omfs.items():
            lst.append((key, val.__repr__(), ).__repr__())
        return stg + '\n' +'\n'.join(lst)
