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
    omd = OtmManagerData()
    omd.add_omf('18WIDE', OtmManagerFile(project_root='/media/beldroega/DATA/DRIVE/TRANSFER/OTM_GOR_ICV1_WIDE18_1'))

    X, y = omd.data()
    I = pd.IndexSlice

    mask = None
    n_class_0 = 0
    n_best_samples_hit = 0
    for i in range(1, 20):
        print('Traning with iteration {} and classification of {}'.format(i,i+1))

        iteration = i

        trd = TrainData(X.loc[I[:, :iteration, :], :],     y.loc[I[:, :iteration, :], :],     iteration, mask, 20)
        ted = TestData( X.loc[I[:,  iteration + 1, :], :], y.loc[I[:,  iteration + 1, :], :], iteration + 1)

        for j in range(25):
            #mo = Neural_Network(input_shape=(27, 1), epochs=15)
            mo = Random_Forest(n_estimators = 500)
            mo.train(trd.Xos, trd.yo)
            probabilities = mo.classify(ted.Xs)
            cl = ClassifiedData(ted, probabilities, 0.40)

            if (cl.y['CLASS'] == 1).sum() > 65 and (cl.y['CLASS'] == 1).sum() < 80:
               break

        save(trd, ted, cl, 'out')

        if iteration == 1:
            mask = pd.Series(True, index=X.loc[I[:, :iteration, :], :].index, name='CLASS')

        _mask = (cl.y['CLASS'] == 1)
        mask = mask.append(_mask)

        n_class_0 += (cl.y['CLASS'] == 0).sum()
        n_best_samples_hit += cl.y['CLASS'].iloc[:20].sum()

    print(n_class_0, file=open('out/n_class_0.txt', 'w'))
    print(n_best_samples_hit, file=open('out/n_best_samples_hit.txt', 'w'))
