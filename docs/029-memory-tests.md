# Memory Tests

## Purpose

Ensure memory behaves correctly.

---

## Test Categories

### Insertion

Can new memories be stored?

---

### Retrieval

Can relevant memories be found?

---

### Ranking

Do important memories rank higher?

---

### Conflict Resolution

Can contradictions be handled?

---

### Decay

Do low-value memories weaken over time?

---

### Consolidation

Can patterns emerge from repeated observations?

---

### Summarization

Can many memories be compressed into meaningful summaries?

---

## Example Tests

### Preference Update

Input:

2026

"Alex likes coffee."

2028

"Alex prefers tea."

Expected:

Current preference:

Tea

Historical memory:

Coffee

---

### Reinforcement

Mention:

"Mimi likes matcha."

10 times.

Expected:

Importance score increases.

---

### Contradiction

Input:

"Mimi dislikes spicy food."

Later:

"Mimi enjoys spicy ramen."

Expected:

Detect conflict.

Do not delete history.

---

### Search

Query:

"What drinks does Mimi enjoy?"

Expected:

Matcha-related memories appear.

---

## Principle

Memory bugs are more dangerous than response bugs.

Incorrect memories damage trust.
