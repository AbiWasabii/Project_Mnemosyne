import ollama

MODEL_NAME = "gemma3:4b" 
# MODEL_NAME = "qwen3:8b" 
# MODEL_NAME = "qwen3:4b" 


def ask_model(prompt):

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": """
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