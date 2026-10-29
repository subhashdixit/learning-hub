# Claude Certified Architect (CCA) - Exam Prep Project

## Project Overview
This is a hands-on learning project to prepare for the Claude Certified Architect exam through practical exercises.

## Project Structure

```
claude_certification_architect_exam_prep/
├── CLAUDE.md (this file)
├── progress.md (track your learning)
├── day1/
│   ├── agentic_architecture/
│   │   ├── agent_loops/
│   │   ├── orchestration/
│   │   └── failure_recovery/
│   └── claude_code/
│       ├── skills/
│       ├── hooks/
│       └── agents/
├── day2/
│   ├── prompting/
│   │   ├── techniques/
│   │   └── structured_output/
│   └── tools_mcp/
│       ├── tool_design/
│       └── mcp_servers/
└── day3/
    └── optimization/
        ├── memory/
        └── tokens/
```

## Learning Goals

### Day 1 (Agentic Architecture + Claude Code)
- Build working agent loops with retry logic
- Create multi-agent orchestration systems
- Implement failure recovery patterns
- Design custom Claude Code skills
- Configure hooks for automation
- Work with subagents

### Day 2 (Prompting + Tools/MCP)
- Practice all prompting techniques
- Build structured output systems
- Design custom tools
- Create MCP server integrations

### Day 3 (Optimization + Review)
- Implement memory management
- Optimize token usage
- Full review and practice exam

## How to Run Exercises

### Python Exercises
```bash
cd day1/agentic_architecture/agent_loops
python exercise_name.py
```

### Claude Code Exercises
```bash
cd day1/claude_code/skills
# Follow instructions in each exercise
```

## Code Style

- **Python:** Use type hints, clear function names
- **Comments:** Explain WHY, not WHAT
- **Tests:** Run after every implementation
- **Git:** Commit after completing each exercise

## Testing Strategy

- Run code after writing
- Test edge cases
- Verify error handling
- Check performance

## Progress Tracking

Update `progress.md` after each session:
- What you learned
- What you built
- Questions that arose
- Concepts to review

## Build Commands

### Python
```bash
# Run Python scripts
python script_name.py

# Install dependencies (if needed)
pip install anthropic
```

### Testing
```bash
# Test individual exercises
python -m pytest test_file.py

# Test all
python -m pytest
```

## Notes

- Focus on understanding WHY, not just memorizing
- Build everything from scratch - hands-on is key
- Reference the study plan PDF for theory
- Ask Claude questions as you learn!

## Exam Domains Coverage

This project covers all 5 domains:
1. Agentic Architecture & Orchestration (27%) - Day 1 morning
2. Claude Code Configuration & Workflows (20%) - Day 1 afternoon
3. Prompt Engineering & Structured Output (20%) - Day 2 morning
4. Tool Design & MCP Integration (18%) - Day 2 afternoon
5. Memory & Token Optimization (15%) - Day 3 morning

## Resources

- Study Plan: `~/CCA_3Day_Study_Plan.pdf`
- Quick Reference: `~/CCA_Quick_Reference.pdf`
- Anthropic Docs: https://docs.anthropic.com
- Claude Code Docs: https://code.claude.com/docs

## Remember

You're learning architecture, not memorizing facts. Each exercise teaches decision-making patterns you'll see on the exam.

Good luck! 🚀
