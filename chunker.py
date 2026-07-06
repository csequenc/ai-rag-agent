class Chunker:
    def __init__(self, chunk_size=400, overlap=80):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text):
        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            remaining = len(text) - end

            if remaining < self.chunk_size / 2:
                chunks.append(text[start:])
                break

            chunks.append(text[start:end])

            start += self.chunk_size - self.overlap

        return chunks
