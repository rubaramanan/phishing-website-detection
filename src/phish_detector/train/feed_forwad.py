from src.phish_detector.classes.feedforward import PhishDetectorFeedForward
from datetime import datetime


def feedforward_train(X, y, X_val, y_val, epochs, batch_size):
    feedforward = PhishDetectorFeedForward()
    feedforward.train(X,
                      y,
                      X_val=X_val,
                      y_val=y_val,
                      batch_size=batch_size,
                      epochs=epochs)
    feedforward.save_model(f"./models/feedforward/feedforwad_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.h5")
