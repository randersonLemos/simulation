import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

OtmManagerFile.set_default_simulation_folder_prefix('otm_IT')
OtmManagerFile.set_default_simulation_file_prefix('run')
OtmManagerFile.set_default_result_file('otm.otm.csv')
OtmManagerFile.set_default_hldg_sample_file('hldg.txt')

import pandas as pd

from Data import *

from sklearn import preprocessing
from imblearn.over_sampling import SMOTE, SVMSMOTE, BorderlineSMOTE, ADASYN

Aux.oversampler = BorderlineSMOTE()
Aux.scaler = preprocessing.MinMaxScaler()

from Models import *

from Registers import *

plt.close()

if __name__ == "__main__":

    THRESHOLD   = 0.20
    NUM_MODELS  = 10
    NUM_CLASS_1 = 10

    NUM_CLASS_0 = 0
    NUM_BEST_SAMPLES = 0

    omd = OtmManagerData()
    omd.add_omf('18WIDE'
            , OtmManagerFile(project_root='/media/beldroega/DATA/DRIVE/TRANSFER/OTM_GOR_ICV1_WIDE18_1')
            )

    X, y = omd.data()
    I = pd.IndexSlice

    mask = pd.Series(True, index=X.loc[I[:, 1, :], :].index, name='CLASS')
    for i in range(1, 20):
        stg  = '>\n>\n>\n>\n>\n'
        stg += 'Traning with iteration {} and classification of iteration {}'.format(i, i+1)
        stg += '<\n<\n<\n<\n<\n'
        print(stg)

        iteration = i

        trd = TrainData(X.loc[I[:, :iteration, :], :], y.loc[I[:, :iteration, :], :]
                , iteration
                , mask
                , NUM_CLASS_1
                )

        ted = TestData( X.loc[I[:,  iteration + 1, :], :], y.loc[I[:,  iteration + 1, :], :]
                , iteration + 1
                )

        probabilities = np.zeros((100, 1), dtype='float32')
        for j in range(NUM_MODELS):
            stg  = '\n\n\n'
            stg += 'Model {}'.format(j)
            stg += '\n\n\n'
            print(stg)

            mo = Neural_Network(input_shape=(27, 1), epochs=15)
            mo.train(trd.Xos, trd.yo)
            probs = mo.classify(ted.Xs)
            probabilities += probs

        probabilities /= NUM_MODELS

        cl = ClassifiedData(ted, probabilities, THRESHOLD)
        save(trd, ted, cl, 'out')

        _mask = (cl.y['CLASS'] == 1)
        mask = mask.append(_mask)

        NUM_CLASS_0 += (cl.y['CLASS'] == 0).sum()
        NUM_BEST_SAMPLES += cl.y['CLASS'].iloc[:20].sum()

    print('NUM_CLASS_0 {}'.format(NUM_CLASS_0), file=open('out/out.txt', 'w'))
    print('NUM_BEST_SAMPLES {}'.format(NUM_BEST_SAMPLES), file=open('out/out.txt', 'a'))
