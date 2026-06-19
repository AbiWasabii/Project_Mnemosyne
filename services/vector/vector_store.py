from services.memory.memory_store import load_memories
from services.vector.embedder import embed


def build_vector_store(owner: str) -> list:
    """
    Build embeddings for all memories.
    """

    memories = load_memories(owner)

    vectors = []

    for memory in memories:

        vectors.append(
            {
                "content": memory["content"],
                "embedding": embed(memory["content"])
            }
        )

    return vectors