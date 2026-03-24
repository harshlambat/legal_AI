from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

print("🔄 Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model loaded")


def create_index(documents, batch_size=64):
    print(f"\n📄 Total documents: {len(documents)}")
    print("🚀 Starting embedding generation...")

    all_embeddings = []

    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]

        print(f"⚙️ Processing batch {i} → {i + len(batch)}")

        try:
            embeddings = model.encode(batch)
            all_embeddings.extend(embeddings)
        except Exception as e:
            print(f"❌ Error in batch {i}: {e}")

    print("\n📦 Converting to numpy array...")
    embeddings_np = np.array(all_embeddings)

    print("🧠 Creating FAISS index...")
    dim = embeddings_np.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings_np)

    print("💾 Saving FAISS index...")
    faiss.write_index(index, "faiss.index")

    print("💾 Saving documents...")
    with open("docs.pkl", "wb") as f:
        pickle.dump(documents, f)

    print("\n✅ FAISS index created successfully!")


def load_index():
    print("📥 Loading FAISS index...")
    index = faiss.read_index("faiss.index")

    print("📥 Loading documents...")
    with open("docs.pkl", "rb") as f:
        documents = pickle.load(f)

    print("✅ Index + documents loaded")

    return index, documents


def search(query, index, documents, k=3):
    print(f"\n🔍 Searching for: {query}")

    q_embed = model.encode([query])
    D, I = index.search(np.array(q_embed), k)

    print("📊 Search results indices:", I)

    results = [documents[i] for i in I[0]]
    return results