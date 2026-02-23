from backend.common.prompt.prompt_loader import load_active_prompt

class RAGPipeline:
    async def run(self, query: str):
        # Load the latest active system prompt from PostgreSQL
        system_prompt = await load_active_prompt("rag_system_prompt")

        # Temporary logic until LLM integration
        return {
            "answer": f"System Prompt Loaded: {system_prompt}\n\nQuery: {query}",
            "sources": ["test.txt"]
        }

rag_pipeline = RAGPipeline()
