from services.memory.memory_store import load_memories

from services.core.llm import ask_model


def compress_memories(owner):

    memories = load_memories(
        owner
    )

    prompt = f"""
Memories:

{memories}

Compress these memories into their most important themes.

Examples:

Love

Growth

Companionship

Curiosity

Meaning

Answer in 3-10 short themes.
"""

    return ask_model(
        prompt
    )