from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import time
import json

from main import run

app = FastAPI(
    title="AI RAG Agent",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query(request: QueryRequest):

    start_time = time.perf_counter()

    answer = run(request.query)

    latency_ms = round(
        (time.perf_counter() - start_time) * 1000,
        2
    )

    log = {
        "timestamp": datetime.now().isoformat(),
        "query": request.query,
        "answer": answer,
        "latency_ms": latency_ms
    }

    with open("logs/requests.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")

    return {
        "answer": answer,
        "sources": []
    }