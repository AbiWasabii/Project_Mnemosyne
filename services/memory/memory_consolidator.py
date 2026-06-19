def consolidate_preferences(memories):

    teas = []

    for memory in memories:

        content = memory["content"].lower()

        if "tea" in content:

            teas.append(content)

    if len(teas) >= 3:

        return {
            "id": "summary_tea",
            "type": "summary",
            "owner": "Mimi",
            "content": "Enjoys tea.",
            "importance": 10
        }

    return None