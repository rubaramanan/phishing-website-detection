from src.phish_detector.classes.feedforward import PhishDetectorFeedForward
from src.utils.feature_extraction import gen_features_predict


def feedforward_prediction(url):
    features = gen_features_predict(url)

    loaded_model = PhishDetectorFeedForward()
    loaded_model.load_models('./models/feedforward')
    pred = loaded_model.test([features])
    return {"Neural Network": pred}
