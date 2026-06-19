from services.memory.memory_decay import calculate_decay

memory = {
    "content": "Likes matcha tea",
    "importance": 8,
    "access_count": 5
}

print(calculate_decay(memory))