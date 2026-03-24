from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import requests

app = FastAPI()

df = pd.read_csv("data.csv")

OLLAMA_URL = "http://localhost:11434/api/generate"

class Query(BaseModel):
    message: str

def get_context(query):
    results = df[df.apply(lambda row: query.lower() in str(row).lower(), axis=1)]
    return results.head(3).to_string()

@app.post("/chat")
def chat(query: Query):
    user_input = query.message

    context = get_context(user_input)

    prompt = f"""
You are a legal assistant.

Use this data:
{context}

Question:
{user_input}
"""

    response = requests.post(OLLAMA_URL, json={
        "model": "llama3:instruct",
        "prompt": prompt,
        "stream": False
    })

    return {"response": response.json().get("response", "")}