---
name: ontology/agent-memory
description: "Agent ontology and memory management. Use when: (1) organizing knowledge structures, (2) managing agent memory, (3) building knowledge graphs, (4) concept mapping. NOT for: simple file storage (use memory files), web scraping, or external data sync."
metadata:
  {
    "openclaw":
      {
        "emoji": "🧠",
        "requires": { "bins": [] },
        "install": []
      }
  }
---

# Agent Ontology and Memory Skill

Manage knowledge structures, ontologies, and agent memory.

## When to Use

✅ **USE this skill when:**

- Organizing domain knowledge into ontologies
- Managing complex agent memory structures
- Building knowledge graphs and relationships
- Concept mapping and categorization
- Structuring domain expertise
- Creating reusable knowledge bases

## When NOT to Use

❌ **DON'T use this skill when:**

- Simple note-taking (use MEMORY.md or memory files)
- File storage operations (use file tools)
- Web scraping (use web tools)
- External database sync (use database tools)

## Core Concepts

### Ontology Structure

```json
{
  "domain": "project-management",
  "entities": [
    {
      "id": "task",
      "properties": ["name", "status", "priority", "assignee"],
      "relationships": ["belongs-to", "depends-on"]
    },
    {
      "id": "project",
      "properties": ["name", "deadline", "budget"],
      "relationships": ["contains"]
    }
  ],
  "relationships": [
    {
      "from": "task",
      "to": "project",
      "type": "belongs-to",
      "cardinality": "many-to-one"
    }
  ]
}
```

### Memory Structure

```json
{
  "short-term": {
    "conversations": [],
    "recent_context": [],
    "working_memory": {}
  },
  "long-term": {
    "facts": [],
    "patterns": [],
    "learnings": []
  },
  "knowledge_graph": {
    "nodes": [],
    "edges": []
  }
}
```

## Usage Patterns

### Creating Ontologies

```python
def create_ontology(domain_name, entities, relationships):
    """Create a new ontology for a domain"""
    ontology = {
        "domain": domain_name,
        "entities": entities,
        "relationships": relationships,
        "created_at": now()
    }
    return ontology

# Example
project_ontology = create_ontology(
    "project-management",
    ["task", "project", "milestone"],
    ["belongs-to", "depends-on", "blocks"]
)
```

### Storing Knowledge

```python
def add_knowledge(memory, fact, confidence=1.0):
    """Add a fact to agent memory"""
    memory["long-term"]["facts"].append({
        "fact": fact,
        "confidence": confidence,
        "timestamp": now()
    })
    return memory
```

### Building Knowledge Graph

```python
def add_relationship(graph, entity1, entity2, relation_type):
    """Add a relationship between entities"""
    graph["edges"].append({
        "from": entity1,
        "to": entity2,
        "type": relation_type,
        "weight": 1.0
    })
    return graph
```

### Querying Knowledge

```python
def query_facts(memory, predicate):
    """Query memory for facts matching a predicate"""
    results = []
    for fact in memory["long-term"]["facts"]:
        if predicate(fact):
            results.append(fact)
    return results
```

## Storage

Store ontologies and memory structures in:

- **Ontologies**: `~/.openclaw/workspace/ontologies/`
- **Memory**: `~/.openclaw/workspace/memory/`
- **Knowledge graphs**: `~/.openclaw/workspace/knowledge/`

## Best Practices

1. **Design for reusability** - Make ontologies general enough for multiple uses
2. **Version control** - Track changes to knowledge structures
3. **Confidence scoring** - Use confidence values for uncertain facts
4. **Regular cleanup** - Remove outdated or low-confidence facts
5. **Link to sources** - Track where knowledge came from

## Example Use Cases

**Domain Knowledge Base**
```python
tech_ontology = create_ontology(
    "technology",
    ["language", "framework", "library"],
    ["implemented-in", "depends-on", "compatible-with"]
)
```

**Project Memory**
```python
project_memory = add_knowledge(
    empty_memory(),
    "Project deadline is 2024-12-31",
    confidence=0.9
)
```

**Knowledge Graph**
```python
tech_graph = add_relationship(
    tech_graph,
    "Python",
    "Django",
    "implemented-in"
)
```

---

*This skill manages agent knowledge structures and memory organization.*
