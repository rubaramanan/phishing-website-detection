from src.phish_detector.train_pipeline import train
from src.utils.get_features_labels import train_data, validate_data

dir = './final_data'
features, labels = train_data(f"{dir}/Phishing_train_dataset.csv")
test_features, test_labels = validate_data(f"{dir}/Phishing_test_dataset.csv")

train(features, labels, test_features, test_labels, 10, 32)
