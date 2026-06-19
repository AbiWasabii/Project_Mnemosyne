from services.memory.memory_store import load_memories
from services.agents.goal_agent import create_goals
from services.core.llm import ask_model


def build_personality(owner: str) -> str:

    memories = load_memories(owner)

    goals = create_goals(owner)

    prompt = f"""
Memories:

{memories}

Goals:

{goals}

Describe this person's personality.

List several traits and a short summary.
"""

    return ask_model(prompt)