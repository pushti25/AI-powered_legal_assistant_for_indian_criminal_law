import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from django.conf import settings
print("🔥 USING NEW LIGHTWEIGHT RAG")


BASE_DIR = settings.BASE_DIR

SC_INDEX_PATH = os.path.join(BASE_DIR, "sc_judgments_faiss.index")
SC_DOCS_PATH = os.path.join(BASE_DIR, "sc_judgments_texts.pkl")

LAW_INDEX_PATH = os.path.join(BASE_DIR, "indian_law_faiss.index")
LAW_DOCS_PATH = os.path.join(BASE_DIR, "indian_law_texts.pkl")

# Global cache (lazy load)
embedder = None
sc_index = None
sc_documents = None
law_index = None
law_documents = None


def load_models():
    global embedder, sc_index, sc_documents, law_index, law_documents

    if embedder is None:
        print("Loading embedding model...")
        embedder = SentenceTransformer("all-MiniLM-L6-v2")

    if sc_index is None:
        print("Loading SC FAISS index...")
        sc_index = faiss.read_index(SC_INDEX_PATH)
        with open(SC_DOCS_PATH, "rb") as f:
            sc_documents = pickle.load(f)

    if law_index is None:
        print("Loading Law FAISS index...")
        law_index = faiss.read_index(LAW_INDEX_PATH)
        with open(LAW_DOCS_PATH, "rb") as f:
            law_documents = pickle.load(f)


def retrieve_context(query, k=1, threshold=0.5):
    load_models()

    query_vec = embedder.encode([query])

    D1, I1 = sc_index.search(np.array(query_vec), k)
    D2, I2 = law_index.search(np.array(query_vec), k)

    sc_results = []
    law_results = []

    # Filter Supreme Court results
    for distance, idx in zip(D1[0], I1[0]):
        if distance < threshold:
            sc_results.append(sc_documents[idx])

    # Filter Law results
    for distance, idx in zip(D2[0], I2[0]):
        if distance < threshold:
            law_results.append(law_documents[idx])

    if not sc_results and not law_results:
        return ""

    context = ""

    if sc_results:
        context += "\n\n--- Supreme Court Judgments ---\n"
        context += "\n\n".join(sc_results)

    if law_results:
        context += "\n\n--- Statutory Provisions ---\n"
        context += "\n\n".join(law_results)

    return context
