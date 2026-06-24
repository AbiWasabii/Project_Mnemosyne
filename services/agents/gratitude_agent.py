from services.agents.wisdom_agent import wisdom
from services.agents.principle_agent import build_principles
from services.agents.regret_agent import infer_regrets

from services.core.llm import ask_model


def gratitude(owner):

    wise = wisdom(owner)

    principles = build_principles(owner)

    regrets = infer_regrets(owner)

    prompt = f"""
Wisdom:

{wise}

Principles:

{principles}

Regrets:

{regrets}

These represent a person's understanding.

What should this person appreciate?

Examples:

- Loved ones.
- Shared experiences.
- Opportunities for growth.
- Simple joys.

Answer in 3-7 concise appreciations.
"""

    return ask_model(prompt)