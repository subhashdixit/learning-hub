# CCA Practice Exam - 60 Questions

**Time Limit:** 120 minutes (2 min/question)
**Passing Score:** 70% (42/60 correct)

**Domain Breakdown:**
- Domain 1 (Agentic Architecture): 16 questions (27%)
- Domain 2 (Claude Code): 12 questions (20%)
- Domain 3 (Prompting): 12 questions (20%)
- Domain 4 (Tools/MCP): 11 questions (18%)
- Domain 5 (Memory/Tokens): 9 questions (15%)

---

## DOMAIN 5: MEMORY & TOKEN OPTIMIZATION (Questions 1-9)

### Question 1
User says: "I'm a senior backend engineer with 10 years Python experience."

What type of memory should this be saved as?

A) FEEDBACK memory with Why and How to apply
B) USER memory describing role and expertise
C) PROJECT memory about current work
D) REFERENCE memory for external resources

<details>
<summary>Answer & Explanation</summary>

**Answer: B) USER memory describing role and expertise**

**Explanation:** This is USER memory - describes who the user is (role, expertise level). No Why/How needed for user memories. USER memories help tailor responses to the user's level.
</details>

---

### Question 2
User says: "Don't use mocks for database tests - we got burned last quarter."

What type of memory?

A) USER memory
B) FEEDBACK memory with Why and How to apply
C) PROJECT memory
D) This should NOT be saved as memory

<details>
<summary>Answer & Explanation</summary>

**Answer: B) FEEDBACK memory with Why and How to apply**

**Explanation:** FEEDBACK memory - guidance on what to do/avoid. MUST include **Why:** (past incident where mocks failed) and **How to apply:** (use real database for integration tests).
</details>

---

### Question 3
What is the default line limit when using the Read tool without specifying a limit parameter?

A) 500 lines
B) 1000 lines
C) 2000 lines
D) No limit - reads entire file

<details>
<summary>Answer & Explanation</summary>

**Answer: C) 2000 lines**

**Explanation:** Read tool defaults to 2000 lines (~40K tokens) if no limit specified. This is critical to know for token optimization - you can waste 40K tokens on large files if you don't use limit parameter.
</details>

---

### Question 4
You need to read the LAST 100 lines of a 10,000-line log file. Which Read parameters?

A) `Read(file_path='log.txt', limit=100)`
B) `Read(file_path='log.txt', offset=9900, limit=100)`
C) `Read(file_path='log.txt', offset=10000, limit=100)`
D) `Read(file_path='log.txt', offset=-100)`

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Read(file_path='log.txt', offset=9900, limit=100)**

**Explanation:** offset=9900 starts at line 9900 (0-indexed), limit=100 reads 100 lines = lines 9900-10000 (the end). This is the most token-efficient way to read recent log entries.
</details>

---

### Question 5
Which Grep output_mode is most token-efficient for finding which files contain a pattern?

A) `output_mode='content'`
B) `output_mode='count'`
C) `output_mode='files_with_matches'`
D) All modes use the same tokens

<details>
<summary>Answer & Explanation</summary>

**Answer: C) output_mode='files_with_matches'**

**Explanation:** files_with_matches returns only file paths (~10 tokens/file) vs content (~30 tokens/line). Most efficient for finding which files match. Use this first, then Read specific files.
</details>

---

### Question 6
User explains: "The auth.py module uses JWT tokens in the validate() function."

Should this be saved as memory?

A) Yes, as USER memory
B) Yes, as PROJECT memory
C) Yes, as REFERENCE memory
D) No, this is a code pattern - read the file instead

<details>
<summary>Answer & Explanation</summary>

**Answer: D) No, this is a code pattern - read the file instead**

**Explanation:** Code patterns should NOT be saved in memory. They can be derived by reading files. Memory is for cross-session context that can't be derived from code, not for documenting implementation details.
</details>

---

### Question 7
A memory says "Use the refresh_token() function in auth.py." What should you do BEFORE using it?

A) Trust the memory and use it immediately
B) Verify with Grep/Read that the function still exists
C) Ask the user if it's still valid
D) Delete the memory and start fresh

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Verify with Grep/Read that the function still exists**

**Explanation:** ALWAYS verify memory before using. Memory can become stale (functions renamed/deleted/refactored). Grep for the function first. Trust current codebase state over memory.
</details>

---

### Question 8
What's the default head_limit for Grep tool?

A) 50
B) 100
C) 250
D) 500

<details>
<summary>Answer & Explanation</summary>

**Answer: C) 250**

**Explanation:** Grep default head_limit is 250. For content mode, this can be 7,500 tokens (250 × 30). Always set head_limit explicitly for content mode to control token usage.
</details>

---

### Question 9
When should you use the Agent tool with subagent_type='Explore' instead of direct Grep/Read?

A) For simple, targeted searches (1-2 operations)
B) For reading a single specific file
C) For broad exploration requiring multiple operations
D) Never - always use direct tools

<details>
<summary>Answer & Explanation</summary>

**Answer: C) For broad exploration requiring multiple operations**

**Explanation:** Agent tool isolates heavy exploration in separate context, returns only summary (~500 tokens). Use for broad searches, >3 operations, unfamiliar codebases. Keeps main context clean.
</details>

---

## DOMAIN 1: AGENTIC ARCHITECTURE & ORCHESTRATION (Questions 10-25)

### Question 10
What is the primary purpose of a reflection loop in an agent system?

A) To retry failed operations
B) To evaluate and improve agent's own outputs
C) To run multiple agents in parallel
D) To handle user interruptions

<details>
<summary>Answer & Explanation</summary>

**Answer: B) To evaluate and improve agent's own outputs**

**Explanation:** Reflection loops let agents evaluate their own work and improve it before returning to user. Like self-review: agent generates output, critiques it, refines it.
</details>

---

### Question 11
In exponential backoff retry logic, what typically happens after each failed attempt?

A) Wait time stays constant
B) Wait time increases exponentially (2x, 4x, 8x...)
C) Wait time decreases
D) Retry immediately without waiting

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Wait time increases exponentially (2x, 4x, 8x...)**

**Explanation:** Exponential backoff: wait 1s, then 2s, then 4s, then 8s... Prevents overwhelming failing services. Gives service time to recover.
</details>

---

### Question 12
What is a hierarchical agent pattern?

A) All agents run in parallel at same level
B) Orchestrator agent delegates to specialized sub-agents
C) Single agent handles all tasks sequentially
D) Agents retry failed tasks indefinitely

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Orchestrator agent delegates to specialized sub-agents**

**Explanation:** Hierarchical: orchestrator (manager) coordinates specialized agents (workers). Like company structure - CEO delegates to department heads.
</details>

---

### Question 13
What should an agent do when max_iterations is reached without success?

A) Keep trying indefinitely
B) Return partial results or failure status gracefully
C) Crash with an error
D) Restart from the beginning

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Return partial results or failure status gracefully**

**Explanation:** Graceful failure: return what was accomplished + clear status. Prevents infinite loops. Better to fail gracefully than run forever.
</details>

---

### Question 14
Which error type should typically trigger a retry?

A) Invalid API key (authentication error)
B) Network timeout or rate limit
C) Invalid function parameters
D) File not found

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Network timeout or rate limit**

**Explanation:** Retry transient failures (network issues, rate limits, temporary unavailability). Don't retry permanent failures (bad auth, invalid params, missing resources).
</details>

---

### Question 15
In a tool calling loop, when should you break out of the loop?

A) After exactly 5 iterations
B) When model returns text_content (no more tool calls)
C) After first tool call succeeds
D) Never - always run fixed iterations

<details>
<summary>Answer & Explanation</summary>

**Answer: B) When model returns text_content (no more tool calls)**

**Explanation:** Break when model stops calling tools (returns final text response). Indicates task is complete. Don't force fixed iterations.
</details>

---

### Question 16
What is the main benefit of parallel agent execution?

A) Easier to debug
B) Reduced total execution time
C) Uses less memory
D) Simpler code

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Reduced total execution time**

**Explanation:** Parallel execution: independent tasks run simultaneously. If tasks A and B each take 10s sequentially = 20s total. In parallel = 10s total.
</details>

---

### Question 17
What should you include in agent error handling?

A) Only log the error
B) Context about what failed and why
C) Ignore the error
D) Retry indefinitely

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Context about what failed and why**

**Explanation:** Error context helps debugging: what operation, what input, what error occurred, at what step. Makes failures actionable.
</details>

---

### Question 18
What is agent state persistence?

A) Agents never save state
B) Saving agent progress for resume after failure
C) Running agents in parallel
D) Agent memory system

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Saving agent progress for resume after failure**

**Explanation:** State persistence: save progress periodically so agent can resume if interrupted or fails. Like video game checkpoints.
</details>

---

### Question 19
When is sequential agent execution preferred over parallel?

A) Always use parallel
B) When tasks are independent
C) When later tasks depend on earlier results
D) When tasks are simple

<details>
<summary>Answer & Explanation</summary>

**Answer: C) When later tasks depend on earlier results**

**Explanation:** Sequential: when task B needs output from task A. Must wait for dependencies. Can't parallelize dependent tasks.
</details>

---

### Question 20
What is a common cause of infinite loops in agent systems?

A) Too many tools
B) No max_iterations limit or improper break condition
C) Using retries
D) Parallel execution

<details>
<summary>Answer & Explanation</summary>

**Answer: B) No max_iterations limit or improper break condition**

**Explanation:** Infinite loops: no max_iterations + no break condition = runs forever. Always have both max limit and proper exit conditions.
</details>

---

### Question 21
What is the purpose of a router agent?

A) Execute all tasks
B) Route requests to appropriate specialized agents
C) Store agent state
D) Handle retries

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Route requests to appropriate specialized agents**

**Explanation:** Router: analyzes request, sends to right specialized agent. Like customer service routing to appropriate department.
</details>

---

### Question 22
How should agents handle partial success?

A) Treat as complete failure
B) Return what succeeded + status of what failed
C) Retry everything
D) Ignore the failure

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Return what succeeded + status of what failed**

**Explanation:** Partial success: return completed work + clear status of incomplete parts. Better than all-or-nothing. User gets some value.
</details>

---

### Question 23
What is idempotency in agent operations?

A) Running faster each time
B) Same operation repeated gives same result (safe to retry)
C) Never repeating operations
D) Random results

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Same operation repeated gives same result (safe to retry)**

**Explanation:** Idempotent: operation can be retried safely without unintended side effects. Like HTTP GET - reading same resource multiple times is safe.
</details>

---

### Question 24
When should you use jitter in retry logic?

A) Never
B) To prevent thundering herd problem (many retries at once)
C) To make retries slower
D) Only for read operations

<details>
<summary>Answer & Explanation</summary>

**Answer: B) To prevent thundering herd problem (many retries at once)**

**Explanation:** Jitter: random variation in retry timing. Prevents all clients retrying simultaneously and overwhelming service. Like adding randomness to prevent traffic jams.
</details>

---

### Question 25
What is circuit breaker pattern?

A) Never retry failures
B) Stop trying after consecutive failures to prevent cascade
C) Retry immediately always
D) Parallel execution

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Stop trying after consecutive failures to prevent cascade**

**Explanation:** Circuit breaker: if service fails N times consecutively, stop trying temporarily (circuit "opens"). Prevents overwhelming broken service and cascading failures.
</details>

---

## DOMAIN 2: CLAUDE CODE CONFIGURATION & WORKFLOWS (Questions 26-37)

### Question 26
Which tool should you use to read a file's contents?

A) Bash with cat
B) Read tool
C) Grep tool
D) Write tool

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Read tool**

**Explanation:** Use Read tool for reading files. Bash is reserved for system commands. Using dedicated tools provides better user experience and permissions.
</details>

---

### Question 27
When should you use Edit tool vs Write tool?

A) Always use Write
B) Edit for modifying existing, Write for new files
C) Always use Edit
D) They're the same

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Edit for modifying existing, Write for new files**

**Explanation:** Edit: modify existing files (sends only diff, efficient). Write: create new files (sends full content). Edit will fail if file doesn't exist.
</details>

---

### Question 28
What is a Claude Code skill?

A) A built-in command
B) User-defined reusable prompt workflow
C) A debugging tool
D) A type of agent

<details>
<summary>Answer & Explanation</summary>

**Answer: B) User-defined reusable prompt workflow**

**Explanation:** Skill: custom prompt workflow user can invoke with /skill-name. Reusable automation for common tasks.
</details>

---

### Question 29
What is a hook in Claude Code?

A) A CLI command
B) Shell command that runs on specific events
C) A type of memory
D) An agent loop

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Shell command that runs on specific events**

**Explanation:** Hook: shell command triggered by events (UserPromptSubmit, ToolResult, etc). Enables automation like running tests after code changes.
</details>

---

### Question 30
When should you use Glob tool?

A) To search file contents
B) To find files by name pattern
C) To read files
D) To execute commands

<details>
<summary>Answer & Explanation</summary>

**Answer: B) To find files by name pattern**

**Explanation:** Glob: find files by pattern (*.py, **/*.ts, src/**/*.jsx). Fast pattern matching on filenames, not contents.
</details>

---

### Question 31
What does Grep tool do?

A) Creates files
B) Searches file contents for patterns
C) Deletes files
D) Finds files by name

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Searches file contents for patterns**

**Explanation:** Grep: search file CONTENTS for regex patterns. Returns matches, counts, or file paths depending on output_mode.
</details>

---

### Question 32
Which tool for executing shell commands?

A) Read
B) Write
C) Bash
D) Edit

<details>
<summary>Answer & Explanation</summary>

**Answer: C) Bash**

**Explanation:** Bash tool: execute shell commands (git, npm, pytest, etc). Only use for system commands, not file operations.
</details>

---

### Question 33
What is a subagent in Claude Code?

A) A background process
B) Specialized agent spawned by main agent
C) A hook
D) A skill

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Specialized agent spawned by main agent**

**Explanation:** Subagent: specialized agent (Explore, Plan, etc) with own tools/context. Spawned via Agent tool for specific subtasks.
</details>

---

### Question 34
When should you use Agent tool with subagent_type='Explore'?

A) Reading single file
B) Simple grep
C) Broad codebase exploration
D) Writing files

<details>
<summary>Answer & Explanation</summary>

**Answer: C) Broad codebase exploration**

**Explanation:** Explore agent: broad codebase search, multiple operations, unfamiliar territory. Isolates heavy exploration in separate context.
</details>

---

### Question 35
What's the purpose of Plan mode?

A) Execute code
B) Design implementation approach before coding
C) Debug errors
D) Create backups

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Design implementation approach before coding**

**Explanation:** Plan mode: design approach, get user approval before implementing. Prevents wasted work on wrong approach. "Measure twice, cut once."
</details>

---

### Question 36
Can Edit tool create new files?

A) Yes, always
B) No, only modifies existing files
C) Only .txt files
D) Only .md files

<details>
<summary>Answer & Explanation</summary>

**Answer: B) No, only modifies existing files**

**Explanation:** Edit: only for existing files. Will error if file doesn't exist. Use Write for new files.
</details>

---

### Question 37
What happens when you use Grep with no output_mode specified?

A) Returns error
B) Defaults to 'files_with_matches'
C) Defaults to 'content'
D) Returns nothing

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Defaults to 'files_with_matches'**

**Explanation:** Grep defaults to files_with_matches mode (just file paths). Most token-efficient default.
</details>

---

## DOMAIN 3: PROMPT ENGINEERING & STRUCTURED OUTPUT (Questions 38-49)

### Question 38
What is chain-of-thought prompting?

A) Multiple prompts in sequence
B) Asking model to show reasoning step-by-step
C) Using multiple tools
D) Parallel execution

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Asking model to show reasoning step-by-step**

**Explanation:** Chain-of-thought: model shows intermediate reasoning steps. "Let's think step by step..." Improves accuracy on complex problems.
</details>

---

### Question 39
What are few-shot examples in prompting?

A) Showing the model example inputs and outputs
B) Using few tokens
C) Short prompts
D) Multiple agents

<details>
<summary>Answer & Explanation</summary>

**Answer: A) Showing the model example inputs and outputs**

**Explanation:** Few-shot: provide examples of desired behavior in prompt. Model learns pattern from examples. Better than just describing what you want.
</details>

---

### Question 40
What is the purpose of XML tags in prompts?

A) Make prompts longer
B) Structure and organize different sections clearly
C) Required for all prompts
D) Only for HTML generation

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Structure and organize different sections clearly**

**Explanation:** XML tags: structure prompts clearly with <input>, <examples>, <instructions> sections. Helps Claude parse different parts of prompt.
</details>

---

### Question 41
What is structured output?

A) Any output
B) Output in specific format like JSON or TypeScript types
C) Long output
D) Multiple responses

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Output in specific format like JSON or TypeScript types**

**Explanation:** Structured output: request specific format (JSON schema, TypeScript types). Easier to parse programmatically. Reduces parsing errors.
</details>

---

### Question 42
What's the benefit of asking for JSON output?

A) Longer responses
B) Easier to parse programmatically
C) More tokens
D) Slower responses

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Easier to parse programmatically**

**Explanation:** JSON: structured, easy to parse, type-safe. vs prose that needs complex text parsing. Direct integration with code.
</details>

---

### Question 43
What is prompt caching?

A) Saving prompts to disk
B) Reusing unchanged prompt parts across requests
C) Deleting prompts
D) Writing prompts

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Reusing unchanged prompt parts across requests**

**Explanation:** Prompt caching: Claude reuses unchanged context (large files, docs) across requests. Reduces cost for repeated context. Pay once, reuse multiple times.
</details>

---

### Question 44
What is system prompt vs user prompt?

A) They're the same
B) System sets behavior/role, user is the request
C) Only system is used
D) Only user is used

<details>
<summary>Answer & Explanation</summary>

**Answer: B) System sets behavior/role, user is the request**

**Explanation:** System: sets context/role/instructions for entire conversation. User: the actual request/question in each turn.
</details>

---

### Question 45
What's prefill in prompting?

A) Extra context
B) Starting Claude's response with specific text
C) Multiple prompts
D) System message

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Starting Claude's response with specific text**

**Explanation:** Prefill: start Claude's response for it. Guides format/tone. "Put words in Claude's mouth" to control output start.
</details>

---

### Question 46
How can you make Claude respond in a specific format?

A) Hope it guesses
B) Show example format or use structured output
C) Use more tokens
D) Multiple prompts

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Show example format or use structured output**

**Explanation:** Format control: show example in prompt or use structured output (JSON schema, TypeScript types). Both work well.
</details>

---

### Question 47
What is role prompting?

A) Multiple users
B) Giving Claude a specific role/persona
C) System commands
D) Memory types

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Giving Claude a specific role/persona**

**Explanation:** Role prompting: "You are an expert Python developer..." Sets expertise level and perspective. Influences response style and depth.
</details>

---

### Question 48
Should prompts be verbose or concise?

A) Always verbose with details
B) Concise but clear with necessary context
C) Single words only
D) Doesn't matter

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Concise but clear with necessary context**

**Explanation:** Concise + clear: include needed context, skip fluff. Saves tokens, clearer intent. Quality over quantity.
</details>

---

### Question 49
What's the benefit of breaking complex tasks in prompts?

A) Uses more tokens
B) Clearer sub-steps, easier to follow and debug
C) Slower
D) No benefit

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Clearer sub-steps, easier to follow and debug**

**Explanation:** Break complex into steps: clearer execution, easier debugging, better results. "Divide and conquer."
</details>

---

## DOMAIN 4: TOOL DESIGN & MCP INTEGRATION (Questions 50-60)

### Question 50
What should a well-designed tool include?

A) No description
B) Clear description, input schema, and error handling
C) Only input parameters
D) No parameters

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Clear description, input schema, and error handling**

**Explanation:** Good tool: description (what it does), input_schema (types/validation), error handling (clear errors), return format. Makes tool usable and reliable.
</details>

---

### Question 51
What is input validation in tool design?

A) Skipping checks
B) Checking parameters are correct type/format before use
C) Only for strings
D) Optional

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Checking parameters are correct type/format before use**

**Explanation:** Input validation: verify params before execution (type, range, format). Prevents errors, provides better error messages, improves UX.
</details>

---

### Question 52
What does MCP stand for?

A) Model Control Protocol
B) Model Context Protocol
C) Memory Context Protocol
D) Model Code Protocol

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Model Context Protocol**

**Explanation:** MCP = Model Context Protocol. Standard for connecting AI systems to data sources and tools. Enables interoperability.
</details>

---

### Question 53
What is an MCP server?

A) Web server
B) Service that exposes tools/resources via MCP protocol
C) Database
D) Agent

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Service that exposes tools/resources via MCP protocol**

**Explanation:** MCP server: exposes tools/resources (files, APIs, databases) to AI via standard protocol. Like API gateway for AI.
</details>

---

### Question 54
What should tools return on error?

A) Nothing
B) Clear error message with context
C) Random data
D) Crash

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Clear error message with context**

**Explanation:** Error returns: clear message (what failed, why, possible fixes). Helps user/model understand and recover from errors.
</details>

---

### Question 55
Should tools have side effects?

A) Always
B) Clearly documented if yes, avoided when possible
C) Never document them
D) Random side effects OK

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Clearly documented if yes, avoided when possible**

**Explanation:** Side effects (writes files, calls API, modifies state): document clearly. User/model should know consequences before calling tool.
</details>

---

### Question 56
What's the benefit of type schemas in tools?

A) Slower execution
B) Validation, better errors, clear expectations
C) More code
D) No benefit

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Validation, better errors, clear expectations**

**Explanation:** Type schemas: automatic validation, clear contracts, better error messages, self-documenting. Prevents invalid inputs.
</details>

---

### Question 57
Should tools do one thing or many things?

A) One focused responsibility (single responsibility)
B) Everything in one tool
C) Random mix
D) Doesn't matter

<details>
<summary>Answer & Explanation</summary>

**Answer: A) One focused responsibility (single responsibility)**

**Explanation:** Single responsibility: one tool, one job. Easier to use, test, maintain, understand. Compose tools for complex tasks.
</details>

---

### Question 58
What is tool discovery?

A) Finding bugs
B) System finding available tools and their capabilities
C) Deleting tools
D) Tool testing

<details>
<summary>Answer & Explanation</summary>

**Answer: B) System finding available tools and their capabilities**

**Explanation:** Tool discovery: system learns what tools exist, their parameters, descriptions. Enables dynamic tool selection and use.
</details>

---

### Question 59
How should tool descriptions be written?

A) Very technical jargon
B) Clear, concise, with example use case
C) One word
D) No description needed

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Clear, concise, with example use case**

**Explanation:** Tool descriptions: clear purpose, when to use, example scenario. Helps model choose right tool for task. Avoid jargon.
</details>

---

### Question 60
What is a resource in MCP?

A) Memory
B) Data that can be accessed (files, APIs, databases)
C) CPU usage
D) Token count

<details>
<summary>Answer & Explanation</summary>

**Answer: B) Data that can be accessed (files, APIs, databases)**

**Explanation:** MCP resource: accessible data sources (files, databases, APIs, web services). Tools operate on resources to provide functionality.
</details>

---

## 📊 ANSWER KEY

### Domain 5 (Memory & Tokens)
1. B | 2. B | 3. C | 4. B | 5. C | 6. D | 7. B | 8. C | 9. C

### Domain 1 (Agentic Architecture)
10. B | 11. B | 12. B | 13. B | 14. B | 15. B | 16. B | 17. B | 18. B | 19. C | 20. B | 21. B | 22. B | 23. B | 24. B | 25. B

### Domain 2 (Claude Code)
26. B | 27. B | 28. B | 29. B | 30. B | 31. B | 32. C | 33. B | 34. C | 35. B | 36. B | 37. B

### Domain 3 (Prompting)
38. B | 39. A | 40. B | 41. B | 42. B | 43. B | 44. B | 45. B | 46. B | 47. B | 48. B | 49. B

### Domain 4 (Tools & MCP)
50. B | 51. B | 52. B | 53. B | 54. B | 55. B | 56. B | 57. A | 58. B | 59. B | 60. B

---

## 🎯 Scoring Guide

- **90-100% (54-60):** Excellent! Ready for exam
- **80-89% (48-53):** Very good! Light review needed
- **70-79% (42-47):** Good! Passing but review weak areas
- **60-69% (36-41):** Fair - More study needed
- **< 60% (< 36):** Need significant review

## 💡 Study Tips

1. **Time yourself:** 120 minutes total
2. **First pass:** Answer all you know confidently (60 min)
3. **Second pass:** Tackle uncertain questions (45 min)
4. **Final pass:** Review flagged questions (15 min)
5. **After exam:** Review ALL explanations, not just wrong answers

**Good luck! 🚀**
