from src.phish_detector.feedforward import PhishDetectorFeedForward
from src.utils.get_features_labels import train_data, validate_data
from datetime import datetime

dir = '../final_data'
features, labels = train_data(f"{dir}/Phishing_train_dataset.csv")
test_features, test_labels = validate_data(f"{dir}/Phishing_test_dataset.csv")


feedforward = PhishDetectorFeedForward()
feedforward.train(features,
                  labels,
                  X_val=test_features,
                  y_val=test_labels,
                  batch_size=32,
                  epochs=100)
feedforward.save_model(f"./models/feedforward/feedforwad_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.h5")
