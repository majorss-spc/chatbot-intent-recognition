
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from app.utils.config import DOCUMENTS_PATH

def load_documents():
    documents = []

    DOCUMENTS_PATH.mkdir(parents=True, exist_ok=True)

    for file_path in DOCUMENTS_PATH.rglob("*"):
        if not file_path.is_file():
            continue

        suffix = file_path.suffix.lower()

        try:
            if suffix == ".pdf":
                loader = PyPDFLoader(str(file_path))
                documents.extend(loader.load())

            elif suffix == ".txt":
                loader = TextLoader(
                    str(file_path),
                    encoding="utf-8"
                )
                documents.extend(loader.load())

        except Exception as error:
            print(f"Could not load {file_path.name}: {error}")

    return documents
