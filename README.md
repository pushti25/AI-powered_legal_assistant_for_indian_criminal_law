# ⚖️ AI-Powered Legal Assistant for Indian Criminal Law

[![Python](https://img.shields.io/badge/Language-Python-3776AB.svg)](https://www.python.org)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-black.svg)](https://ollama.com)
[![AI](https://img.shields.io/badge/Domain-Artificial%20Intelligence-blueviolet.svg)](#)
[![Indian Criminal Law](https://img.shields.io/badge/Domain-Indian%20Criminal%20Law-orange.svg)](#)

> **Project Name:** AI-Powered Legal Assistant for Indian Criminal Law  
> **Application Type:** AI / Natural Language Processing Project  
> **Domain:** Legal Technology & Artificial Intelligence

---

## ⚖️ Overview

**AI-Powered Legal Assistant for Indian Criminal Law** is an AI-based project designed to provide a conversational interface for working with information related to Indian criminal law.

The project contains a `legal_agent` component, an `ipc-vector-db` component, and an Ollama connectivity test. It is designed around retrieving relevant legal information from a prepared knowledge base and using a local language model to support the assistant workflow.

The included Ollama test communicates with a local Ollama server and uses the `phi3:latest` model.

### Key Capabilities

- ⚖️ **Indian Criminal Law Knowledge Base**
- 🔎 **Legal Information Retrieval**
- 🤖 **Local AI Model Support using Ollama**
- 💬 **AI-powered legal assistant workflow**
- 🔐 **Local language-model execution**
- 🧪 **Ollama connectivity testing**

---

## 🧠 How the Project Works

```text
User Query
    │
    ▼
Legal Agent
    │
    ▼
IPC / Legal Vector Database
    │
    ▼
Relevant Legal Information
    │
    ▼
Local Ollama Language Model
    │
    ▼
Assistant Response
```

The exact internal implementation is defined by the source code in `legal_agent/` and `ipc-vector-db/`.

---

## 📁 Repository Structure

```text
AI-powered_legal_assistant_for_indian_criminal_law/
│
├── ipc-vector-db/                 # IPC / legal vector database component
│
├── legal_agent/                   # Legal assistant / agent component
│
├── test_ollama.py                 # Tests local Ollama connectivity
│
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment configuration template
├── .gitignore                     # Git ignored files
├── LICENSE                        # Project license notice
└── README.md                      # Project documentation
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application programming |
| **Ollama** | Local language-model runtime |
| **Phi-3** | Local model used by the Ollama test |
| **Vector Database** | Legal information retrieval |
| **Requests** | HTTP communication with Ollama |

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/pushti25/AI-powered_legal_assistant_for_indian_criminal_law.git
cd AI-powered_legal_assistant_for_indian_criminal_law
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama from:

https://ollama.com

Then download the model:

```bash
ollama pull phi3:latest
```

Make sure Ollama is running.

### 5. Test Ollama

```bash
python test_ollama.py
```

---

## 🔐 Environment Configuration

Never commit passwords, API keys, tokens, or other secrets to GitHub.

Create a local `.env` file if your implementation requires environment variables:

```env
# Add project-specific variables here.
# Never commit real secrets.
```

---

## 🧪 Testing

The repository contains:

```text
test_ollama.py
```

The test checks communication with the local Ollama API:

```text
http://localhost:11434/api/generate
```

using:

```text
phi3:latest
```

---

## 🎯 Project Objective

The objective of this project is to explore the use of artificial intelligence, local language models, and legal information retrieval for building an assistant that can help users interact with Indian criminal-law information.

---

## 🔮 Future Enhancements

- 💬 Interactive chat interface
- 🔎 Improved semantic legal-document retrieval
- 📚 Expanded legal knowledge base
- 🧾 Case-law and legal-document retrieval
- 🧠 Source citations for generated answers
- 📊 Retrieval and answer-quality evaluation
- 🌐 Web-based user interface
- 🗂️ Multiple legal-document formats
- 🔄 Controlled legal-data updates

---

## ⚠️ Legal Disclaimer

This project is intended for **educational and informational purposes**.

It is not a substitute for advice from a qualified legal professional. AI-generated information may be incomplete, outdated, or incorrect. Important legal information should be verified against authoritative and current legal sources.

---

## 🛡️ License

This project is provided for educational and informational purposes. See the `LICENSE` file for the project notice.
