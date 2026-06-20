from services.agents.self_reflection_agent import self_reflect
from services.agents.dream_agent import dream
from services.agents.goal_agent import create_goals

from services.core.llm import ask_model


def create_long_term_goals(owner):

    reflection = self_reflect(owner)

    dreams = dream(owner)

    goals = create_goals(owner)

    prompt = f"""
Reflection:

{reflection}

Dreams:

{dreams}

Current goals:

{goals}

These describe a person's experiences and aspirations.

Suggest long-term goals over months or years.

Examples:

- Strengthen important relationships.
- Continue learning and growing.
- Build meaningful projects.
- Create a fulfilling life.

Answer in 2-4 sentences.
"""

    return ask_model(prompt)