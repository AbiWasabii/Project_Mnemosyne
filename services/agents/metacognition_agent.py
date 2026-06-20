from services.agents.self_reflection_agent import self_reflect
from services.agents.identity_engine import build_identity
from services.agents.belief_engine import build_beliefs
from services.agents.value_engine import build_values

from services.core.llm import ask_model


def analyze_thinking(owner):

    reflection = self_reflect(owner)

    identity = build_identity(owner)

    beliefs = build_beliefs(owner)

    values = build_values(owner)

    prompt = f"""
Reflection:

{reflection}

Identity:

{identity}

Beliefs:

{beliefs}

Values:

{values}

These describe a person's mind.

Analyze how this person thinks.

Examples:

- Emotionally driven.
- Relationship-oriented.
- Curious.
- Reflective.
- Practical.

Do not repeat facts.

Answer in 2-5 sentences.
"""

    return ask_model(prompt)