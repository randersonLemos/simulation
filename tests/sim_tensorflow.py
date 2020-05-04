import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sb
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print('Tensorflow version: {}'.format(tf.__version__))

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

def build_model():
    model = keras.Sequential([
        layers.Dense(1000, activation='relu', input_shape=[len(X.keys())]),
        layers.Dense(1000, activation='relu', input_shape=[len(X.keys())]),
        layers.Dense(1000, activation='relu', input_shape=[len(X.keys())]),
        layers.Dense(1),
        ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mse','mae'])

    return model

def get_data():
    prod_lst = []
    prod_lst.append('Wildcat'); prod_lst.append('PRK014'); prod_lst.append('PRK028')
    prod_lst.append('PRK045');  prod_lst.append('PRK052'); prod_lst.append('PRK060')
    prod_lst.append('PRK061');  prod_lst.append('PRK083'); prod_lst.append('PRK084')
    prod_lst.append('PRK085')

    inje_lst = []
    inje_lst.append(('IRK004',('IRK004-G','IRK004-W', ), )); inje_lst.append(('IRK028',('IRK028-G','IRK028-W', ), ))
    inje_lst.append(('IRK029',('IRK029-G','IRK029-W', ), )); inje_lst.append(('IRK036',('IRK036-G','IRK036-W', ), ))
    inje_lst.append(('IRK049',('IRK049-G','IRK049-W', ), )); inje_lst.append(('IRK050',('IRK050-G','IRK050-W', ), ))
    inje_lst.append(('IRK056',('IRK056-G','IRK056-W', ), )); inje_lst.append(('IRK063',('IRK063-G','IRK063-W', ), ))


    from simulation.output.utils import get_tables
    from simulation.output.sector_keys import Sector_Keys

    lst = []
    models = []
    for path in omf.simulation_file_paths('.rwo'):
        tables = get_tables(path)
        #tables.date_range(end='2040')

        model = path.stem; print(model)
        models.append(model)

        for well_name, alias in inje_lst:
            tables.add(tables.join(well_name, *alias, dell=True)) # join xxxxxx-w and xxxxxx-g to xxxxxx

        df = pd.DataFrame()
        df = tables.get(Sector_Keys.sector()).df

        for prod in prod_lst:
            for col in tables.get(prod).df:
                df[col.replace('WELL', prod)] = tables.get(prod).df[col]

        for inje in inje_lst:
            for col in tables.get(inje[0]).df:
                df[col.replace('WELL', inje[0])] = tables.get(inje[0]).df[col]

        for prod in prod_lst:
            for col in tables.grp_col_spe_well(prod):
                df['{} {}'.format(prod,col.replace('_', ' '))] = tables.grp_col_spe_well(prod)[col]

        for inje in inje_lst:
            for col in tables.grp_col_spe_well(inje[0]):
                df['{} {}'.format(inje[0],col.replace('_', ' '))] = tables.grp_col_spe_well(inje[0])[col]

        for col in df:
            if 'WPC' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'WATER CUMU SC', split[2])] = df[col]
                del df[col]

            if 'WPR' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'WATER RATE SC', split[2])] = df[col]
                del df[col]

            if 'GPC' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'GAS CUMU SC', split[2])] = df[col]
                del df[col]

            if 'GPR' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'GAS RATE SC', split[2])] = df[col]
                del df[col]

            if 'OPC' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'OIL CUMU SC', split[2])] = df[col]
                del df[col]

            if 'OPR' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'OIL RATE SC', split[2])] = df[col]
                del df[col]

            if 'GOR Z' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'GOR SC', split[2])] = df[col]
                del df[col]

            if 'WCUT Z' in col:
                split = col.split()
                df['{} {} ({})'.format(split[0], 'WCUT SC', split[2])] = df[col]
                del df[col]

        del df['TIME']
        df.dropna(inplace=True)
        lst.append(df)

        #if model == 'model0003': break

    return lst

def lst_df_to_df_ml(lst_df):
    lst = []
    for df in lst_df:
        for col in df:
            if 'AVG' in col:
                del df[col]

            if 'STATE' in col:
                del df[col]

            if 'RECOVERY' in col:
                del df[col]

            if 'GOR' in col:
                del df[col]

            if 'WCUT' in col:
                del df[col]

            if 'OCUT' in col:
                del df[col]

            if 'LIQ' in col:
                del df[col]

            if 'BHPD' in col:
                del df[col]

            if 'OIL' in col:
                if not '(Z' in col:
                    del df[col]

            if 'GAS' in col:
                if not '(Z' in col:
                    del df[col]

            if 'WATER' in col:
                if not '(Z' in col:
                    del df[col]

        df = df[df.index < '2040']
        df = df.iloc[slice(0,-1,2)]
        lst.append(df.stack())
    print('\n'.join(list(df.columns)), file=open('columns_selected.txt', 'w'))
    return pd.concat(lst, axis=1, keys=['model{:04d}'.format(idx+1) for idx in range(len(lst))]).T



if __name__ == '__main__':
    omf = OtmManagerFile()
    omf.set_project_root('/media/pamonha/DATA/DRIVE/IDLHC_20200101/OTM_ICV_01S_WIDE')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')
    omd = OtmManagerData(omf)

    import pickle
    if os.path.exists('./Dfs.pickle'):
        with open('./Dfs.pickle', 'rb') as f:
            Dfs = pickle.load(f)
    else:
        Dfs = get_data()
        with open('./Dfs.pickle', 'wb') as f:
            pickle.dump(Dfs, f)

    X = lst_df_to_df_ml(Dfs)
    Xtrai = X.iloc[:-100]
    Xtest = X.iloc[-100:]

    y = omd.data().y().loc[X.index]; y = (y/1000000).applymap(int)
    ytrai = y.loc[Xtrai.index]
    ytest = y.loc[Xtest.index]

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))

    model = build_model()

    EPOCHS = 500

    history = model.fit(
            scaler.fit_transform(Xtrai), ytrai,
            epochs=EPOCHS, validation_split=0.2, verbose=0,
            callbacks=[tfdocs.modeling.EpochDots()])

    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    hist.tail()

    plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)
    plotter.plot({'Basic': history}, metric='mse')

#        arr = np.array(random.sample(sample_space,27)).reshape(1,27)
#        pre = model.predict(arr).item()
#        if pre > y.max().item()*1.1:
#            print(pre, arr)
#            bag.append((pre, arr ))
#
#    for model in X.T:
#        si_npv = y.T[model].to_numpy()
#        si_arr = X.T[model].to_numpy()
#        for dl_npv, dl_arr in bag:
#            if np.linalg.norm(si_arr - dl_arr) < 4000:
#                print('npv: {}, arr: {} (si)'.format(si_npv.item(), si_arr.squeeze().tolist()))
#                print('npv: {}, arr: {} (dl)'.format(dl_npv, dl_arr.squeeze().tolist()))