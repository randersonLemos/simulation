import pandas as pd
import warnings
from .data import Data


class OtmManagerData:
    def __init__(self, OtmManagerFile):
        self.omf = OtmManagerFile


    def data(self, npv_sorted=True):
        X = self._inputs()
        y = self._outputs()

        del X['PROBABILITY']
        #del y['ITERATION']

        if npv_sorted:
            warnings.warn('Sorted from the worst to the best NPV value...')
            y = y.sort_values(by='NPV', ascending=True)
            X = X.loc[y.index]
        return Data(X,y)


    def _inputs(self):
        lst = []
        for path in self.omf.hldg_sample_file_paths():
            lst.append(pd.read_csv(path, sep='\t'))

        df = pd.concat(lst)
        df = df.sort_values(by=['ID'])
        df = df.set_index('ID')
        return df


    def _outputs(self):
        df = pd.read_csv(self.omf.result_file_path(), skiprows=2, sep=';')
        df = df.rename(columns={'VALUE':'NPV', 'MODEL':'ID'})
        df = df.set_index('ID')

        del df['OBJECTIVE FUNCTION']

        return df