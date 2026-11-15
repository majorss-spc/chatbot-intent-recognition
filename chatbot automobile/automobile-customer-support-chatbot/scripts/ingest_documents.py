
from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.vector_store import create_vector_store


def main():

    print("\nStarting Automobile Document Ingestion...\n")

    documents = load_documents()

    if not documents:

        print(
            "No PDF or TXT documents found in data/documents."
        )

        print(
            "Please add automobile manuals and run this script again."
        )

        return

    print(f"Loaded {len(documents)} document pages/files.")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} text chunks.")

    create_vector_store(chunks)

    print("\nDocuments successfully stored in ChromaDB!")

    print("Automobile RAG Knowledge Base is ready.\n")


if __name__ == "__main__":
    main()
