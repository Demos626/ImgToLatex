# from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
# from tflearn.data_utils import shuffle
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import tensorflow as tf
# import scipy.misc

class Neural:
    def __init__(self):
        self.network = input_data(shape=[None, 32, 32, 1], name='input')
        self.network = conv_2d(self.network, 32, 3, activation='relu', regularizer="L2", trainable=True)
        self.network = conv_2d(self.network, 32, 3, activation='relu', regularizer="L2", trainable=True)
        self.network = max_pool_2d(self.network, 2)
        self.network = local_response_normalization(self.network)
        self.network = conv_2d(self.network, 64, 3, activation='relu', regularizer="L2", trainable=True)
        self.network = conv_2d(self.network, 64, 3, activation='relu', regularizer="L2", trainable=True)
        self.network = max_pool_2d(self.network, 2)
        self.network = local_response_normalization(self.network)
        self.network = fully_connected(self.network, 512, activation='tanh', trainable=True)
        self.network = dropout(self.network, 0.8)
        self.network = fully_connected(self.network, 256, activation='tanh', trainable=True)
        self.network = fully_connected(self.network, 115, activation='softmax')
        self.network = regression(self.network, optimizer='adam', learning_rate=0.001,
                            loss='categorical_crossentropy', name='target')
        self.model = tflearn.DNN(self.network, tensorboard_verbose=3)
        self.model.load('data\\v12.tflearn')
    # # Build a HDF5 dataset (only required once)
    # from tflearn.data_utils import build_hdf5_image_dataset
    # build_hdf5_image_dataset('test', image_shape=(64, 64), mode='folder', output_path='data.h5', categorical_labels=True)
    # from tflearn.data_utils import image_preloader
    def recognize(self, X):
    # X, Y = image_preloader ('test2', image_shape=(32,32), mode='folder', categorical_labels=True)
        X = np.reshape(X, (-1, 32, 32, 1))
        
        T = self.model.predict_label(X)
        return T
        # for i in range(len(T)):
        #     print(d[str(T[i][0]).zfill(3)])
