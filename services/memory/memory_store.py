import json
from pathlib import Path


BASE_PATH = Path("data/memory")


def load_memories(owner: str):

    owner = owner.lower()

    memories = []

    folder = BASE_PATH / owner

    if not folder.exists():
        return memories
 
    for file in folder.glob("*.json"):

        with open(file, "r", encoding="utf-8") as f:

            data = json.load(f)

            if isinstance(data, list):

                for memory in data:

                    exists = False

                    for item in memories:

                        if item["id"] == memory["id"]:

                            exists = True
                            break

                    if not exists:

                        memories.append(memory)

    return memories


def append_memory(owner, filename, memory):

    owner = owner.lower()

    path = BASE_PATH / owner / filename

    if path.exists():

        with open(path, "r", encoding="utf-8") as f:

            memories = json.load(f)

    else:

        memories = []

    exists = False

    for item in memories:

        if item["id"] == memory["id"]:

            exists = True
            break

    if not exists:

        memories.append(memory)

    with open(path, "w", encoding="utf-8") as f:

        json.dump(
            memories,
            f,
            indent=4
        )