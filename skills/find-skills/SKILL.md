---
name: find-skills
description: "Find and locate AgentSkills in the workspace. Use when: (1) searching for skills by name/keyword, (2) discovering available skills, (3) checking skill existence, (4) listing all skills. NOT for: creating/editing skills (use skill-creator), executing skill-specific tasks."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔎",
        "requires": { "bins": [] },
        "install": []
      }
  }
---

# Find Skills Skill

Locate and discover AgentSkills in the workspace.

## When to Use

✅ **USE this skill when:**

- Searching for skills by name or keyword
- Discovering available skills
- Checking if a specific skill exists
- Listing all installed skills
- Finding skills with certain capabilities

## When NOT to Use

❌ **DON'T use this skill when:**

- Creating new skills (use skill-creator skill)
- Editing existing skills (use skill-creator skill)
- Executing skill-specific tasks (use the skill directly)

## Search Locations

Skills can be found in:

1. **Workspace skills**: `~/.openclaw/workspace/skills/`
2. **Global skills**: `~/.npm/node_modules/openclaw/skills/`

## Commands

### List All Skills

```bash
# Workspace skills
ls ~/.openclaw/workspace/skills/

# Global skills
ls ~/.npm/node_modules/openclaw/skills/
```

### Search by Name

```bash
# Find skill by name
find ~/.openclaw/workspace/skills/ -name "*skill-name*"
find ~/.npm/node_modules/openclaw/skills/ -name "*skill-name*"
```

### Search by Keyword

```bash
# Search in SKILL.md descriptions
grep -r "keyword" ~/.openclaw/workspace/skills/
grep -r "keyword" ~/.npm/node_modules/openclaw/skills/
```

### Check Skill Existence

```bash
# Check if skill exists
[ -d ~/.openclaw/workspace/skills/skill-name ] && echo "Exists" || echo "Not found"
```

## Skill Metadata

Each skill has a `SKILL.md` file with frontmatter:

```yaml
---
name: skill-name
description: Skill description text
metadata:
  {
    "openclaw":
      {
        "emoji": "🔎",
        "requires": {},
        "install": []
      }
  }
---
```

## Best Practices

1. **Search both locations** - Workspace skills override global skills
2. **Check frontmatter** - Read name/description to understand capabilities
3. **Verify structure** - Ensure skill has valid SKILL.md
4. **Check dependencies** - Review `requires` and `install` metadata

## Example Usage

**"Find all skills related to GitHub"**
```bash
grep -r -i "github" ~/.openclaw/workspace/skills/
grep -r -i "github" ~/.npm/node_modules/openclaw/skills/
```

**"Check if weather skill exists"**
```bash
ls ~/.openclaw/workspace/skills/ | grep weather
```

---

*This skill helps discover and locate AgentSkills in the workspace.*
