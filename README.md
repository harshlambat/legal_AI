# AI Legal Assistant

A full-stack AI legal assistant using FastAPI, Ollama, and RAG.

## Features
- Local LLM (LLaMA3 via Ollama)
- Legal dataset search (RAG)
- FastAPI backend
- Simple frontend UI

## Run Instructions

### 1. Install dependencies
pip install -r backend/requirements.txt

### 2. Run Ollama
ollama run llama3:instruct

### 3. Run backend
cd backend
uvicorn main:app --reload

### 4. Open frontend
Open frontend/index.html
