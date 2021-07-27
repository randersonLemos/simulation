import copy
import numpy as np
import pandas as pd
import center_gor

 
df = pd.read_csv("W:/OTM_GOR_ICV1_USS5_U1_5_16/otm_idlhc_pdf.csv", sep=';', skiprows=5)
df = df.set_index('ITERATION')
_df = df.copy()
#piv = df.pivot_table(index=['ITERATION', 'ATTRIBUTE'], columns='VALUE', values='PROBABILITY')
#piv = piv.reset_index().set_index('ITERATION')
#piv = piv.fillna(-1)

for idx in df.index.unique():
    aux = df.loc[idx,:].reset_index().set_index(['ITERATION', 'ATTRIBUTE', 'VALUE'])
    
    print('ITERATION {}'.format(idx))
    print('AUX')
    print(aux.reset_index().pivot(index='ATTRIBUTE', columns='VALUE', values='PROBABILITY'))
    
    msk = aux >= 0.8
        
    print('\nMSK')    
    print(msk.reset_index().pivot(index='ATTRIBUTE', columns='VALUE', values='PROBABILITY'))
    
    

    print('\nAUX[MSK]')    
    print(aux[msk].reset_index().pivot(index='ATTRIBUTE', columns='VALUE', values='PROBABILITY'))
    #input('Press enter...')
    
    if msk.sum().sum() >= 1:
        break
    
df = aux.copy()
df = df[~msk]
df = df.reset_index().set_index(['ITERATION', 'ATTRIBUTE'])

ih = center_gor.Interval_Handle(300, 3700, 5)

for id in df.index.unique():
    aux = df.loc[id, :]
    if aux.isnull().values.any():
        print(aux)
        ipt = input('Enter with the sequence of values for generation' +
                    'of the new values interval optimization:\n')
        print('---')        
        nih = copy.deepcopy(ih)
        lst = ipt.split(',')
        for el in lst:
            nih = nih.new_intervals(int(el))
        
        for i in range(aux.shape[0]):
            aux.iloc[i,0] = nih.lst[i]; aux.iloc[i,1] = 0.20
    df.loc[id, :] = aux


df = df.reset_index().pivot(index=['ITERATION', 'ATTRIBUTE'], columns='VALUE', values='PROBABILITY')

it = df.index.get_level_values(0).unique().item()

df = df.applymap(lambda x: '{:.2f}'.format(x))
  
print(df)

df.index = df.index.get_level_values(1).astype('str')
df.columns = df.columns.astype('str')

for att in df.index:
    for val in df.columns:
        if df.loc[att, val] != 'nan':
            df.loc[att, val] = '{:<4}'.format(val) + ' (' + df.loc[att, val] + ')' 
        else:
            df.loc[att, val] = ''
df.index = df.index + ' INT'

txt  = ''
txt += 'Keep until iteration {}\n'.format(it-1)
txt += '{} new ranges\n'.format(msk.sum().sum())
txt += df.to_string()
import re
txt = re.sub(' +', ' ', txt)
with open('W:\\new_search_space_it_{}.txt'.format(it), 'w') as fh:
    fh.write(txt)