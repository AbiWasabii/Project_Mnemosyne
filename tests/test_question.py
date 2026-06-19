from services.memory.question_answer import answer_question

prompt = answer_question(
    owner="Mimi",
    question="What tea does Mimi like?"
)

print(prompt)