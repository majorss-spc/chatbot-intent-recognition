
from pathlib import Path

from langchain_chroma import Chroma

from app.llm.model import get_embeddings
from app.utils.config import CHROMA_DB_PATH, COLLECTION_NAME


def create_vector_store(documents):
    if not documents:
        raise ValueError("No documents available for ingestion.")

    Path(CHROMA_DB_PATH).mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=get_embeddings(),
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DB_PATH
    )

    return vector_store


def get_vector_store():
    Path(CHROMA_DB_PATH).mkdir(
        parents=True,
        exist_ok=True
    )

    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DB_PATH,
        embedding_function=get_embeddings()
    )
