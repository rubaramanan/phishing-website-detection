import os
from datetime import datetime
from pathlib import Path

import numpy as np
from keras.layers import Input, Dense
from keras.models import Sequential, load_model
from keras.utils import to_categorical


class PhishDetectorFeedForward:
    def __init__(self):
        self.model = Sequential(
            [
                Input((10,)),
                Dense(256, activation='relu'),
                Dense(256, activation='relu'),
                Dense(2, activation='softmax')
            ]
        )

        self.model.compile(optimizer='Adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def train(self, X, y, X_val=None, y_val=None, batch_size=32, epochs=10):
        y = to_categorical(y,
                           num_classes=2)
        y_val = to_categorical(y_val,
                               num_classes=2)
        self.model.fit(X,
                       y,
                       batch_size=batch_size,
                       epochs=epochs,
                       validation_data=(X_val, y_val) if X_val is not None and y_val is not None else None)

    def test(self, X):
        pred = self.model.predict(X)
        labels = {0: 'Phish',
                  1: 'Legitimate'}
        key = np.argmax(pred)
        return labels[key]

    def save_model(self, path):
        self.model.save(path)

    def load_models(self, path):
        paths = sorted(Path(path).iterdir(), key=os.path.getmtime)
        print(paths[0])
        self.model = load_model(paths[0])
