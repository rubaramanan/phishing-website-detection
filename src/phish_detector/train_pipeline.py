from src.phish_detector.train.state_of_the_art import sota_train
from src.phish_detector.train.feed_forwad import feedforward_train
from src.utils.get_features_labels import train_data, validate_data

dir = '../../final_data'
features, labels = train_data(f"{dir}/Phishing_train_dataset.csv")
test_features, test_labels = validate_data(f"{dir}/Phishing_test_dataset.csv")

feedforward_train(features, labels, test_features, test_labels, 100, 32)
sota_train(features, labels, test_features, test_labels, 100, 32)

