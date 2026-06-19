from services.memory.question_answer import answer_question


def memory_agent(owner, question):

    return answer_question(
        owner=owner,
        question=question
    )