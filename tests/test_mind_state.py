from services.core.mind_state import build_mind_state


mind = build_mind_state("Alex")

for key, value in mind.items():

    print()

    print(key.upper())

    print(value)