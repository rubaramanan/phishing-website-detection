from src.phish_detector.classes.traditional_ml import PhishDetectorLR
from src.utils.feature_extraction import gen_features_predict


def lr_prediction(url):
    features = gen_features_predict(url)

    model = PhishDetectorLR()
    model.load_models('./models/traditional_ml')
    pred = model.test([features])
    return {"Traditional ML": pred}
