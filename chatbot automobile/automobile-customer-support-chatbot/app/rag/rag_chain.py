
from app.llm.model import get_llm
from app.rag.vector_store import get_vector_store


def generate_rag_response(question: str):

    vector_store = get_vector_store()

    documents = vector_store.similarity_search(
        question,
        k=4
    )

    if not documents:
        return {
            "answer": (
                "I could not find relevant information in "
                "the automobile knowledge base."
            ),
            "sources": []
        }

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are an Automobile Customer Support Assistant.

Answer the user's question using ONLY the provided context.

Instructions:
1. Give clear and helpful answers.
2. Do not invent technical specifications.
3. If the answer is not available in the context,
   clearly say that the knowledge base does not contain
   sufficient information.
4. For serious vehicle problems, recommend consulting
   a qualified mechanic.

AUTOMOBILE KNOWLEDGE CONTEXT:

{context}

USER QUESTION:

{question}

ANSWER:
"""

    response = get_llm().invoke(prompt)

    sources = list(set(
        str(document.metadata.get("source", "Automobile Knowledge Base"))
        for document in documents
    ))

    return {
        "answer": response.content,
        "sources": sources
    }
