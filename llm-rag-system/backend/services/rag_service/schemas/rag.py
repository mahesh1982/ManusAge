from pydantic import BaseModel
from typing import List

class RAGQueryRequest(BaseModel):
    query: str

class RAGQueryResponse(BaseModel):
    answer: str
    sources: List[str]
    
    