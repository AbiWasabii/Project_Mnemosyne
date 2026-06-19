from datetime import date

from services.memory.memory_store import load_memories


def create_daily_journal(owner: str) -> dict:
    """
    Create a simple journal from recent memories.
    """

    memories = load_memories(owner)

    summary = ""

    for memory in memories[-5:]:

        summary += memory["content"] + ". "

    return {
        "date": str(date.today()),
        "owner": owner,
        "summary": summary
    }