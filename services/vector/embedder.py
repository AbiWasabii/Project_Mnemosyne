import ollama
from services.config import EMBED_MODEL


def embed(text: str) -> list:

    response = ollama.embed(
        model=EMBED_MODEL,
        input=text
    )

    return response["embeddings"][0]