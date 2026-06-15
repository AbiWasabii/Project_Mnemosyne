from services.memory.memory_store import load_memories
from services.memory.memory_scoring import calculate_score


def search_memory(owner, keyword):

    memories = load_memories(owner)

    results = []

    keyword = keyword.lower()

    for memory in memories:

        if keyword in memory["content"].lower():

            memory["score"] = calculate_score(memory)

            results.append(memory)

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results