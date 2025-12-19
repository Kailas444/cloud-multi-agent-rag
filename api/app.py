from fastapi import FastAPI
from orchestration.graph import app as graph_app

app = FastAPI()

@app.post("/query")
def query_llm(payload: dict):
    state = {
        "query": payload["query"],
        "retrieved_docs": []
    }
    result = graph_app.invoke(state)
    return {
        "answer": result["final_answer"],
        "sources": result.get("citations", [])
    }
