import pandas as pd


def train_data(path):
    df = pd.read_csv(path)
    return df.drop('Result', axis=1).values.astype('float32'), df.Result.values.astype('float32')


def validate_data(path):
    df = pd.read_csv(path)
    return df.drop('Result', axis=1).values.astype('float32'), df.Result.values.astype('float32')
