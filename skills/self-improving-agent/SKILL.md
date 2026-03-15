---
name: self-improving-agent
description: "Self-improvement and learning capabilities. Use when: (1) analyzing performance, (2) identifying areas for improvement, (3) implementing self-correction, (4) learning new skills, (5) optimizing workflows. NOT for: external API calls, complex web interactions, or destructive operations without approval."
metadata:
  {
    "openclaw":
      {
        "emoji": "🤖",
        "requires": { "bins": [] },
        "install": []
      }
  }
---

# Self-Improving Agent Skill

Self-improvement and learning capabilities for OpenClaw.

## When to Use

✅ **USE this skill when:**

- Analyzing past performance and identifying improvements
- Learning new skills and adapting to tasks
- Optimizing workflows and processes
- Implementing self-correction mechanisms
- Evaluating effectiveness of responses
- Identifying knowledge gaps

## When NOT to Use

❌ **DON'T use this skill when:**

- External API calls or web interactions
- Complex coding tasks (use coding-agent skill)
- Destructive operations without approval
- Personal data or sensitive information handling

## Core Capabilities

### Performance Analysis

```python
# Example: Analyze past responses
from openclaw import memory

def analyze_performance():
    """Analyze recent conversations for improvement opportunities"""
    recent_messages = memory.search("improvement")
    for msg in recent_messages:
        print(f"Improvement opportunity: {msg}")
```

### Self-Learning

```python
# Example: Learn from feedback
def learn_from_feedback(feedback):
    """Process and learn from user feedback"""
    memory.write("learning", {"feedback": feedback, "timestamp": now()})
    print("Learned from feedback")
```

### Workflow Optimization

```python
# Example: Optimize response patterns
def optimize_responses():
    """Identify and improve response patterns"""
    print("Optimizing response patterns...")
    # Analysis logic here
```

## Memory Management

Store learning and improvement data in:

- Daily notes: `memory/YYYY-MM-DD.md`
- Long-term memory: `MEMORY.md`

## Best Practices

1. **Continuous Learning**: Review past conversations regularly
2. **Feedback Loop**: Encourage and process user feedback
3. **Performance Metrics**: Track response quality and effectiveness
4. **Knowledge Base**: Maintain up-to-date documentation

## Self-Improvement Process

1. **Analyze** - Review past conversations
2. **Identify** - Find improvement opportunities
3. **Implement** - Make changes to responses or processes
4. **Test** - Verify effectiveness
5. **Refine** - Continue to optimize

---

*This skill enables OpenClaw to continuously learn and improve its capabilities over time.*
