from services.agents.reflection_agent import reflection_agent
from services.agents.personality_builder import build_personality
from services.agents.goal_agent import create_goals
from services.agents.dream_agent import dream
from services.core.llm import ask_model


def self_reflect(owner):

    reflection = reflection_agent(owner)

    personality = build_personality(owner)

    goals = create_goals(owner)

    dreams = dream(owner)

    prompt = f"""
Reflection:

{reflection}

Personality:

{personality}

Goals:

{goals}

Dream:

{dreams}

Describe what kind of person this is becoming.

Keep the answer concise.
"""

    return ask_model(prompt)