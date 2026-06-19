from services.memory.memory_store import load_memories
from services.memory.episode_creator import create_episode

memories = load_memories("Alex")

episode = create_episode(
    owner="Alex",
    memories=memories
)

print(episode)