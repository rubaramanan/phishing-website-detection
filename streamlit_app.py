import streamlit as st
from src.phish_detector.predict_pipeline import predict
from src.phish_detector.predict.feed_forward import feedforward_prediction
from src.phish_detector.predict.state_of_the_art import sota_prediction
from src.phish_detector.predict.traditional_ml import lr_prediction
from src.phish_detector.predict.ensemble import xgb_prediction
import pandas as pd


def phish_detection():
    menu = ["Voted Weight result", "Neural network - Feedforward", "State of the art - GAN",
            "Traditional ML - Logistic Regression", "Ensemble - XGBoost"]  # navigation menu
    choice = st.sidebar.selectbox("Phish Detector", menu)
    st.title("Phish Detector")
    with st.form(key='url'):
        process_streamlit_ui(choice)


def process_streamlit_ui(choice):
    url = st.text_input("Type your url")
    submit_text = st.form_submit_button(label='Submit')
    if submit_text:
        predict_dic = {'Voted Weight result': lambda: predict(url),
                       'Neural network - Feedforward': lambda: feedforward_prediction(url),
                       'State of the art - GAN': lambda: sota_prediction(url),
                       'Traditional ML - Logistic Regression': lambda: lr_prediction(url),
                       'Ensemble - XGBoost': lambda: xgb_prediction(url)
                       }

        value = predict_dic[choice]()
        df = pd.json_normalize(value)
        df = df.T
        df.columns = ['Result']
        df.index.name = 'Models'
        st.dataframe(df)


if __name__ == '__main__':
    phish_detection()
