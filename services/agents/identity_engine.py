from services.agents.personality_builder import build_personality
from services.agents.goal_agent import create_goals
from services.agents.dream_agent import dream
from services.agents.self_reflection_agent import self_reflect
from services.agents.emotion_agent import detect_emotions

from services.core.llm import ask_model


def build_identity(owner):

    personality = build_personality(owner)

    goals = create_goals(owner)

    dreams = dream(owner)

    reflection = self_reflect(owner)

    emotions = detect_emotions(owner)

    prompt = f"""
Personality:

{personality}

Goals:

{goals}

Dreams:

{dreams}

Self Reflection:

{reflection}

Emotions:

{emotions}

These represent a person's thoughts, feelings, memories and aspirations.

Describe this person's identity.

Who are they fundamentally?

Do not simply repeat facts.

Keep the answer concise.

Answer in 2-4 sentences.
"""

    return ask_model(prompt)