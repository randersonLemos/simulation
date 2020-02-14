import copy
import pandas
from pathlib import Path


class FieldDf:
    csvName = ''
    csvRoot = Path('')
    csvSep  = ','
    simsFolder = Path('')
    dfIndex = ''
    dfColsSelect = []
    dfColsRename = {}

    def __init__(self, name, group_folder, sim_folder):
        self.name = name
        self.groupFolder = group_folder
        self.simFolder = sim_folder
        self.df = pandas.read_csv(self.csvRoot / self.simsFolder /
                                  self.groupFolder / self.simFolder / self.csvName,
                                  sep=self.csvSep)

        if self.dfIndex: self.df = self.df.set_index(self.dfIndex)
        if self.dfColsSelect: self.df = self.df[self.dfColsSelect]
        if self.dfColsRename: self.df = self.df.rename(columns=self.dfColsRename)

        self.simDivisor= ''

    def div(self, other_obj):
        df = (self.df.iloc[:,:] / other_obj.df).fillna(0)
        copy_self = copy.deepcopy(self)
        copy_self.df = df
        copy_self.simDivisor = other_obj.groupFolder + '/' + other_obj.simFolder
        return copy_self
