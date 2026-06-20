from services.agents.identity_engine import build_identity
from services.agents.belief_engine import build_beliefs
from services.agents.value_engine import build_values
from services.agents.metacognition_agent import analyze_thinking

from services.core.llm import ask_model


def preserve_self(owner):

    identity = build_identity(owner)

    beliefs = build_beliefs(owner)

    values = build_values(owner)

    thinking = analyze_thinking(owner)

    prompt = f"""
Identity:

{identity}

Beliefs:

{beliefs}

Values:

{values}

Thinking style:

{thinking}

These represent a person's mind.

What should this person protect in order to preserve who they are?

Examples:

- Relationships.
- Important memories.
- Core values.
- Long-term goals.

Do not repeat facts.

Answer in 2-5 sentences.
"""

    return ask_model(prompt)