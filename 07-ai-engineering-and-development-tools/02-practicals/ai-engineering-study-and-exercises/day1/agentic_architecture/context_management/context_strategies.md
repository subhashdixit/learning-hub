# Context Management Strategies

## What is Context?

**Context** = Conversation memory between user and Claude
- Limited to 200k tokens
- Fills up during long conversations
- Need strategies to manage it!

---

## Strategy 1: Compression

**What:** Summarize old messages

**How to do:**
- Command: `/compact` in Claude Code
- In code: Keep recent + system prompt, summarize middle

**Example:**
```
Before: 50 messages (30k tokens)
After: System + Summary + Recent 10 (8k tokens)
Saved: 22k tokens!
```

**When:** Conversation getting long and slow

---

## Strategy 2: Selective Context

**What:** Only include relevant information

**How to do:**
- Send only files related to current task
- Don't send entire codebase

**Example:**
```python
# Task: Fix login bug

# BAD: Send everything
context = all_1000_files  # 50k tokens

# GOOD: Send only relevant
context = ["auth.py", "login.html"]  # 2k tokens
```

**When:** Working on specific feature

---

## Strategy 3: Sub-agents

**What:** Spawn separate agents for research

**How to do:**
- In Claude Code: Automatically spawns Explore agents
- They use their own 200k token budget
- Return summary to main conversation

**Example:**
```
Main Agent (you): "Research authentication"
  ↓ spawns
Sub-agent: Reads 20 files (uses 15k tokens in separate context)
  ↓ returns
Summary: "Auth uses JWT..." (500 tokens in main context)
```

**When:** Need to explore/research without cluttering main chat

---

## Exam Tips

**Common question patterns:**
1. "Context window full, what to do?" → Use sub-agents
2. "Long conversation slowing down?" → Compress
3. "Working on login, have 1000 files?" → Selective context

**Remember:** Sub-agents are your friend for keeping context clean!
