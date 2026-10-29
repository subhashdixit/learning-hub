# Day 3 Flashcards - Memory & Token Optimization

Print these, cut them out, and quiz yourself!

---

## 🧠 MEMORY SYSTEM FLASHCARDS (Cards 1-15)

### Card 1
**FRONT:** What are the 4 memory types in Claude Code?

**BACK:**
1. USER - profile, preferences
2. FEEDBACK - guidance (+ Why + How)
3. PROJECT - current work (+ Why + How)
4. REFERENCE - external resources

---

### Card 2
**FRONT:** Which memory types require "Why" and "How to apply" sections?

**BACK:** FEEDBACK and PROJECT

---

### Card 3
**FRONT:** User says: "I'm a senior backend engineer with 10 years Python experience"
What memory type?

**BACK:** USER (role and expertise)

---

### Card 4
**FRONT:** User says: "Don't use mocks for database tests - we got burned last quarter"
What memory type?

**BACK:** FEEDBACK (guidance with reason - needs Why + How to apply)

---

### Card 5
**FRONT:** User says: "We're in code freeze until March 15 for the release"
What memory type?

**BACK:** PROJECT (current constraint with deadline - needs Why + How to apply)

---

### Card 6
**FRONT:** User says: "Check the Linear project 'INGEST' for pipeline bugs"
What memory type?

**BACK:** REFERENCE (external resource location)

---

### Card 7
**FRONT:** User explains: "The auth.py file uses JWT tokens in the validate() function"
Should you save this as memory?

**BACK:** NO - code patterns should be derived by reading files, not saved in memory

---

### Card 8
**FRONT:** What is MEMORY.md?

**BACK:** Index file that's always loaded (first 200 lines), contains pointers to individual memory files in format: `- [Title](file.md) — description`

---

### Card 9
**FRONT:** How long should MEMORY.md index entries be?

**BACK:** Under 150 characters

---

### Card 10
**FRONT:** What should you NEVER save in memory? (Name 4 things)

**BACK:**
1. Code patterns (read files instead)
2. Git history (use git log)
3. Debugging solutions (in code already)
4. Ephemeral details (yesterday's work)

---

### Card 11
**FRONT:** Memory says "Use the refresh_token() function in auth.py"
What should you do BEFORE using it?

**BACK:** VERIFY by Grep/Read - check if refresh_token still exists in auth.py. Trust current state over memory.

---

### Card 12
**FRONT:** When is a memory considered STALE? (Name 3 indicators)

**BACK:**
1. Referenced files/functions don't exist
2. Deadlines have passed
3. Conflicts with current codebase state

---

### Card 13
**FRONT:** What's the correct memory file structure?

**BACK:**
```
---
name: Memory Name
description: One-line description
type: user|feedback|project|reference
---

Content here
(+ Why & How to apply for feedback/project)
```

---

### Card 14
**FRONT:** User says: "I prefer FastAPI over Flask for this project"
USER or FEEDBACK memory?

**BACK:** USER (personal preference, not guidance about what to do/avoid)

---

### Card 15
**FRONT:** User says: "Perfect! The integration test approach worked great, keep doing that"
What memory type?

**BACK:** FEEDBACK (validation of approach - guidance to continue - needs Why + How to apply)

---

## 🎯 TOKEN OPTIMIZATION FLASHCARDS (Cards 16-40)

### Card 16
**FRONT:** What's the default Read tool line limit?

**BACK:** 2000 lines (~40,000 tokens)

---

### Card 17
**FRONT:** What's the default Grep head_limit?

**BACK:** 250 results

---

### Card 18
**FRONT:** Token estimation: approximately how many characters per token?

**BACK:** ~4 characters for text, ~3.5 characters for code

---

### Card 19
**FRONT:** What are the 3 Grep output modes?

**BACK:**
1. files_with_matches (~10 tokens/file)
2. count (~5 tokens/file)
3. content (~30 tokens/line)

---

### Card 20
**FRONT:** Which Grep output mode is most token-efficient?

**BACK:** files_with_matches (just file paths, ~10 tokens each)

---

### Card 21
**FRONT:** Which Grep output mode is least token-efficient?

**BACK:** content (full matching lines, ~30 tokens per line)

---

### Card 22
**FRONT:** You need to read the LAST 100 lines of a 10,000 line log file.
What Read parameters?

**BACK:**
```python
Read(file_path='...', offset=9900, limit=100)
```

---

### Card 23
**FRONT:** You need to read lines 500-600 of a file.
What Read parameters?

**BACK:**
```python
Read(file_path='...', offset=500, limit=100)
```
(offset is 0-indexed, so line 501 in output)

---

### Card 24
**FRONT:** What does the Read tool's `offset` parameter do?

**BACK:** Specifies which line to START reading from (0-indexed)

---

### Card 25
**FRONT:** What does the Read tool's `limit` parameter do?

**BACK:** Specifies how many lines to read

---

### Card 26
**FRONT:** Read offset is 0-indexed, but line numbers in the output start at...?

**BACK:** 1 (uses cat -n format)

---

### Card 27
**FRONT:** What's the two-step Grep approach?

**BACK:**
Step 1: Grep with files_with_matches (find which files)
Step 2: Read specific files with limit (targeted reading)

---

### Card 28
**FRONT:** When should you use Agent tool with subagent_type='Explore'?

**BACK:**
- Broad exploration ("find all...", "explore...")
- Expected >3 Grep/Read operations
- Large unfamiliar codebase
- Keep main context clean

---

### Card 29
**FRONT:** Why use Agent tool for exploration instead of direct Grep/Read?

**BACK:** Agent runs in SEPARATE context, returns only summary (~500 tokens) vs 30K+ tokens in main context

---

### Card 30
**FRONT:** Token optimization: when should you NOT optimize?

**BACK:** Tasks < 5,000 tokens - optimization overhead > benefit

---

### Card 31
**FRONT:** Token optimization thresholds:
< 5K tokens = ?
5-20K tokens = ?
20-50K tokens = ?
\> 50K tokens = ?

**BACK:**
- < 5K: No optimization
- 5-20K: Basic limits (head_limit, limit)
- 20-50K: Agent isolation
- \> 50K: Chunking

---

### Card 32
**FRONT:** Which Claude model for simple tasks (<5K tokens, no reasoning)?

**BACK:** Haiku 4.5 (fastest, most economical)

---

### Card 33
**FRONT:** Which Claude model for moderate tasks (some reasoning)?

**BACK:** Sonnet 4.6 (balanced capability and cost)

---

### Card 34
**FRONT:** Which Claude model for complex tasks (heavy reasoning, architecture)?

**BACK:** Opus 4.6 (most capable, highest cost)

---

### Card 35
**FRONT:** You need to find which files contain 'authentication'.
Optimal Grep command?

**BACK:**
```python
Grep(
    pattern='authentication',
    output_mode='files_with_matches',
    head_limit=50
)
```

---

### Card 36
**FRONT:** You need to see actual error messages with 2 lines of context.
Optimal Grep command?

**BACK:**
```python
Grep(
    pattern='error',
    output_mode='content',
    head_limit=20,
    C=2  # context lines
)
```

---

### Card 37
**FRONT:** When using Grep with output_mode='content', what parameter should you ALWAYS set?

**BACK:** head_limit (to control output size, default 250 can be too large)

---

### Card 38
**FRONT:** You need to read a 100-line config file.
Should you optimize with offset/limit?

**BACK:** NO - file is small, optimization overhead > benefit, just read it fully

---

### Card 39
**FRONT:** Task requires ~50K tokens of exploration.
Should you use direct Grep/Read or Agent?

**BACK:** Agent tool - keeps main context clean, isolates heavy work in separate context

---

### Card 40
**FRONT:** What's the token cost difference between:
- Read full file (default)
- Read with limit=100

**BACK:**
- Full: ~40,000 tokens (2000 lines)
- Limited: ~2,000 tokens (100 lines)
- Savings: 38,000 tokens (95%)

---

## 🎯 MIXED SCENARIO FLASHCARDS (Cards 41-50)

### Card 41
**FRONT:** User says "I prefer React over Vue" - Is this USER or FEEDBACK?

**BACK:** USER (personal preference, not guidance on what to do/avoid)

---

### Card 42
**FRONT:** User says "The auth function is in auth.py line 45" - Save to memory?

**BACK:** NO - this is current code state, can be verified by reading file

---

### Card 43
**FRONT:** You read memory that says "Sprint ends Friday" but today is Monday (6 days after).
Is memory stale?

**BACK:** YES - deadline has passed, memory is outdated

---

### Card 44
**FRONT:** Finding a function in a 5000-line file.
Better approach: Read full file OR Grep then targeted Read?

**BACK:** Grep then targeted Read
- Grep: ~300 tokens (find line number)
- Read: ~2K tokens (100 lines around target)
- Total: ~2.3K vs 100K for full read

---

### Card 45
**FRONT:** Exploring 20+ files to understand authentication system.
Direct tools or Agent?

**BACK:** Agent (subagent_type='Explore') - multiple operations, separate context, returns summary

---

### Card 46
**FRONT:** FEEDBACK memory must always include what two sections?

**BACK:** **Why:** (the reason/past incident) and **How to apply:** (when to use this guidance)

---

### Card 47
**FRONT:** Memory says "Use old_api() function" but Grep finds no match.
What do you do?

**BACK:** Memory is STALE. Search for new API approach in current code. Trust current state, not memory.

---

### Card 48
**FRONT:** Task needs 3,000 tokens.
Optimize with Agent tool?

**BACK:** NO - task is small (<5K), optimization overhead > benefit

---

### Card 49
**FRONT:** You need match COUNTS not content.
Which Grep output_mode?

**BACK:** count (most efficient for counting, ~5 tokens per file)

---

### Card 50
**FRONT:** Writing simple unit tests for one function.
Which model: Haiku, Sonnet, or Opus?

**BACK:** Haiku or Sonnet (simple/moderate task, no complex reasoning needed)

---

## 📝 How to Use These Flashcards

1. **Print and cut** them out (or use digitally)
2. **Quiz yourself** - read front, answer, check back
3. **Make two piles** - "Know well" and "Need review"
4. **Focus on** the "Need review" pile
5. **Repeat** until all cards are in "Know well"

## 🎯 Mastery Test

Can you answer all 50 cards correctly without looking?
- 45-50 correct: **Excellent!** Ready for exam
- 40-44 correct: **Good!** Review weak areas
- 35-39 correct: **Fair** - Need more practice
- <35 correct: **Study more** - Review exercises

**Goal: 90%+ correct (45/50) before taking the real exam**

Good luck! 🚀
