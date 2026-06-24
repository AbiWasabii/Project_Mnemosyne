from services.agents.reflection_agent import reflection_agent
from services.agents.personality_builder import build_personality
from services.agents.goal_agent import create_goals

from services.agents.identity_engine import build_identity
from services.agents.belief_engine import build_beliefs
from services.agents.value_engine import build_values
from services.agents.metacognition_agent import analyze_thinking
from services.agents.self_preservation_agent import preserve_self
from services.agents.wisdom_agent import wisdom


def build_mind_state(owner):

    return {

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
            build_values(owner),

        "thinking":
            analyze_thinking(owner),

        "self_preservation":
            preserve_self(owner),

        "wisdom":
            wisdom(owner)

    }