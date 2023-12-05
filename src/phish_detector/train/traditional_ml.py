from src.phish_detector.classes.traditional_ml import PhishDetectorLR
from datetime import datetime


def lr_train(X, y, X_val, y_val):
    lr = PhishDetectorLR()
    lr.train(X,
             y,
             X_val=X_val,
             y_val=y_val)
    lr.save_model(f"./models/traditional_ml/lr_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.pickle")
