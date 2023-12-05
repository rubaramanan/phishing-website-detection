from src.phish_detector.classes.ensemble import PhishDetectorXGBoost
from src.utils.feature_extraction import gen_features_predict


def xgb_prediction(url):
    features = gen_features_predict(url)

    model = PhishDetectorXGBoost()
    model.load_models('./models/ensemble')
    pred = model.test([features])
    return {"Ensemble": pred}
