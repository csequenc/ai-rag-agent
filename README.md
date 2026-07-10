# AI RAG Agent: From First Principles to LangChain

A production-style AI agent built in two stages:

- **Manual Implementation** – Build an AI agent from first principles to understand how planners, tool dispatch, and Retrieval-Augmented Generation (RAG) work internally.
- **Framework Implementation** – Refactor the same agent using modern LangChain (`create_agent`) while reusing the same RAG pipeline and tools.

This project demonstrates the evolution from implementing an AI agent manually to leveraging a modern framework without sacrificing understanding of the underlying concepts.

---

# Features

## Manual Implementation

- Custom LLM planner
- Structured JSON tool selection
- Dynamic tool registry
- Manual tool dispatch
- Calculator tool
- Retrieval-Augmented Generation (RAG)

## Framework Implementation

- LangChain `@tool`
- LangChain `create_agent`
- Automatic tool selection
- Automatic tool execution
- Weather API tool
- Reusable RAG tool

## RAG Pipeline

- Document chunking with overlap
- Sentence Transformer embeddings
- FAISS vector search
- Cross-Encoder reranking
- Grounded answer generation using Groq

---

# Repository Branches

## `manual-implementation`

Implements every component manually.

```
User
    ↓
Planner Prompt
    ↓
JSON Output
    ↓
Tool Registry
    ↓
Tool Dispatch
    ↓
Tool Execution
    ↓
Response
```

---

## `main`

Refactors the project using LangChain.

```
User
    ↓
create_agent()
    ↓
Automatic Tool Calling
    ↓
Tool Execution
    ↓
Final Response
```

This demonstrates how modern frameworks abstract the same workflow implemented manually.

---

# Architecture (Framework Version)

```
                    User Query
                         │
                         ▼
                 LangChain Agent
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
   Calculator Tool   RAG Search    Weather Tool
                         │
                         ▼
                Sentence Transformers
                         │
                         ▼
                     FAISS Search
                         │
                         ▼
                 Cross Encoder Reranker
                         │
                         ▼
                  Retrieved Context
                         │
                         ▼
                 Groq Response Generation
                         │
                         ▼
                    Final Response
```

---

# Technologies

- Python
- LangChain
- Groq
- FAISS
- Sentence Transformers
- HuggingFace Transformers
- Cross Encoder
- Requests
- python-dotenv

---

# Project Structure

```
ai-rag-agent/
│
├── framework_agent.py
├── framework_tools.py
├── framework_rag.py
│
├── chunker.py
├── retriever.py
├── reranker.py
├── generator.py
├── utils.py
│
├── data/
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd ai-rag-agent
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

# Run

```bash
python framework_agent.py
```

---

# Example Queries

```
25 * 17
```

```
What is climate change?
```

```
What is the weather in Delhi?
```

```
Summarize the causes of global warming.
```

---

# Learning Outcomes

This project was intentionally built in two stages to understand both the implementation details and the framework abstractions behind modern AI agents.

Concepts covered:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- FAISS Indexing
- Cross-Encoder Reranking
- Tool Calling
- Dynamic Tool Registry
- Planner Design
- LangChain Tools
- LangChain `create_agent`
- External API Integration
- Modular AI Agent Design

---

# Future Improvements

- Persistent FAISS index
- Streaming responses
- Conversation memory
- Multi-tool reasoning
- LangGraph workflows
- MCP integration
- Multi-agent architecture
