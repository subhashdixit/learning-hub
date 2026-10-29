# Memory Management Exercises

**Exam Weight:** ~7-8% of total exam

## Key Concepts to Master

### 1. Claude Code Memory System
- User memories (profile, preferences)
- Feedback memories (guidance from corrections)
- Project memories (ongoing work context)
- Reference memories (external resources)

### 2. Memory Lifecycle
- When to save vs when to read
- Memory freshness and staleness
- Verification before using memory
- Update vs create new memory

### 3. Memory Best Practices
- Semantic organization
- Avoiding duplication
- Memory indexing (MEMORY.md)
- Frontmatter structure

---

## Exercise Structure

1. **Exercise 1:** Memory CRUD Operations
2. **Exercise 2:** Memory Types Classification
3. **Exercise 3:** Memory Staleness Detection
4. **Exercise 4:** Memory Index Management
5. **Exercise 5:** Real-world Memory Scenario

---

## Running the Exercises

```bash
cd day3/optimization/memory

# Run each exercise
python exercise1_memory_crud.py
python exercise2_memory_types.py
python exercise3_staleness_check.py
python exercise4_index_management.py
python exercise5_real_scenario.py
```

---

## Learning Objectives

After completing these exercises, you should be able to:
- ✅ Identify when to save different memory types
- ✅ Structure memory files correctly with frontmatter
- ✅ Detect and handle stale memories
- ✅ Manage the MEMORY.md index efficiently
- ✅ Apply memory best practices in real scenarios

---

## Exam Tips

- **Memory is NOT for code patterns** - those are derived from reading files
- **Verify before using** - memories can become stale
- **Type matters** - user/feedback/project/reference have different use cases
- **Index first** - MEMORY.md is always loaded, individual files loaded on demand
- **Update > Duplicate** - check for existing memories before creating new ones
