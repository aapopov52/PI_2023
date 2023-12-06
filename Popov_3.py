from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str
    
app = FastAPI()

model_name = "IlyaGusev/rubertconv_toxic_clf"
pip = pipeline("text-classification", model=model_name, tokenizer=model_name, framework="pt") 

@app.get("/")
def root():
    return {"message": "Классификатор текста"}

@app.post("/predict/")
def predict(item: Item):
    if item.text == '':
        return 'Текст для классификации не введён'
    else:
        return pip(item.text)[0]
