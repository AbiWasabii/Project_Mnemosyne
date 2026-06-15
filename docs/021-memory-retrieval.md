# Memory Retrieval

## Purpose

Retrieve the most relevant memories.

Not the most recent memories.

---

## Retrieval Factors

### Similarity

Semantic closeness to the query.

Weight:

40%

---

### Importance

How valuable the memory is.

Weight:

30%

---

### Recency

How recently the memory was accessed.

Weight:

15%

---

### Frequency

How often the memory has been used.

Weight:

15%

---

## Retrieval Process

User question

↓

Embedding search

↓

Top candidate memories

↓

Score calculation

↓

Reranking

↓

Final memories

↓

Context for model

---

## Memory Count

Default:

Top 5 memories.

Maximum:

Top 10 memories.

---

## Pinned Memories

Pinned memories are always considered first.

Examples:

* Family
* Partners
* Life goals
* Core beliefs

---

## Principle

Relevance beats recency.

Importance beats quantity.
