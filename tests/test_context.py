from services.memory.context_builder import build_context

memories = [
    {
        "content": "Likes matcha tea"
    },
    {
        "content": "Visited Japan"
    }
]

print(build_context(memories))