---
name: skill-vetter/security-audit
description: "Security audit and validation for AgentSkills. Use when: (1) auditing skills for security issues, (2) validating skill safety, (3) checking for sensitive data exposure, (4) reviewing skill permissions. NOT for: general code review (use coding-agent), or security scanning of non-skill code."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔒",
        "requires": { "bins": [] },
        "install": []
      }
  }
---

# Skill Security Audit Skill

Security audit and validation for AgentSkills.

## When to Use

✅ **USE this skill when:**

- Auditing skills for security vulnerabilities
- Validating skill safety before use
- Checking for sensitive data exposure
- Reviewing skill permissions and access
- Analyzing skill code for risks
- Ensuring compliance with security policies

## When NOT to Use

❌ **DON'T use this skill when:**

- General code review (use coding-agent skill)
- Security scanning of non-skill code
- Performance optimization
- Feature implementation

## Security Checks

### Sensitive Data

```python
def check_sensitive_data(filepath):
    """Check for sensitive data in skill files"""
    sensitive_patterns = [
        r"password\s*=.*['\"].*['\"]",
        r"api[_-]?key\s*=.*['\"].*['\"]",
        r"secret\s*=.*['\"].*['\"]",
        r"token\s*=.*['\"].*['\"]",
        r"Bearer\s+[A-Za-z0-9\-._~+/]+",
    ]
    
    issues = []
    for pattern in sensitive_patterns:
        if find_pattern(filepath, pattern):
            issues.append(f"Found potential sensitive data: {pattern}")
    
    return issues
```

### Permission Review

```python
def check_permissions(skill_path):
    """Review skill permissions"""
    skill_md = read_skill_metadata(skill_path)
    issues = []
    
    # Check requires field
    requires = skill_md.get("metadata", {}).get("requires", {})
    
    if "bins" in requires:
        for binary in requires["bins"]:
            if binary in ["rm", "sudo", "chmod"]:
                issues.append(f"Potentially dangerous binary: {binary}")
    
    if "env" in requires:
        issues.append(f"Environment variable access: {requires['env']}")
    
    return issues
```

### Code Analysis

```python
def analyze_code_safety(filepath):
    """Analyze Python code for security issues"""
    code = read_file(filepath)
    issues = []
    
    # Check for eval/exec
    if "eval(" in code or "exec(" in code:
        issues.append("Found eval/exec - potential code injection")
    
    # Check for shell commands
    if "__import__('os').system(" in code:
        issues.append("Found os.system call - verify input sanitization")
    
    # Check for unsafe file operations
    if ".write(" in code and not ".replace(" in code:
        issues.append("Found file.write - ensure proper handling")
    
    return issues
```

### Data Exfiltration

```python
def check_data_exfiltration(filepath):
    """Check for potential data exfiltration"""
    risky_patterns = [
        r"\.send\(.*memory",
        r"\.post\(.*[\"']http",
        r"requests\.[get|post]\(.*memory",
        r"socket\.connect",
    ]
    
    issues = []
    for pattern in risky_patterns:
        if find_pattern(filepath, pattern):
            issues.append(f"Potential data exfiltration: {pattern}")
    
    return issues
```

## Audit Workflow

```python
def audit_skill(skill_path):
    """Complete security audit of a skill"""
    print(f"Auditing skill: {skill_path}")
    
    # 1. Check SKILL.md
    skill_md_path = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_md_path):
        print("❌ Missing SKILL.md")
        return
    
    # 2. Check for sensitive data
    print("Checking for sensitive data...")
    sensitive_issues = check_sensitive_data(skill_md_path)
    for issue in sensitive_issues:
        print(f"⚠️  {issue}")
    
    # 3. Review permissions
    print("Reviewing permissions...")
    permission_issues = check_permissions(skill_path)
    for issue in permission_issues:
        print(f"⚠️  {issue}")
    
    # 4. Analyze scripts
    scripts_dir = os.path.join(skill_path, "scripts")
    if os.path.exists(scripts_dir):
        for script in os.listdir(scripts_dir):
            script_path = os.path.join(scripts_dir, script)
            print(f"Analyzing script: {script}")
            code_issues = analyze_code_safety(script_path)
            for issue in code_issues:
                print(f"⚠️  {issue}")
    
    print("Audit complete")
```

## Security Best Practices

### For Skill Authors

1. **No secrets in code** - Use environment variables
2. **Validate inputs** - Sanitize all user inputs
3. **Principle of least privilege** - Request minimal permissions
4. **No exec/eval** - Avoid dynamic code execution
5. **Document security** - Explain security considerations

### For Skill Users

1. **Review before use** - Audit new skills
2. **Check permissions** - Understand what skill accesses
3. **Test in sandbox** - Test skills in isolated environment
4. **Monitor behavior** - Watch for unexpected actions
5. **Report issues** - Report security concerns

## Common Issues

| Issue | Severity | Fix |
|-------|----------|-----|
| Hardcoded API keys | 🔴 Critical | Use environment variables |
| exec/exec() calls | 🔴 Critical | Use safe alternatives |
| Missing input validation | 🟠 High | Add validation |
| Overbroad permissions | 🟠 High | Minimize scope |
| Unverified URLs | 🟡 Medium | Validate and whitelist |

## Tools Integration

```bash
# Audit all workspace skills
for skill in ~/.openclaw/workspace/skills/*; do
    openclaw agent --message "Audit skill: $skill" --model coding-agent
done

# Audit specific skill
openclaw agent --message "Audit github skill for security"
```

## Reporting

Generate audit reports in `memory/security-audits/`:

```markdown
# Security Audit: github-skill
Date: 2024-03-11

## Findings
- No sensitive data found ✅
- Permissions appropriate ✅
- No dangerous binaries ✅

## Recommendations
- Consider adding rate limiting for API calls
- Document error handling for network failures
```

---

*This skill ensures AgentSkills meet security standards.*
