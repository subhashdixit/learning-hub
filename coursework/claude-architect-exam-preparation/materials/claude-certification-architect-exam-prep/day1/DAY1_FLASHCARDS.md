# 📇 Day 1 Flashcards - Quick Review

Use these flashcards to memorize key concepts for the exam!

---

## 🤖 AGENT LOOPS & RETRY LOGIC

### Q: What is exponential backoff?
**A:** Increasing wait time between retries exponentially
- Attempt 1: 1s, Attempt 2: 2s, Attempt 3: 4s, Attempt 4: 8s
- Formula: delay = initial_delay × (2^attempt)

### Q: What are the 3 Circuit Breaker states?
**A:**
1. CLOSED (Normal) - Requests flow, tracking failures
2. OPEN (Failing) - All requests fail immediately
3. HALF-OPEN (Testing) - Try ONE request to test recovery

### Q: What is Graceful Fallback?
**A:** Provide alternative when primary fails
- Try 1: Live API → Try 2: Cache → Try 3: Default value

---

## 🎭 ORCHESTRATION PATTERNS

### Q: What are the 3 orchestration patterns?
**A:**
1. Sequential - Tasks in order (A → B → C)
2. Parallel - Tasks at once (A ‖ B ‖ C)  
3. Hierarchical - Boss delegates to workers

### Q: Orchestration Comparison?
**A:**
| Pattern | Speed | Use Case |
|---------|-------|----------|
| Sequential | ⚡ Slow | Tasks depend on each other |
| Parallel | ⚡⚡⚡ Fast | Independent tasks |
| Hierarchical | ⚡⚡ Variable | Complex workflows |

---

## 🔧 TOOL BOUNDARIES

### Q: Right Tool for the Job principle?
**A:**
| Task | Use This | NOT This |
|------|----------|----------|
| Read file | Read | cat |
| Edit file | Edit | sed |
| Find files | Glob | find |
| Search content | Grep | grep |
| Run tests | Bash | ✓ |

---

## 🧠 CONTEXT MANAGEMENT

### Q: What are the 3 context management strategies?
**A:**
1. Context Compression - Summarize conversation history
2. Selective Context - Load only relevant files
3. Sub-Agents - Separate agent with own 200K tokens

### Q: Why use Sub-Agents?
**A:**
- Fresh 200K token budget (separate from main!)
- Doesn't clutter main conversation
- Specialized for research tasks

---

## ⚙️ SKILLS

### Q: What are Claude Code Skills?
**A:** Custom commands you create
- Located: .claude/skills/skill-name/SKILL.md
- Use: /skill-name

### Q: SKILL.md format?
**A:**
```markdown
---
name: skill-name
description: What it does
---
Instructions for Claude
```

---

## 🪝 HOOKS

### Q: What are the 3 hook types?
**A:**
1. PreToolUse - Before Claude uses tool
2. PostToolUse - After Claude uses tool
3. UserPromptSubmit - When you send message

### Q: Where to configure hooks?
**A:**
- Global: ~/.claude/settings.json
- Project: .claude/settings.local.json

---

## 🔐 PERMISSION MODES

### Q: What are the 3 permission modes?
**A:**
1. Default - Ask everything
2. AcceptEdits - Auto-approve file edits
3. Plan - Read-only (no modifications)

### Q: Permission Modes Comparison?
**A:**
| Mode | File Reads | File Edits | Bash |
|------|------------|------------|------|
| Default | Ask | Ask | Ask |
| AcceptEdits | Auto ✓ | Auto ✓ | Ask |
| Plan | Auto ✓ | Block ✗ | Block ✗ |

### Q: How to switch modes?
**A:** Shift + Tab → Select mode

---

## 🤖 SUBAGENTS

### Q: What are Subagents?
**A:** Separate Claude instances for specific tasks
- Each gets own 200K token budget!

### Q: When spawned?
**A:** Automatically for research tasks, complex searches

---

## 💾 MEMORY SYSTEM

### Q: What are the 4 memory types?
**A:**
1. User - About you (role, preferences)
2. Feedback - How to work (corrections/confirmations)
3. Project - Ongoing work (deadlines, decisions)
4. Reference - External info (where things are)

### Q: Memory file structure?
**A:**
```markdown
---
name: memory_name
description: One-line description
type: user|feedback|project|reference
---
Content with **Why:** and **How to apply:**
```

---

## 🎯 EXAM SCENARIOS

### Q: Network error calling API?
**A:** Retry with exponential backoff

### Q: Service failing 5+ times?
**A:** Circuit Breaker

### Q: API down, need to show something?
**A:** Graceful Fallback (cache → default)

### Q: Tasks where each needs previous result?
**A:** Sequential Orchestration (A → B → C)

### Q: Fetch from 3 independent APIs?
**A:** Parallel Orchestration (A ‖ B ‖ C)

### Q: Complex workflow with specialists?
**A:** Hierarchical Orchestration (Boss → Workers)

### Q: Read a file - Tool or Bash?
**A:** Read tool (NOT cat)

### Q: Long conversation approaching limit?
**A:** Context Compression

### Q: Large codebase, specific feature?
**A:** Selective Context

### Q: Research task?
**A:** Sub-Agent (Explore)

### Q: Planning phase, no modifications?
**A:** Plan Mode

### Q: User corrects you?
**A:** Save as Feedback Memory

### Q: User is senior engineer?
**A:** Save as User Memory

### Q: Project deadline?
**A:** Save as Project Memory

### Q: External system reference?
**A:** Save as Reference Memory

---

## 🔑 MEMORIZATION AIDS

### Q: Agent Loop patterns?
**A:**
- **R**etry - Try again
- **C**ircuit - Stop trying
- **F**allback - Alternative

### Q: Orchestration patterns?
**A:**
- **S**equential - One after another
- **P**arallel - All at once
- **H**ierarchical - Boss and workers

### Q: Hook types?
**A:**
- **Pre** - Before
- **Post** - After
- **User** - Message sent

### Q: Permission modes?
**A:**
- **D**efault - Do nothing (ask all)
- **A**cceptEdits - Allow edits
- **P**lan - Prevent changes

### Q: Memory types?
**A:**
- **U**ser - About you
- **F**eedback - From you
- **P**roject - Current work
- **R**eference - External links

---

**🎉 Master these for Day 1 success!**
