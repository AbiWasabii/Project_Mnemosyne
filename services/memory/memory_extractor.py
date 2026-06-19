def extract_memories(chat_text):

    if "matcha" in chat_text.lower():

        return [
            {
                "id":"auto",
                "type":"preference",
                "owner":"Mimi",
                "content":"Likes matcha tea",
                "importance":8
            }
        ]

    return []