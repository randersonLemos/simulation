import pandas as pd
import numpy as np

df = pd.read_csv("W:/OTM_GOR_ICV1_USS5_U1_3_1/otm_idlhc_pdf.csv", sep=';', skiprows=5)
piv = df.pivot_table(index=['ITERATION', 'ATTRIBUTE'], columns='VALUE', values='PROBABILITY')

I = pd.IndexSlice
its = piv.index.get_level_values(0).unique()
for it in its:
    cur = piv.loc[I[it,:],:]
    msk = cur > 0.8
    print(cur[msk])
    if msk.sum().sum():
        break
    
cur = cur[~msk]    
cur = cur.astype('str')
cur.index = cur.index.get_level_values(1).astype('str')
cur.columns = cur.columns.astype('str')

for att in cur.index:
    for val in cur.columns:
        cur.loc[att, val] = val + ' (' + cur.loc[att, val].upper() + ')' 
    
cur.index = cur.index + ' INT'

txt  = ''
txt += 'From iteration {}\n'.format(it)
txt += '{} new ranges\n'.format(msk.sum().sum())
txt += cur.to_string()

with open('W:\\new_search_space_it_{}.txt'.format(it), 'w') as fh:
    fh.write(txt)