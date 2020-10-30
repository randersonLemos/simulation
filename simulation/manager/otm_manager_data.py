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


    def data(self):
        X = self._inputs()
        y = self._outputs()

        return X.loc[y.index], y


    def _inputs(self):
        Df = pd.DataFrame()
        for key in self.omfs:
            #for path in self.omfs[key].hldg_sample_file_paths():
            #    try:
            #        df = pd.read_csv(path, sep='\t')
            #        del df['PROBABILITY']
            #        lst.append(df)
            #    except FileNotFoundError:
            #        path = self.omfs[key].result_file_path()
            #        df = pd.read_csv(path, sep=';', skiprows=2)
            #        df = df.rename(columns={'MODEL': 'ID'})
            #        del df['TEMPLATE']
            #        del df['ITERATION']
            #        del df['NPVM']
            #        lst.append(df)
            #        break

            try:
                path = self.omfs[key].result_file_path()
                df = pd.read_csv(path, sep=';', skiprows=2)
                df = df.rename(columns={'MODEL': 'RUN', 'ITERATION': 'ITE'})
                del df['TEMPLATE']; del df['NPVM']
                df['GRP'] = key
                df = df.set_index(['GRP', 'ITE', 'RUN'])
                Df = Df.append(df)

            except FileNotFoundError:
                print('Need to be implemented...')
                raise

        return Df


    def _outputs(self):
        Df = pd.DataFrame()
        for key in self.omfs:
            df = pd.read_csv(self.omfs[key].result_file_path(), skiprows=2, sep=';')
            if 'VALUE' in df:
                df = df.rename(columns={'VALUE':'NPV', 'MODEL':'RUN', 'ITERATION':'ITE'})
                del df['OBJECTIVE FUNCTION']
            else: # For MERO 2020.04
                df = df[['ITERATION', 'MODEL', 'NPVM']]
                df = df.rename(columns={'MODEL':'RUN', 'NPVM': 'NPV', 'ITERATION':'ITE'})

            df['GRP'] = key
            df = df.set_index(['GRP', 'ITE', 'RUN'])

            Df = Df.append(df)

        return Df

    def __repr__(self):
        stg = '##### OtmManagerFiles loaded #####'
        lst = []
        for key, val in self.omfs.items():
            lst.append((key, val.__repr__(), ).__repr__())
        return stg + '\n' +'\n'.join(lst)
