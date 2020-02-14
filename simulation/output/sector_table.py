import pandas as pd
from itertools import zip_longest
from dictionary.scripts.sector_keys import Sector_Keys

class Sector_Table:
    dic = {}
    dic['DATE'] = Sector_Keys.date()
    dic['TIME'] = Sector_Keys.time()
    dic['Oil Recovery Factor SCTR'] = Sector_Keys.recovery_factor()
    dic['Water Prod Rate SCTR'] = Sector_Keys.wat_rate_sc()
    dic['Water Prod Cum SCTR'] = Sector_Keys.cum_wat_sc()
    dic['Oil Prod Rate SCTR'] = Sector_Keys.oil_rate_sc()
    dic['Oil Prod Cum SCTR'] = Sector_Keys.cum_oil_sc()
    dic['Gas Prod Rate SCTR'] = Sector_Keys.gas_rate_sc()
    dic['Gas Prod Cum SCTR'] = Sector_Keys.cum_gas_sc()
    dic['Liquid Prod Rate SCTR'] = Sector_Keys.liq_rate_sc()
    dic['Liquid Prod Cum SCTR'] = Sector_Keys.cum_liq_sc()
    dic['Ave Pres POVO SCTR'] = Sector_Keys.avg_pressure()
    dic['Water Cut SCTR'] = Sector_Keys.wat_cut_sc()

    def __init__(self,  lst):
        self.file = lst[0]
        self.what = Sector_Keys.sector()
        cols = lst[1].split('\t')
        for idx, col, in enumerate(cols):
            if col in self.dic: cols[idx] = self.dic[col]
        self.units = list(zip(cols, map(str.lower, lst[4].split('\t'))))
        data = [raw.split('\t') for raw in lst[5:]]

        self.df = pd.DataFrame(data, columns=cols)
        self.df = self.df.apply(pd.to_numeric, errors='ignore')
        self.df['Date'] = self.df['Date'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df = self.df.set_index('Date', drop=True)
