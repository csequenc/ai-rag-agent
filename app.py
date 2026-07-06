from chunker import Chunker
from retriever import Retriever
from generator import Generator
from utils import load_documents


# Create Chunker
chunker = Chunker(
    chunk_size=100,
    overlap=20
)

# Load Documents
chunks = load_documents(
    "data",
    chunker
)

# Build Retriever
retriever = Retriever()
retriever.build_index(chunks)

# Create Generator
generator = Generator(
    api_key="YOUR_GROQ_API_KEY"
)

THRESHOLD = 0.30

# Chat Loop
while True:

    query = input("\nAsk a question (or type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    results = retriever.search(query)

    print("\nRetrieved Chunks:\n")

    for rank, chunk in enumerate(results, start=1):
        print("-" * 40)
        print(f"Rank   : {rank}")
        print(f"Score  : {chunk['score']:.4f}")
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
