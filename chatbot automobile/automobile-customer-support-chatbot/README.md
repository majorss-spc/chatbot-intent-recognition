
# Automobile Customer Support Chatbot

An AI-powered automobile customer support chatbot developed using Python, FastAPI, LangChain, Retrieval-Augmented Generation (RAG), ChromaDB and an Intent Recognition Orchestrator.

## Technologies Used

- Python
- FastAPI
- LangChain
- OpenAI LLM
- OpenAI Embeddings
- ChromaDB
- Retrieval-Augmented Generation
- Intent Recognition
- HTML, CSS and JavaScript

## Main Features

1. Intent classification
2. Automobile document loading
3. Text splitting
4. Vector embeddings
5. ChromaDB vector storage
6. Semantic document retrieval
7. Context-based response generation
8. FastAPI chatbot API
9. Web-based chatbot interface

## Project Setup

Install dependencies:

```powershell
pip install -r requirements.txt
```

Configure your OpenAI API key in `.env`.

Add automobile PDF or TXT manuals inside:

`data/documents/`

Create the knowledge base:

```powershell
python -m scripts.ingest_documents
```

Start the backend:

```powershell
uvicorn app.main:app --reload
```

Open the chatbot:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

Health check:

`http://127.0.0.1:8000/health`
