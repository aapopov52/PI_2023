from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

pipe = pipeline('text-classification', model='SamLowe/roberta-base-go_emotions', top_k=None)

@app.get("/")
def root():
    return {"Определение тональности текста на английском языке"}

@app.post("/predict/")
def predict(item: Item):
    if item.text == '':
        return 'Текст не введен'
    else :
        return pipe(item.text )[0]