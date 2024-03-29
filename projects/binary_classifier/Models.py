import numpy as np

import tensorflow as tf; print(tf.__version__)
from tensorflow import keras
from tensorflow.keras import layers
from keras.layers.advanced_activations import LeakyReLU

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

class Neural_Network:
    def __init__(self, input_shape, epochs):
        self.input_shape = input_shape
        self.epochs = epochs

        self._processing()

    def _processing(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=self.input_shape), # input_shape: (a, b)
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense( 1, activation=tf.nn.sigmoid),
        ])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )

        self.model = model

    def train(self, X, y):
        count = self.epochs

        while count:
            index = np.arange(len(X))
            np.random.shuffle(index)
            X.to_numpy()[index,:]
            self.model.fit(X.to_numpy()[index,:], y.to_numpy()[index], epochs=1)
            count -= 1

    def classify(self, X):
        return  self.model.predict(X)


from sklearn.ensemble import RandomForestClassifier

class Random_Forest:
    def __init__(self, n_estimators):
        self.n_estimators= n_estimators

        self._processing()

    def _processing(self):
        # Create the model with 100 trees
        model = RandomForestClassifier(  n_estimators = 100
                                       , bootstrap = True
                                       , max_features = 'auto'
                                       , verbose = 1
                                      )

        self.model = model

    def train(self, X, y):
        # Fit on training data
        self.model.fit(X, y)

    def classify(self, X):
        return  self.model.predict_proba(X)[:, 1]


