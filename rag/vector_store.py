import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

INDEX_PATH = "rag/faiss.index"
MEMORY_PATH = "rag/memory.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")
dimension = 384


# Load existing index if exists
if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
else:
    index = faiss.IndexFlatL2(dimension)

# Load memory
if os.path.exists(MEMORY_PATH):
    with open(MEMORY_PATH, "rb") as f:
        memory = pickle.load(f)
else:
    memory = []


def save_memory():
    faiss.write_index(index, INDEX_PATH)
    with open(MEMORY_PATH, "wb") as f:
        pickle.dump(memory, f)


def add_to_vector_store(text):
    embedding = model.encode([text])
    index.add(np.array(embedding).astype("float32"))
    memory.append(text)
    save_memory()


def search_vector_store(query, top_k=2):
    if len(memory) == 0:
        return "No past incidents found."

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding).astype("float32"), top_k)

    results = [memory[i] for i in indices[0] if i < len(memory)]
    return results