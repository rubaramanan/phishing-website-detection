from src.phish_detector.classes.ensemble import PhishDetectorXGBoost
from datetime import datetime


def xgb_train(X, y, X_val, y_val):
    xgb = PhishDetectorXGBoost()
    xgb.train(X,
              y,
              X_val=X_val,
              y_val=y_val)
    xgb.save_model(f"./models/ensemble/xgb_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.pickle")
