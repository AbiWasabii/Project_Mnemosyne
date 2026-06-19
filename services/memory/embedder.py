import ollama


MODEL_NAME = "nomic-embed-text"


def embed(text):

    response = ollama.embeddings(
        model=MODEL_NAME,
        prompt=text
    )

    return response["embedding"]