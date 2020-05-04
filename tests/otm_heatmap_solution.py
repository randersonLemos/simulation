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
    omf.set_project_root('/media/pamonha/DATA/DRIVE/IDLHC_20200101/OTM_ICV_01S_WIDE')
    omf.set_simulation_folder_prefix('otm_iteration')
    omf.set_simulation_file_prefix('model')
    omf.set_result_file('otm.csv')
    omf.set_hldg_sample_file('hldg.txt')

    return omf, OtmManagerData(omf)

if __name__ == '__main__':
    omf, omd = load_data()
    X = omd.data().X()
    y = omd.data().y()

    X = X.head(5).append(X.tail(5))
    X = X.apply(lambda x: (x - x.min())/(x.max()-x.min()))

    y = y.head(5).append(y.tail(5))
    y = (y/1000000).applymap(int)


    from sklearn.metrics.pairwise import euclidean_distances
    XdmatrixArr = euclidean_distances(X,X)
    NXdmatrixArr = XdmatrixArr/XdmatrixArr.max()

    mask = np.zeros_like(NXdmatrixArr)
    mask[np.triu_indices_from(mask)] = True

    ydmatrixArr = euclidean_distances(y, y)
    NydmatrixArr = ydmatrixArr#/ydmatrixArr.max()


    with sb.plotting_context('talk'):
        fig, ax = plt.subplots(figsize=(10,10), tight_layout=True)

        sb.heatmap(NXdmatrixArr, annot=NXdmatrixArr, fmt='^0.2f', mask=mask.T, square=True, cmap=sb.cubehelix_palette(10), cbar=False, ax=ax, linewidths=0.75)
        sb.heatmap(NydmatrixArr, annot=NydmatrixArr, fmt='^4.0f', mask=mask, square=True, cmap=sb.cubehelix_palette(10), cbar=False, ax=ax, linewidth=0.75)

        ax.tick_params(labeltop=True, labelright=True)
        ticklabels = []
        for i in range(len(X.index)):
            if i == 0:
                ticklabels.append('1º wst')
            if i == 1:
                ticklabels.append('2º wst')
            if i == 2:
                ticklabels.append('3º wst')
            if i > 2 and i < int(len(X.index)/2):
                ticklabels.append('{}º wst'.format(i+1))
            if i == len(X.index) - 1:
                ticklabels.append('1º bst')
            if i == len(X.index) - 2:
                ticklabels.append('2º bst')
            if i == len(X.index) - 3:
                ticklabels.append('3º bst')
            if i >= int(len(X.index)/2) and i < len(X.index) - 3:
                ticklabels.append('{}º bst'.format(int(len(X.index)/2)-(i - int(len(X.index)/2))))

        ax.set_xticklabels(ticklabels, rotation=90)
        ax.set_yticklabels(ticklabels, rotation=0, verticalalignment='center')
        ax.xaxis.set_ticks_position('both')
        ax.yaxis.set_ticks_position('both')

        ax_divider = make_axes_locatable(ax)

        cax1 = ax_divider.append_axes("right", size="7%", pad="20%")
        cbar1 = fig.colorbar(ax.get_children()[0], cax=cax1, ticks=np.linspace(0,1,11))
        cbar1.ax.yaxis.set_ticks_position("right")
        cbar1.ax.tick_params(size=0)

        cax2 = ax_divider.append_axes("left", size="7%", pad="20%")
        cbar2 = fig.colorbar(ax.get_children()[1], cax=cax2, ticks=np.linspace(0,265,11).astype('int'))
        cbar2.ax.yaxis.set_ticks_position("left")
        cbar2.ax.tick_params(size=0)

        plt.show()