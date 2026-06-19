from services.agents.memory_agent import memory_agent
from services.agents.timeline_agent import timeline_agent
from services.agents.episode_agent import episode_agent


def route(owner, question):

    q = question.lower()

    if "when" in q:

        return timeline_agent(owner)

    if "episode" in q:

        return episode_agent(owner)

    return memory_agent(
        owner,
        question
    )