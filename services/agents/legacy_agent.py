from services.agents.wisdom_agent import wisdom
from services.agents.principle_agent import build_principles
from services.agents.gratitude_agent import gratitude

from services.core.llm import ask_model


def legacy(owner):

    wise = wisdom(owner)

    principles = build_principles(owner)

    thankful = gratitude(owner)

    prompt = f"""
Wisdom:

{wise}

Principles:

{principles}

Gratitude:

{thankful}

These represent a person's understanding.

What legacy would this person hope to leave behind?

Examples:

- Loving relationships.

- Meaningful memories.

- Positive impact on others.

- A life well lived.

Do not repeat facts.

Answer in 2-5 sentences.
"""

    return ask_model(prompt)