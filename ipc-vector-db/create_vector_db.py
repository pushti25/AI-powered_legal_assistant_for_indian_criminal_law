import os
import pickle
import kagglehub
import faiss
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer


# 1. Download Dataset

dataset_path = kagglehub.dataset_download(
    "adarshsingh0903/legal-dataset-sc-judgments-india-19502024"
)

print("Dataset path:", dataset_path)

# 2. Collect ALL PDF files (RECURSIVE)
pdf_files = []

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(root, file))

print("Total PDF files found:", len(pdf_files))

if len(pdf_files) == 0:
    raise RuntimeError("No PDF files found in dataset.")

# 🔒 SAFE LIMIT for 8GB RAM (increase later)
pdf_files = pdf_files[:50]
print("PDF files selected:", len(pdf_files))


# 3. Chunking Function

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    text = text.replace("\n", " ")

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


# 4. Extract Text from PDFs (PyMuPDF)

texts = []
print("Extracting text from PDFs...")

for i, pdf_path in enumerate(pdf_files, 1):
    try:
        doc = fitz.open(pdf_path)
        full_text = ""

        for page in doc:
            full_text += page.get_text()

        if full_text.strip():
            texts.extend(chunk_text(full_text))

        print(f"Processed {i}/{len(pdf_files)} PDFs")

    except Exception as e:
        print(f"Skipped {pdf_path}: {e}")

print("Total chunks created:", len(texts))

if len(texts) == 0:
    raise RuntimeError("No text extracted from PDFs.")


# 5. Create Embeddings (LOW RAM)

# 5. Create Embeddings (Correct Cosine Similarity)

model = SentenceTransformer("all-MiniLM-L6-v2")

dimension = 384
index = faiss.IndexFlatIP(dimension)  # Inner Product for cosine similarity

batch_size = 64
print("Creating embeddings...")

for i in range(0, len(texts), batch_size):
    batch = texts[i:i + batch_size]
    embeddings = model.encode(batch, convert_to_numpy=True)

    embeddings = embeddings.astype("float32")

    # Normalize embeddings for cosine similarity
    faiss.normalize_L2(embeddings)

    index.add(embeddings)


# 6. Save Vector Database

faiss.write_index(index, "sc_judgments_faiss.index")

with open("sc_judgments_texts.pkl", "wb") as f:
    pickle.dump(texts, f)

print("\n✅ VECTOR DATABASE CREATED SUCCESSFULLY")
print("Total chunks stored:", len(texts))