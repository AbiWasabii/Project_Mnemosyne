Extract important facts from the conversation.

Possible types:

- preference
- event
- goal
- relationship

Return JSON only.

Example:

Input:

"Mimi likes matcha tea."

Output:

[
{
"id":"auto",
"type":"preference",
"owner":"Mimi",
"content":"Likes matcha tea",
"importance":8
}
]