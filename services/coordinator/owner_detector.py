def detect_owner(question):

    question = question.lower()

    if "mimi" in question:
        return "Mimi"

    if "alex" in question:
        return "Alex"

    if "she" in question:
        return "Shared"

    if "he" in question:
        return "Shared"

    return "Shared"