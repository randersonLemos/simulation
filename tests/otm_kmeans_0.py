import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
if os.path.dirname(os.path.dirname(os.path.abspath(__file__))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simulation.utils.otm_manager_file import OtmManagerFile
from simulation.utils.otm_manager_data import OtmManagerData

if __name__ == '__main__':   
    omf = OtmManagerFile()
    omf.set_project_root('H:/OTM_ICV_01S_WIDE')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')
    
    omd = OtmManagerData(omf)
    
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=20)
    kmeans.fit(omd.data().X.to_numpy())