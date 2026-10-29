"""
🎯 EXAMPLE 3: Tool Design Best Practices

Learn what makes a GOOD tool vs a BAD tool.
Exam questions often ask: "What's wrong with this tool?"

Run: python3 03_BEST_PRACTICES.py
"""

import json

print("=" * 70)
print("TOOL DESIGN BEST PRACTICES")
print("=" * 70)
print("\nExam questions will show you tools and ask:")
print("  • 'What's wrong with this tool?'")
print("  • 'Which principle is violated?'")
print("  • 'How should this be improved?'")
print("\nLet's learn the principles!\n")

# ============================================================================
# PRINCIPLE 1: Single Responsibility
# ============================================================================

print("=" * 70)
print("PRINCIPLE 1: SINGLE RESPONSIBILITY")
print("=" * 70)
print("\nEach tool should do ONE thing well.\n")

print("❌ BAD EXAMPLE:")
print("-" * 70)
bad_tool = {
    "name": "file_operations",  # Too broad!
    "description": "Handle file operations",
    "input_schema": {
        "properties": {
            "action": {
                "enum": ["read", "write", "delete", "search", "copy", "move"]
            },
            "file_path": {"type": "string"},
            "content": {"type": "string"},
            "destination": {"type": "string"}
        }
    }
}
print(json.dumps(bad_tool, indent=2))
print("\n⚠️  PROBLEMS:")
print("   • Does too many things (read, write, delete, search, copy, move)")
print("   • Hard for Claude to know when to use it")
print("   • Some parameters only apply to some actions")
print("   • Confusing and error-prone")

print("\n✅ GOOD EXAMPLE:")
print("-" * 70)
print("Break into separate tools:")
print("   • read_file(file_path)")
print("   • write_file(file_path, content)")
print("   • delete_file(file_path)")
print("   • search_files(query)")
print("   • copy_file(source, destination)")
print("   • move_file(source, destination)")
print("\n✅ BENEFITS:")
print("   • Each tool has clear purpose")
print("   • Claude knows exactly when to use each one")
print("   • Parameters match the action")
print("   • Easy to understand and maintain")

# ============================================================================
# PRINCIPLE 2: Clear, Descriptive Names
# ============================================================================

print("\n\n" + "=" * 70)
print("PRINCIPLE 2: CLEAR, DESCRIPTIVE NAMES")
print("=" * 70)
print("\nUse verb + noun pattern, snake_case\n")

print("❌ BAD EXAMPLES:")
print("-" * 70)
bad_names = [
    ("do_thing", "Too vague - what thing?"),
    ("helper", "Not descriptive"),
    ("util", "What utility?"),
    ("process", "Process what?"),
    ("getData", "camelCase, not snake_case")
]
for name, reason in bad_names:
    print(f"   • '{name}' - {reason}")

print("\n✅ GOOD EXAMPLES:")
print("-" * 70)
good_names = [
    ("send_email", "Clear: sends an email"),
    ("calculate_tax", "Clear: calculates tax"),
    ("search_products", "Clear: searches products"),
    ("create_github_issue", "Clear: creates GitHub issue"),
    ("fetch_weather", "Clear: fetches weather data")
]
for name, reason in good_names:
    print(f"   • '{name}' - {reason}")

# ============================================================================
# PRINCIPLE 3: Detailed Descriptions
# ============================================================================

print("\n\n" + "=" * 70)
print("PRINCIPLE 3: DETAILED DESCRIPTIONS")
print("=" * 70)
print("\nClaude READS descriptions to decide when to use tools!\n")

print("❌ BAD DESCRIPTION:")
print("-" * 70)
print('"Gets data"')
print("\n⚠️  PROBLEMS:")
print("   • What data?")
print("   • From where?")
print("   • What fields are returned?")

print("\n✅ GOOD DESCRIPTION:")
print("-" * 70)
print('"Fetches user profile from PostgreSQL database by user_id.')
print('Returns: name, email, account creation date, and subscription tier."')
print("\n✅ BENEFITS:")
print("   • Clear what data (user profile)")
print("   • Clear where from (PostgreSQL)")
print("   • Clear input needed (user_id)")
print("   • Clear what's returned (name, email, etc.)")

# ============================================================================
# PRINCIPLE 4: Validate Inputs
# ============================================================================

print("\n\n" + "=" * 70)
print("PRINCIPLE 4: VALIDATE INPUTS")
print("=" * 70)
print("\nALWAYS validate before executing!\n")

print("❌ BAD CODE (No validation):")
print("-" * 70)
print("""
def delete_file(file_path):
    os.remove(file_path)  # Dangerous!
    return {"success": True}
""")
print("\n⚠️  PROBLEMS:")
print("   • No validation - could delete anything!")
print("   • What if file_path is '../../../etc/passwd'?")
print("   • What if file doesn't exist?")
print("   • Security risk!")

print("\n✅ GOOD CODE (With validation):")
print("-" * 70)
print("""
def delete_file(file_path):
    # 1. Validate path is safe
    if '..' in file_path:
        return {"success": False, "error": "Invalid path"}

    # 2. Check file exists
    if not os.path.exists(file_path):
        return {"success": False, "error": "File not found"}

    # 3. Check permissions
    if not has_permission(file_path):
        return {"success": False, "error": "Permission denied"}

    # 4. Now safe to delete
    os.remove(file_path)
    return {"success": True}
""")
print("\n✅ BENEFITS:")
print("   • Validates path is safe")
print("   • Checks file exists")
print("   • Checks permissions")
print("   • Returns clear errors")

# ============================================================================
# PRINCIPLE 5: Return Structured Data, Not Exceptions
# ============================================================================

print("\n\n" + "=" * 70)
print("PRINCIPLE 5: RETURN STRUCTURED DATA, NOT EXCEPTIONS")
print("=" * 70)
print("\nClaude can't catch Python exceptions!\n")

print("❌ BAD CODE (Throws exceptions):")
print("-" * 70)
print("""
def get_user(user_id):
    user = db.get(user_id)
    if not user:
        raise Exception("User not found")  # Claude can't catch this!
    return user
""")
print("\n⚠️  PROBLEMS:")
print("   • Exception crashes the system")
print("   • Claude can't understand the error")
print("   • User sees cryptic error message")

print("\n✅ GOOD CODE (Returns error objects):")
print("-" * 70)
print("""
def get_user(user_id):
    user = db.get(user_id)
    if not user:
        return {
            "success": False,
            "error": "User not found",
            "error_code": "USER_NOT_FOUND"
        }

    return {
        "success": True,
        "data": user
    }
""")
print("\n✅ BENEFITS:")
print("   • Claude can read the error")
print("   • Claude can explain to user")
print("   • Consistent format (success/error)")
print("   • error_code helps with handling")

# ============================================================================
# PRINCIPLE 6: Consistent Return Format
# ============================================================================

print("\n\n" + "=" * 70)
print("PRINCIPLE 6: CONSISTENT RETURN FORMAT")
print("=" * 70)
print("\nAlways use the same structure!\n")

print("✅ RECOMMENDED FORMAT:")
print("-" * 70)
print("""
SUCCESS:
{
    "success": true,
    "data": { ... actual data ... },
    "metadata": {
        "took_ms": 150,
        "cached": false
    }
}

ERROR:
{
    "success": false,
    "error": "Clear error message",
    "error_code": "ERROR_TYPE",
    "details": { ... optional details ... }
}
""")

print("✅ BENEFITS:")
print("   • Predictable structure")
print("   • Easy to check success/error")
print("   • Metadata provides context")
print("   • Works for all tools")

# ============================================================================
# PRINCIPLE 7: Use Enums for Fixed Choices
# ============================================================================

print("\n\n" + "=" * 70)
print("PRINCIPLE 7: USE ENUMS FOR FIXED CHOICES")
print("=" * 70)

print("\n❌ BAD:")
print("-" * 70)
print('"status": {"type": "string"}  # Any string allowed!')
print("\n⚠️  PROBLEM: User could pass invalid values:")
print("   • 'activ' (typo)")
print("   • 'Active' (wrong case)")
print("   • 'running' (not a valid status)")

print("\n✅ GOOD:")
print("-" * 70)
print('"status": {')
print('    "type": "string",')
print('    "enum": ["active", "inactive", "pending"]')
print('}')
print("\n✅ BENEFITS:")
print("   • Only valid values accepted")
print("   • Claude sees available options")
print("   • Prevents typos and errors")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n\n" + "=" * 70)
print("📚 BEST PRACTICES SUMMARY")
print("=" * 70)
print("""
✅ CHECKLIST FOR GOOD TOOL DESIGN:

1. ☑ Single Responsibility
   Each tool does ONE thing well

2. ☑ Clear Name
   Use verb + noun, snake_case (e.g., send_email)

3. ☑ Detailed Description
   Claude reads this to decide when to use the tool

4. ☑ Validate Inputs
   Check paths, permissions, existence before executing

5. ☑ Return Structured Data
   Use objects, not exceptions (Claude can't catch them)

6. ☑ Consistent Format
   Always return {"success": bool, "data/error": ...}

7. ☑ Use Enums
   For fixed choices (status, category, etc.)

8. ☑ Document Everything
   Every parameter needs a description

9. ☑ Security First
   Sanitize inputs, check permissions, validate paths

10. ☑ Test Edge Cases
    What if file doesn't exist? Division by zero? Empty input?


🎯 FOR THE EXAM:

Questions will show you tools with problems. You need to identify:
• Missing validations
• Vague descriptions
• Wrong types
• No error handling
• Too many responsibilities
• Missing enums
• Unclear names

Look for these RED FLAGS:
❌ "Gets data" (vague description)
❌ "file_operations" with 10 actions (too broad)
❌ raise Exception() (should return error object)
❌ No parameter descriptions
❌ status as string without enum
❌ No input validation
""")

print("\n" + "=" * 70)
print("✅ BEST PRACTICES COMPLETE!")
print("=" * 70)
print("\nNow you can identify good vs bad tools!")
