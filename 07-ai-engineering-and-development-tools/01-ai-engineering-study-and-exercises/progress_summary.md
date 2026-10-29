# CCA Exam Prep — Progress Summary

**Date:** 2026-03-29

---

## Completed Topics

### Day 1 Morning — Agentic Architecture & Orchestration

**Status:** Complete

**Exercises built:**
- `01_basic_loop.py` — Agent loop with retry logic and exponential backoff
- `02_circuit_breaker.py` — Circuit breaker (stops retrying after threshold)
- `03_graceful_fallback.py` — Fallback chain: live → cache → default
- `01_sequential.py` — Sequential orchestration (A→B→C)
- `02_parallel.py` — Parallel orchestration (all at once)
- `03_hierarchical.py` — Hierarchical orchestration (boss + workers)
- Tool boundaries reference doc
- Context management strategies reference doc

**Key concepts learned:**
- Exponential backoff prevents hammering a failing service
- Circuit breaker opens after N failures to save resources
- Graceful fallback ensures the system always returns something useful
- Sequential = ordered steps, Parallel = concurrent tasks, Hierarchical = coordinator + specialists
- Always use dedicated tools (Read, Edit) instead of Bash for file operations
- Context management strategies: compression, selective context, sub-agents

---

### Day 1 Afternoon — Claude Code Configuration & Workflows

**Status:** Complete

**Topics covered:**
- Custom skill creation (`.claude/skills/name/SKILL.md`)
- Hook configuration — 3 types: PreToolUse, PostToolUse, UserPromptSubmit
- Permission modes: default (ask all), acceptEdits (auto edits), plan (read-only)
- Subagent workflows — spawned Explore agent, saved 32k tokens
- Memory system — 4 types: user, feedback, project, reference

**Key concepts learned:**
- Skills = reusable slash commands, stored locally or globally
- Hooks = automated shell commands triggered by Claude Code events
- Permission mode switching via Shift+Tab
- Subagents use a separate 200k token budget, preventing context exhaustion
- Memory persists across sessions automatically

---

### Day 2 Morning — Prompt Engineering & Structured Output

**Status:** Complete

**Exercises built:**
- `00_COMPARISON_ALL_TECHNIQUES.py` — Side-by-side comparison of all 5 techniques
- Zero-shot examples (classification, extraction, generation)
- Few-shot examples (learning from 2–5 examples)
- Chain-of-Thought implementation (step-by-step reasoning)
- Structured output with JSON schema validation
- Prompt injection prevention patterns
- 8 exam-style practice scenarios with answers

**Key concepts learned:**

Technique decision tree:
- User-submitted input / chatbot → Injection Prevention
- Need exact JSON / API output → Structured Output
- Math / multi-step reasoning → Chain-of-Thought
- Specific format / house style → Few-Shot
- Simple / common task → Zero-Shot

JSON schema essentials:
- Types: string, number, integer, boolean, array, object
- `required: []` — fields that must exist
- `enum: []` — fixed set of allowed values
- Always validate before passing to API or database

Real-world pipeline: Natural language → Claude → JSON → Validate → API/Database

---

## Not Yet Started

| Session | Topics |
|---|---|
| Day 2 Afternoon | Tool design, MCP server setup, integration examples |
| Day 3 Morning | Memory management, token optimization, cost strategies |
| Day 3 Afternoon | Full review, practice questions, mock exam |

---

## Exam Domain Coverage So Far

| Domain | Weight | Status |
|---|---|---|
| Agentic Architecture & Orchestration | 27% | Done |
| Claude Code Configuration & Workflows | 20% | Done |
| Prompt Engineering & Structured Output | 20% | Done |
| Tool Design & MCP Integration | 18% | Not started |
| Memory & Token Optimization | 15% | Not started |

**Coverage: 67% of exam weight completed**
