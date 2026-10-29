# Token Optimization Exercises

**Exam Weight:** ~7-8% of total exam

## Key Concepts to Master

### 1. Token Counting Basics
- How tokens are counted (Claude tokenizer)
- Code vs text token efficiency
- Whitespace and formatting impact

### 2. Context Window Management
- Input token limits
- Output token limits
- Context compression strategies

### 3. Optimization Techniques
- Efficient prompt design
- Tool output optimization
- File reading strategies (offset/limit)
- Structured output benefits

### 4. Cost vs Performance Trade-offs
- When to optimize vs when not to
- Model selection (Opus vs Sonnet vs Haiku)
- Caching strategies

---

## Exercise Structure

1. **Exercise 1:** Token Counting Fundamentals
2. **Exercise 2:** Context Window Strategies
3. **Exercise 3:** Efficient File Reading
4. **Exercise 4:** Tool Output Optimization
5. **Exercise 5:** Cost-Performance Analysis

---

## Running the Exercises

```bash
cd day3/optimization/tokens

# Run each exercise
python exercise1_token_counting.py
python exercise2_context_window.py
python exercise3_file_reading.py
python exercise4_tool_output.py
python exercise5_cost_analysis.py
```

---

## Learning Objectives

After completing these exercises, you should be able to:
- ✅ Calculate token usage accurately
- ✅ Choose optimal file reading strategies
- ✅ Design token-efficient prompts
- ✅ Balance token usage with performance
- ✅ Apply caching strategically

---

## Exam Tips

- **Read tool supports offset/limit** - use for large files
- **Grep has head_limit parameter** - avoid massive results
- **Structured output is token-efficient** - less parsing needed
- **Model selection matters** - Haiku for simple, Opus for complex
- **Caching reduces costs** - for repeated context

---

## Token Budget Guidelines

| Operation | Typical Tokens | Optimization Strategy |
|-----------|----------------|----------------------|
| Small prompt | 100-500 | No optimization needed |
| Medium task | 2K-10K | Use Read offset/limit |
| Large codebase search | 10K-50K | Use Grep with head_limit |
| Full file analysis | 50K+ | Process in chunks |

---

## Critical for Exam

- Know when to use `offset` and `limit` with Read tool
- Understand `head_limit` for Grep tool
- Recognize when to use Agent tool for exploration vs direct tools
- Understand prompt caching for repeated context
