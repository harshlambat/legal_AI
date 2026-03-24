🧠 Overview
-----------

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline for legal queries.

Instead of generic AI responses, it:

*   Retrieves **relevant legal documents**
    
*   Uses a **local LLM (Ollama / LLaMA 3)** to generate grounded answers
    
*   Provides **structured, context-aware legal guidance**
    

⚙️ Architecture
---------------

User Query  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Frontend (HTML/JS)  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
FastAPI Backend       
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
FAISS Vector Search (Semantic Retrieval)       
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Top-K Legal Context          
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Local LLM (Ollama - LLaMA3)  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Final Answer (Structured Response)  

🔥 Features
-----------

*   ⚡ **Semantic Search (FAISS)** — retrieves relevant legal data using embeddings
    
*   🧠 **Local LLM Integration** — runs fully offline using Ollama
    
*   🔍 **RAG Pipeline** — combines retrieval + generation for accurate answers
    
*   💬 **Interactive Chat UI** — clean frontend interface
    
*   📂 **Scalable Dataset Support** — handles thousands of legal documents
    
*   🛡️ **Privacy-first** — no external API dependency
    

🏗️ Tech Stack
--------------

### Backend

*   FastAPI
    
*   FAISS (Vector Database)
    
*   Sentence Transformers (all-MiniLM-L6-v2)
    
*   Ollama (LLaMA 3)
    

### Frontend

*   HTML / CSS / JavaScript
    

### AI / ML

*   Embedding Models
    
*   RAG (Retrieval-Augmented Generation)
    

📦 Installation (Local Setup)
-----------------------------

### 1️⃣ Clone Repository
```bash   
   git clone https://github.com/harshlambat/legal_AI.gitcd legal_AI   
```

### 2️⃣ Setup Backend
```bash   
   cd backend 
   pip install -r requirements.txt   `
```
### 3️⃣ Install Ollama
```bash   
   curl -fsSL https://ollama.com/install.sh | sh   `
```
Run model :

```bash   
   ollama run llama3   `
```

### 4️⃣ Create FAISS Index
```bash   
   python create_index.py   `
```
### 5️⃣ Run Backend
```bash   
   python -m uvicorn main:app --reload   `
```
### 6️⃣ Run Frontend

Open:
```bash   
    frontend/index.html   `
```

🧪 Example Query
----------------
```   Can I claim land in India?   ```

### ✅ Output

*   Paragraph Answer
    
*   Legal Explanation
    
*   Recommended Actions
    

📊 Dataset
----------

*   Contains structured legal documents (JSON → processed into embeddings)
    
*   Supports scalable ingestion and indexing
    
*   ~20K+ legal entries processed
    

🚀 Deployment
-------------

Supports deployment on:

*   DigitalOcean / AWS (VPS)
    
*   Nginx + FastAPI
    
*   Ollama for local inference
    

⚠️ Limitations
--------------

*   Responses depend on dataset quality
    
*   CPU-based inference can be slow
    
*   No legal liability (informational use only)
    

👨‍💻 Author
------------

**Harsh Lambat**
