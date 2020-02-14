import pandas as pd
from dictionary.scripts.well_keys import Well_Keys

class Well_Table:
    dic = {}
    dic['Well state'] = Well_Keys.well_state()
    dic['DATE'] = Well_Keys.date()
    dic['TIME'] = Well_Keys.time()
    dic['Cumulative Oil SC'] = Well_Keys.cum_oil_sc()
    dic['Cumulative Gas SC'] = Well_Keys.cum_gas_sc()
    dic['Cumulative Water SC'] = Well_Keys.cum_wat_sc()
    dic['Cumulative Liquid SC'] = Well_Keys.cum_liq_sc()
    dic['Liquid Rate SC'] = Well_Keys.liq_rate_sc()
    dic['Oil Rate SC - Instantaneous On-time'] = Well_Keys.ins_oil_rate_sc()
    dic['Gas Rate SC - Instantaneous On-time'] = Well_Keys.ins_gas_rate_sc()
    dic['Water Rate SC - Instantaneous On-time'] = Well_Keys.ins_wat_rate_sc()
    dic['Oil Cut SC - %'] = Well_Keys.oil_cut_sc()
    dic['Water Cut SC - %'] = Well_Keys.wat_cut_sc()
    dic['Well Bottom-hole Pressure'] = Well_Keys.well_bhp()
    dic['Well BHP Derivative'] = Well_Keys.well_bhpd()

    def __init__(self,  lst):
        self.file = lst[0]
        self.what = lst[1][6:]

        cols = lst[2].split('\t')
        for idx, col in enumerate(cols):
            if col in self.dic: cols[idx] = self.dic[col]

        self.units = list(zip(cols, map(str.lower,lst[3].split('\t'))))

        data = [raw.split('\t') for raw in lst[4:]]
        self.df = pd.DataFrame(data, columns=cols)
        self.df = self.df.apply(pd.to_numeric, errors='ignore')
        self.df['Date'] = self.df['Date'].apply(pd.to_datetime, format='%Y/%m/%d', errors='ignore')
        self.df = self.df.set_index('Date', drop=True)
