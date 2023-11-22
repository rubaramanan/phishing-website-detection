import streamlit as st
from src.phish_detector.predict_pipeline import predict
from src.phish_detector.predict.feed_forward import feedforward_prediction
from src.phish_detector.predict.state_of_the_art import sota_prediction
import pandas as pd


def phish_detection():
    menu = ["Final result", "LSTM", "GAN"]  # navigation menu
    choice = st.sidebar.selectbox("Phish Detector", menu)
    st.title("Phish Detector")
    with st.form(key='url'):
        process_streamlit_ui(choice)


def process_streamlit_ui(choice):
    url = st.text_input("Type your url")
    submit_text = st.form_submit_button(label='Submit')
    if submit_text:
        predict_dic = {'Final result': lambda: predict(url),
                       'LSTM': lambda: feedforward_prediction(url),
                       'GAN': lambda: sota_prediction(url)}

        value = predict_dic[choice]()
        df = pd.json_normalize(value)
        df = df.T
        df.columns = ['Result']
        df.index.name = 'Models'
        st.dataframe(df)


if __name__ == '__main__':
    phish_detection()
