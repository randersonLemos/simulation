from header import *
import tensorflow as tf
from keras.layers.advanced_activations import LeakyReLU
from sklearn import preprocessing
from imblearn.over_sampling import SMOTE, SVMSMOTE, BorderlineSMOTE, ADASYN

plt.close()

omd = OtmManagerData()
omd.add_omf('18WIDE', OtmManagerFile(project_root='/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_18WIDE1_1'))
#omd.add_omf('2CSS1', OtmManagerFile(project_root='/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_2CSS1_1'))
data = omd.data().Xy()

def data_from_it(ite):
    idx = pd.IndexSlice
    return data.loc[idx[:, ite, :], :]

def Xy_from_data(data):
    X = data.iloc[:,:-1].to_numpy().reshape(len(data), 27, 1)
    y = data.iloc[:,-1].to_numpy().squeeze()
    return X,y

def more_data_with_noise(df, cycles):
    holder = pd.DataFrame(columns=df.columns)
    for i in range(cycles):
        for i in range(len(df)):
            row = df.iloc[i,:]
            choice = np.random.choice(27)
            el = row.iloc[choice]
            el = int(el + np.random.normal(0, 30, 1))
            row.iloc[choice] = el
            holder = holder.append(row)
        df = df.append(holder)
    df = df.astype('int')
    return df

data_train, data_test = data_from_it([1]).sort_values(by='NPV'), data_from_it([2]).sort_values(by='NPV')
data_train['NPV'] = (data_train['NPV'] / 1000).astype('int') / 1000; data_test['NPV'] = (data_test['NPV'] / 1000).astype('int') / 1000
data_train = data_train.set_index('NPV', append=True); data_test = data_test.set_index('NPV', append=True)
data_train['CLASS'] = -1; data_test['CLASS'] = -1
qty = 10
data_train.loc[:-qty, 'CLASS'] = 0
data_train.loc[-qty:, 'CLASS'] = 1

#data_train = more_data_with_noise(data_train, 3)

#oversample = SMOTE()
#oversample = SVMSMOTE()
oversample = BorderlineSMOTE()
#oversample = ADASYN()

Xo, yo = oversample.fit_resample(data_train.iloc[:,:-1], data_train.iloc[:,-1])
Xo['CLASS'] = yo

scale = preprocessing.MinMaxScaler()
Xo.iloc[:,:-1] = scale.fit_transform(Xo.iloc[:,:-1])

X,y = Xy_from_data(Xo)

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(27,1)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense( 1, activation=tf.nn.sigmoid),
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

count = 15
while count:
    index = np.arange(len(X))
    np.random.shuffle(index)
    model.fit(X[index,:,:], y[index], epochs=1)
    count -= 1

data_test.iloc[:,:-1] = scale.transform(data_test.iloc[:,:-1])
predictions = model.predict(Xy_from_data(data_test)[0])
data_test['CLASS'] = [1 if el > 0.49 else 0 for el in predictions]

fig, axs = plt.subplots(2, figsize=(10,8), tight_layout=True)
data_test.reset_index().plot(kind='scatter', x='NPV', y='CLASS', ax=axs[0])
data_test['CLASS'].value_counts().plot(kind='bar', ax=axs[1])
axs[0].set_title('Hits {} over 20 best sample' .format(data_test.iloc[-20:,:]['CLASS'].sum()))
axs[1].set_title(data_test['CLASS'].value_counts().to_string().replace('\n', ' | ').replace('    ', '->'))
plt.savefig('out.png')
