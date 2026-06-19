import ollama
from services.config import MODEL_NAME


def ask_model(prompt: str) -> str:

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content":
                """
Answer concisely.
Use the provided memories.
Do not ask follow-up questions unless necessary.
Limit answers to 1-3 sentences.
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]