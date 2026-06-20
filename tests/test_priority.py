from services.core.priority_system import prioritize_memories

from services.memory.memory_store import load_memories


memories = load_memories(
    "Alex"
)

ranked = prioritize_memories(
    memories
)

print()

for memory in ranked:

    print(

        memory["importance"],

        "-",

        memory["content"]

    )