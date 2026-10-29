# Tool Boundaries - What Each Tool Can/Cannot Do

## The Problem: Using Wrong Tool

### ❌ WRONG: Using Bash for File Operations

```python
# BAD: Agent uses bash to edit file
def bad_agent_edit_file():
    bash_command = "sed -i 's/old_text/new_text/' file.txt"
    run_bash(bash_command)
```

**Why wrong:**
- Hard to review changes
- Unsafe (can damage files)
- Not cross-platform
- Claude Code has dedicated tools!

---

### ✅ CORRECT: Using Edit Tool

```python
# GOOD: Agent uses Edit tool
def good_agent_edit_file():
    edit_file(
        path="file.txt",
        old_string="old_text",
        new_string="new_text"
    )
```

**Why correct:**
- Safe and reviewable
- Cross-platform
- Shows exact changes
- Proper tool for the job!

---

## Tool Boundaries Reference

### 1. Read Tool

**Purpose:** Read file contents

**CAN:**
- ✅ Read any file
- ✅ Read specific line ranges
- ✅ Read images/PDFs

**CANNOT:**
- ❌ Modify files
- ❌ Create files
- ❌ Delete files

**Example:**
```python
# ✅ GOOD
content = read_file("config.json")

# ❌ BAD - use Edit instead
# Can't modify while reading
```

---

### 2. Edit Tool

**Purpose:** Modify existing files

**CAN:**
- ✅ Replace text in existing files
- ✅ Update specific sections
- ✅ Make precise changes

**CANNOT:**
- ❌ Create new files (use Write)
- ❌ Delete files
- ❌ Read without modifying (use Read)

**Example:**
```python
# ✅ GOOD
edit_file(
    path="app.py",
    old_string="DEBUG = False",
    new_string="DEBUG = True"
)

# ❌ BAD - file doesn't exist yet
# edit_file("new_file.py", ...) # Error!
```

---

### 3. Write Tool

**Purpose:** Create new files

**CAN:**
- ✅ Create new files
- ✅ Write complete content
- ✅ Overwrite existing files (if needed)

**CANNOT:**
- ❌ Make small edits (use Edit)
- ❌ Append to files efficiently

**Example:**
```python
# ✅ GOOD - Creating new file
write_file(
    path="new_script.py",
    content="print('Hello')"
)

# ❌ BAD - Use Edit for existing files
# write_file("existing.py", ...) # Overwrites everything!
```

---

### 4. Bash Tool

**Purpose:** Run system commands

**CAN:**
- ✅ Run tests
- ✅ Install packages
- ✅ Git commands
- ✅ Start servers

**SHOULD NOT:**
- ❌ Read files (use Read)
- ❌ Edit files (use Edit)
- ❌ Create files (use Write)
- ❌ Search code (use Grep)

**Example:**
```python
# ✅ GOOD
bash("npm test")
bash("git status")
bash("python script.py")

# ❌ BAD - use Read tool
# bash("cat file.txt")

# ❌ BAD - use Edit tool
# bash("sed -i 's/old/new/' file.txt")

# ❌ BAD - use Grep tool
# bash("grep 'pattern' *.py")
```

---

### 5. Glob Tool

**Purpose:** Find files by pattern

**CAN:**
- ✅ Search for files by name
- ✅ Use wildcards (*.py, src/**/test_*.js)
- ✅ List matching files

**CANNOT:**
- ❌ Search file contents (use Grep)
- ❌ Read files (use Read)

**Example:**
```python
# ✅ GOOD
files = glob("**/*.py")
test_files = glob("tests/test_*.py")

# ❌ BAD - use Grep for content search
# glob("files containing 'TODO'")  # Wrong tool!
```

---

### 6. Grep Tool

**Purpose:** Search file contents

**CAN:**
- ✅ Search text in files
- ✅ Use regex patterns
- ✅ Filter by file type

**CANNOT:**
- ❌ Find files by name (use Glob)
- ❌ Modify files (use Edit)

**Example:**
```python
# ✅ GOOD
grep("def main", "*.py")
grep("TODO", glob="src/**")

# ❌ BAD - use Glob for filenames
# grep("test_*.py")  # This searches FOR that text, not filenames!
```

---

## Common Exam Scenarios

### Scenario 1: Need to update API key in config file

**Question:** Which tool?

**A)** Bash: `sed -i 's/old_key/new_key/' config.json` ❌
**B)** Edit: Replace old_key with new_key ✅
**C)** Write: Overwrite entire file ❌

**Answer: B** - Edit tool for precise changes

---

### Scenario 2: Need to find all Python files in project

**Question:** Which tool?

**A)** Bash: `find . -name "*.py"` ❌
**B)** Grep: Search for ".py" ❌
**C)** Glob: `**/*.py` ✅

**Answer: C** - Glob tool for file patterns

---

### Scenario 3: Need to find files containing "TODO" comments

**Question:** Which tool?

**A)** Glob: `**/*TODO*` ❌ (searches filenames)
**B)** Grep: `TODO` in all files ✅
**C)** Bash: `grep -r "TODO"` ❌ (use dedicated tool)

**Answer: B** - Grep searches file contents

---

### Scenario 4: Need to run tests

**Question:** Which tool?

**A)** Bash: `npm test` ✅
**B)** Edit: Modify test files ❌
**C)** Read: Read test results ❌

**Answer: A** - Bash for running commands

---

## Why Tool Boundaries Exist

### 1. Safety
- Dedicated tools are safer
- Changes are reviewable
- Harder to make mistakes

### 2. Clarity
- Clear what each tool does
- Easy to understand agent actions
- Better permission control

### 3. Cross-Platform
- Dedicated tools work everywhere
- Bash commands vary by OS
- Consistent behavior

### 4. Permission Control
- User can allow/deny specific tools
- "Allow edits but not commands"
- Fine-grained control

---

## Best Practices

1. **Always use the right tool for the job**
   - Don't use Bash when Read/Edit/Write exist
   - Don't use Grep for finding filenames

2. **Read before Edit**
   - Always read a file before editing
   - Understand context before changes

3. **Prefer dedicated tools over Bash**
   - Read/Edit/Write > cat/sed/echo
   - Grep/Glob > grep/find commands

4. **Use Bash for what it's meant for**
   - Running tests
   - Package management
   - Git operations
   - Starting services

---

## Quiz Yourself

For each task, which tool should you use?

1. Change one line in existing file → **Edit**
2. Create a new Python script → **Write**
3. Find all JavaScript files → **Glob**
4. Search for "FIXME" in code → **Grep**
5. Run the test suite → **Bash**
6. View contents of README → **Read**

---

## Remember

**Tool boundaries keep agents safe, predictable, and effective!**

Using the right tool = following best practices = passing the exam! 🎯
