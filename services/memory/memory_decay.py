from datetime import datetime


def decay_score(memory):

    score = memory.get("importance", 5)

    access_count = memory.get("access_count", 0)

    score += access_count

    created_at = memory.get(
        "created_at",
        datetime.now().strftime("%Y-%m-%d")
    )

    created_date = datetime.strptime(
        created_at,
        "%Y-%m-%d"
    )

    age_days = (
        datetime.now() - created_date
    ).days

    score -= age_days * 0.01

    return round(score, 2)