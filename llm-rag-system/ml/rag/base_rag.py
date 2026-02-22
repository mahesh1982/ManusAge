import logging
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM

logger = logging.getLogger("RAGPipeline")

#logger.info(">>> BaseRAGPipeline __init__ CALLED <<<")

class BaseRAGPipeline:
    def __init__(self, data_path="data/documents"):
        logger.info(">>> BaseRAGPipeline __init__ CALLED <<<")
        self.data_path = data_path

        # Local embedding model
        self.embed_model = HuggingFaceEmbedding(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Local LLM model (no OpenAI)
        logger.info("Loading Qwen2.5-1.5B-Instruct model...")
        self.llm = HuggingFaceLLM(
                                    model_name="Qwen/Qwen2.5-1.5B-Instruct",
                                    tokenizer_name="Qwen/Qwen2.5-1.5B-Instruct",
                                    max_new_tokens=256,
                                    device_map="auto"
                                )

        logger.info("LLM loaded successfully.")


        self.index = None

    def load_documents(self):
        logger.info("Loading documents from directory.")
        return SimpleDirectoryReader(self.data_path).load_data()

    def build_index(self):
        logger.info("Building RAG index using HuggingFace embeddings.")
        documents = self.load_documents()
        self.index = VectorStoreIndex.from_documents(
            documents,
            embed_model=self.embed_model
        )
        logger.info("RAG index built successfully.")
        return self.index

    def query(self, text: str):
        if not self.index:
            raise ValueError("Index not built or loaded.")
        logger.info(f"Executing RAG query: {text}")
        query_engine = self.index.as_query_engine(llm=self.llm)
        return query_engine.query(text)
