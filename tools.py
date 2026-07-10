from rag import retriever, reranker
THRESHOLD = 0.30

def calculate(expression):
    try:
        result = eval(expression)
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def rag_search(query):

    results = retriever.search(
        query,
        top_k=5
    )

    results = reranker.rerank(
        query,
        results
    )

    if not results or results[0]["score"] < THRESHOLD:
        return "No relevant information found in the documents."

    lines = []

    for rank, chunk in enumerate(results, start=1):

        lines.append(
            f"""
    Context {rank}
    Source: {chunk['source']}
    Text:
    {chunk['text']}
    --------------------
    """
        )

    observation = "\n".join(lines)

    return observation