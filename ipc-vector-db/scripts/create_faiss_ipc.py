import os
import json
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_DIR = os.path.join("..", "data")

print("Scanning JSON files...")
json_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
print("Found:", json_files)

texts = []

# ----------------------------
# 1️⃣ Extract From All JSON Files
# ----------------------------

for file in json_files:
    file_path = os.path.join(DATA_DIR, file)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    act_name = file.replace(".json", "").upper()

    print(f"Processing {act_name}...")

    for section in data:

        # Handle IPC-like structure
        section_number = section.get("Section") or section.get("section") or ""
        title = (
            section.get("section_title")
            or section.get("title")
            or ""
        )
        description = (
            section.get("section_desc")
            or section.get("description")
            or ""
        )
        chapter_title = section.get("chapter_title", "")

        combined_text = f"""
Act: {act_name}

Chapter: {chapter_title}
Section {section_number}: {title}

{description}
"""

        texts.append(combined_text.strip())

print("Total sections collected:", len(texts))


# ----------------------------
# 2️⃣ Create Embeddings (Cosine)
# ----------------------------

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

dimension = 384
index = faiss.IndexFlatIP(dimension)

batch_size = 64
print("Creating embeddings...")

for i in range(0, len(texts), batch_size):
    batch = texts[i:i + batch_size]
    embeddings = model.encode(batch, convert_to_numpy=True)
    embeddings = embeddings.astype("float32")

    faiss.normalize_L2(embeddings)

    index.add(embeddings)

    print(f"Processed {i + len(batch)}/{len(texts)}")

print("Embeddings complete.")


# ----------------------------
# 3️⃣ Save Files
# ----------------------------

faiss.write_index(index, "indian_law_faiss.index")

with open("indian_law_texts.pkl", "wb") as f:
    pickle.dump(texts, f)

print("\n✅ Unified Indian Law FAISS created successfully.")
print("Files generated:")
print("- indian_law_faiss.index")
print("- indian_law_texts.pkl")
