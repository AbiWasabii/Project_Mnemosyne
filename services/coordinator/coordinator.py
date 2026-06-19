from services.coordinator.owner_detector import detect_owner
from services.memory.question_answer import answer_question
from services.core.session import session



def ask(question: str) -> str:

    owner = detect_owner(question)

    if owner == "Shared":

        if session["current_owner"] is not None:

            owner = session["current_owner"]

    answer = answer_question(
        owner=owner,
        question=question
    )

    return answer