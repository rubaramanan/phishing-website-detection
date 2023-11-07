from src.utils.feature_extraction import gen_features_predict
from src.phish_detector.feedforward import PhishDetectorFeedForward

features = gen_features_predict('http://172.17.0.1:8080/hello')
print(features)

loaded_model = PhishDetectorFeedForward()
loaded_model.load_models('./models/feedforward')

pred = loaded_model.test([features])
print(pred)
