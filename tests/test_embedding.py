from services.vector.embedder import embed


vector = embed(
    "Alex drives a Proton S70"
)

print(len(vector))