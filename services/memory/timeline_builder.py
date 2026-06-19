def build_timeline(memories):

    timeline = []

    for memory in memories:

        if "created_at" in memory:

            timeline.append(
                (
                    memory["created_at"],
                    memory["content"]
                )
            )

    timeline.sort()

    return timeline