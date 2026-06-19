from services.agents.reflection_agent import reflection_agent
from services.agents.goal_agent import create_goals


def background_think(owner):

    reflection = reflection_agent(owner)

    goals = create_goals(owner)

    thought = {

        "owner": owner,

        "reflection":
            reflection,

        "goals":
            goals

    }

    return thought