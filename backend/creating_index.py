from vector_store import create_index

print("Loading processed data...")

with open("processed_data.txt", "r", encoding="utf-8") as f:
    docs = f.read().split("\n\n")

print(f"Loaded {len(docs)} documents")

create_index(docs)