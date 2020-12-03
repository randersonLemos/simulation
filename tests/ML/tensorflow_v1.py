from header import *

plt.close()

class Aux:

    oversampler = None
    scaler = None

class TrainData(Aux):

    def __init__(self, X, y, iteration, qty, mask=None):
        self.X = X.copy()
        self.y = y.copy()

        if not isinstance(mask, type(None)):
            self.X = self.X[mask]
            self.y = self.y[mask]
            #import pdb; pdb.set_trace()

        self.iteration = iteration
        self.qty = qty

        self._processing()

    def _processing(self):

        self.y['NPV'] = ((self.y['NPV'] / 1000).astype(int)) / 1000

        self.y = self.y.sort_values(by='NPV', ascending=False)
        self.X = self.X.loc[self.y.index, :]

        self.y['CLASS'] = -1
        self.y.iloc[:self.qty, -1] = 1
        self.y.iloc[self.qty:, -1] = 0

        self.Xo = self.X.copy()
        self.yo = self.y.iloc[:,-1].copy()
        if self.oversampler:
            self.Xo, self.yo = self.oversampler.fit_resample(self.Xo, self.yo)

        self.Xos = self.Xo.copy()
        if self.scaler:
            self.Xos = self.scaler.fit_transform(self.Xos)
            self.Xos = pd.DataFrame(self.Xos, index=self.Xo.index, columns=self.Xo.columns)

class TestData(Aux):

    def __init__(self, X, y, iteration):
        self.X = X.copy()
        self.y = y.copy()
        self.iteration = iteration

        self._processing()

    def _processing(self):

        self.y['NPV'] = ((self.y['NPV'] / 1000).astype(int)) / 1000

        self.y = self.y.sort_values(by='NPV', ascending=False)
        self.X = self.X.loc[self.y.index, :]

        self.Xs = self.X.copy()
        if self.scaler:
            self.Xs = self.scaler.transform(self.Xs)
            self.Xs = pd.DataFrame(self.Xs, index=self.X.index, columns=self.X.columns)

class Classifier:

    def __init__(self, y, probs, threshold):
        self.y = y.copy()

        self.y['PROBS'] = probs
        self.y['CLASS'] = [1 if el > threshold else 0 for el in probs]

class Model:

    def __init__(self, kind):
        self.kind = kind

        self._processing()

    def _processing(self):
        if self.kind == 'neural_network':
            self.model = self._neural_network()

    def _neural_network(self):
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

        return model

    def train(self, X, y, epochs=None):
        if self.kind == 'neural_network':
            self.epochs = epochs
            if self.epochs == None:
                raise ValueError('Define number of epochs...')

            count = self.epochs

            while count:
                index = np.arange(len(X))
                np.random.shuffle(index)
                X.to_numpy()[index,:]
                self.model.fit(X.to_numpy()[index,:], y.to_numpy()[index], epochs=1)
                count -= 1

    def classify(self, X):
        if self.kind == 'neural_network':
            return  self.model.predict(X)

def plot(TrainDataObj, TestDataObj, ClassifierObj, savefig_root):
    trd = TrainDataObj
    ted = TestDataObj
    cl  = ClassifierObj

    fig, axs = plt.subplots(1,2, figsize=(10,8), tight_layout=True)

    title  = 'Tranning with iteration {} data and classification of iteration {} data'.format(trd.iteration, ted.iteration)
    title += '\nTrain data size {}'.format(len(trd.X))
    title += '\nTrain data oversampled size {}'.format(len(trd.Xos))
    title += '\nHit {} over 20 best samples'.format(cl.y['CLASS'].iloc[:20].sum())
    fig.suptitle(title, fontsize=20)

    _x = cl.y['CLASS'].tolist()
    _y = cl.y['NPV'].astype('int').tolist()

    axs[0].scatter(_x, _y, s=250)
    axs[0].scatter(_x[:20], _y[:20], s=250)

    axs[0].set_ylabel('NPV [MM$]')
    axs[0].set_xlabel('CLASS')

    axs[0].set_xticks([0,1])
    axs[0].set_xlim([-0.25, 1.25])

    axs[0].yaxis.set_major_locator(ticker.LinearLocator(5))
    axs[0].yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))

    _x = [0,1]
    _y = cl.y['CLASS'].value_counts()[_x].tolist()
    axs[1].bar(_x, _y)

    axs[1].set_ylabel('Qty')
    axs[1].set_xlabel('CLASS')

    axs[1].set_xticks([0,1])
    axs[1].set_yticks([0, 25, 50 , 75, 100])

    rects = axs[1].patches
    labels = _y

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        axs[1].text(rect.get_x() + rect.get_width() / 2, height / 2, label,
                ha='center', va='center', fontsize=18)

    plt.savefig('{}/ml_it_{}_it_{}'.format(savefig_root, trd.iteration, ted.iteration))
    plt.close()

if __name__ == "__main__":
    omd = OtmManagerData()
    omd.add_omf('18WIDE', OtmManagerFile(project_root='/media/beldroega/DATA/DRIVE/TRANSFER/OTM_GOR_ICV1_WIDE18_1'))
    X, y = omd.data()
    I = pd.IndexSlice

    Aux.oversampler = BorderlineSMOTE()
    Aux.scaler = preprocessing.MinMaxScaler()

    mask = None
    n_class_0 = 0
    for i in range(1, 20):
        iteration = i

        trd = TrainData(X.loc[I[:, iteration, :], :], y.loc[I[:, iteration, :], :], iteration, 10, mask)
        ted = TestData(X.loc[I[:, iteration + 1, :], :], y.loc[I[:, iteration + 1, :], :], iteration + 1)

        for j in range(25):
            mo = Model(kind='neural_network')
            mo.train(trd.Xos, trd.yo, epochs=15)
            prob = mo.classify(ted.Xs)

            cl = Classifier(ted.y, prob, 0.40)

            if (cl.y['CLASS'] == 1).sum() > 65 and (cl.y['CLASS'] == 1) < 85):
                break

        plot(trd, ted, cl, 'fig')

        mask = (cl.y['CLASS'] == 1)
        n_class_0 += (cl.y['CLASS'] == 0).sum()
