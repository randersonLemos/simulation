import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

import seaborn as sb
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling


if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData


def build_model():
    model = keras.Sequential([
        layers.Dense(2500, activation='relu', input_shape=[len(X.keys())]),
        layers.Dense(1),
        ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'])

    return model

if __name__ == '__main__':

    omf = OtmManagerFile()
    omf.set_project_root('/media/pamonha/DATA/DRIVE/IDLHC_20200101/OTM_ICV_01S_WIDE')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')

    omd = OtmManagerData(omf)
    X, y = omd.data().X(), omd.data().y()

#    model = build_model()
#
#    EPOCHS = 5000
#
#    history = model.fit(
#            X, y,
#            epochs=EPOCHS, validation_split=0.1, verbose=0,
#            callbacks=[tfdocs.modeling.EpochDots()])
#
#    hist = pd.DataFrame(history.history)
#    hist['epoch'] = history.epoch
#    hist.tail()
#
#    plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)
#    plotter.plot({'Basic': history}, metric='mse')
#
#    import random
#    sample_space = list(range(300,3300,100))
#    np.array(random.sample(sample_space,27)).reshape(1,27)
#    bag = []
#    count = 1
#    while len(bag) < 50:
#        print('count: {}'.format(count)); count += 1
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
#
#        
#
#            