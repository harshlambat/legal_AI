from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import ollama
from vector_store import load_index, search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load FAISS
index, documents = load_index()

@app.get("/")
def home():
    return {"message": "Legal AI Backend Running 🚀"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_query = data.get("message", "")

    results = search(user_query, index, documents)
    context = "\n\n".join(results)

    prompt = f"""
You are a legal AI assistant.

Use context:

{context}

Question: {user_query}
"""

    def generate():
        stream = ollama.chat(
            model="llama3:instruct",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in stream:
            yield chunk['message']['content']

    return StreamingResponse(generate(), media_type="text/plain")