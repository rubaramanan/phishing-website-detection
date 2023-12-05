from src.phish_detector.train.feed_forwad import feedforward_train
from src.phish_detector.train.state_of_the_art import sota_train
from src.phish_detector.train.ensemble import xgb_train
from src.phish_detector.train.traditional_ml import lr_train


def train(X, y, X_val, y_val, epochs, batch_size):
    feedforward_train(X, y, X_val, y_val, epochs, batch_size)
    sota_train(X, y, X_val, y_val, epochs, batch_size)
    xgb_train(X, y, X_val, y_val)
    lr_train(X, y, X_val, y_val)
