prod_lst = []
prod_lst.append('Wildcat')
prod_lst.append('PRK014')
prod_lst.append('PRK028')
prod_lst.append('PRK045')
prod_lst.append('PRK052')
prod_lst.append('PRK060')
prod_lst.append('PRK061')
prod_lst.append('PRK083')
prod_lst.append('PRK084')
prod_lst.append('PRK085')

inje_lst = []
inje_lst.append(('IRK004',('IRK004-G','IRK004-W', ), ))
inje_lst.append(('IRK028',('IRK028-G','IRK028-W', ), ))
inje_lst.append(('IRK029',('IRK029-G','IRK029-W', ), ))
inje_lst.append(('IRK036',('IRK036-G','IRK036-W', ), ))
inje_lst.append(('IRK049',('IRK049-G','IRK049-W', ), ))
inje_lst.append(('IRK050',('IRK050-G','IRK050-W', ), ))
inje_lst.append(('IRK056',('IRK056-G','IRK056-W', ), ))
inje_lst.append(('IRK063',('IRK063-G','IRK063-W', ), ))


import os
import pandas as pd
import matplotlib.pyplot as plt
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.output.utils import get_tables
from simulation.utils.otm_manager_file import OtmManagerFile
from simulation.utils.otm_manager_data import OtmManagerData
from simulation.common.sector_keys import Sector_Keys

if __name__ == '__main__':
    omf = OtmManagerFile()
    omf.set_project_root('H:/OTM_ICV_01S_WIDE')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')
    
    omd = OtmManagerData(omf)
    data = omd.data()
    
    Df = pd.DataFrame()
    lst = []
    for path in omf.simulation_file_paths('.rwo'):
        tables = get_tables(path)
        
        model = path.stem; print(model)
        
        for well_name, alias in inje_lst:
            tables.add(tables.join(well_name, *alias)) # join xxxxxx-w and xxxxxx-g to xxxxxx
            tables.dell(alias[0]); tables.dell(alias[1])        
        
        df = tables.get(Sector_Keys.sector()).df     
        
        for prod in prod_lst:
            for col in tables.get(prod).df:
                df[col.replace('well', prod)] = tables.get(prod).df[col]
                
        for inje in inje_lst:
            for col in tables.get(inje[0]).df:
                df[col.replace('well', inje[0])] = tables.get(inje[0]).df[col] 
                
        del df['TIME']
        df.dropna(inplace=True)
        df.reset_index(inplace=True)        
        df['ITERATION'] = path.parent.stem[-1]
        df['MODEL'] = model
        
        for col in data.Xy.T[model].index:
            df[col] = data.Xy.T[model][col]
            if col == 'NPV':
                df = df.rename(columns={'NPV':'FINAL_NPV'.format()})
        
        lst.append(df)
    
    Df = pd.concat(lst).reset_index(drop=True)
    Df.to_excel('output.xlsx')