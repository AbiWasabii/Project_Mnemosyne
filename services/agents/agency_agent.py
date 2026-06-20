from services.agents.goal_agent import create_goals
from services.agents.long_term_goal_agent import create_long_term_goals
from services.agents.value_engine import build_values

from services.core.llm import ask_model


def decide_next_action(owner):

    goals = create_goals(owner)

    long_term_goals = create_long_term_goals(owner)

    values = build_values(owner)

    prompt = f"""
Goals:

{goals}

Long-term goals:

{long_term_goals}

Values:

{values}

These represent the person's objectives and values.

Suggest the next action this person should take.

Focus on practical actions.

Answer in 1-3 sentences.
"""

    return ask_model(prompt)