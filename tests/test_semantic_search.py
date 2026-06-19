from services.vector.semantic_search import semantic_search

results = semantic_search(
    owner="Alex",
    question="What vehicle do I own?"
)

print(results)