from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Nota: en el siguiente paso crearemos src/nlp_utils.py con la función clean_tokens
from src.nlp_utils import clean_tokens

app = FastAPI(title="Mini NLP (ADSO)")

class TextIn(BaseModel):
    text: str

class TokensOut(BaseModel):
    tokens: List[str]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/classify", response_model=TokensOut)
def classify(payload: TextIn):
    tokens = clean_tokens(payload.text)
    return {"tokens": tokens}
