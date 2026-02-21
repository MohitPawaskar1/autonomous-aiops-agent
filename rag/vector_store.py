import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_FILE = "rag/faiss_index.bin"
META_FILE = "rag/metadata.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")

dimension = 384

if os.path.exists(INDEX_FILE):
    index = faiss.read_index(INDEX_FILE)
else:
    index = faiss.IndexFlatL2(dimension)

if os.path.exists(META_FILE):
    with open(META_FILE, "rb") as f:
        metadata = pickle.load(f)
else:
    metadata = []


def save_index():
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(metadata, f)


def add_text(text, meta):
    embedding = model.encode([text])
    index.add(np.array(embedding).astype("float32"))
    metadata.append(meta)
    save_index()


def search_text(query, top_k=1):
    if index.ntotal == 0:
        return []

    embedding = model.encode([query])
    D, I = index.search(np.array(embedding).astype("float32"), top_k)

    results = []
    for idx in I[0]:
        if idx < len(metadata):
            results.append(metadata[idx])

    return results