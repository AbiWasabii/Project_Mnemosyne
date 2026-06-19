def extract_keyword(question):

    question = question.lower()

    stop_words = [
        "what",
        "does",
        "do",
        "is",
        "are",
        "the",
        "a",
        "an",
        "like",
        "likes",
        "mimi",
        "alex"
    ]

    words = question.split()

    keywords = []

    for word in words:

        word = word.strip("?.,!")

        if word not in stop_words:

            keywords.append(word)

    return keywords