def create_episode(owner, memories):

    contents = []

    for memory in memories:
        contents.append(memory["content"])

    return {
        "type": "episode",
        "owner": owner,
        "summary": ". ".join(contents)
    }