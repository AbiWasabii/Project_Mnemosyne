from services.memory.memory_store import load_memories


def build_memory_graph(owner):

    memories = load_memories(owner)

    graph = {

        "owner": owner,

        "memories": []

    }

    for memory in memories:

        graph["memories"].append(
            memory["content"]
        )

    return graph