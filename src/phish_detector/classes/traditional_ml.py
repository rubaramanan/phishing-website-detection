from sklearn.linear_model import LogisticRegression
import numpy as np
from pathlib import Path
import pickle
import os


class PhishDetectorLR:
    def __init__(self):
        self.model = LogisticRegression(C=1, max_iter=100, penalty='l1', solver='saga')

    def train(self, X, y, X_val=None, y_val=None):
        self.model.fit(X, y)
        score = self.model.score(X_val, y_val)
        print(f"LR's validation accuracy: {score}")

    def test(self, X):
        pred = self.model.predict(X)
        labels = {0: 'Legitimate',
                  1: 'Phish'}
        key = pred.item()
        return labels[key]

    def save_model(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)

    def load_models(self, path):
        paths = sorted(Path(path).iterdir(), key=os.path.getmtime)
        with open(paths[0], 'rb') as f:
            self.model = pickle.load(f)
