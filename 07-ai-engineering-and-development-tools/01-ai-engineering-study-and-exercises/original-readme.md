# 🎓 Claude Certified Architect (CCA) - Exam Prep Repository

> Complete 3-day intensive study guide for the Claude Certified Architect certification exam

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Exam Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](https://github.com/subhashdixit/claude-certification-architect-exam-prep)
[![Study Days](https://img.shields.io/badge/Study%20Days-3-blue.svg)](https://github.com/subhashdixit/claude-certification-architect-exam-prep)

---

## 📚 Overview

This repository contains comprehensive study materials for the **Claude Certified Architect** exam, covering all 5 domains with hands-on exercises, flashcards, summaries, and practice questions.

**Total Exam Coverage:** 100% across all domains
**Study Time:** 3 days intensive preparation
**Practice Questions:** 60+ exam-style questions

---

## 🎯 Exam Domains Covered

| Domain | Weight | Status |
|--------|--------|--------|
| **1. Agentic Architecture & Orchestration** | 27% | ✅ Complete |
| **2. Claude Code Configuration & Workflows** | 20% | ✅ Complete |
| **3. Prompt Engineering & Structured Output** | 20% | ✅ Complete |
| **4. Tool Design & MCP Integration** | 18% | ✅ Complete |
| **5. Memory & Token Optimization** | 15% | ✅ Complete |

---

## 📂 Repository Structure

```
claude_certification_architect_exam_prep/
│
├── COMPLETE_FLASHCARDS.md          # 50+ flashcards covering all domains
├── COMPLETE_SUMMARY.md             # Comprehensive summary of all 3 days
├── CLAUDE.md                       # Project instructions and guidelines
│
├── day1/                           # Day 1: Agentic Architecture + Claude Code (47%)
│   ├── DAY1_FLASHCARDS.md
│   ├── DAY1_COMPLETE_SUMMARY.md
│   ├── agentic_architecture/
│   │   ├── agent_loops/           # Retry logic, circuit breaker, fallback
│   │   ├── orchestration/         # Sequential, parallel, hierarchical
│   │   ├── context_management/    # Compression, selective, sub-agents
│   │   └── tool_boundaries/       # Right tool for the job
│   └── claude_code/
│       ├── skills/                # Custom commands
│       └── hooks/                 # Automation triggers
│
├── day2/                           # Day 2: Prompting + Tools/MCP (38%)
│   ├── DAY2_FLASHCARDS.md
│   ├── DAY2_COMPLETE_SUMMARY.md
│   ├── prompting/
│   │   ├── techniques/            # 5 prompting techniques with examples
│   │   └── structured_output/     # JSON schema validation
│   └── tools_mcp/
│       ├── tool_design/           # 7 best practices + common patterns
│       └── mcp_servers/           # MCP protocol, 3 message types
│
├── day3/                           # Day 3: Memory & Token Optimization (15%)
│   ├── DAY3_FLASHCARDS.md
│   ├── DAY3_COMPLETE_SUMMARY.md
│   ├── optimization/
│   │   ├── memory/                # 4 memory types, staleness detection
│   │   └── tokens/                # Read/Grep optimization, model selection
│   └── review/
│
└── practice_questions/
    ├── PRACTICE_EXAM_60_QUESTIONS.md    # Full practice exam
    ├── INTERACTIVE_EXAM.html             # Interactive exam interface
    └── CCA_OFFICIAL_STYLE_EXAM.html      # Official exam style format
```

---

## 🚀 Quick Start

### Option 1: Study with Flashcards (Recommended for Quick Review)

```bash
# Start with the complete flashcards
open COMPLETE_FLASHCARDS.md

# Review daily, aim for 90%+ accuracy
```

**Flashcard Coverage:**
- 50+ cards covering all 5 domains
- Day 1: Agent loops, orchestration, Claude Code features
- Day 2: Prompting techniques, tool design, MCP
- Day 3: Memory types, token optimization

### Option 2: Deep Dive with Complete Summary

```bash
# Read the comprehensive summary
open COMPLETE_SUMMARY.md
```

**Summary Contents:**
- All concepts explained in detail
- Decision trees and comparison tables
- Real exam scenarios
- Common pitfalls and tips

### Option 3: Day-by-Day Study Plan

**Day 1: Agentic Architecture + Claude Code (47%)**
```bash
cd day1
python agentic_architecture/agent_loops/01_basic_loop.py
python agentic_architecture/orchestration/01_sequential.py
# Review: DAY1_FLASHCARDS.md
```

**Day 2: Prompting + Tools/MCP (38%)**
```bash
cd day2
python prompting/techniques/00_COMPARISON_ALL_TECHNIQUES.py
python tools_mcp/tool_design/03_BEST_PRACTICES.py
# Review: DAY2_FLASHCARDS.md
```

**Day 3: Memory & Token Optimization (15%)**
```bash
cd day3
python optimization/memory/exercise1_memory_crud.py
python optimization/tokens/exercise3_file_reading.py
# Review: DAY3_FLASHCARDS.md
```

---

## 📖 Study Materials

### 📇 Flashcards

| File | Cards | Topics |
|------|-------|--------|
| **COMPLETE_FLASHCARDS.md** | 50+ | All domains combined |
| **day1/DAY1_FLASHCARDS.md** | 25+ | Agent loops, orchestration, Claude Code |
| **day2/DAY2_FLASHCARDS.md** | 30+ | Prompting, tools, MCP |
| **day3/DAY3_FLASHCARDS.md** | 50 | Memory, token optimization |

**How to use:**
1. Read question (front)
2. Answer mentally
3. Check answer (back)
4. Sort into "Know well" vs "Need review" piles
5. Focus on weak areas

**Goal: 90%+ accuracy before taking exam**

---

### 📚 Complete Summaries

| File | Pages | Coverage |
|------|-------|----------|
| **COMPLETE_SUMMARY.md** | ~100 | All 3 days combined |
| **day1/DAY1_COMPLETE_SUMMARY.md** | ~40 | Agentic Architecture + Claude Code |
| **day2/DAY2_COMPLETE_SUMMARY.md** | ~35 | Prompting + Tools/MCP |
| **day3/DAY3_COMPLETE_SUMMARY.md** | ~25 | Memory + Token Optimization |

Each summary includes:
- Detailed concept explanations
- Code examples
- Decision trees
- Comparison tables
- Exam scenarios
- Quick self-tests

---

### 💻 Hands-On Exercises

**Day 1 Exercises:**
- `01_basic_loop.py` - Exponential backoff retry logic
- `02_circuit_breaker.py` - Circuit breaker pattern (3 states)
- `03_graceful_fallback.py` - Fallback hierarchy
- `01_sequential.py` - Sequential orchestration
- `02_parallel.py` - Parallel orchestration
- `03_hierarchical.py` - Hierarchical orchestration

**Day 2 Exercises:**
- `01_zero_shot.py` - Zero-shot prompting
- `00_COMPARISON_ALL_TECHNIQUES.py` - All 5 techniques compared
- `01_SIMPLE_TOOL_EXAMPLE.py` - Basic tool structure
- `03_BEST_PRACTICES.py` - 7 tool design principles
- `00_MCP_GUIDE.py` - Complete MCP overview

**Day 3 Exercises:**
- `exercise1_memory_crud.py` - Create/read/update/delete memory
- `exercise2_memory_types.py` - Practice 4 memory types
- `exercise3_staleness_check.py` - Detect stale memories
- `exercise3_file_reading.py` - Read tool optimization
- `exercise5_cost_analysis.py` - Token cost calculations

---

### 🎯 Practice Exams

| File | Questions | Format |
|------|-----------|--------|
| **PRACTICE_EXAM_60_QUESTIONS.md** | 60 | Markdown, detailed explanations |
| **INTERACTIVE_EXAM.html** | 60 | Browser-based, instant feedback |
| **CCA_OFFICIAL_STYLE_EXAM.html** | 60 | Official exam interface simulation |

**Practice Exam Features:**
- 60 questions covering all domains
- Multiple choice (4 options each)
- Detailed explanations for each answer
- Score tracking
- Timed mode (2 minutes per question)

**How to use:**
```bash
# Open interactive exam in browser
open practice_questions/INTERACTIVE_EXAM.html

# Or review questions in markdown
open practice_questions/PRACTICE_EXAM_60_QUESTIONS.md
```

---

## 🎓 Study Strategy

### Week 1: Foundation
- [ ] Read COMPLETE_SUMMARY.md
- [ ] Review COMPLETE_FLASHCARDS.md daily
- [ ] Complete Day 1 exercises
- [ ] Complete Day 2 exercises
- [ ] Complete Day 3 exercises

### Week 2: Practice
- [ ] Take practice exam (untimed)
- [ ] Review wrong answers
- [ ] Re-study weak domains
- [ ] Re-take practice exam
- [ ] Aim for 90%+ score

### Week 3: Review
- [ ] Daily flashcard review (15 min)
- [ ] Read decision trees and comparison tables
- [ ] Take timed practice exam
- [ ] Review common pitfalls
- [ ] **Schedule real exam**

---

## 📊 Key Concepts by Domain

### Domain 1: Agentic Architecture (27%)

**Must Know:**
- ✅ Exponential backoff formula
- ✅ Circuit breaker 3 states (CLOSED → OPEN → HALF-OPEN)
- ✅ Graceful fallback hierarchy
- ✅ Sequential vs Parallel vs Hierarchical orchestration
- ✅ Context management strategies

**Decision Tree:**
```
Network error? → Retry with exponential backoff
Service failing 5+ times? → Circuit breaker
API down, must show something? → Graceful fallback
Tasks depend on each other? → Sequential orchestration
Independent tasks? → Parallel orchestration
Complex workflow? → Hierarchical orchestration
```

---

### Domain 2: Claude Code (20%)

**Must Know:**
- ✅ Skills: Custom commands in `.claude/skills/`
- ✅ Hooks: 3 types (PreToolUse, PostToolUse, UserPromptSubmit)
- ✅ Permission modes: Default, AcceptEdits, Plan
- ✅ Subagents: Separate 200K token budget
- ✅ Memory: 4 types (user, feedback, project, reference)

**Decision Tree:**
```
Research only? → Plan mode
Trust file edits? → AcceptEdits mode
Maximum control? → Default mode
Long conversation? → Context compression
Large codebase? → Selective context
Research task? → Sub-agent (Explore)
```

---

### Domain 3: Prompt Engineering (20%)

**Must Know:**
- ✅ Zero-Shot: Simple tasks, no examples
- ✅ Few-Shot: Show 2-5 examples for specific format
- ✅ Chain-of-Thought: "Let's think step by step" for reasoning
- ✅ Structured Output: JSON schema for APIs/databases
- ✅ Injection Prevention: XML tags for user input

**Decision Tree:**
```
User-facing with untrusted input? → Injection Prevention
Need exact JSON/XML? → Structured Output
Multi-step reasoning? → Chain-of-Thought
Unusual format? → Few-Shot
Simple/common task? → Zero-Shot
```

---

### Domain 4: Tool Design & MCP (18%)

**Must Know:**
- ✅ 4 tool parts: Name, Description, Input Schema, Function
- ✅ 7 best practices: Single responsibility, clear names, detailed descriptions, validate inputs, return structured data, consistent format, use enums
- ✅ 3 MCP message types: initialize, tools/list, tools/call
- ✅ Tool vs MCP: Internal logic → Tool, External service → MCP

**Red Flags:**
- ❌ Vague descriptions ("Gets data")
- ❌ Throws exceptions (Claude can't catch)
- ❌ Multi-responsibility (one tool, many actions)
- ❌ No validation

---

### Domain 5: Memory & Token Optimization (15%)

**Must Know:**
- ✅ Memory types: USER (profile), FEEDBACK (guidance + Why/How), PROJECT (work + Why/How), REFERENCE (external)
- ✅ What NOT to save: Code patterns, git history, debugging solutions
- ✅ Staleness: Verify before using, trust current state
- ✅ Read optimization: offset + limit parameters
- ✅ Grep modes: files_with_matches (10 tokens), count (5 tokens), content (30 tokens)
- ✅ Two-step approach: Grep → targeted Read

**Token Thresholds:**
```
< 5K tokens → No optimization
5-20K tokens → Basic limits (head_limit, limit)
20-50K tokens → Agent isolation
> 50K tokens → Chunking
```

---

## 🎯 Exam Tips

### Time Management
- **2 minutes per question** (60 questions = 120 minutes)
- Skip hard ones, come back later
- Don't overthink simple questions

### Common Traps
- ❌ "Save code patterns" → NO (read files instead)
- ❌ "Use memory without verifying" → NO (always verify)
- ❌ "Read full large file" → NO (use limit parameter)
- ❌ "Tool for external service" → NO (use MCP)
- ❌ "Throw exceptions" → NO (return error objects)

### Trigger Words
- "user-submitted" → Injection Prevention
- "exact JSON" → Structured Output
- "reasoning/math" → Chain-of-Thought
- "specific format" → Few-Shot
- "simple task" → Zero-Shot
- "network error" → Retry with backoff
- "service failing" → Circuit breaker

---

## 🏆 Success Checklist

Before taking the exam, ensure you can:

**Memory:**
- [ ] Name all 4 memory types
- [ ] Know which types need Why + How to apply
- [ ] Explain what NOT to save
- [ ] Describe staleness detection

**Tokens:**
- [ ] Estimate token counts (~4 chars/token)
- [ ] Know default Read limit (2000 lines)
- [ ] Know default Grep head_limit (250)
- [ ] Apply two-step Grep approach

**Prompting:**
- [ ] Name all 5 techniques
- [ ] Match techniques to scenarios
- [ ] Write JSON schemas
- [ ] Apply injection prevention

**Tools/MCP:**
- [ ] Name 4 parts of a tool
- [ ] Apply 7 best practices
- [ ] Know 3 MCP message types
- [ ] Decide: Tool vs MCP

**Architecture:**
- [ ] Explain exponential backoff
- [ ] Describe circuit breaker states
- [ ] Compare orchestration patterns
- [ ] Choose context strategy

---

## 📈 Progress Tracking

Track your progress:

```bash
# Check what you've completed
cat progress.md

# Update after each session
echo "✅ Completed Day 1 exercises" >> progress.md
```

---

## 🤝 Contributing

Found an error or want to improve the materials? Contributions welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-exercises`)
3. Commit your changes (`git commit -m 'Add better examples'`)
4. Push to the branch (`git push origin improve-exercises`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Study materials prepared with **Claude Opus 4.6**
- Based on official **Claude Certified Architect** exam guide
- Community feedback and contributions

---

## 📧 Contact

**Repository Owner:** Subhash Dixit
**Email:** subhashdixit17@gmail.com
**GitHub:** [@subhashdixit](https://github.com/subhashdixit)

---

## 🎯 Final Tips

1. **Flashcards daily** - 15 minutes, aim for 90%+ accuracy
2. **Hands-on practice** - Run all exercises, understand WHY
3. **Practice exam** - Take it multiple times, review wrong answers
4. **Decision trees** - Memorize trigger words and patterns
5. **Sleep well** - Night before exam, review flashcards only

---

**Good luck with your Claude Certified Architect exam! 🚀**

*Last Updated: April 2026*
