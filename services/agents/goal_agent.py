from services.agents.daily_journal_agent import create_daily_journal
from services.core.llm import ask_model


def create_goals(owner: str) -> str:

    journal = create_daily_journal(owner)

    prompt = f"""
Daily Journal:

{journal["summary"]}

Based on this journal, suggest 1-3 goals.

Answer concisely.
"""

    return ask_model(prompt)