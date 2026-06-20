from services.agents.value_engine import build_values
from services.agents.belief_engine import build_beliefs
from services.agents.metacognition_agent import analyze_thinking
from services.agents.self_preservation_agent import preserve_self

from services.core.llm import ask_model


def wisdom(owner):

    values = build_values(owner)

    beliefs = build_beliefs(owner)

    thinking = analyze_thinking(owner)

    preservation = preserve_self(owner)

    prompt = f"""
Values:

{values}

Beliefs:

{beliefs}

Thinking Style:

{thinking}

Self Preservation:

{preservation}

These represent a person's accumulated understanding.

Given all this, what is the wisest approach to life?

Do not repeat facts.

Answer in 2-5 sentences.
"""

    return ask_model(prompt)