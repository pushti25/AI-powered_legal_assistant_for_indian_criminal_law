import logging
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)

import faiss
import pickle
from sentence_transformers import SentenceTransformer

# ===============================
# 1. Load Vector Database
# ===============================
print("Loading vector database...")

index = faiss.read_index("sc_judgments_faiss.index")

with open("sc_judgments_texts.pkl", "rb") as f:
    texts = pickle.load(f)

print("Total chunks loaded:", len(texts))

# ===============================
# 2. Load Embedding Model
# ===============================
model = SentenceTransformer("all-MiniLM-L6-v2")

# ===============================
# 3. Search Loop
# ===============================
while True:
    query = input("\nEnter your legal query (type 'exit' to stop): ")

    if query.lower() == "exit":
        print("Exiting search.")
        break

    query_embedding = model.encode([query])

    k = 5  # number of results
    distances, indices = index.search(query_embedding, k)

    print("\n" + "="*75)
    print(f"🔎 Search Results for: '{query}'")
    print("="*75)

    for i, idx in enumerate(indices[0]):
        content = texts[idx]
        score = distances[0][i]

        print("\n" + "-"*75)
        print(f"Result {i+1}")
        print("-"*75)

        print("📄 Document Match Details")
        print(f"   • Similarity Score : {score:.4f}")
        print(f"   • Chunk ID         : {idx}")
        print(f"   • Content Length   : {len(content)} characters")

        print("\n📝 Content Preview:")
        preview = content[:800].replace("\n", "\n   ")
        print(f"   {preview}")

    print("\n" + "="*75)