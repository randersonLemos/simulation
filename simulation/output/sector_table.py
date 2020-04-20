import pandas as pd
from itertools import zip_longest
from simulation.common.sector_keys import Sector_Keys

class Sector_Table:
    dic = {}
    dic['DATE'] = Sector_Keys.date()
    dic['TIME'] = Sector_Keys.time()
    dic['Oil Recovery Factor SCTR'] = Sector_Keys.recovery_factor()
   
    dic['Water Prod Rate SCTR'] = Sector_Keys.wat_dot_prod_sc()
    dic['Water Prod Cum SCTR'] = Sector_Keys.wat_prod_sc()
    
    dic['Oil Prod Rate SCTR'] = Sector_Keys.oil_dot_prod_sc()
    dic['Oil Prod Cum SCTR'] = Sector_Keys.oil_prod_sc()
    
    dic['Gas Prod Rate SCTR'] = Sector_Keys.gas_dot_prod_sc()
    dic['Gas Prod Cum SCTR'] = Sector_Keys.gas_prod_sc()
    
    dic['Liquid Prod Rate SCTR'] = Sector_Keys.liq_dot_prod_sc()
    dic['Liquid Prod Cum SCTR'] = Sector_Keys.liq_prod_sc()
    
    dic['Water Inje Rate SCTR'] = Sector_Keys.wat_dot_inje_sc()
    dic['Water Inje Cum SCTR'] = Sector_Keys.wat_inje_sc()
    
    dic['Oil Inje Rate SCTR'] = Sector_Keys.oil_dot_inje_sc()
    dic['Oil Inje Cum SCTR'] = Sector_Keys.oil_inje_sc()
    
    dic['Gas Inje Rate SCTR'] = Sector_Keys.gas_dot_inje_sc()
    dic['Gas Inje Cum SCTR'] = Sector_Keys.gas_inje_sc()
    
    dic['Liquid Inje Rate SCTR'] = Sector_Keys.liq_dot_inje_sc()
    dic['Liquid Inje Cum SCTR'] = Sector_Keys.liq_inje_sc()
        
    dic['Ave Pres POVO SCTR'] = Sector_Keys.avg_pressure()
    dic['Gas Oil Ratio SCTR'] = Sector_Keys.gor_sc()
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
        self.df['DATE'] = self.df['DATE'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df = self.df.set_index('DATE', drop=True)
