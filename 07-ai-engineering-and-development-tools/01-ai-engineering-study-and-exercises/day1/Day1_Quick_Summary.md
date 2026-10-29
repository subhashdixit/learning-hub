# Day 1 Quick Summary - CCA Exam Prep

**Date Completed:** March 27, 2026
**Topics Covered:** Agentic Architecture + Claude Code (47% of exam)

---

## Morning Session: Agentic Architecture

### 1. Agent Loops

**Key Concepts:**
- **Retry logic:** Try up to max_retries (e.g., 3) with exponential backoff (2, 4, 8 seconds)
- **Circuit breaker:** Stop after threshold failures (e.g., 5 total) across ALL requests
- **Graceful fallback:** Live → Cache → Default (always provide something to user)

**Difference:**
- `max_retries` = Local (per request)
- `circuit_breaker_threshold` = Global (across all requests)

**Files:** 01_basic_loop.py, 02_circuit_breaker.py, 03_graceful_fallback.py

---

### 2. Orchestration Patterns

**Three patterns:**

| Pattern | When | Example |
|---------|------|---------|
| **Sequential** | Steps depend on each other | Fetch → Validate → Process |
| **Parallel** | Independent tasks | Weather + Traffic + Events (3x faster!) |
| **Hierarchical** | Complex task, need specialists | Main agent → Sub-agents |

**Key:** Choose based on task dependencies!

**Files:** 01_sequential.py, 02_parallel.py, 03_hierarchical.py

---

### 3. Tool Boundaries

**Core Rule:** Use the RIGHT tool, not Bash!

| Tool | CAN | CANNOT |
|------|-----|--------|
| **Read** | Read files | Edit/create files |
| **Edit** | Modify existing files | Create new files |
| **Write** | Create new files | Modify existing |
| **Bash** | Run commands | File operations (use dedicated tools!) |
| **Glob** | Find files by name | Search file contents |
| **Grep** | Search file contents | Find files by name |

**Exam tip:** Always use dedicated tools over Bash for file operations!

---

### 4. Context Management

**Problem:** 200k token limit

**Solutions:**
1. **Compression** - `/compact` command, summarize old messages
2. **Selective Context** - Only include relevant files
3. **Sub-agents** - Offload research (uses separate 200k tokens)

**When:** Use sub-agents for exploration to keep main context clean!

---

## Afternoon Session: Claude Code

### 5. Skills

**What:** Custom commands (like Siri shortcuts)

**Structure:**
```
.claude/skills/name/
└── SKILL.md
```

**Frontmatter:**
```yaml
---
name: hello
description: Say hello
---
Instructions for Claude...
```

**Types:**
- **Global:** ~/.claude/skills/ (works everywhere)
- **Local:** project/.claude/skills/ (project-specific)

**Exam tip:** Team-shared skills go in project/.claude (version controlled)

---

### 6. Hooks

**What:** Auto-actions triggered by events

**Three types:**

| Hook Type | When | Use For |
|-----------|------|---------|
| **PreToolUse** | BEFORE action | Validation (e.g., before git push) |
| **PostToolUse** | AFTER action | Formatting, linting (e.g., after edit) |
| **UserPromptSubmit** | ON message | Logging, workflows |

**Configuration:** In `.claude/settings.json`

**Example:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit(*.py)",
      "hooks": [{"type": "command", "command": "black ${filePath}"}]
    }]
  }
}
```

**Exam tip:** PostToolUse for auto-format, PreToolUse for validation!

---

### 7. Permission Modes

**Six modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| **default** | Ask everything | Learning, sensitive work |
| **acceptEdits** | Auto edits, ask commands | Daily coding (BEST BALANCE) |
| **plan** | Read-only | Exploring code |
| **auto** | Smart decisions | Long tasks (Teams+) |
| **dontAsk** | Pre-approved only | CI/CD |
| **bypassPermissions** | No checks | NEVER in production! |

**Switch:** Press `Shift+Tab` to cycle through modes

**Exam tip:** acceptEdits = best balance for development work

---

### 8. Subagents

**What:** Helper agents spawned for specific tasks

**Types:**
- **Explore:** Research codebase
- **Plan:** Design implementation
- **General-purpose:** Complex tasks

**Key benefit:** Uses separate 200k token budget, keeps YOUR context clean!

**How to trigger:** "Research X", "Explore Y", "Find all Z"

**Exam tip:** Sub-agents for exploration = clean main context (important!)

---

### 9. Memory System

**What:** Persistent memory across sessions

**Four types:**

| Type | What to Store | Example |
|------|---------------|---------|
| **user** | About you | Role, preferences, expertise |
| **feedback** | How to work | "Always run tests first" |
| **project** | Current work | Goals, deadlines, ongoing tasks |
| **reference** | External info | "Bugs in Linear project AUTH" |

**Location:** `~/.claude/projects/YOUR_PROJECT/memory/`

**How:** Automatic! Just tell Claude important things

**Exam tip:** Memory is automatic, types are important to know

---

## Key Exam Takeaways

### Most Important Concepts:

1. **Circuit breaker vs max_retries:** Global vs per-request limits
2. **Orchestration choice:** Sequential (dependent), Parallel (independent), Hierarchical (complex)
3. **Tool boundaries:** Use dedicated tools, NOT Bash for files
4. **Sub-agents:** Keep main context clean for exploration
5. **Hooks:** PreToolUse (before), PostToolUse (after)

### Common Exam Patterns:

**"Agent keeps retrying forever..."**
→ Need circuit breaker + retry limit

**"Fetch from 3 APIs..."**
→ Parallel orchestration

**"Auto-format after editing..."**
→ PostToolUse hook

**"Search 1000 files, context full..."**
→ Spawn sub-agent

**"Edit one line in file..."**
→ Use Edit tool, NOT Bash

---

## Practice Questions Answered Correctly:

- Agent loops: 4/5 (80%)
- Orchestration: 3/3 (100%)
- Total: 7/8 (87.5%)

**Strong areas:** Orchestration patterns, graceful fallback
**Review:** Difference between local and global counters

---

## Files Created Today:

**Python examples:** 6 files
**Reference docs:** 5 files
**Configuration:** 2 files (.claude/settings.json, skills)
**Total:** 13 learning resources

---

## Time Spent: ~4 hours

**Tokens used:** 127k / 200k (plenty left!)

**Next:** Day 2 - Prompt Engineering + Tools/MCP (38% of exam)

---

## Quick Self-Test:

1. What's the difference between circuit breaker and max_retries?
2. When do you use parallel vs sequential orchestration?
3. Which hook type for auto-formatting files?
4. Why use sub-agents for research?
5. Which tool to edit existing files?

**Answers:**
1. Circuit breaker = global (all requests), max_retries = per request
2. Parallel = independent tasks, Sequential = dependent steps
3. PostToolUse (runs after edit)
4. Keeps main context clean, uses separate 200k tokens
5. Edit tool (NOT Bash!)

---

**Ready for Day 2? Review this summary tomorrow before starting!** 🚀
