from datetime import datetime


def calculate_score(memory):

    score = memory.get("importance", 0)

    score += memory.get("access_count", 0)

    return score