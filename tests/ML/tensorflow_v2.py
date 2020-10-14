import tensorflow as tf
from header import *
from sklearn import preprocessing
from imblearn.over_sampling import SMOTE, BorderlineSMOTE


plt.close()


dic = {}
dic[1] = ['18WIDE', '/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_18WIDE1_1']
dic[2] = ['02CSS1', '/media/pamonha/DATA/DRIVE/OTM_20200101/OTM_GOR_ICV1_2CSS1_1']


class Handle_Data:
    def __init__(self, key):
        omd = OtmManagerData()
        omd.add_omf(dic[key][0], OtmManagerFile(dic[key][1]))
        df = omd.data().Xy()
        df['NPV'] = ((df['NPV'] / 1000).astype('int')) / 1000
        self.df = df.set_index('NPV', append=True)

    def get_data_ite(self, ite):
        idx = pd.IndexSlice
        return self.df.loc[idx[:, ite, :], :]

    def set_train_data(self, df, n_class_1, shuffle):
        self.train_label  = df.sort_values(by='NPV')
        self.train_target = pd.DataFrame(columns=['CLASS'], index=self.train_label.index)
        self.train_target.iloc[:len(df) - n_class_1,:] = 0
        self.train_target.iloc[len(df) - n_class_1:,:] = 1

        if shuffle:
            self.train_label = self.train_label.sample(frac=1)
            self.train_target = self.train_target.loc[self.train_label.index, :]

        self.train_target = self.train_target.astype('int')

        return self.train_label, self.train_target

    def set_test_data(self, df):
        self.test_label = df
        self.test_target = pd.DataFrame(columns=['CLASS'], index=self.test_label.index)
        self.test_target['CLASS'] = -1

        return self.test_label


def tensorShape(df):
    if len(df.shape) == 1:
        arr = df.to_numpy().squeeze()
    else:
        arr = df.to_numpy().reshape(df.shape[0], df.shape[1], 1)
    return arr


hd = Handle_Data(1)

train_iteration = [1]
test_iteration = [2]
n_class_1 = 10

train_label, train_target = hd.set_train_data(hd.get_data_ite(train_iteration), n_class_1, shuffle=True)

oversample = BorderlineSMOTE()
train_label, train_target = oversample.fit_resample(train_label, train_target)

scale = preprocessing.MinMaxScaler()
train_label.iloc[:,:] = scale.fit_transform(train_label)

n_times = 10

for i in range(n_times):
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(27,1)),
        tf.keras.layers.Dense(250, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation=tf.nn.sigmoid),
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )


    model.fit(tensorShape(train_label), tensorShape(train_target), epochs=15)

    test_label = hd.set_test_data(hd.get_data_ite(test_iteration)).sort_index(level='NPV')
    test_label.iloc[:,:] = scale.transform(test_label)
    predictions = model.predict(tensorShape(test_label))

    test_target = pd.DataFrame(columns=['CLASS'], index=test_label.index)
    test_target['CLASS'] = [1 if el > 0.50 else 0 for el in predictions]

    fig, axs = plt.subplots(2, figsize=(5,4), tight_layout=True)
    test_target.reset_index().plot(kind='scatter', x='NPV', y='CLASS', ax=axs[0])
    test_target['CLASS'].value_counts().plot(kind='bar', ax=axs[1])
    axs[0].set_title('Hitted {} of the 20 best samples'.format(test_target.iloc[-20:].sum()[0]))
    axs[0].set_yticks([0,1])
    axs[1].set_title('Classification of the IDLHC samples')
    axs[1].set_yticks([0, 25,50])
    axs[1].set_ylabel('QTY')

    labels = test_target['CLASS'].value_counts().to_list()
    rects = axs[1].patches

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        axs[1].text(rect.get_x() + rect.get_width() / 2, height - 15, label,
                ha='center', va='bottom', fontsize=12)


    plt.savefig('./fig/out_{}.png'.format(i+1)); plt.close()
