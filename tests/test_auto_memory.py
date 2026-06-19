from services.memory.memory_extractor import extract_memories
from services.memory.memory_store import append_memory

text = "Mimi likes matcha tea."

memories = extract_memories(text)

for memory in memories:

    append_memory(
        owner=memory["owner"],
        filename="preferences.json",
        memory=memory
    )

print("Memory saved.")