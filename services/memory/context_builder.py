def build_context(memories):

    if not memories:
        return ""

    context = "Relevant memories:\n\n"

    for memory in memories:
        context += f"- {memory['content']}\n"

    return context