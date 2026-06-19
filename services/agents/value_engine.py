from services.agents.belief_engine import build_beliefs
from services.agents.identity_engine import build_identity
from services.agents.emotion_agent import detect_emotions

from services.core.llm import ask_model


def build_values(owner):

    beliefs = build_beliefs(owner)

    identity = build_identity(owner)

    emotions = detect_emotions(owner)

    prompt = f"""
Beliefs:

{beliefs}

Identity:

{identity}

Emotions:

{emotions}

These represent a person's experiences, feelings and beliefs.

Infer the values that matter most to this person.

Examples:

- Love
- Family
- Companionship
- Curiosity
- Growth
- Loyalty
- Happiness
- Creativity

Values are deeper than memories.

Do not repeat facts.

Answer in 2-5 sentences.
"""

    return ask_model(prompt)