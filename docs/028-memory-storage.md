# Memory Storage

## Purpose

Provide durable and explainable storage for memories.

---

## Philosophy

Storage should be simple before becoming powerful.

---

## Evolution

### v0.2

JSON files.

Examples:

* conversations.json
* preferences.json
* goals.json

---

### v0.2.1

SQLite.

Purpose:

* Better querying
* Faster retrieval
* Structured data

---

### v0.3

Photo and document memory.

---

### v0.4

Knowledge graph.

---

## Memory Types

### Facts

Stable information.

Examples:

* Birthdays
* Names
* Preferences

---

### Events

Things that happened.

Examples:

* Trips
* Anniversaries

---

### Goals

Future intentions.

Examples:

* Visit Japan
* Start a business

---

### Relationships

Connections between people.

Examples:

* Partner
* Family
* Friends

---

## Metadata

Each memory should contain:

* id
* owner
* type
* content
* importance
* confidence
* tags
* source
* created_at
* updated_at

---

## States

* Active
* Dormant
* Archived
* Deleted

---

## Principle

History is append-only.

Never overwrite the past.
