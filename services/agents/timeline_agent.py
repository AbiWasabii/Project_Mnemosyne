from services.memory.memory_store import load_memories
from services.memory.timeline_builder import build_timeline


def timeline_agent(owner):

    memories = load_memories(owner)

    return build_timeline(memories)