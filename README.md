# RAG App — Document Question Answering with Retrieval, Reranking, and Groq

A modular Retrieval-Augmented Generation (RAG) application that answers
questions grounded in your own documents. Built to understand each
piece of a production RAG pipeline from first principles, not by
wrapping a framework.

## What it does

- Ingests all `.txt` documents in a `data/` folder
- Splits them into overlapping chunks
- Embeds chunks with a sentence-transformer model
- Retrieves the most relevant chunks for a query using FAISS
- Reranks retrieved chunks with a cross-encoder for better ordering
- Rejects low-confidence retrievals instead of hallucinating
  ("I don't know based on the provided documents.")
- Generates a grounded answer using an LLM (Groq)

## Architecture

```
Documents (data/)
      │
      ▼
  Chunker          — splits text into overlapping chunks
      │
      ▼
  Retriever        — embeds chunks, builds a FAISS index, searches
      │
      ▼
  Reranker         — cross-encoder reorders retrieved candidates
      │
      ▼
  Generator        — builds the prompt, calls the LLM, returns the answer
```

Each component has a single responsibility and no knowledge of the
others' internals — swapping the LLM provider, embedding model, or
reranker only requires changing one file.

## Why these design choices

- **Chunking with overlap**: prevents ideas from being cut in half at
  chunk boundaries.
- **FAISS `IndexFlatIP` on normalized vectors**: exact cosine similarity
  search, chosen for simplicity and because dataset size doesn't yet
  require approximate search.
- **Similarity threshold before generation**: if the best retrieved
  chunk scores below the threshold, the app refuses to answer rather
  than letting the LLM guess from irrelevant context.
- **Reranking**: FAISS retrieves candidates fast but only compares
  embeddings computed independently; a cross-encoder reads the query
  and chunk together and reorders the top candidates more accurately.

## Setup

```bash
pip install -r requirements.txt
```

Set your Groq API key as an environment variable rather than hardcoding it:

```bash
export GROQ_API_KEY="your_key_here"
```

Add your own `.txt` documents to the `data/` folder.

## Usage

```bash
python app.py
```

```
Ask a question (or type 'exit' to quit): What does FAISS do?

Retrieved Chunks:
----------------------------------------
Rank   : 1
Score  : 0.81
Rerank : 8.92
Source : ai_notes.txt
Text   : FAISS performs fast nearest neighbour search...

Answer:
FAISS is a library for efficient similarity search over vectors...
```

## Project structure

```
rag-app/
├── app.py          # orchestrates the pipeline
├── chunker.py       # splits documents into overlapping chunks
├── retriever.py     # embeddings + FAISS index + search
├── reranker.py      # cross-encoder reranking
├── generator.py      # prompt construction + LLM call
├── utils.py         # document loading
├── data/            # your source documents (.txt)
└── requirements.txt
```

## Known limitations

- The FAISS index and embeddings are rebuilt on every run rather than
  persisted to disk — acceptable at this dataset size, but the next
  improvement would be caching the index and rebuilding only when
  documents change.
- Chunking splits on a fixed character count rather than
  paragraph/sentence boundaries, so a chunk can occasionally start or
  end mid-sentence.
- Currently supports `.txt` files only.
