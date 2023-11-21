from src.phish_detector.classes.feedforward import PhishDetectorFeedForward


def feedforward_prediction(features):
    loaded_model = PhishDetectorFeedForward()
    loaded_model.load_models('./models/feedforward')
    pred = loaded_model.test([features])
    return pred
