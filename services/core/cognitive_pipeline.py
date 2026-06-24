from services.core.mind_state import build_mind_state

from services.agents.principle_agent import build_principles
from services.agents.regret_agent import infer_regrets
from services.agents.gratitude_agent import gratitude
from services.agents.legacy_agent import legacy


def build_cognitive_pipeline(owner):

    mind = build_mind_state(owner)

    principles = build_principles(owner)

    regrets = infer_regrets(owner)

    grateful = gratitude(owner)

    future_legacy = legacy(owner)

    return {

        "mind": mind,

        "principles": principles,

        "regrets": regrets,

        "gratitude": grateful,

        "legacy": future_legacy

    }