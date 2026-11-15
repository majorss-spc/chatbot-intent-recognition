
from app.rag.vector_store import get_vector_store


def retrieve_documents(question, k=4):
    vector_store = get_vector_store()

    if vector_store._collection.count() == 0:
        return []

    return vector_store.similarity_search(
        question,
        k=k
    )
