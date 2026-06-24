from services.agents.principle_agent import build_principles
from services.agents.wisdom_agent import wisdom

from services.core.llm import ask_model


def infer_regrets(owner):

    principles = build_principles(owner)

    wise = wisdom(owner)

    prompt = f"""
Principles:

{principles}

Wisdom:

{wise}

These represent a person's understanding.

Infer possible regrets this person should avoid.

Examples:

- Neglecting important relationships.
- Forgetting meaningful experiences.
- Taking loved ones for granted.
- Ignoring opportunities for growth.

Answer in 3-7 concise regrets.
"""

    return ask_model(prompt)