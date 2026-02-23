#import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#from ml.rag.base_rag import BaseRAGPipeline
#from llm-rag-system.ml.rag.base_rag import BaseRAGPipeline
from .schemas.rag import RAGQueryRequest, RAGQueryResponse
from .service.rag_pipeline import rag_pipeline
from backend.common.logging.logger import logger

#logging.basicConfig(
#    level=logging.INFO,
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#)

#logger = logging.getLogger("RAGService")

app = FastAPI(
    title="RAG Service"
)

#rag_pipeline = BaseRAGPipeline()

# Request model
class QueryRequest(BaseModel):
    query: str

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "rag_service"}

# Placeholder RAG endpoint
@app.post("/query", response_model = RAGQueryResponse)
async def query_rag(request: RAGQueryRequest):
    logger.info("Received a new RAG query request.")
    try:
        result = await rag_pipeline.run(request.query)
        logger.info("RAG query processed successfully.")
        return RAGQueryResponse(answer=result["answer"], sources=result["sources"])

    except Exception as e:
        logger.error(f"RAG pipeline execution failed: {e}")
        return HTTPException(status_code=500, detail="RAG pipeline execution failed.")
