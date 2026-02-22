import logging
from fastapi import FastAPI
from pydantic import BaseModel
from ml.rag.base_rag import BaseRAGPipeline
#from llm-rag-system.ml.rag.base_rag import BaseRAGPipeline

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("RAGService")

app = FastAPI(
    title="ManusAge - RAG Service",
    description="Core RAG microservice for ManusAge project",
    version="0.1.0"
)

rag_pipeline = BaseRAGPipeline()

# Request model
class QueryRequest(BaseModel):
    query: str

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "rag_service"}

# Placeholder RAG endpoint
@app.post("/query")
async def query_rag(request: QueryRequest):
    try:
        logger.info(f"Received query: {request.query}")

        # Build index only once
        if rag_pipeline.index is None:
            logger.info("Building RAG index for the first time...")
            rag_pipeline.build_index()
            logger.info("RAG index built successfully.")

        # Query the index
        response = rag_pipeline.query(request.query)
        logger.info("Query executed successfully.")

        return {
            "query": request.query,
            "answer": str(response),
            "sources": []
        }

    except Exception as e:
        logger.error(f"Error in RAG query: {str(e)}")
        return {"error": str(e)}
