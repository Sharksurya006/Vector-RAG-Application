# 🔎 Vector RAG Application

A lightweight **Retrieval-Augmented Generation (RAG)** pipeline built with **LangChain**, **FAISS**, and **GROQ LLM** — designed to load your documents, index them as vectors, rewrite fuzzy user queries into sharper search queries, retrieve the most relevant chunks, and generate a grounded, summarized answer.

> Ask a question in plain English → the app rewrites it for better retrieval → searches your document corpus semantically → summarizes the retrieved context into a clean answer.

---

## ✨ Features

- 📄 **Document ingestion** — load and process documents from a local folder
- 🧠 **Vector indexing with FAISS** — fast, in-memory/on-disk similarity search
- ✏️ **Query rewriting** — automatically reformulates raw user queries for higher-quality retrieval
- 🔍 **Semantic search + summarization** — retrieves top-k relevant chunks and summarizes them using GROQ's LLM
- ⚡ **Simple CLI interface** — ask questions directly from the terminal
- 🧩 **Modular design** — data loading, vector store, query rewriting, and search are cleanly separated

---

## 🏗️ How It Works

```
                ┌─────────────────┐
                │   data/ folder    │
                │ (your documents) │
                └────────┬─────────┘
                         │  load_all_documents()
                         ▼
                ┌─────────────────┐
                │  FaissVectorStore │
                │  (build / load)   │
                └────────┬─────────┘
                         │
   User Query ──▶ QueryReWriting ──▶ rewritten query
                         │
                         ▼
                ┌─────────────────┐
                │    RAGSearch      │
                │ search_and_summarize()
                └────────┬─────────┘
                         │
                         ▼
                 📝 Summarized Answer
```

1. **Load** — `load_all_documents()` reads and parses documents from the `data/` directory.
2. **Embed & Index** — `FaissVectorStore` builds (or loads a previously built) FAISS index from the documents.
3. **Rewrite** — `QueryReWriting` takes the raw user question and rewrites it into a more retrieval-friendly query.
4. **Retrieve & Summarize** — `RAGSearch.search_and_summarize()` performs a top-k similarity search against the FAISS index and passes the retrieved context to the GROQ LLM to generate a summarized answer.

---

## 🛠️ Tech Stack

| Layer               | Technology                                   |
|---------------------|-----------------------------------------------|
| Language             | Python                                        |
| Orchestration         | LangChain (`langchain`, `langchain-core`, `langchain-community`) |
| Vector Store          | FAISS (`faiss-cpu`)                          |
| Embeddings             | `sentence-transformers`                      |
| LLM Provider           | GROQ (`langchain_groq`)                      |
| Document Parsing       | `pypdf`, `pymupdf`                           |
| Config / Secrets       | `python-dotenv`                              |
| Experimentation        | `ipykernel` (Jupyter support)                |

---

## 📁 Project Structure

```
Vector-RAG-Application/
├── data/                    # Drop your source documents here
├── faiss_store/             # Persisted FAISS vector index
├── src/
│   ├── data_loader.py       # Loads & parses documents from data/
│   ├── vectorstore.py       # FaissVectorStore — build/load/query the index
│   ├── search.py            # RAGSearch — retrieval + LLM summarization
│   └── query_rewritting.py  # QueryReWriting — reformulates user queries
├── app.py                   # Main entry point (CLI)
├── requirements.txt         # pip dependencies
├── pyproject.toml           # Project metadata / uv dependencies
├── uv.lock                  # Locked dependency versions (uv)
└── .python-version          # Pinned Python version
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sharksurya006/Vector-RAG-Application.git
cd Vector-RAG-Application
```

### 2. Set up your environment

Using **uv** (recommended, since the repo ships a `uv.lock`):

```bash
uv sync
```

Or using **pip**:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure your GROQ API key

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Add your documents

Place the files you want to query into the `data/` folder.

### 5. Build the vector index

In `app.py`, uncomment the index-building line for the first run:

```python
store.build_from_documents(docs)
```

This creates and persists the FAISS index inside `faiss_store/`. On subsequent runs, you can switch back to:

```python
store.load()
```

### 6. Run the app

```bash
python app.py
```

You'll be prompted to type your question:

```
Ask whatever you want? What is Deep Learning and explain its advantage?
```

The app will rewrite your query, retrieve the most relevant chunks from FAISS, and print a summarized, grounded answer.

---

## 🧪 Example

```text
Ask whatever you want? What is Deep Learning and explain its advantage?
==============================
Actual query: What is Deep Learning and explain its advantage?
==============================
Rewritted-query: Explain deep learning and its key advantages over traditional machine learning
==============================
Summary: <LLM-generated, context-grounded answer based on your documents>
```

---

## 🗺️ Roadmap Ideas

- [ ] Add a web UI (Streamlit / FastAPI)
- [ ] Support additional vector stores (Chroma is already a dependency)
- [ ] Add chat history / multi-turn conversation support
- [ ] Add evaluation metrics for retrieval quality
- [ ] Dockerize for one-command setup

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Sharksurya006/Vector-RAG-Application/issues) or open a pull request.

---

## 📄 License

No license has been specified yet for this repository. Consider adding one (e.g., MIT) to clarify how others can use this project.

---

## 👤 Author

**Surya S**
GitHub: [@Sharksurya006](https://github.com/Sharksurya006)