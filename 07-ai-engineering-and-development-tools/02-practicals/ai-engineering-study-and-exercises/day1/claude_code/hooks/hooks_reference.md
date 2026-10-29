# Hooks Reference Guide

## What Are Hooks?

**Hooks** = Automatic actions triggered at specific events

**Like:** IFTTT for Claude Code - "When X happens, do Y"

---

## The 3 Hook Types

### 1. PreToolUse (BEFORE)

**Runs:** BEFORE a tool executes

**Use for:**
- Validation before dangerous operations
- Checking prerequisites
- Warnings

**Example:**
```json
"PreToolUse": [
  {
    "matcher": "Bash(git commit *)",
    "hooks": [{
      "type": "command",
      "command": "echo 'About to commit!'"
    }]
  }
]
```

**When triggers:** Before running git commit

---

### 2. PostToolUse (AFTER)

**Runs:** AFTER a tool executes successfully

**Use for:**
- Auto-formatting files
- Running linters
- Notifications
- Cleanup actions

**Example:**
```json
"PostToolUse": [
  {
    "matcher": "Edit(*.py)",
    "hooks": [{
      "type": "command",
      "command": "black ${filePath}"
    }]
  }
]
```

**When triggers:** After editing any Python file

---

### 3. UserPromptSubmit (ON MESSAGE)

**Runs:** When user sends a message

**Use for:**
- Logging
- Analytics
- Custom workflows

**Example:**
```json
"UserPromptSubmit": [
  {
    "hooks": [{
      "type": "command",
      "command": "echo 'Message received'"
    }]
  }
]
```

**When triggers:** Every user message

---

## Matchers (Pattern Matching)

### Tool Matchers:

| Matcher | Matches |
|---------|---------|
| `Edit(*.py)` | Any Python file edit |
| `Edit(app.js)` | Specific file edit |
| `Write(test_*.py)` | Test files creation |
| `Bash(git commit *)` | Git commit commands |
| `Bash(npm *)` | Any npm command |

### Wildcards:

- `*` - Match anything
- `*.py` - Any Python file
- `test_*` - Files starting with "test_"

---

## Variables

**Available in hooks:**

| Variable | Meaning | Example |
|----------|---------|---------|
| `${filePath}` | File being operated on | `/path/to/file.py` |
| `${command}` | Command being run | `git commit -m "..."` |

**Use in commands:**
```json
"command": "echo 'Edited: ${filePath}'"
```

---

## Real-World Examples

### Example 1: Auto-format on Edit

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit(*.py)",
        "hooks": [{
          "type": "command",
          "command": "black ${filePath}"
        }]
      }
    ]
  }
}
```

**What:** Formats Python files after editing

---

### Example 2: Run Tests Before Commit

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git commit *)",
        "hooks": [{
          "type": "command",
          "command": "npm test"
        }]
      }
    ]
  }
}
```

**What:** Runs tests before allowing commit

---

### Example 3: Lint JavaScript on Save

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit(*.js)",
        "hooks": [{
          "type": "command",
          "command": "eslint --fix ${filePath}"
        }]
      }
    ]
  }
}
```

**What:** Auto-fixes linting issues in JavaScript

---

## Exam Tips

### Common Questions:

**Q: "Auto-format files after editing. Which hook?"**
**A:** PostToolUse (after action)

**Q: "Validate before git push. Which hook?"**
**A:** PreToolUse (before action)

**Q: "Log every user interaction. Which hook?"**
**A:** UserPromptSubmit (on message)

---

## Best Practices

1. **Use PreToolUse for validation**
   - Check before destructive operations
   - Prevent mistakes

2. **Use PostToolUse for cleanup**
   - Auto-format code
   - Run linters
   - Update dependencies

3. **Use specific matchers**
   - `Edit(*.py)` better than `Edit(*)`
   - Avoid unnecessary hook triggers

4. **Keep hooks fast**
   - Slow hooks delay operations
   - Use background tasks for long operations

---

## Summary

| Hook Type | When | Use For |
|-----------|------|---------|
| **PreToolUse** | Before action | Validation, warnings |
| **PostToolUse** | After action | Formatting, linting |
| **UserPromptSubmit** | On message | Logging, workflows |

**Remember:** Hooks automate repetitive tasks and enforce consistency!
