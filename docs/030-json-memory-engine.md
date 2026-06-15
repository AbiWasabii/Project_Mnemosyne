# JSON Memory Engine

## Purpose

Implement the first persistent memory system.

---

## Philosophy

Simple before powerful.

Reliable before intelligent.

---

## Storage

data/memory/

---

## Files

facts.json

preferences.json

events.json

goals.json

relationships.json

timeline.json

---

## Example

preferences.json

[
{
"id": "",
"owner": "Mimi",
"content": "Likes matcha.",
"importance": 8,
"confidence": 1.0
}
]

---

## Advantages

Human-readable.

Easy backups.

Easy debugging.

No external dependencies.

---

## Limitations

Slow search.

Limited scale.

No semantic retrieval.

---

## Upgrade Path

JSON

↓

SQLite

↓

Vector Database

↓

Knowledge Graph

---

## Principle

Every layer should be replaceable.

Memories are not.
