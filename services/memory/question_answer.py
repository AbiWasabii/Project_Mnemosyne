from services.memory.memory_search import search_memory
from services.memory.context_builder import build_context
from services.memory.keyword_extractor import extract_keyword
from services.core.llm import ask_model


def answer_question(owner, question):

    keywords = extract_keyword(question)

    memories = search_memory(owner, keywords)

    print("\nRelevant memories:")

    if memories:
        for memory in memories:
            print("-", memory["content"])
    else:
        print("(none)")
        return "I don't know."

    context = build_context(memories)

    prompt = f"""
These memories are facts.

{context}

Rules:

1. Use ONLY the memories above.
2. Never invent information.
3. If no relevant memories exist, answer exactly:

I don't know.

4. Do not guess.
5. Do not use outside knowledge.

Question:

{question}

Answer:
"""

    answer = ask_model(prompt)

    return answer