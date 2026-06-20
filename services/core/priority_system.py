def prioritize_memories(memories):

    sorted_memories = sorted(

        memories,

        key=lambda memory:
        memory.get(
            "importance",
            0
        ),

        reverse=True

    )

    return sorted_memories