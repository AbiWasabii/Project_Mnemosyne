def extract_fact(text):

    text = text.strip()

    if "likes" in text.lower():

        return {
            "type": "preference",
            "content": text
        }

    return None