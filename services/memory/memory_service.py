from services.memory.memory_search import search_memory


def answer_question(question):

    question = question.lower()

    if "mimi" in question:
        owner = "mimi"
    elif "alex" in question:
        owner = "alex"
    else:
        owner = "shared"

    keyword = ""

    if "tea" in question:
        keyword = "matcha"

    results = search_memory(owner, keyword)

    if results:
        return results[0]["content"]

    return "No memory found."