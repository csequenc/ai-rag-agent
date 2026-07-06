from chunker import Chunker
from retriever import Retriever

text = open("data/ai_notes.txt", "r", encoding="utf-8").read()

chunker = Chunker(
    chunk_size=100,
    overlap=20
)

chunks = chunker.chunk_text(
    text,
    "ai_notes.txt"
)

retriever = Retriever()

retriever.build_index(chunks)

query = "What does FAISS do?"

results = retriever.search(query)

for result in results:
    print("-" * 40)
    print("Score :", result["score"])
    print("Source:", result["source"])
    print(result["text"])
