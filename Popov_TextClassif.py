from transformers import pipeline

model_name = "IlyaGusev/rubertconv_toxic_clf"
pipe = pipeline("text-classification", model=model_name, tokenizer=model_name, framework="pt") 

text = "Наконец то я выбрал эту модель!!!"
pipe([text])
