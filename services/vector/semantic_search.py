import math

from services.vector.embedder import embed
from services.vector.vector_store import build_vector_store


def cosine_similarity(v1: list, v2: list) -> float:

    dot_product = sum(a * b for a, b in zip(v1, v2))

    magnitude1 = math.sqrt(
        sum(a * a for a in v1)
    )

    magnitude2 = math.sqrt(
        sum(b * b for b in v2)
    )

    return dot_product / (
        magnitude1 * magnitude2
    )


def semantic_search(
    owner: str,
    question: str
) -> list:

    query_embedding = embed(question)

    vectors = build_vector_store(owner)

    results = []

    for vector in vectors:

        similarity = cosine_similarity(
            query_embedding,
            vector["embedding"]
        )

        results.append(
            {
                "content": vector["content"],
                "score": similarity
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:3]