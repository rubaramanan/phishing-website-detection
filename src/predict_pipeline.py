from src.phish_detector.predict.feed_forward import feedforward_prediction
from src.utils.feature_extraction import gen_features_predict
from src.phish_detector.predict.state_of_the_art import sota_prediction


def predict(url):
    features = gen_features_predict(url)

    feed_pred = feedforward_prediction(features)
    sota_pred = sota_prediction(features)

    results = {'GAN result': sota_pred,
               'Feedforward result': feed_pred}

    return {'Final results': get_final_results(results),
            'results': results}


def get_final_results(results: dict):
    result_values = list(results.values())
    print(result_values)
    leg_count = result_values.count('Legitimate')

    # has to change 1 as 2
    if leg_count > 1:
        return 'Legitimate'
    if leg_count < 1:
        return 'Phish'
    if leg_count == 1:
        return 'Suspicious'
