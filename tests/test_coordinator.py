import time

from services.coordinator.coordinator import ask


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    if not question.strip():
        continue

    start = time.time()

    answer = ask(question)

    elapsed = round(time.time() - start, 2)

    print(
        f"\nMnemosyne ({elapsed}s): {answer}"
    )