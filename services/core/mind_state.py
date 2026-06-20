from services.agents.self_reflection_agent import self_reflect
from services.agents.personality_builder import build_personality
from services.agents.goal_agent import create_goals
from services.agents.identity_engine import build_identity
from services.agents.belief_engine import build_beliefs
from services.agents.value_engine import build_values


def build_mind_state(owner):

    return {

        "reflection": self_reflect(owner),

        "personality": build_personality(owner),

        "goals": create_goals(owner),

        "identity": build_identity(owner),

        "beliefs": build_beliefs(owner),

        "values": build_values(owner)

    }