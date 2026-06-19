from services.coordinator.owner_detector import detect_owner
from services.memory.question_answer import answer_question
from services.core.session import session


def ask(question):

    owner = detect_owner(question)

    if owner == "Shared":

        if session["current_owner"] is not None:

            owner = session["current_owner"]

    answer = answer_question(
        owner=owner,
        question=question
    )

    session["current_owner"] = owner
    session["last_question"] = question
    session["last_answer"] = answer

    return answer