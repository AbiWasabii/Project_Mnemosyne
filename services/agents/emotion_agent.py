from services.memory.memory_store import load_memories
from services.core.llm import ask_model

from services.agents.world_model_agent import build_world_model
from services.agents.relationship_agent import build_relationship


def detect_emotions(owner):
    memories = load_memories(owner)
    world = build_world_model()
    relationship = build_relationship()
    prompt = f"""
World model:

{world}

Relationships:

{relationship}

Memories:

{memories}

These memories describe real people, relationships, places and experiences.

Treat names as people unless otherwise specified.

Focus on feelings, not facts.

Infer the emotions associated with these memories.

Examples:

Relationship with girlfriend:
- love
- affection
- attachment

Enjoying a vehicle:
- pride
- enjoyment

Shared experiences:
- happiness
- companionship

Do NOT repeat facts.

Do NOT describe who owns what.

Do NOT simply summarize the memories.

Answer in 1-3 sentences.

Describe emotions only.
"""
    answer = ask_model(prompt)
    print("MODEL RETURNED:")
    print(answer)
    return answer

