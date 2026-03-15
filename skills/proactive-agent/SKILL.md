---
name: proactive-agent
description: "Proactive agent capabilities for autonomous tasks. Use when: (1) scheduling periodic checks, (2) monitoring changes, (3) triggering actions based on conditions, (4) background task management. NOT for: user-initiated tasks, real-time responses, or immediate execution."
metadata:
  {
    "openclaw":
      {
        "emoji": "⚡",
        "requires": { "bins": [] },
        "install": []
      }
  }
---

# Proactive Agent Skill

Enable autonomous and proactive agent behavior.

## When to Use

✅ **USE this skill when:**

- Scheduling periodic tasks and checks
- Monitoring files, resources, or web endpoints
- Triggering actions based on conditions
- Background task management
- Automated notifications
- Cron job scheduling
- Long-running processes

## When NOT to Use

❌ **DON'T use this skill when:**

- User-initiated immediate tasks
- Real-time interactive responses
- One-time quick operations
- Manual file operations

## Core Capabilities

### Periodic Tasks

```python
# Example: Periodic check using cron
import cron

def setup_periodic_check():
    """Setup a periodic health check"""
    cron.add(
        name="daily-health-check",
        schedule={
            "kind": "cron",
            "expr": "0 9 * * *"  # 9 AM daily
        },
        payload={
            "kind": "systemEvent",
            "text": "Run daily health check"
        }
    )
```

### Monitoring

```python
def monitor_file(filepath, callback):
    """Monitor a file for changes"""
    import time
    import os
    
    last_modified = 0
    
    while True:
        current_modified = os.path.getmtime(filepath)
        if current_modified != last_modified:
            callback(filepath)
            last_modified = current_modified
        time.sleep(60)  # Check every minute
```

### Conditional Trigers

```python
def check_conditions_and_act():
    """Check conditions and trigger actions"""
    # Check conditions
    if needs_attention():
        # Trigger action
        message.send(
            channel="slack",
            target="#alerts",
            message="Attention needed!"
        )
```

### Background Tasks

```python
def run_background_task(task_function, interval):
    """Run a task in the background"""
    import threading
    import time
    
    def task_runner():
        while True:
            task_function()
            time.sleep(interval)
    
    thread = threading.Thread(target=task_runner, daemon=True)
    thread.start()
    return thread
```

## OpenClaw Integration

### Cron Jobs

```bash
# Schedule a cron job
openclaw cron add --job '{
  "name": "daily-check",
  "schedule": {
    "kind": "cron",
    "expr": "0 9 * * *"
  },
  "payload": {
    "kind": "systemEvent",
    "text": "Morning check"
  }
}'

# List cron jobs
openclaw cron list

# Run a job immediately
openclaw cron run daily-check
```

### Wake Events

```bash
# Send wake event
openclaw cron wake --text "Check email now" --mode now
```

### Heartbeats

Configure in `HEARTBEAT.md`:

```markdown
# HEARTBEAT.md

## Daily Tasks

- Check emails
- Review calendar
- Monitor systems
- Send alerts if needed
```

## Common Patterns

### Email Monitoring

```python
def check_urgent_emails():
    """Check for urgent emails periodically"""
    emails = email_client.get_unread()
    urgent = [e for e in emails if is_urgent(e)]
    
    if urgent:
        message.send(
            channel="slack",
            message=f"Found {len(urgent)} urgent emails"
        )
```

### System Health

```python
def monitor_system_health():
    """Monitor system health"""
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    
    if cpu > 90 or memory > 90:
        message.send(
            channel="alerts",
            message=f"High CPU: {cpu}%, Memory: {memory}%"
        )
```

### File Watcher

```python
def watch_config_file():
    """Watch configuration file for changes"""
    monitor_file(
        "config.yaml",
        lambda f: reload_configuration(f)
    )
```

## Best Practices

1. **Be efficient** - Don't poll too frequently
2. **Rate limit notifications** - Don't spam alerts
3. **Error handling** - Handle failures gracefully
4. **Logging** - Log all proactive actions
5. **Testing** - Test cron expressions and logic

## Storage

Store proactive configurations in:

- `HEARTBEAT.md` - Heartbeat tasks
- `memory/proactive-state.json` - State tracking
- Cron jobs (managed by OpenClaw)

---

*This skill enables autonomous and proactive agent behavior.*
