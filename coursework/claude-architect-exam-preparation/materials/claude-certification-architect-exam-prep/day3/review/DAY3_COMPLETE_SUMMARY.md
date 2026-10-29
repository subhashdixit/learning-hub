# Day 3 Complete Review: Memory & Token Optimization

**Domain Weight:** 15% of exam (9 questions out of 60)

---

## 🧠 MEMORY SYSTEM - Complete Summary

### The 4 Memory Types

| Type | Purpose | Structure | When to Save |
|------|---------|-----------|--------------|
| **USER** | User profile, expertise, preferences | Direct content | "I'm a...", "I prefer...", "I work on..." |
| **FEEDBACK** | Guidance on approach | Content + **Why** + **How to apply** | "Don't...", "Keep doing...", validations |
| **PROJECT** | Current work context | Content + **Why** + **How to apply** | Deadlines, sprints, decisions, constraints |
| **REFERENCE** | External resources | Location + purpose | URLs, dashboards, docs, wikis |

### Memory File Structure

```markdown
---
name: Memory Name
description: One-line description (for relevance matching)
type: user|feedback|project|reference
---

Content here.

For feedback/project types:
**Why:** The reason/motivation
**How to apply:** When and where this applies
```

### What NOT to Save

❌ **Code patterns** - derive from reading files
❌ **Git history** - use `git log`
❌ **Debugging solutions** - already in code
❌ **Architecture details** - read current state
❌ **Ephemeral details** - "what we did yesterday"

### MEMORY.md Index

- Always loaded (first 200 lines)
- Format: `- [Title](file.md) — one-line description`
- Keep entries < 150 characters
- Organize by topic, not chronologically

### Staleness Detection

**Memory is STALE when:**
- Referenced files/functions don't exist
- Deadlines have passed
- Architecture has changed
- Conflicts with current codebase state

**ALWAYS verify before using:**
```
1. Read memory
2. Grep/Read to verify references still exist
3. If not found → memory is stale
4. Trust current state over memory
```

---

## 🎯 TOKEN OPTIMIZATION - Complete Summary

### Token Basics

- **~4 characters = 1 token** (English text)
- **~3.5 characters = 1 token** (code)
- Whitespace counts
- JSON structure adds overhead

### Context Window Limits

- **Input:** Up to 200K tokens (Claude Opus)
- **Output:** ~4K tokens per response
- **Default Read:** 2000 lines = ~40K tokens
- **Default Grep head_limit:** 250 results

### Read Tool Optimization

| Scenario | Parameters | Tokens | Rationale |
|----------|-----------|--------|-----------|
| Small file (<500 lines) | None | ~10K | Read fully |
| Start of large file | `limit=100` | ~2K | Just beginning |
| End of large file | `offset=9900, limit=100` | ~2K | Recent logs |
| Middle section | `offset=2500, limit=100` | ~2K | Specific area |
| Around line N | `offset=N-50, limit=100` | ~2K | Context around target |

**Key parameters:**
- `limit` - how many lines to read
- `offset` - where to start (0-indexed)
- Lines in output start at 1 (cat -n format)

### Grep Tool Optimization

**Output modes:**

| Mode | Returns | Tokens/Result | Best For |
|------|---------|---------------|----------|
| `files_with_matches` | File paths | ~10 | Finding which files |
| `count` | Match counts | ~5 | Counting occurrences |
| `content` | Matching lines | ~30 | Seeing actual matches |

**Key parameters:**
- `output_mode` - what to return
- `head_limit` - max results (default: 250)
- `-A`, `-B`, `-C` - context lines

**Two-step approach:**
```python
# Step 1: Find files (cheap)
Grep(pattern='auth', output_mode='files_with_matches', head_limit=5)
# ~50 tokens

# Step 2: Read specific files (targeted)
Read(file_path='<from_grep>', limit=100)
# ~2K tokens per file

# Total: Much cheaper than content mode!
```

### Agent Tool for Context Isolation

**Use Agent when:**
- Broad exploration ("find all...", "explore...")
- Multiple file searches
- Expected >3 Grep/Read operations
- Large codebase unfamiliar territory

**Why?**
- Agent runs in **separate context**
- Returns only summary to main context
- Main context stays clean (~500 tokens vs 30K+)

### Model Selection

| Model | Cost | Best For | Examples |
|-------|------|----------|----------|
| **Haiku 4.5** | Lowest | Simple tasks, <5K tokens, no reasoning | Find function, fix typo, format code |
| **Sonnet 4.6** | Medium | Moderate tasks, some reasoning | Write tests, review PR, add features |
| **Opus 4.6** | Highest | Complex tasks, heavy reasoning, >20K tokens | Refactor architecture, design API, debug complex issues |

### Optimization Decision Tree

```
Token count < 5K?
  → NO OPTIMIZATION (overhead > benefit)

Token count 5-20K?
  → BASIC LIMITS (use head_limit, limit)

Token count 20-50K?
  → AGENT ISOLATION (use Agent tool)

Token count > 50K?
  → CHUNKING (process in parts)
```

---

## 📊 Exam Question Patterns

### Memory Questions

**Pattern 1: Identify memory type**
```
Q: User says "I prefer integration tests over unit tests"
A: USER memory (preference)

Q: User says "Don't use mocks - we got burned last quarter"
A: FEEDBACK memory (+ Why + How to apply)
```

**Pattern 2: Should you save?**
```
Q: User explains how the auth.py module works
A: NO - code patterns, derive from reading

Q: User says "We're in code freeze until Friday"
A: YES - PROJECT memory
```

**Pattern 3: Staleness detection**
```
Q: Memory says "Use old_function()" but grep finds nothing
A: Memory is STALE - verify before using, trust current state
```

### Token Questions

**Pattern 1: Optimal Read strategy**
```
Q: Read last 100 lines of 10K line log file
A: Read(file_path='...', offset=9900, limit=100)

Q: Read function around line 500
A: Read(file_path='...', offset=450, limit=100)
```

**Pattern 2: Grep optimization**
```
Q: Find which files contain 'authentication'
A: Grep(pattern='auth', output_mode='files_with_matches')

Q: See actual error messages with context
A: Grep(pattern='error', output_mode='content', head_limit=20, C=2)
```

**Pattern 3: When to use Agent**
```
Q: Explore unfamiliar large codebase
A: Use Agent(subagent_type='Explore') - isolates context

Q: Find one specific function
A: Direct Grep - simple enough
```

---

## 🎴 FLASHCARDS

### Memory Flashcards

**Card 1:**
```
Q: What are the 4 memory types?
A: user, feedback, project, reference
```

**Card 2:**
```
Q: Which memory types need "Why" and "How to apply"?
A: feedback and project
```

**Card 3:**
```
Q: What should NOT be saved in memory?
A: Code patterns, git history, debugging solutions, ephemeral details
```

**Card 4:**
```
Q: What is MEMORY.md?
A: Index file, always loaded (first 200 lines), points to individual memory files
```

**Card 5:**
```
Q: How to detect stale memory?
A: Check if referenced files/functions still exist, verify against current state
```

**Card 6:**
```
Q: User says "I'm a senior backend engineer" - memory type?
A: USER (profile/role)
```

**Card 7:**
```
Q: User says "Stop using mocks, they failed us" - memory type?
A: FEEDBACK (+ Why + How to apply)
```

**Card 8:**
```
Q: User says "Sprint ends March 15" - memory type?
A: PROJECT (+ Why + How to apply)
```

**Card 9:**
```
Q: User says "Check Linear project INGEST" - memory type?
A: REFERENCE (external resource)
```

**Card 10:**
```
Q: Before using memory, you must always...?
A: VERIFY it against current codebase state
```

### Token Flashcards

**Card 11:**
```
Q: Default Read tool line limit?
A: 2000 lines (~40K tokens)
```

**Card 12:**
```
Q: Default Grep head_limit?
A: 250 results
```

**Card 13:**
```
Q: Token estimation: ~X characters per token?
A: ~4 for text, ~3.5 for code
```

**Card 14:**
```
Q: Most token-efficient Grep output mode?
A: files_with_matches (~10 tokens per file)
```

**Card 15:**
```
Q: Least token-efficient Grep output mode?
A: content (~30 tokens per line)
```

**Card 16:**
```
Q: Read last 100 lines of log file - parameters?
A: offset=(total_lines - 100), limit=100
```

**Card 17:**
```
Q: When to use Agent tool for exploration?
A: Broad search, >3 operations, large unfamiliar codebase
```

**Card 18:**
```
Q: What does offset parameter do in Read?
A: Specifies which line to start from (0-indexed)
```

**Card 19:**
```
Q: Two-step Grep approach?
A: 1) files_with_matches (find files), 2) Read specific files (targeted)
```

**Card 20:**
```
Q: Optimization threshold - when to optimize?
A: >5K tokens worth optimizing, <5K not worth it
```

**Card 21:**
```
Q: Which model for simple tasks (<5K tokens)?
A: Haiku 4.5
```

**Card 22:**
```
Q: Which model for complex architecture work?
A: Opus 4.6
```

**Card 23:**
```
Q: Agent tool benefit for context?
A: Runs in separate context, returns only summary (~500 tokens vs 30K+)
```

**Card 24:**
```
Q: Grep content mode - always use what parameter?
A: head_limit (to control output size)
```

**Card 25:**
```
Q: Read offset is 0-indexed, but line numbers in output?
A: Start at 1 (cat -n format)
```

---

## 🚨 Common Pitfalls

### Memory Pitfalls

1. ❌ **Saving code patterns**
   - Memory: "The auth module uses JWT tokens"
   - ✅ Should: Read auth.py to see current implementation

2. ❌ **Not verifying before using**
   - Memory: "Use refresh_token()"
   - ✅ Should: Grep for it first, verify it exists

3. ❌ **Missing Why/How to apply**
   - Feedback: "Don't use mocks"
   - ✅ Should: "Don't use mocks. **Why:** Past incident. **How:** Use real DB for integration tests"

4. ❌ **Duplicate memories**
   - Creating new memory instead of updating existing
   - ✅ Should: Check for existing memory first

5. ❌ **Index entries too long**
   - Entry: 200 characters
   - ✅ Should: Keep under 150 characters

### Token Pitfalls

1. ❌ **Reading full large files**
   - `Read(file_path='/10000_line_file.py')`
   - ✅ Should: Use limit parameter

2. ❌ **Grep content without head_limit**
   - `Grep(pattern='error', output_mode='content')`
   - ✅ Should: Add head_limit=20

3. ❌ **Not using two-step approach**
   - Grep content mode immediately
   - ✅ Should: files_with_matches → targeted reads

4. ❌ **Over-optimizing small tasks**
   - Splitting 100-line file into chunks
   - ✅ Should: Just read the whole thing

5. ❌ **Not using Agent for exploration**
   - Multiple Greps in main context
   - ✅ Should: Use Agent for broad searches

---

## 📈 Domain Coverage Summary

### Day 3 Focus: Domain 5 (15% of exam)

**Memory Management (7-8%):**
- Memory types and when to use them ✅
- Memory file structure ✅
- MEMORY.md index management ✅
- Staleness detection ✅
- Verification before using ✅

**Token Optimization (7-8%):**
- Token counting basics ✅
- Read tool optimization ✅
- Grep tool optimization ✅
- Two-step approach ✅
- Agent tool for context isolation ✅
- Model selection ✅

---

## 🎯 Quick Decision Matrix

### Memory Decision Matrix

| User Says | Memory Type | Include Why/How? |
|-----------|-------------|------------------|
| "I'm a..." | USER | No |
| "I prefer..." | USER | No |
| "Don't..." | FEEDBACK | YES |
| "Keep doing..." | FEEDBACK | YES |
| "Sprint ends..." | PROJECT | YES |
| "Deadline is..." | PROJECT | YES |
| "Check URL..." | REFERENCE | No |
| "Bug tracker at..." | REFERENCE | No |
| "The code works like..." | NONE - Don't save | N/A |
| "Yesterday we..." | NONE - Don't save | N/A |

### Token Decision Matrix

| Scenario | Tool Strategy | Parameters |
|----------|---------------|------------|
| Small file (<500 lines) | Read fully | None needed |
| Large file (start) | Read with limit | limit=100 |
| Large file (end) | Read with offset+limit | offset=9900, limit=100 |
| Find which files | Grep files mode | output_mode='files_with_matches' |
| See match content | Grep content + limit | output_mode='content', head_limit=20 |
| Count occurrences | Grep count mode | output_mode='count' |
| Broad exploration | Agent tool | subagent_type='Explore' |
| Simple find | Direct Grep | Basic params |

---

## 💯 Exam Success Checklist

Before taking the exam, ensure you can:

### Memory
- [ ] Name all 4 memory types
- [ ] Explain when to use each type
- [ ] Write proper frontmatter structure
- [ ] Know what NOT to save
- [ ] Explain staleness detection
- [ ] Know to verify before using
- [ ] Understand MEMORY.md purpose

### Tokens
- [ ] Estimate token counts (~4 chars/token)
- [ ] Know default Read limit (2000 lines)
- [ ] Know default Grep head_limit (250)
- [ ] Use offset/limit correctly
- [ ] Choose right Grep output_mode
- [ ] Apply two-step approach
- [ ] Know when to use Agent
- [ ] Select appropriate model

---

## 🎓 Final Tips for Exam

1. **Memory questions:** Look for keywords
   - "I'm/I prefer" → USER
   - "Don't/Stop" → FEEDBACK
   - "Deadline/Sprint" → PROJECT
   - "Check/URL" → REFERENCE

2. **Token questions:** Calculate roughly
   - Don't need exact counts
   - Focus on relative comparison
   - "Which uses fewer tokens?" - compare approaches

3. **Time management:**
   - 2 minutes per question
   - Skip hard ones, come back later
   - Don't overthink simple questions

4. **Common traps:**
   - "Save code patterns" → NO
   - "Use memory without verifying" → NO
   - "Read full large file" → NO
   - "Grep content without head_limit" → NO

---

## 🚀 You're Ready!

You've mastered:
✅ All 4 memory types
✅ Memory lifecycle and verification
✅ Token counting and optimization
✅ Read/Grep parameter usage
✅ Agent tool for context isolation
✅ Model selection strategies

**Now practice with the exam and review weak areas!**

Good luck! 💪🎯
