from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self, model_name="BAAI/bge-reranker-base"):

        self.model = CrossEncoder(model_name)

    def rerank(self, query, results):

        # Nothing to rerank
        if len(results) <= 1:
            return results

        # Create (query, chunk) pairs
        pairs = [
            [query, chunk["text"]]
            for chunk in results
        ]

        # Get reranker scores
        scores = self.model.predict(pairs)

        # Add reranker score to each chunk
        for chunk, score in zip(results, scores):
            chunk["rerank_score"] = float(score)

        # Sort by reranker score
        results.sort(
            key=lambda chunk: chunk["rerank_score"],
            reverse=True
        )

        return results
