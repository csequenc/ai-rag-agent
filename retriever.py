from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class Retriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):

        # Calling the model of Sentence Transformer
        self.model = SentenceTransformer(model_name)

        self.index = None
        self.chunks = None

    def build_index(self, chunks):

        self.chunks = chunks

        texts = [chunk["text"] for chunk in chunks]

        # Turning chunks to embeddings
        embeddings = self.model.encode(texts)

        embeddings = embeddings.astype("float32")

        # Normalize
        faiss.normalize_L2(embeddings)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

    def search(self, query, top_k=3):

        # Query Embedding
        query_embedding = self.model.encode([query])
    
        query_embedding = query_embedding.astype("float32")
    
        faiss.normalize_L2(query_embedding)
    
        scores, indices = self.index.search(
            query_embedding,
            top_k
        )
    
        results = []
    
        for score, idx in zip(scores[0], indices[0]):
    
            if idx == -1:
                continue
            chunk = self.chunks[idx]
            
            results.append({
                "text": chunk["text"],
                "source": chunk["source"],
                "score": float(score)
            })
    
        return results
        
