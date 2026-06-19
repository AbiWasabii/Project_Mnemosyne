from services.agents.reflection_agent import reflection_agent
from services.agents.daily_journal_agent import create_daily_journal
from services.agents.goal_agent import create_goals
from services.agents.personality_builder import build_personality
from services.agents.relationship_agent import build_relationship
from services.agents.world_model_agent import build_world_model


def think(owner):

    return {

        "reflection": reflection_agent(owner),

        "journal": create_daily_journal(owner),

        "goals": create_goals(owner),

        "personality": build_personality(owner),

        "relationship": build_relationship(),

        "world_model": build_world_model()

    }