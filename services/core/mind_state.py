from services.agents.reflection_agent import reflection_agent
from services.agents.personality_builder import build_personality
from services.agents.goal_agent import create_goals
from services.agents.identity_engine import build_identity
from services.agents.belief_engine import build_beliefs
from services.agents.value_engine import build_values


def build_mind_state(owner):

    state = {

        "reflection":
            reflection_agent(owner),

        "personality":
            build_personality(owner),

        "goals":
            create_goals(owner),

        "identity":
            build_identity(owner),

        "beliefs":
            build_beliefs(owner),

        "values":
            build_values(owner)

    }

    return state