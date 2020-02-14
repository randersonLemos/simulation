# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 14:04:55 2019

@author: randerson
"""

import re
import copy
import pathlib
import warnings
import pandas as pd
from .well_table import Well_Table
from .sector_table import Sector_Table
from .special_table import Special_Table
from dictionary.scripts.well_keys import Well_Keys
from dictionary.scripts.sector_keys import Sector_Keys

class Tables():
    def __init__(self):
        self._dic = {}

    def add(self, obj_tab):
        self._dic[obj_tab.what] = obj_tab

    def get(self, key):
        return self._dic[key]

    def dell(self, key):
        del self._dic[key]

    def join(self, key, key1, key2, dell=False):
        if type(self._dic[key1]) != type(self._dic[key2]):
            raise TypeError('Instances are not from the same class.')
        warnings.warn('For now method join accepts only objects from class Well_Table.')
        df = self._dic[key1].df + self._dic[key2].df
        df[Well_Keys.well_state()] = df[Well_Keys.well_state()].apply(lambda x: 1 if x else 0)
        df[Well_Keys.well_bhp()]   = df[Well_Keys.well_bhp()]  / 2.0
        df[Well_Keys.well_bhpd()]  = df[Well_Keys.well_bhpd()] / 2.0
        table = copy.deepcopy(self._dic[key1])
        table.what = key
        table.df = df
        if dell:
            self.dell(key1)
            self.dell(key2)
        return table

    def keys(self):
        return self._dic.keys()

    def columns(self):
        return set([col for key in self._dic for col in self._dic[key].df.columns])

    def field_recovery_factor(self):
        return self._dic[Sector_Keys.sector()].df[Sector_Keys.recovery_factor()].copy()

    def field_average_pressure(self):
        return self._dic[Sector_Keys.sector()].df[Sector_Keys.avg_pressure()].copy()

    def field_oil_production(self):
        return self._dic[Sector_Keys.sector()].df[Sector_Keys.cum_oil_sc()].copy()

    def field_gas_production(self):
        return self._dic[Sector_Keys.sector()].df[Sector_Keys.cum_gas_sc()].copy()

    def field_water_production(self):
        return self._dic[Sector_Keys.sector()].df[Sector_Keys.cum_wat_sc()].copy()

    def grp_col(self, column):
        dic = {}
        for key in self._dic:
            if column in self._dic[key].df.columns:
                dic[key] = self._dic[key].df[column]
        return pd.DataFrame.from_dict(dic)

    def grp_col_spe_well(self, well):
        dic = {}
        for key in self._dic:
            if isinstance(self._dic[key], Special_Table):
                for col in self._dic[key].df.columns:
                    if well in col:
                        dic[re.sub(r'\w\w\w\d\d\d',key,col)] = self._dic[key].df[col]
        return pd.DataFrame.from_dict(dic)

    def to_csv(self, dir):
        dir = pathlib.Path(dir)
        dir.mkdir(parents=True, exist_ok=True)

        self._dic[Sector_Keys.sector()].df.to_csv(dir / '{}.csv'.format('Field'))

        for key in self._dic:
            if isinstance(self._dic[key], Well_Table):
                df1 = self._dic[key].df
                df2 = self.grp_col_spe_well(key) # specials
                df = pd.concat([df1, df2], axis=1, sort=False)
                df.fillna(0).to_csv(dir / '{}.csv'.format(key))