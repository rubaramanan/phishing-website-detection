import pandas as pd


def train_data(path):
    df = pd.read_csv(path)
    return df.drop('Result', axis=1), df.Result


def validate_data(path):
    df = pd.read_csv(path)
    return df.drop('Result', axis=1), df.Result
