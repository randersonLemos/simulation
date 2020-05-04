import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.decomposition import PCA
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.manager.otm_manager_file import OtmManagerFile
from simulation.manager.otm_manager_data import OtmManagerData

def load_data():
    omf = OtmManagerFile()
    omf.set_project_root('H:\OTM_ICV_01S_WIDE_RUNNING')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')

    return omf, OtmManagerData(omf)

if __name__ == '__main__':
    omf, omd = load_data()
    X = omd.data().X()
    y = (omd.data().y()/1000000).applymap(int)