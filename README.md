🧠 Overview
-----------

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline for legal queries.

Instead of generic AI responses, it:

*   Retrieves **relevant legal documents**
    
*   Uses a **local LLM (Ollama / LLaMA 3)** to generate grounded answers
    
*   Provides **structured, context-aware legal guidance**
    

⚙️ Architecture
---------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   User Query   ↓Frontend (HTML/JS)   ↓FastAPI Backend   ↓FAISS Vector Search (Semantic Retrieval)   ↓Top-K Legal Context   ↓Local LLM (Ollama - LLaMA3)   ↓Final Answer (Structured Response)   `

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

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/harshlambat/legal_AI.gitcd legal_AI   `

### 2️⃣ Setup Backend

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd backendpip install -r requirements.txt   `

### 3️⃣ Install Ollama

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   curl -fsSL https://ollama.com/install.sh | sh   `

Run model:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ollama run llama3   `

### 4️⃣ Create FAISS Index

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python create_index.py   `

### 5️⃣ Run Backend

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m uvicorn main:app --reload   `

### 6️⃣ Run Frontend

Open:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   frontend/index.html   `

🧪 Example Query
----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Can I claim unclaimed land in India?   `

### ✅ Output

*   Short Answer
    
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
    

🔮 Future Improvements
----------------------

*   📚 Add legal citations & references
    
*   ⚡ GPU acceleration for faster inference
    
*   🧠 Reranking models for higher accuracy
    
*   🌐 Multi-language legal support
    
*   👤 User authentication & history
    

👨‍💻 Author
------------

**Harsh Lambat**
