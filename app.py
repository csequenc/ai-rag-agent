from chunker import Chunker
from retriever import Retriever
from generator import Generator

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

query = input("Ask a question: ")

results = retriever.search(query)

generator = Generator(
    api_key="YOUR_GROQ_API_KEY"
)

response = generator.generate(
    query,
    results
)

print(response)
