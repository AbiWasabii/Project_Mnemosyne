from services.memory.memory_store import load_memories
from services.memory.memory_consolidator import consolidate_preferences


memories = load_memories("Mimi")

summary = consolidate_preferences(memories)

print(summary)