from services.memory.memory_store import load_memories


def dream(owner):

    memories = load_memories(owner)

    summary = ""

    for memory in memories:

        summary += memory["content"] + ". "

    return {

        "owner": owner,

        "dream":
            summary

    }