
import requests

from langchain_core.embeddings import Embeddings
from langchain_core.messages import AIMessage

from app.utils.config import (
    CHAT_API_URL,
    CHAT_MODEL_NAME,
    CHAT_API_KEY,
    EMBEDDING_API_URL,
    EMBEDDING_API_KEY,
    EMBEDDING_DIMENSIONS,
)


# ==========================================
# QUASAR CHAT MODEL
# ==========================================

class QuasarChatModel:

    def invoke(self, prompt):

        if not CHAT_API_URL or not CHAT_API_KEY:
            raise ValueError("Quasar Chat API configuration missing.")

        if hasattr(prompt, "to_string"):
            prompt = prompt.to_string()

        if not isinstance(prompt, str):
            prompt = str(prompt)

        payload = {
            "model": CHAT_MODEL_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "top_p": 0.9,
            "max_tokens": 1000
        }

        try:
            response = requests.post(
                CHAT_API_URL,
                headers={
                    "Content-Type": "application/json",
                    "X-API-KEY": CHAT_API_KEY
                },
                json=payload,
                timeout=120
            )

            if not response.ok:
                print("\nQUASAR CHAT API ERROR")
                print("STATUS:", response.status_code)
                print("BODY:", response.text[:3000])

                response.raise_for_status()

            result = response.json()

            # OpenAI-compatible response format
            if "choices" in result:
                content = result["choices"][0]["message"]["content"]

            # Alternative response format
            elif "content" in result:
                content = result["content"]

            elif "response" in result:
                content = result["response"]

            else:
                raise ValueError(
                    f"Unexpected Quasar response: {str(result)[:1000]}"
                )

            return AIMessage(content=str(content))

        except requests.RequestException as error:
            print("Quasar request failed:", repr(error))
            raise


def get_llm():
    return QuasarChatModel()


# ==========================================
# QUASAR EMBEDDING MODEL
# ==========================================

class QuasarEmbeddings(Embeddings):

    def __init__(self):
        self.api_url = EMBEDDING_API_URL
        self.api_key = EMBEDDING_API_KEY

    def _get_single_embedding(self, text):

        response = requests.post(
            self.api_url,
            headers={
                "Content-Type": "application/json",
                "X-API-KEY": self.api_key
            },
            json={
                "texts": [text],
                "dimensions": EMBEDDING_DIMENSIONS
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        vector = (
            result.get("embeddings")
            if isinstance(result, dict)
            else result
        )

        if (
            isinstance(vector, list)
            and vector
            and isinstance(vector[0], (int, float))
        ):
            pass

        elif (
            isinstance(vector, list)
            and len(vector) == 1
            and isinstance(vector[0], list)
        ):
            vector = vector[0]

        else:
            raise ValueError(
                f"Unexpected embedding response: {str(result)[:500]}"
            )

        if len(vector) != EMBEDDING_DIMENSIONS:
            raise ValueError(
                f"Expected {EMBEDDING_DIMENSIONS} dimensions, "
                f"received {len(vector)}."
            )

        return [float(value) for value in vector]

    def embed_documents(self, texts):
        return [
            self._get_single_embedding(text)
            for text in texts
        ]

    def embed_query(self, text):
        return self._get_single_embedding(text)


def get_embeddings():
    return QuasarEmbeddings()
