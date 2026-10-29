# Day 3 Afternoon: Comprehensive Review

**Goal:** Review all 5 exam domains and identify weak areas

---

## Review Structure

### 1. Domain-by-Domain Review (60 minutes)
Go through each domain systematically:

#### Domain 1: Agentic Architecture & Orchestration (27%)
- [ ] Agent loop patterns (simple, reflection, hierarchical)
- [ ] Tool calling and error handling
- [ ] Multi-agent orchestration
- [ ] Failure recovery strategies
- [ ] Retry logic and exponential backoff

**Review materials:** `day1/agentic_architecture/`

#### Domain 2: Claude Code Configuration & Workflows (20%)
- [ ] Custom skills creation
- [ ] Hook configuration (UserPromptSubmit, etc.)
- [ ] Subagent spawning and management
- [ ] Claude Code tools (Read, Write, Edit, Grep, Glob, Bash)
- [ ] When to use each tool

**Review materials:** `day1/claude_code/`

#### Domain 3: Prompt Engineering & Structured Output (20%)
- [ ] All prompting techniques (chain-of-thought, few-shot, etc.)
- [ ] XML tags for structure
- [ ] Structured output (JSON, TypeScript types)
- [ ] Prompt optimization
- [ ] Context management in prompts

**Review materials:** `day2/prompting/`

#### Domain 4: Tool Design & MCP Integration (18%)
- [ ] Tool design principles
- [ ] Input validation
- [ ] Error handling in tools
- [ ] MCP server architecture
- [ ] Tool discovery and registration

**Review materials:** `day2/tools_mcp/`

#### Domain 5: Memory & Token Optimization (15%)
- [ ] Memory types (user, feedback, project, reference)
- [ ] Memory lifecycle
- [ ] Staleness detection
- [ ] Token counting basics
- [ ] Read/Grep optimization (offset, limit, head_limit)
- [ ] Model selection

**Review materials:** `day3/optimization/`

---

### 2. Quick Reference Flashcards (30 minutes)

Create flashcards for key concepts:

```
Q: What are the 4 memory types in Claude Code?
A: user, feedback, project, reference

Q: What's the default Read tool line limit?
A: 2000 lines (~40K tokens)

Q: When should you use Agent tool with subagent_type=Explore?
A: Broad codebase exploration that might require >3 queries

Q: What are the 3 Grep output modes?
A: files_with_matches, count, content

Q: What's the structure of feedback/project memories?
A: Content + **Why:** + **How to apply:**
```

---

### 3. Common Pitfalls Checklist (15 minutes)

Review these common mistakes:

**Memory:**
- ❌ Saving code patterns (should derive from files)
- ❌ Not verifying memory before using
- ❌ Creating duplicate memories

**Token Optimization:**
- ❌ Reading full large files without limit
- ❌ Using Grep content mode without head_limit
- ❌ Not using Agent tool for broad exploration

**Tools:**
- ❌ Using Bash for file operations (use Read/Write/Edit)
- ❌ Not handling tool errors
- ❌ Missing required parameters

**Prompting:**
- ❌ Not using XML tags for structure
- ❌ Verbose prompts without clear structure
- ❌ Not specifying output format

**Agents:**
- ❌ No retry logic for transient failures
- ❌ Not handling agent failures gracefully
- ❌ Infinite loops without max iterations

---

### 4. Practice Exam (120 minutes)

Take the full practice exam: `day3/review/practice_exam.py`

- 60 questions
- 120 minutes
- Passing score: 70% (42/60)
- Simulates real exam conditions

---

### 5. Weak Area Focus (60 minutes)

After practice exam, identify your weak domains:

- **< 60% correct:** Critical - intensive review needed
- **60-75% correct:** Moderate - targeted review
- **> 75% correct:** Strong - light review

Go back to exercises in weak areas and repeat them.

---

## Review Tips

1. **Don't just read - do**
   - Run the exercises again
   - Write code from scratch
   - Explain concepts out loud

2. **Focus on "WHY" not "WHAT"**
   - Understand reasoning behind patterns
   - Know when to apply each approach

3. **Time yourself**
   - Practice answering questions quickly
   - Real exam is ~2 minutes per question

4. **Use the Quick Reference**
   - Keep it handy during review
   - Test yourself without looking

5. **Identify patterns**
   - Many questions test the same concepts
   - Learn to recognize question types

---

## Final Exam Prep

Before taking the real exam:

1. ✅ Completed all Day 1-3 exercises
2. ✅ Scored 70%+ on practice exam
3. ✅ Reviewed weak areas
4. ✅ Can explain all 5 domains clearly
5. ✅ Feel confident with hands-on tasks

---

## Time Management for Real Exam

- **60 questions in 120 minutes = 2 min/question**
- First pass: Answer all questions you know (60 min)
- Second pass: Tackle harder questions (45 min)
- Final pass: Review flagged questions (15 min)

**Strategy:**
- Flag uncertain questions
- Don't spend > 3 min on any single question
- Come back to hard ones after finishing easy ones

---

## You've Got This! 🚀

Three days of hands-on practice has prepared you well. Trust your preparation and approach the exam with confidence!
