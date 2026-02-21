from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ManusAge - RAG Service",
    description="Core RAG microservice for ManusAge project",
    version="0.1.0"
)

# Request model
class QueryRequest(BaseModel):
    query: str

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "rag_service"}

# Placeholder RAG endpoint
@app.post("/query")
def query_rag(request: QueryRequest):
    # RAG not implemented yet — this is just a skeleton
    return {
        "query": request.query,
        "answer": "RAG pipeline not implemented yet",
        "sources": []
    }
