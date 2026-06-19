from services.memory.memory_store import load_memories
from services.memory.memory_decay import decay_score


def search_memory(owner, keywords):

    memories = load_memories(owner)

    results = []

    for memory in memories:

        content = memory["content"].lower()

        for keyword in keywords:

            if keyword in content:

                memory["score"] = decay_score(memory)

                results.append(memory)

                break

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results