from services.agents.identity_engine import build_identity
from services.agents.self_reflection_agent import self_reflect
from services.agents.goal_agent import create_goals

from services.core.llm import ask_model


def build_beliefs(owner):

    identity = build_identity(owner)

    reflection = self_reflect(owner)

    goals = create_goals(owner)

    prompt = f"""
Identity:

{identity}

Reflection:

{reflection}

Goals:

{goals}

These represent a person's experiences and aspirations.

Infer the beliefs this person holds.

Beliefs are things they consider true about life.

Examples:

- Relationships are important.
- Growth is valuable.
- Curiosity leads to understanding.
- Meaningful experiences should be preserved.

Do not repeat memories.

Answer in 2-5 sentences.
"""

    return ask_model(prompt)