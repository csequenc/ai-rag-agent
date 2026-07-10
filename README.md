# Modular AI Agent with RAG and Dynamic Tool Calling

A modular AI agent built from first principles that combines Retrieval-Augmented Generation (RAG) with LLM-based tool calling.

The project demonstrates how modern AI agents work internally by implementing document retrieval, reranking, tool selection, dynamic tool execution, and grounded response generation without relying on agent frameworks.

---

## Features

- Document chunking with overlap
- Semantic retrieval using Sentence Transformers
- FAISS vector search
- Cross-encoder reranking
- Grounded response generation using Groq
- LLM-based planner
- Structured JSON tool calling
- Dynamic tool registry
- Calculator tool
- RAG search tool
- Modular and extensible architecture

---

## Architecture

```
                           User Query
                                │
                                ▼
                         LLM Planner
                                │
                 JSON Tool Decision
                                │
             ┌──────────────────┴──────────────────┐
             │                                     │
             ▼                                     ▼
      Calculator Tool                      RAG Search Tool
                                                   │
                                                   ▼
                                      Sentence Transformer
                                                   │
                                                   ▼
                                               FAISS Search
                                                   │
                                                   ▼
                                            Cross Encoder
                                                   │
                                                   ▼
                                          Retrieved Context
             └──────────────────┬──────────────────┘
                                ▼
                      Grounded Response Generation
                                │
                                ▼
                           Final Response
```

---

## Components

### Planner

Uses an LLM to determine which tool should be executed.

Example output:

```json
{
    "tool": "calculate",
    "input": "20*5"
}
```

or

```json
{
    "tool": "rag_search",
    "input": "What is climate change?"
}
```

---

### Tool Registry

Tools are executed dynamically using a registry.

```python
self.tools = {
    "calculate": calculate,
    "rag_search": rag_search
}
```

This makes adding future tools straightforward without modifying the execution logic.

---

### Chunker

Splits documents into overlapping chunks to preserve context across chunk boundaries.

---

### Retriever

- SentenceTransformer embeddings
- FAISS IndexFlatIP
- Cosine similarity search

---

### Reranker

Uses a Cross Encoder to improve retrieval quality by reranking the retrieved chunks.

---

### Generator

Creates a grounded prompt using the retrieved context and generates the final answer using Groq.

---

## Technologies Used

- Python
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- Cross Encoder Reranking
- Groq API
- python-dotenv

---

## Project Structure

```
rag-engine/
│
├── main.py
├── planner.py
├── agent.py
├── tools.py
├── rag.py
├── chunker.py
├── retriever.py
├── reranker.py
├── generator.py
├── utils.py
├── data/
├── requirements.txt
└── README.md
```

---

## Running the Project

### Clone the repository

```bash
git clone <repository-url>
cd rag-engine
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment

Create a `.env` file.

```
GROQ_API_KEY=your_api_key_here
```

### Run

```bash
python main.py
```

---

## Example

```
You: calculate 20*5

Planner Decision:
{
    "tool": "calculate",
    "input": "20*5"
}

Agent:
The answer is 100.
```

```
You: Why is climate change dangerous?

Planner Decision:
{
    "tool": "rag_search",
    "input": "Why is climate change dangerous?"
}

Agent:
Climate change increases sea levels, intensifies storms,
causes extreme weather events, and threatens ecosystems
and human societies.
```

---

## Future Improvements

- Persist FAISS index to disk
- Semantic chunking
- Conversation memory
- External API tools
- ReAct-style planning loop
- LangChain / LangGraph implementation

---

## Learning Outcomes

This project was implemented from scratch to understand the core ideas behind modern AI systems before using higher-level frameworks.

Key concepts implemented:

- Retrieval-Augmented Generation (RAG)
- FAISS vector indexing
- Cross-encoder reranking
- LLM planning
- JSON tool calling
- Dynamic tool dispatch
- Grounded response generation
