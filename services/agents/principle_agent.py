from services.agents.wisdom_agent import wisdom
from services.agents.value_engine import build_values
from services.agents.belief_engine import build_beliefs

from services.core.llm import ask_model


def build_principles(owner):

    wise = wisdom(owner)

    values = build_values(owner)

    beliefs = build_beliefs(owner)

    prompt = f"""
Wisdom:

{wise}

Values:

{values}

Beliefs:

{beliefs}

These represent a person's accumulated understanding.

Infer the principles this person should live by.

Examples:

- Love should be nurtured.
- Memories matter.
- Loyalty is valuable.
- Growth never stops.
- Meaningful experiences should be preserved.

Express them as short principles.

Answer with 3-7 principles.
"""

    return ask_model(prompt)