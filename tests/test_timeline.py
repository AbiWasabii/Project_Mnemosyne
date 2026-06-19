from services.memory.memory_store import load_memories
from services.memory.timeline_builder import build_timeline

memories = load_memories("Alex")

timeline = build_timeline(memories)

for date, event in timeline:

    print(date)
    print("-", event)