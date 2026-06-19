from services.memory.memory_store import load_memories


def reflection_agent(owner):

    memories = load_memories(owner)

    recent = []

    for memory in memories[-5:]:

        recent.append(
            memory["content"]
        )

    reflection = {

        "owner": owner,

        "recent_memories": recent,

        "summary":
            f"{owner} has accumulated {len(memories)} memories."

    }

    return reflection