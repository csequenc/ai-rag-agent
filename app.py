import os
from dotenv import load_dotenv

from chunker import Chunker
from retriever import Retriever
from reranker import Reranker
from generator import Generator
from utils import load_documents

# Configuration
CHUNK_SIZE = 100
OVERLAP = 20
TOP_K = 5
THRESHOLD = 0.30

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")


# Initialize Components
chunker = Chunker(
    chunk_size=CHUNK_SIZE,
    overlap=OVERLAP
)

chunks = load_documents(
    "data",
    chunker
)

retriever = Retriever()
retriever.build_index(chunks)

reranker = Reranker()

generator = Generator(
    api_key=API_KEY
)


# Chat Loop
while True:

    query = input("\nAsk a question (or type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    results = retriever.search(
        query,
        top_k=TOP_K
    )

    results = reranker.rerank(
        query,
        results
    )

    print("\nRetrieved Chunks:\n")

    for rank, chunk in enumerate(results, start=1):
        print("-" * 40)
        print(f"Rank   : {rank}")
        print(f"Score  : {chunk['score']:.4f}")
        print(f"Rerank : {chunk['rerank_score']:.4f}")
        print(f"Source : {chunk['source']}")
        print(f"Text   : {chunk['text']}")

    if not results or results[0]["score"] < THRESHOLD:
        print("\nAnswer:\n")
        print("I don't know based on the provided documents.")
        continue

    response = generator.generate(
        query,
        results
    )

    print("\nAnswer:\n")
    print(response)
