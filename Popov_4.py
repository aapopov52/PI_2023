import streamlit as st
from transformers import pipeline


#@st.cache(allow_output_mutation=True)
def load_model():
    model_name = "IlyaGusev/rubertconv_toxic_clf"
    return pipeline("text-classification", model=model_name, tokenizer=model_name, framework="pt") 
    #return pipeline(
    #         task = 'sentiment-analysis', 
    #         model = 'SkolkovoInstitute/russian_toxicity_classifier')


st.title('Анализ тональности текста')
pipe = load_model()

text = st.text_area("Введите текст для классификации:")
result = st.button('Классифицировать')
if result:
    if text != '':
        st.write('**Результат классификации:**')
        st.write(pipe(text))
    else:
        st.write("Введите текст для классификации.")        
        
