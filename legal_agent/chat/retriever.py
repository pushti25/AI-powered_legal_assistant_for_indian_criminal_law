import faiss
import pickle
from sentence_transformers import SentenceTransformer
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load SC judgments
sc_index = faiss.read_index(os.path.join(BASE_DIR, "sc_judgments_faiss.index"))
sc_texts = pickle.load(open(os.path.join(BASE_DIR, "sc_judgments_texts.pkl"), "rb"))

# Load Indian law dataset
law_index = faiss.read_index(os.path.join(BASE_DIR, "indian_law_faiss.index"))
law_texts = pickle.load(open(os.path.join(BASE_DIR, "indian_law_texts.pkl"), "rb"))


def retrieve_from_sc(query, k=3):
    emb = model.encode([query])
    _, indices = sc_index.search(emb, k)
    return [sc_texts[i] for i in indices[0]]


def retrieve_from_law(query, k=3):
    emb = model.encode([query])
    _, indices = law_index.search(emb, k)
    return [law_texts[i] for i in indices[0]]


def retrieve_all(query):
    sc_results = retrieve_from_sc(query)
    law_results = retrieve_from_law(query)

    return {
        "judgments": sc_results,
        "acts": law_results
    }
