from services.agents.identity_engine import build_identity
from services.agents.belief_engine import build_beliefs
from services.agents.value_engine import build_values
from services.agents.curiosity_agent import generate_questions

from services.core.llm import ask_model


def imagine(owner):

    identity = build_identity(owner)

    beliefs = build_beliefs(owner)

    values = build_values(owner)

    curiosity = generate_questions(owner)

    prompt = f"""
Identity:

{identity}

Beliefs:

{beliefs}

Values:

{values}

Curiosity:

{curiosity}

These represent a person's mind.

Imagine new ideas, experiences, projects or possibilities.

Examples:

- New hobbies.
- Future adventures.
- New projects.
- Creative pursuits.

Be imaginative but realistic.

Answer in 2-5 sentences.
"""

    return ask_model(prompt)