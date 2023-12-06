import streamlit as st
from transformers import pipeline

st.header('Приложение для классификации тональности текста')

def load_model():
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    return classifier

text_classification =load_model()
def text_model_output():
    text_input = st.text_input(label='Пишите ваш текст на английском')
    button = st.button(label='Классифировать текст')
    if button:
        model_outputs = text_classification(text_input)
        st.text(model_outputs[0])

text_model_output()

