# ManusAge — Document Age Estimation System

ManusAge is an end-to-end GenAI platform designed to estimate the age of handwritten or printed text on paper by analyzing ink characteristics, document features, and contextual metadata.  
It combines vision models, RAG pipelines, LLM reasoning, evaluation tools, and agentic orchestration into a scalable, production-ready architecture.

---

## 🚀 Project Goals

- Estimate the age of ink or printed text on documents
- Provide explainable reasoning using RAG + LLM
- Support vision-based document analysis
- Enable fine-tuning and evaluation workflows
- Run as modular microservices (RAG, Eval, Admin)
- Support scalable and reliable deployment
- Follow real-world engineering and MLOps practices

---

## 📁 Project Structure
llm-rag-system/
backend/
services/
ragservicee/
eval_service/
adminservicee/
common/
config/
logging/
ml/
rag/
eval/
finetune/
models/
data/
configs/
tests/
infra/


---

- [x] Service running successfully at `http://localhost:8000/docs`

---

## 🛠️ Tech Stack

- **FastAPI** — microservices  
- **Uvicorn** — ASGI server  
- **LlamaIndex** — RAG pipeline  
- **ChromaDB** — vector store  
- **Pydantic** — request/response models  
- **Python-dotenv** — config management  

More components (vision models, evaluation, fine-tuning, agents) will be added in upcoming phases.

---

## 📌 Next Steps

- Implement basic RAG pipeline  
- Add document loaders  
- Add vector store initialization  
- Build evaluation microservice  
- Add agentic orchestration layer  
- Integrate vision model for ink analysis  

---

## 📄 License

This project is for educational and portfolio purposes.



