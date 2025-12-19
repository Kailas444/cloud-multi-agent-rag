# Cloud-Deployed Multi-Agent RAG System

## Features
- Multi-Agent Architecture
- ReAct Reasoning
- RAG with Vector DB
- Gemini LLM
- LangGraph Orchestration
- Cloud Deployable

## Run Locally
```bash
pip install -r requirements.txt
uvicorn api.app:app --reload
python ui/gradio_ui.py
