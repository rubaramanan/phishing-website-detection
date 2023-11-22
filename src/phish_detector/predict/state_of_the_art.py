import torch

from src.utils.feature_extraction import gen_features_predict


def sota_prediction(url):
    features = gen_features_predict(url)

    model = torch.load("./models/sota/discriminator.pth")
    pred = model(torch.FloatTensor(features))
    predc = pred.argmax().item()
    labels = {0: 'Legitimate',
              1: 'Phish'}
    return {"State of the Art": labels[predc]}
