from services.memory.memory_store import load_memories


def build_relationship() -> dict:

    alex_memories = load_memories("Alex")

    mimi_memories = load_memories("Mimi")

    return {

        "owners": [
            "Alex",
            "Mimi"
        ],

        "alex_memory_count":
            len(alex_memories),

        "mimi_memory_count":
            len(mimi_memories)
    }