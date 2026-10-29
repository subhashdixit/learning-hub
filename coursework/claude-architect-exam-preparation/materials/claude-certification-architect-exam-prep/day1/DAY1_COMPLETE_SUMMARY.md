# 📚 Day 1 Complete Summary - Agentic Architecture + Claude Code

**Exam Coverage:** 47% (Agentic Architecture 27% + Claude Code 20%)

---

## 🤖 Morning Session: Agentic Architecture & Orchestration (27% of Exam)

### Overview
Learn how to build robust agent systems with retry logic, orchestration patterns, and failure recovery.

---

## PART 1: AGENT LOOPS WITH RETRY LOGIC

### What Is an Agent Loop?
A pattern where an agent repeatedly tries to accomplish a task until it succeeds or reaches a failure threshold.

### Basic Agent Loop Pattern
```python
def agent_loop(task, max_retries=3):
    attempts = 0

    while attempts < max_retries:
        try:
            result = execute_task(task)
            if result.success:
                return result
        except Exception as e:
            attempts += 1
            if attempts >= max_retries:
                raise
            # Wait before retry
            time.sleep(2 ** attempts)  # Exponential backoff

    raise MaxRetriesExceeded()
```

---

## 1. BASIC RETRY LOGIC

### Purpose
Handle temporary failures (network issues, rate limits, transient errors)

### Pattern
```python
def retry_with_exponential_backoff(
    func,
    max_retries=3,
    initial_delay=1,
    backoff_factor=2
):
    """
    Retry function with exponential backoff

    Delays: 1s, 2s, 4s, 8s...
    """
    for attempt in range(max_retries):
        try:
            return func()
        except TemporaryError as e:
            if attempt == max_retries - 1:
                raise

            delay = initial_delay * (backoff_factor ** attempt)
            print(f"Attempt {attempt + 1} failed. Retrying in {delay}s...")
            time.sleep(delay)
```

### Key Concepts

**Exponential Backoff:**
- Attempt 1: Wait 1 second
- Attempt 2: Wait 2 seconds
- Attempt 3: Wait 4 seconds
- Attempt 4: Wait 8 seconds

**Why Exponential?**
- Gives system time to recover
- Reduces load on failing service
- More polite than hammering with retries

### When to Use
✅ Temporary failures (network hiccups)
✅ Rate limits
✅ Transient API errors
✅ Database connection issues

### When NOT to Use
❌ Permanent failures (invalid credentials)
❌ Logic errors (bad code)
❌ Validation errors (bad input)

---

## 2. CIRCUIT BREAKER PATTERN

### What Is It?
Stop trying after threshold - prevent wasting resources on a failing service.

### Analogy
Like an electrical circuit breaker:
- Normal operation: Closed (requests flow)
- Too many failures: Open (stop sending requests)
- After timeout: Half-open (try one request to test)

### States

**CLOSED (Normal):**
- Requests flow normally
- Track failures
- If failures > threshold → OPEN

**OPEN (Failing):**
- All requests fail immediately
- Don't waste time trying
- After timeout → HALF-OPEN

**HALF-OPEN (Testing):**
- Try ONE request
- Success → CLOSED (recovered!)
- Failure → OPEN (still broken)

### Implementation
```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = "CLOSED"

    def call(self, func):
        # If OPEN, check if timeout passed
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.timeout:
                self.state = "HALF_OPEN"
            else:
                raise CircuitOpenError("Circuit breaker is OPEN")

        # Try the function
        try:
            result = func()
            # Success! Reset if half-open, or clear failures
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
            self.failures = 0
            return result

        except Exception as e:
            self.failures += 1
            self.last_failure_time = time.time()

            # Too many failures? Open circuit
            if self.failures >= self.failure_threshold:
                self.state = "OPEN"

            raise
```

### When to Use
✅ External API calls
✅ Database connections
✅ Microservices communication
✅ Any service that can fail

### Benefits
- Prevents cascading failures
- Saves resources (don't retry what's broken)
- Fast failure (immediate response when open)
- Automatic recovery testing (half-open state)

---

## 3. GRACEFUL FALLBACK PATTERN

### What Is It?
Provide alternative when primary method fails.

### Hierarchy
```
Try: Live API call
  ↓ Fails
Fallback 1: Cached data
  ↓ Not available
Fallback 2: Default value
  ↓
Return: Best available result
```

### Implementation
```python
def get_weather_with_fallback(city):
    # Try 1: Live API
    try:
        return fetch_from_weather_api(city)
    except APIError:
        print("Live API failed, trying cache...")

    # Try 2: Cache
    cached = get_from_cache(city)
    if cached and not is_expired(cached):
        return cached

    # Try 3: Default
    return {
        "city": city,
        "temperature": "unavailable",
        "source": "default"
    }
```

### Fallback Strategies

**1. Cache:**
- Use recent cached data
- Better than nothing
- Mark as "cached" for transparency

**2. Default Value:**
- Sensible defaults
- Example: Show "N/A" for weather

**3. Degraded Service:**
- Partial functionality
- Example: Show text without images

**4. Alternative Source:**
- Backup API
- Secondary database

### When to Use
✅ User-facing applications (need to show something)
✅ Non-critical data (approximation OK)
✅ High availability required

### Best Practices
- Always indicate when using fallback
- Log fallback usage for monitoring
- Clear hierarchy (live → cache → default)
- Set expiration for cached data

---

## PART 2: ORCHESTRATION PATTERNS

### What Is Orchestration?
Coordinating multiple agents or tasks to accomplish a complex goal.

---

## 1. SEQUENTIAL ORCHESTRATION

### Pattern
Tasks execute one after another. Each task depends on the previous task's result.

```
Task A → Task B → Task C → Result
```

### Implementation
```python
def sequential_orchestration():
    # Step 1: Research
    research_result = research_agent.run()

    # Step 2: Analyze (uses research result)
    analysis_result = analysis_agent.run(research_result)

    # Step 3: Report (uses analysis)
    report = report_agent.run(analysis_result)

    return report
```

### When to Use
✅ Tasks depend on previous results
✅ Need to pass data between tasks
✅ Order matters

### Example Use Cases
- Research → Analyze → Report
- Scrape → Clean → Store
- Fetch → Process → Display

### Characteristics
- **Speed:** ⚡ Slow (sequential, no parallelism)
- **Complexity:** ⭐ Simple (easy to understand)
- **Data Flow:** Linear (A → B → C)

---

## 2. PARALLEL ORCHESTRATION

### Pattern
Tasks execute simultaneously. They don't depend on each other.

```
    ┌─ Task A ─┐
    ├─ Task B ─┤ → Combine Results
    └─ Task C ─┘
```

### Implementation
```python
import concurrent.futures

def parallel_orchestration():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Start all tasks at once
        future_a = executor.submit(fetch_from_api_a)
        future_b = executor.submit(fetch_from_api_b)
        future_c = executor.submit(fetch_from_api_c)

        # Wait for all to complete
        results = {
            'a': future_a.result(),
            'b': future_b.result(),
            'c': future_c.result()
        }

    return combine_results(results)
```

### When to Use
✅ Independent tasks
✅ No data dependencies
✅ Speed is important

### Example Use Cases
- Fetch from multiple APIs simultaneously
- Process multiple files at once
- Run multiple searches in parallel

### Characteristics
- **Speed:** ⚡⚡⚡ Fast (all tasks at once)
- **Complexity:** ⭐⭐ Medium (need to handle concurrency)
- **Data Flow:** Parallel (A || B || C)

### Benefits
- Much faster than sequential
- Better resource utilization
- Can handle failures independently

### Considerations
- Need thread-safe operations
- Handle partial failures
- Combine results at the end

---

## 3. HIERARCHICAL ORCHESTRATION

### Pattern
Boss agent delegates tasks to worker agents.

```
      Boss Agent
      /    |    \
Worker A  Worker B  Worker C
```

### Implementation
```python
class BossAgent:
    def __init__(self):
        self.workers = {
            'researcher': ResearchWorker(),
            'analyst': AnalystWorker(),
            'writer': WriterWorker()
        }

    def orchestrate(self, task):
        # Boss decides which workers to use
        if task.type == "research_report":
            # Delegate to workers
            research = self.workers['researcher'].execute(task)
            analysis = self.workers['analyst'].execute(research)
            report = self.workers['writer'].execute(analysis)
            return report

        elif task.type == "quick_summary":
            # Skip some workers for quick tasks
            research = self.workers['researcher'].execute(task)
            return self.workers['writer'].execute(research)
```

### When to Use
✅ Complex workflows
✅ Different types of tasks
✅ Need specialization (each worker expert in one thing)
✅ Dynamic task routing

### Example Use Cases
- Research boss → Data collector, Analyzer, Report writer
- CI/CD boss → Build worker, Test worker, Deploy worker
- Customer service boss → Classifier, Support agent, Escalation agent

### Characteristics
- **Speed:** ⚡⚡ Variable (depends on workflow)
- **Complexity:** ⭐⭐⭐ High (most complex)
- **Data Flow:** Tree-like (boss → workers)

### Benefits
- Clear separation of concerns
- Each worker specialized
- Boss makes decisions
- Easy to add new workers

---

## ORCHESTRATION COMPARISON

| Pattern | Speed | Complexity | Use Case | Data Flow |
|---------|-------|------------|----------|-----------|
| Sequential | ⚡ Slow | ⭐ Simple | A depends on B | A → B → C |
| Parallel | ⚡⚡⚡ Fast | ⭐⭐ Medium | Independent tasks | A ‖ B ‖ C |
| Hierarchical | ⚡⚡ Variable | ⭐⭐⭐ High | Complex workflows | Boss → Workers |

---

## PART 3: TOOL BOUNDARIES

### What Are Tool Boundaries?
**Tool boundaries** = Understanding what tools can do vs what agents should do.

### The Right Tool for the Job Principle

**❌ DON'T use Bash for:**
- Reading files → Use **Read** tool
- Editing files → Use **Edit** tool
- Searching files → Use **Glob** tool
- Searching content → Use **Grep** tool
- Writing files → Use **Write** tool

**✅ DO use Bash for:**
- Running tests
- Building/compiling
- Git operations
- Package management (npm, pip)
- System commands

### Why Tool Boundaries Matter

**Benefits of using right tools:**
1. **Faster** - Dedicated tools are optimized
2. **Clearer** - User sees exactly what you're doing
3. **Safer** - Less chance of mistakes
4. **Reviewable** - User can approve specific actions

### Example: Wrong vs Right

**❌ WRONG:**
```python
# Using Bash to read a file
bash("cat config.json")
```

**✅ RIGHT:**
```python
# Using Read tool
Read("config.json")
```

**Why better?**
- Read tool shows file path clearly
- User can review the specific file
- Better permission handling
- More reliable

### Tool Selection Guide

| Task | Use This Tool | NOT This |
|------|---------------|----------|
| Read file | Read | cat, head, tail |
| Edit file | Edit | sed, awk, echo |
| Find files | Glob | find, ls |
| Search content | Grep | grep, rg |
| Write file | Write | echo >, cat <<EOF |
| Run tests | Bash | ✓ Correct |
| Git commands | Bash | ✓ Correct |

---

## PART 4: CONTEXT MANAGEMENT

### The Problem
Claude has a token limit (200K tokens). Large codebases can exceed this.

### Strategies

### 1. Context Compression
**Idea:** Summarize previous conversation, keep only important parts.

**When to use:** Long conversations, lots of history

**How:**
```
Full conversation (150K tokens)
     ↓ Compress
Summary (20K tokens) + Recent messages (30K)
     = 50K tokens!
```

### 2. Selective Context
**Idea:** Only include relevant files/information.

**When to use:** Large codebases, working on specific feature

**How:**
- Don't load entire codebase
- Load only files related to current task
- Load on-demand as needed

**Example:**
```
Task: Fix bug in auth.py

DON'T load:
- database.py (not related)
- ui.py (not related)
- tests/* (not needed)

DO load:
- auth.py (the file)
- config.py (auth config)
- utils.py (auth uses it)
```

### 3. Sub-Agents
**Idea:** Spawn separate agent for specific task. Sub-agent has its own 200K token budget!

**When to use:**
- Research tasks (lots of file reading)
- Need to explore large codebase
- Want to protect main conversation tokens

**How:**
```python
# Main agent (200K tokens)
Agent(
    description="Research vim mode implementation",
    subagent_type="Explore"
)
# Sub-agent gets its own 200K tokens!
```

**Benefits:**
- Sub-agent has separate 200K token budget
- Main conversation stays clean
- Can run multiple sub-agents
- Results summarized back to main agent

### Context Management Comparison

| Strategy | When to Use | Token Savings | Complexity |
|----------|-------------|---------------|------------|
| Compression | Long conversations | High | Low |
| Selective Context | Large codebases | High | Medium |
| Sub-Agents | Research tasks | Very High | Low |

---

# ⚙️ Afternoon Session: Claude Code Configuration & Workflows (20% of Exam)

## Overview
Learn Claude Code features: skills, hooks, permission modes, subagents, and memory system.

---

## PART 1: SKILLS

### What Are Skills?
**Skills** = Custom commands you create for Claude Code

Like bash aliases, but more powerful!

### Structure
```
.claude/skills/skill-name/
└── SKILL.md       ← Defines the skill
```

### SKILL.md Format
```markdown
---
name: skill-name
description: What this skill does
---

Instructions for Claude when this skill is invoked.

This can include:
- What to do
- What tools to use
- What format to output
- Special requirements
```

### Example: Hello Skill
```markdown
---
name: hello
description: Say hello and show current directory
---

When invoked, say "Hello!" and show the current working directory.
Use the Bash tool to run `pwd` and display the result.
```

### Creating a Skill

**1. Local Skill** (project-specific):
```bash
mkdir -p .claude/skills/my-skill
nano .claude/skills/my-skill/SKILL.md
```

**2. Global Skill** (all projects):
```bash
mkdir -p ~/.claude/skills/my-skill
nano ~/.claude/skills/my-skill/SKILL.md
```

### Using a Skill
```bash
/my-skill
# or
/my-skill arg1 arg2
```

### Skill Best Practices
- ✅ Clear, descriptive name
- ✅ Detailed description
- ✅ Explicit instructions
- ✅ Specify tools to use
- ✅ Document expected inputs/outputs

### Common Skill Patterns

**1. Automation Skill:**
```markdown
---
name: test
description: Run all tests and show results
---

Run the test suite using pytest.
Show test results with colors.
If tests fail, show the failure details.
```

**2. Workflow Skill:**
```markdown
---
name: commit
description: Create a git commit with conventional commit message
---

1. Run git status to see changes
2. Run git diff to understand changes
3. Stage changes with git add
4. Create commit with clear message following conventional commits
5. Show git log to verify
```

**3. Information Skill:**
```markdown
---
name: project-info
description: Show project information and structure
---

Display:
1. Project name and description from package.json
2. Main dependencies
3. Directory structure (tree -L 2)
4. Recent commits (git log -5 --oneline)
```

---

## PART 2: HOOKS

### What Are Hooks?
**Hooks** = Automatic actions triggered by events

Like git hooks, but for Claude Code!

### Hook Types

### 1. PreToolUse Hook
**Triggers:** Before Claude uses a tool
**Use case:** Validation, logging, preparation

**Example:**
```json
{
  "hooks": {
    "PreToolUse": {
      "command": "echo 'About to use tool: {{tool_name}}'"
    }
  }
}
```

### 2. PostToolUse Hook
**Triggers:** After Claude uses a tool
**Use case:** Cleanup, notifications, logging

**Example:**
```json
{
  "hooks": {
    "PostToolUse": {
      "command": "echo 'Finished using tool: {{tool_name}}'"
    }
  }
}
```

### 3. UserPromptSubmit Hook
**Triggers:** When you send a message to Claude
**Use case:** Logging, timestamps, notifications

**Example:**
```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "echo '💬 USER-HOOK: You sent a message!'"
    }
  }
}
```

### Hook Configuration

**Location:**
- `~/.claude/settings.json` (global)
- `.claude/settings.local.json` (project-specific)

**Format:**
```json
{
  "hooks": {
    "HookName": {
      "command": "shell command to run",
      "blocking": true  // optional: wait for completion
    }
  }
}
```

### Hook Variables

Available in hook commands:
- `{{tool_name}}` - Name of the tool used
- `{{timestamp}}` - Current timestamp
- `{{project_path}}` - Project directory

### Hook Best Practices
- ✅ Keep hooks fast (don't slow down workflow)
- ✅ Use for automation, not blocking tasks
- ✅ Log errors (hooks fail silently)
- ✅ Test hooks before relying on them

### Common Hook Use Cases

**1. Logging:**
```json
{
  "hooks": {
    "PostToolUse": {
      "command": "echo '$(date): {{tool_name}}' >> ~/claude-log.txt"
    }
  }
}
```

**2. Notifications:**
```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "osascript -e 'display notification \"Message sent\" with title \"Claude\"'"
    }
  }
}
```

**3. Validation:**
```json
{
  "hooks": {
    "PreToolUse": {
      "command": "validate-tool {{tool_name}}"
    }
  }
}
```

---

## PART 3: PERMISSION MODES

### What Are Permission Modes?
Control what Claude can do automatically vs what needs approval.

### The 3 Modes

### 1. Default Mode (Ask Everything)
**Behavior:** Claude asks permission for every tool use

**When to use:**
- Working on critical code
- Don't know Claude well yet
- Want full control

**Switch:** Default mode

---

### 2. AcceptEdits Mode (Auto-approve edits)
**Behavior:**
- ✅ Auto-approve: Read, Edit, Write, Glob, Grep
- ❓ Ask permission: Bash, other tools

**When to use:**
- Trust Claude with file operations
- Want faster file editing
- Still want control over system commands

**Switch:** `Shift + Tab` → Select "acceptEdits"

---

### 3. Plan Mode (Read-only)
**Behavior:**
- ✅ Auto-approve: Read, Glob, Grep (read-only)
- ❌ Block: Edit, Write, Bash (modifications)

**When to use:**
- Planning phase (research only)
- Don't want Claude to change anything
- Exploring codebase

**Switch:** Use `EnterPlanMode` tool or `Shift + Tab`

---

### Permission Mode Comparison

| Mode | File Reads | File Edits | Bash Commands | Use Case |
|------|------------|------------|---------------|----------|
| Default | Ask | Ask | Ask | Maximum control |
| AcceptEdits | Auto ✓ | Auto ✓ | Ask | Faster editing |
| Plan | Auto ✓ | Block ✗ | Block ✗ | Read-only research |

### Switching Modes
**Keyboard:** `Shift + Tab` → Select mode
**Programmatic:** Claude can enter plan mode with `EnterPlanMode` tool

---

## PART 4: SUBAGENTS

### What Are Subagents?
**Subagents** = Separate Claude instances spawned for specific tasks

### Key Benefit
**Each subagent gets its own 200K token budget!**

Main agent: 200K tokens
Subagent 1: 200K tokens (separate!)
Subagent 2: 200K tokens (separate!)

### When Claude Spawns Subagents
**Automatically** for:
- Research tasks (Explore agent)
- Complex searches
- Need to read many files

**Example:**
```
You: "Search for all implementations of vim mode"

Claude: "I'll use the Explore agent to search..."
  → Spawns Explore subagent
  → Subagent searches (uses its 200K tokens)
  → Returns summary to main agent
```

### Subagent Types

**1. Explore Agent:**
- **Purpose:** Codebase exploration
- **Tools:** Read, Glob, Grep
- **Use case:** "Find all files that...", "How does X work?"

**2. General-Purpose Agent:**
- **Purpose:** Complex multi-step tasks
- **Tools:** All tools
- **Use case:** Research, complex operations

**3. Plan Agent:**
- **Purpose:** Implementation planning
- **Tools:** Read-only tools
- **Use case:** Architectural decisions

### Benefits of Subagents
1. **Token Budget:** Fresh 200K tokens
2. **Isolation:** Doesn't clutter main conversation
3. **Specialization:** Focused on one task
4. **Parallel Work:** Multiple subagents can work simultaneously

### Example Use Case

**Task:** Understand authentication system in large codebase

**Without Subagent:**
- Main agent reads 50+ files
- Uses 150K tokens (getting close to limit!)
- Main conversation cluttered

**With Subagent:**
```
Main Agent (20K tokens used):
  "I'll spawn an Explore agent to research auth"

Explore Subagent (own 200K budget):
  - Reads auth.py
  - Reads auth_middleware.py
  - Reads user_model.py
  - Reads config.py
  - ... (50+ files)
  → Summarizes findings

Main Agent (22K tokens used):
  Receives summary (2K tokens)
  "Here's how auth works: [summary]"
```

**Result:** Main conversation stays clean, used 32K tokens saved!

---

## PART 5: MEMORY SYSTEM

### What Is It?
**Memory** = Persistent file-based storage at `~/.claude/projects/[project]/memory/`

Survives across conversations!

### Memory Types

### 1. User Memory
**Stores:** Information about YOU

**When to save:**
- Your role (senior engineer, student, etc.)
- Your preferences (how you like to work)
- Your knowledge level
- Your goals

**Example:**
```markdown
---
name: user_role
description: User is a senior backend engineer
type: user
---

The user is a senior backend engineer with 10 years of experience.
They prefer TypeScript over JavaScript and focus on API design.
```

**How Claude uses it:**
- Tailors explanations to your level
- Suggests solutions matching your preferences
- Understands your perspective

---

### 2. Feedback Memory
**Stores:** How to work with you (corrections & confirmations)

**When to save:**
- You correct Claude ("don't do that", "stop doing X")
- You confirm an approach ("yes, exactly", "perfect")

**Example:**
```markdown
---
name: testing_approach
description: User wants integration tests, not mocks
type: feedback
---

User wants real database integration tests, NOT mocks.

**Why:** Last quarter, mocked tests passed but prod migration failed.

**How to apply:** Always use real database for integration tests.
Never mock database connections in integration tests.
```

**How Claude uses it:**
- Avoids repeating mistakes
- Remembers what worked
- Adapts to your preferences

---

### 3. Project Memory
**Stores:** Ongoing work, goals, initiatives

**When to save:**
- Who's doing what
- Project deadlines
- Important decisions
- Ongoing bugs/features

**Example:**
```markdown
---
name: q4_mobile_release
description: Mobile team release freeze starting March 5
type: project
---

Merge freeze begins 2026-03-05 for mobile release cut.

**Why:** Mobile team cutting release branch for app store submission.

**How to apply:** Flag any non-critical PRs scheduled after March 5.
Critical bug fixes only during freeze.
```

**How Claude uses it:**
- Understands current project context
- Makes relevant suggestions
- Considers deadlines

---

### 4. Reference Memory
**Stores:** Pointers to external information

**When to save:**
- Where information lives
- External tools/systems
- Documentation locations

**Example:**
```markdown
---
name: bug_tracking
description: Pipeline bugs tracked in Linear project INGEST
type: reference
---

Pipeline bugs are tracked in Linear project "INGEST".

**What:** All ingestion pipeline issues
**Where:** https://linear.app/company/project/INGEST
**When to use:** When working on pipeline bugs or creating issues
```

**How Claude uses it:**
- Knows where to look for information
- Can reference correct systems
- Provides accurate links

---

### Memory Structure

**File Format:**
```markdown
---
name: memory_name
description: One-line description (used for relevance)
type: user|feedback|project|reference
---

Memory content here.

For feedback/project memories:
- Lead with the fact/rule
- **Why:** The reason/motivation
- **How to apply:** When this applies
```

**Index File:**
`MEMORY.md` - Lists all memories with links

```markdown
# Memory Index

## User
- [user_role](user_role.md) - Senior backend engineer

## Feedback
- [testing_approach](testing_approach.md) - Use real DB, not mocks

## Project
- [q4_mobile_release](q4_mobile_release.md) - Merge freeze March 5

## Reference
- [bug_tracking](bug_tracking.md) - Linear project INGEST
```

---

### Memory Best Practices

**What TO save:**
✅ User role and preferences
✅ Important feedback (corrections & confirmations)
✅ Ongoing project work
✅ External system references

**What NOT to save:**
❌ Code patterns (get from current codebase)
❌ Git history (use git log)
❌ Temporary task details
❌ Already in CLAUDE.md files

**Maintenance:**
- Update stale memories
- Remove outdated information
- Keep descriptions specific
- Organize by topic, not chronologically

---

### Memory vs Other Persistence

| Type | Use For | Survives | Scope |
|------|---------|----------|-------|
| Memory | User prefs, project context | Across sessions | Project |
| Plan | Current implementation approach | Current conversation | Task |
| Tasks | Work breakdown for current session | Current conversation | Task |
| CLAUDE.md | Project rules, conventions | Permanent | Project |

---

## 🎯 EXAM PREPARATION - Day 1

### What You NEED to Know

**Agent Loops:**
✅ Basic retry with exponential backoff
✅ Circuit breaker (3 states: closed, open, half-open)
✅ Graceful fallback (live → cache → default)

**Orchestration:**
✅ Sequential (A → B → C)
✅ Parallel (A ‖ B ‖ C)
✅ Hierarchical (Boss → Workers)

**Tool Boundaries:**
✅ Right tool for job (Read vs cat, Edit vs sed)
✅ When to use Bash vs dedicated tools

**Context Management:**
✅ Compression (summarize history)
✅ Selective context (load only relevant files)
✅ Sub-agents (separate 200K token budget)

**Skills:**
✅ What they are (custom commands)
✅ Structure (SKILL.md in .claude/skills/)
✅ How to create and use

**Hooks:**
✅ 3 types (PreToolUse, PostToolUse, UserPromptSubmit)
✅ When they trigger
✅ Common use cases

**Permission Modes:**
✅ Default (ask everything)
✅ AcceptEdits (auto-approve edits)
✅ Plan (read-only)
✅ How to switch (Shift + Tab)

**Subagents:**
✅ Separate 200K token budget
✅ When Claude spawns them
✅ Benefits (isolation, specialization)

**Memory:**
✅ 4 types (user, feedback, project, reference)
✅ When to save each type
✅ Structure (name, description, type, content)

---

### Common Exam Question Patterns

**Pattern 1: "Best approach for this scenario?"**
- Network error → Retry with exponential backoff
- Service keeps failing → Circuit breaker
- Must show something → Graceful fallback

**Pattern 2: "Which orchestration pattern?"**
- Tasks depend on each other → Sequential
- Independent tasks → Parallel
- Complex workflow with specialization → Hierarchical

**Pattern 3: "How to manage context?"**
- Long conversation → Compression
- Large codebase → Selective context
- Research task → Sub-agent

**Pattern 4: "What permission mode?"**
- Research only → Plan mode
- Trust file edits → AcceptEdits
- Maximum control → Default

**Pattern 5: "What memory type?"**
- About user → User memory
- Correction from user → Feedback memory
- Project deadline → Project memory
- External system → Reference memory

---

## Quick Self-Test

Can you answer these?

1. What's the difference between retry and circuit breaker?
2. Name the 3 orchestration patterns?
3. When should you use Read tool vs cat command?
4. What are the 4 memory types?
5. Name the 3 permission modes?
6. What's the benefit of subagents?
7. Name the 3 hook types?
8. What's exponential backoff?
9. When does circuit breaker go from OPEN to HALF-OPEN?
10. What's the difference between Sequential and Parallel orchestration?

If you can answer all 10, you understand Day 1! ✅

---

**Combined with Day 2, you've covered 85% of the exam!** 🎉

**Next:** Day 3 - Optimization & Review (15%)

Good luck! 🚀
