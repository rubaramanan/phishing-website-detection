from src.phish_detector.predict.feed_forward import feedforward_prediction
from src.phish_detector.predict.state_of_the_art import sota_prediction
from src.phish_detector.predict.ensemble import xgb_prediction
from src.phish_detector.predict.traditional_ml import lr_prediction


def predict(url):

    results = feedforward_prediction(url)
    results |= sota_prediction(url)
    results |= lr_prediction(url)
    results |= xgb_prediction(url)

    return {'Voted weight': voted_weight_result(results)} | results


def voted_weight_result(results: dict):
    result_values = list(results.values())
    print(result_values)
    leg_count = result_values.count('Legitimate')

    threshold = len(result_values) / 2

    if leg_count > threshold:
        return 'Legitimate'
    if leg_count < threshold:
        return 'Phish'
    if leg_count == threshold:
        return 'Suspicious'
