"""
🎯 EXAMPLE 1: Simple Tool Design - Calculator

This shows the 4 parts EVERY tool needs:
1. Name
2. Description
3. Input Schema (parameters)
4. Function (the code)

Run: python3 01_SIMPLE_TOOL_EXAMPLE.py
"""

import json
from typing import Dict, Any

print("=" * 70)
print("TOOL DESIGN - SIMPLE CALCULATOR EXAMPLE")
print("=" * 70)

print("\n📚 TOOL HAS 4 PARTS:\n")
print("1. NAME - What it's called")
print("2. DESCRIPTION - What it does (Claude reads this!)")
print("3. INPUT SCHEMA - Parameters with types (JSON schema)")
print("4. FUNCTION - The actual Python code")

# ============================================================================
# PART 1 & 2 & 3: Name, Description, Input Schema
# ============================================================================

tool_definition = {
    "name": "calculator",                                    # ← PART 1: Name
    "description": "Perform basic arithmetic: add, subtract, multiply, divide",  # ← PART 2: Description
    "input_schema": {                                        # ← PART 3: Input Schema
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide"],
                "description": "Which math operation to perform"
            },
            "a": {
                "type": "number",
                "description": "First number"
            },
            "b": {
                "type": "number",
                "description": "Second number"
            }
        },
        "required": ["operation", "a", "b"]
    }
}

print("\n" + "=" * 70)
print("PARTS 1, 2, 3: TOOL DEFINITION (What Claude sees)")
print("=" * 70)
print(json.dumps(tool_definition, indent=2))

print("\n💡 EXPLANATION:")
print("   • name: 'calculator' - short, clear")
print("   • description: Claude reads this to decide when to use the tool")
print("   • input_schema: Same as JSON schemas from this morning!")
print("       - operation: enum with 4 choices")
print("       - a and b: numbers")
print("       - all 3 are required")

# ============================================================================
# PART 4: Function Implementation
# ============================================================================

def calculator(operation: str, a: float, b: float) -> Dict[str, Any]:
    """
    PART 4: The actual function that does the work
    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {"error": "Cannot divide by zero"}
        result = a / b
    else:
        return {"error": f"Unknown operation: {operation}"}

    return {"result": result}

print("\n" + "=" * 70)
print("PART 4: FUNCTION IMPLEMENTATION (The Python code)")
print("=" * 70)
print("""
def calculator(operation: str, a: float, b: float) -> Dict[str, Any]:
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {"error": "Cannot divide by zero"}
        result = a / b

    return {"result": result}
""")

print("💡 EXPLANATION:")
print("   • Takes 3 parameters: operation, a, b")
print("   • Does the math based on operation")
print("   • Returns result as a dictionary")
print("   • Returns error if divide by zero (not an exception!)")

# ============================================================================
# TEST THE TOOL
# ============================================================================

print("\n" + "=" * 70)
print("🧪 TESTING THE TOOL")
print("=" * 70)

test_cases = [
    {"operation": "add", "a": 10, "b": 5},
    {"operation": "multiply", "a": 7, "b": 3},
    {"operation": "divide", "a": 20, "b": 4},
    {"operation": "divide", "a": 10, "b": 0}  # Error case
]

for i, test in enumerate(test_cases, 1):
    result = calculator(**test)
    print(f"\nTest {i}:")
    print(f"  Input:  {test}")
    print(f"  Output: {result}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("📚 SUMMARY - THE 4 PARTS OF A TOOL")
print("=" * 70)
print("""
Every tool MUST have these 4 parts:

1. NAME
   - Short, descriptive
   - Use snake_case
   - Example: "calculator", "send_email", "search_files"

2. DESCRIPTION
   - Clear explanation of what it does
   - Claude READS this to decide when to use it!
   - Example: "Perform basic arithmetic operations"

3. INPUT SCHEMA
   - JSON schema defining parameters
   - Same structure we learned this morning!
   - Includes: types, descriptions, required fields, enums

4. FUNCTION
   - The actual Python code
   - Takes parameters, does work, returns result
   - Return structured data (dict), NOT exceptions!

✅ This calculator tool has all 4 parts!
""")

print("=" * 70)
print("✅ EXAMPLE 1 COMPLETE!")
print("=" * 70)
print("\nNext: Let's see more complex examples...")
print("But first, make sure you understand this simple one!")
