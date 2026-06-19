from services.memory.memory_store import append_memory


def create_memory(owner, fact):

    memory = {
        "id": f"{owner.lower()}_pref_auto",
        "type": fact["type"],
        "owner": owner,
        "content": fact["content"],
        "importance": 8
    }

    append_memory(
        owner,
        "preferences.json",
        memory
    )