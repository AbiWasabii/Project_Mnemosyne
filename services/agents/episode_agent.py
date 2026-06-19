from services.memory.memory_store import load_memories
from services.memory.episode_creator import create_episode


def episode_agent(owner):

    memories = load_memories(owner)

    return create_episode(
        owner,
        memories
    )