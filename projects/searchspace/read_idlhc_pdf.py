import pandas as pd
import numpy as np

df = pd.read_csv("./otm_idlhc_pdf.csv", sep=';', skiprows=5)
#df = df.loc[  df['ITERATION'] == df['ITERATION'].max()  ]
piv = df.pivot_table(index=['ITERATION', 'ATTRIBUTE'], columns='VALUE', values='PROBABILITY')

lst = []
iteration = 0
for index, row in piv.iterrows():  
    stg = ''
    if iteration != index[0]:
        stg  += 'ITERATION {}\n'.format(index[0])
        iteration = index[0]
        
    stg += '{} INT'.format(index[1])
    for index, el in row.items():
        if not np.isnan(el):
            stg += ' {:4d} ({:4.2f})'.format(index, el)
    lst.append(stg)

print('\n'.join(lst))
