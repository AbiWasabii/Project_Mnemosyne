from services.core.thought_compressor import compress_memories
from services.agents.reflection_agent import reflection_agent

from services.core.llm import ask_model


def subconscious_thought(owner):

    themes = compress_memories(
        owner
    )

    reflection = reflection_agent(
        owner
    )

    prompt = f"""
Themes:

{themes}

Reflection:

{reflection}

Generate one subconscious thought.

Examples:

- Relationships should be nurtured.

- Meaningful experiences should be preserved.

- Personal growth is important.

Keep it to 1-3 sentences.
"""

    return ask_model(
        prompt
    )