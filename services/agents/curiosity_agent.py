from services.agents.identity_engine import build_identity
from services.agents.belief_engine import build_beliefs

from services.core.llm import ask_model


def generate_questions(owner):

    identity = build_identity(owner)

    beliefs = build_beliefs(owner)

    prompt = f"""
Identity:

{identity}

Beliefs:

{beliefs}

These represent a person's understanding.

What important things might they still not know?

Generate curious questions.

Examples:

- What new hobbies could I explore?
- How can I strengthen my relationships?
- What skills should I learn?
- What experiences would enrich my life?

Answer in 3-5 questions.
"""

    return ask_model(prompt)