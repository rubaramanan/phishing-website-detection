import torch


def sota_prediction(features):
    model = torch.load("./models/sota/discriminator.pth")
    pred = model(torch.FloatTensor(features))
    predc = pred.argmax().item()
    labels = {0: 'Legitimate',
              1: 'Phish'}
    return labels[predc]
