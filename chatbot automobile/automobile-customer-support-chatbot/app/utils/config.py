
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

CHAT_API_URL = os.getenv("CHAT_API_URL", "")
CHAT_MODEL_NAME = os.getenv("CHAT_MODEL_NAME", "gpt-4o")
CHAT_API_KEY = os.getenv("CHAT_API_KEY", "")

EMBEDDING_API_URL = os.getenv("EMBEDDING_API_URL", "")
EMBEDDING_MODEL_NAME = os.getenv(
    "EMBEDDING_MODEL_NAME", "text-embeddings"
)
EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY", "")
EMBEDDING_DIMENSIONS = int(
    os.getenv("EMBEDDING_DIMENSIONS", "746")
)

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH", "./data/processed/chroma_db"
)

if not os.path.isabs(CHROMA_DB_PATH):
    CHROMA_DB_PATH = str(ROOT_DIR / CHROMA_DB_PATH)

DOCUMENTS_PATH = ROOT_DIR / "data" / "documents"
COLLECTION_NAME = "automobile_knowledge"
