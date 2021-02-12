from header import *
from sklearn.decomposition import PCA
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

omd = OtmManagerData()
omd.add_omf('18WIDE', OtmManagerFile(project_root='/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_18WIDE1_1'))

X, y = omd.data().X(), omd.data().y()
idx = pd.IndexSlice

from sklearn.metrics.pairwise import euclidean_distances
index = y.sort_values(by='NPV').index
XdmatrixArr = euclidean_distances(X.loc[index,:], X.loc[index,:])
df = pd.DataFrame(data=XdmatrixArr,
        index=index.get_level_values(2),
        columns=index.get_level_values(2))

mask = np.zeros_like(df)
mask[np.triu_indices_from(mask)] = True

fig, ax = plt.subplots(figsize=(12,12), tight_layout=True)

sb.heatmap(df, mask=mask, square=True, cbar=True, ax=ax)