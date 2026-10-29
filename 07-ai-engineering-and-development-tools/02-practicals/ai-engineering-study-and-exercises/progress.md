# CCA Exam Prep - Progress Tracker

## Overview

Track your daily progress, learnings, and questions.

---

## Day 1: Agentic Architecture + Claude Code

### Morning Session (9:00 AM - 12:30 PM)

**Status:** ✅ COMPLETED
**Topics:** Agent loops, orchestration, tool boundaries, context management

#### Completed:

- [x] Agent loop with retry logic (01_basic_loop.py)
- [x] Circuit breaker implementation (02_circuit_breaker.py)
- [x] Graceful fallback (03_graceful_fallback.py)
- [x] Sequential orchestration (01_sequential.py)
- [x] Parallel orchestration (02_parallel.py)
- [x] Hierarchical orchestration (03_hierarchical.py)
- [x] Tool boundaries (reference doc)
- [x] Context management strategies (reference doc)

#### Key Learnings:
- Retry logic with exponential backoff prevents temporary failures
- Circuit breaker stops wasting resources after threshold (e.g., 5 failures)
- Graceful fallback provides alternatives (live → cache → default)
- Sequential: steps in order (A→B→C), Parallel: all at once (A,B,C), Hierarchical: boss + workers
- Use right tool: Edit for editing, Read for reading, NOT Bash for file operations
- Context management: compression, selective context, or sub-agents

#### Questions/Doubts:
- None so far!

---

### Afternoon Session (1:30 PM - 5:00 PM)

**Status:** ✅ COMPLETED
**Topics:** Claude Code skills, hooks, permission modes, subagents, memory

#### Completed:

- [x] Custom skill creation (hello skill example)
- [x] Hook configuration (3 hook types: Pre, Post, UserPrompt)
- [x] Permission mode testing (switched modes with Shift+Tab)
- [x] Subagent workflows (spawned Explore agent - saved 32k tokens!)
- [x] Memory system understanding (4 types: user, feedback, project, reference)

#### Key Learnings:
- Skills = custom commands in .claude/skills/name/SKILL.md (local or global)
- Hooks = auto-actions: PreToolUse (before), PostToolUse (after), UserPromptSubmit (on message)
- Permission modes: default (ask all), acceptEdits (auto edits), plan (read-only) - switch with Shift+Tab
- Subagents = spawned automatically for research, use separate 200k token budget
- Memory = automatic persistence: user (about you), feedback (how to work), project (current work), reference (external info)

#### Questions/Doubts:
- None - Day 1 complete!

---

## Day 2: Prompt Engineering + Tools/MCP

### Morning Session (9:00 AM - 12:30 PM)

**Status:** ✅ COMPLETED
**Topics:** Prompting techniques, structured output

#### Completed:

- [x] All 5 prompting techniques comparison (00_COMPARISON_ALL_TECHNIQUES.py)
- [x] Zero-shot examples (basic classification, extraction, generation)
- [x] Few-shot examples (learning from 2-5 examples)
- [x] Chain-of-Thought implementation (step-by-step reasoning)
- [x] Structured output with validation (JSON schemas)
- [x] Prompt injection prevention (security patterns)
- [x] Practice scenarios (8 exam-style questions with answers)
- [x] DAY2_FLASHCARDS.md - 50+ flashcards for quick review
- [x] DAY2_COMPLETE_SUMMARY.md - Full reference document

#### Key Learnings:

**Decision Tree for Techniques:**
- User-facing input? → Injection Prevention
- Need exact JSON? → Structured Output
- Multi-step reasoning? → Chain-of-Thought
- Unusual format? → Few-Shot (show examples)
- Simple/common task? → Zero-Shot

**Trigger Words to Memorize:**
- "user-submitted", "chatbot" → Injection Prevention
- "API", "database", "exact format" → Structured Output
- "reasoning", "math", "step-by-step" → Chain-of-Thought
- "specific format", "our style" → Few-Shot
- "simple", "straightforward" → Zero-Shot

**JSON Schema Essentials:**
- Types: string, number, integer, boolean, array, object
- required: [] - fields that MUST exist
- enum: [] - fixed set of values
- Always validate before using!

**Real-World Pattern:**
Natural language → Claude extracts to JSON → Validate → API/Database

#### Questions/Doubts:

None - all techniques clear!

---

### Afternoon Session (1:30 PM - 5:00 PM)

**Status:** ✅ COMPLETED
**Topics:** Tool design, MCP integration

#### Completed:

- [x] Tool design fundamentals (4 parts: name, description, schema, function)
- [x] Simple tool example (calculator - 01_SIMPLE_TOOL_EXAMPLE.py)
- [x] Complex parameters (nested objects, enums, defaults - 02_COMPLEX_PARAMETERS_EXAMPLE.py)
- [x] 7 best practices (03_BEST_PRACTICES.py)
- [x] MCP introduction - WHY it exists (01_WHY_MCP_EXISTS.py)
- [x] MCP architecture - HOW it works (02_HOW_MCP_WORKS.py)
- [x] Decision guide - WHEN to use (03_MCP_VS_TOOLS_DECISION.py)
- [x] DAY2_FLASHCARDS.md - Includes tool + MCP flashcards
- [x] DAY2_COMPLETE_SUMMARY.md - Complete reference

#### Key Learnings:

**Tool Anatomy (4 parts):**
1. Name - snake_case, verb + noun (e.g., send_email)
2. Description - Claude READS this to decide when to use
3. Input Schema - JSON schema for parameters
4. Function - The actual Python code

**7 Best Practices:**
1. Single Responsibility - one tool = one action
2. Clear Names - descriptive, verb + noun
3. Detailed Descriptions - Claude reads these!
4. Validate Inputs - security and safety checks
5. Return Structured Data - NOT exceptions (Claude can't catch them)
6. Consistent Format - {"success": bool, "data/error": ...}
7. Use Enums - for fixed choices

**Common Tool Patterns:**
- CRUD: create, read, update, delete (4 separate tools)
- Search: query + filters + pagination + sorting
- External API: handle rate limits, retries, auth
- File Ops: validate paths, check permissions
- Computation: pure functions, deterministic

**MCP (Model Context Protocol):**
- **What:** Standard protocol for connecting Claude to external services
- **Analogy:** USB-C for AI integrations
- **Why:** Solve integration duplication (reusable community servers)
- **Architecture:** Client ↔ MCP Server ↔ External Service
- **Protocol:** JSON-RPC 2.0 over stdio or HTTP/SSE
- **3 Message Types:** initialize, tools/list, tools/call

**Decision: Tool vs MCP:**
- **INTERNAL logic** → Regular Tool (calculate_tax, validate_email)
- **EXTERNAL service** → MCP Server (GitHub, Slack, Salesforce)
- Multiple operations + auth → MCP
- Simple operation + no external service → Tool

**Community MCP Servers:**
- @modelcontextprotocol/server-github
- @modelcontextprotocol/server-slack
- @modelcontextprotocol/server-postgres
- @modelcontextprotocol/server-filesystem

#### Questions/Doubts:

None - all concepts clear!

---

## Day 3: Optimization + Review

### Morning Session (9:00 AM - 12:30 PM)

**Status:** Not Started
**Topics:** Memory management, token optimization

#### Completed:

- [ ] Memory system implementation
- [ ] Token counting examples
- [ ] Context compression
- [ ] Cost optimization strategies

#### Key Learnings:

#### Questions/Doubts:

---

### Afternoon Session (1:30 PM - 5:00 PM)

**Status:** Not Started
**Topics:** Full review

#### Completed:

- [ ] All domain reviews
- [ ] Practice questions
- [ ] Mock exam

#### Key Learnings:

#### Questions/Doubts:

---

## Overall Progress

**Completed Exercises:** 0/25
**Weak Areas to Review:**
---------------------

**Confidence by Domain (1-5):**

- Agentic Architecture: ___/5
- Claude Code: ___/5
- Prompt Engineering: ___/5
- Tools/MCP: ___/5
- Optimization: ___/5

---

## Notes

*Use this section for any additional thoughts, insights, or reminders.*
