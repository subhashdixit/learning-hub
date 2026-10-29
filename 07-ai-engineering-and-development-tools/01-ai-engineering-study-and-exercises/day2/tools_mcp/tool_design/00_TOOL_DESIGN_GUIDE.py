"""
🎯 TOOL DESIGN - Complete Guide

Learn how to design custom tools for Claude.
This is 18% of the CCA exam!

WHAT ARE TOOLS?
- Tools let Claude TAKE ACTIONS (not just talk)
- Examples: search files, call APIs, run calculations, access databases

TOOL ANATOMY:
1. Name - what it's called
2. Description - what it does (Claude reads this!)
3. Parameters - inputs with types (JSON schema!)
4. Function - the actual code that runs

Run: python3 00_TOOL_DESIGN_GUIDE.py
"""

import json
from typing import Dict, Any, List


# ============================================================================
# EXAMPLE 1: Simple Tool Design
# ============================================================================

def example_1_simple_tool():
    """
    SIMPLE TOOL: Calculator

    This shows the basic structure every tool needs.
    """
    print("=" * 70)
    print("EXAMPLE 1: SIMPLE TOOL DESIGN - Calculator")
    print("=" * 70)

    # Tool Definition (what Claude sees)
    tool_definition = {
        "name": "calculator",
        "description": "Perform basic arithmetic operations: add, subtract, multiply, divide",
        "input_schema": {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract", "multiply", "divide"],
                    "description": "The mathematical operation to perform"
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

    print("\n📋 TOOL DEFINITION:")
    print(json.dumps(tool_definition, indent=2))

    # Tool Implementation (the actual function)
    def calculator(operation: str, a: float, b: float) -> Dict[str, Any]:
        """The function that actually does the work"""
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

    # Test the tool
    print("\n🧪 TESTING THE TOOL:")
    print("-" * 70)

    test_cases = [
        {"operation": "add", "a": 10, "b": 5},
        {"operation": "multiply", "a": 7, "b": 3},
        {"operation": "divide", "a": 20, "b": 4},
        {"operation": "divide", "a": 10, "b": 0}  # Error case
    ]

    for test in test_cases:
        result = calculator(**test)
        print(f"calculator({test}) = {result}")

    print("\n💡 KEY POINTS:")
    print("   • name: Short, descriptive (snake_case)")
    print("   • description: Clear explanation - Claude reads this to decide when to use it!")
    print("   • input_schema: JSON schema for parameters (like morning session!)")
    print("   • Function: The actual Python code that executes")


# ============================================================================
# EXAMPLE 2: Tool with Complex Parameters
# ============================================================================

def example_2_complex_parameters():
    """
    COMPLEX TOOL: Search with filters

    Shows how to handle complex nested parameters.
    """
    print("\n\n" + "=" * 70)
    print("EXAMPLE 2: TOOL WITH COMPLEX PARAMETERS")
    print("=" * 70)

    tool_definition = {
        "name": "search_database",
        "description": "Search a database with filters and sorting options",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query string"
                },
                "filters": {
                    "type": "object",
                    "description": "Optional filters to apply",
                    "properties": {
                        "category": {
                            "type": "string",
                            "enum": ["electronics", "clothing", "books", "food"]
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price in dollars"
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price in dollars"
                        },
                        "in_stock": {
                            "type": "boolean",
                            "description": "Only show in-stock items"
                        }
                    }
                },
                "sort_by": {
                    "type": "string",
                    "enum": ["price_asc", "price_desc", "name", "popularity"],
                    "description": "How to sort results"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of results to return",
                    "minimum": 1,
                    "maximum": 100,
                    "default": 10
                }
            },
            "required": ["query"]
        }
    }

    print("\n📋 TOOL DEFINITION:")
    print(json.dumps(tool_definition, indent=2))

    print("\n💡 NOTICE:")
    print("   • Nested object: 'filters' contains multiple sub-properties")
    print("   • Optional parameters: Only 'query' is required")
    print("   • Constraints: limit has min/max bounds")
    print("   • Defaults: limit defaults to 10 if not provided")
    print("   • Enums: category and sort_by have fixed choices")

    print("\n📝 EXAMPLE USAGE BY CLAUDE:")
    example_calls = [
        {
            "query": "laptop",
            "filters": {"category": "electronics", "max_price": 1500, "in_stock": True},
            "sort_by": "price_asc",
            "limit": 5
        },
        {
            "query": "shoes",
            "filters": {"category": "clothing"},
            "sort_by": "popularity"
        },
        {
            "query": "python book"
            # No filters - still valid!
        }
    ]

    for i, call in enumerate(example_calls, 1):
        print(f"\nCall {i}:")
        print(json.dumps(call, indent=2))


# ============================================================================
# EXAMPLE 3: Tool Design Best Practices
# ============================================================================

def example_3_best_practices():
    """
    BEST PRACTICES: What makes a good tool?

    Critical for the exam!
    """
    print("\n\n" + "=" * 70)
    print("EXAMPLE 3: TOOL DESIGN BEST PRACTICES")
    print("=" * 70)

    print("""
🎯 PRINCIPLE 1: SINGLE RESPONSIBILITY
Each tool should do ONE thing well.

❌ BAD: "file_operations" (too broad - read, write, delete, search?)
✅ GOOD: "read_file", "write_file", "search_files" (separate tools)

WHY: Claude needs to understand exactly when to use each tool.


🎯 PRINCIPLE 2: CLEAR, DESCRIPTIVE NAMES

❌ BAD: "do_thing", "helper", "util"
✅ GOOD: "calculate_tax", "send_email", "fetch_weather"

WHY: Name tells Claude what the tool does at a glance.


🎯 PRINCIPLE 3: DETAILED DESCRIPTIONS

❌ BAD: "Gets data"
✅ GOOD: "Fetches user profile data from the database by user_id.
         Returns name, email, and account creation date."

WHY: Claude reads descriptions to decide when to use the tool!


🎯 PRINCIPLE 4: VALIDATE INPUTS

Always validate parameters before executing:
- Check required fields exist
- Validate types match schema
- Check constraints (min/max, enum values)
- Sanitize user input (prevent injection!)

WHY: Prevent errors, security issues, invalid API calls.


🎯 PRINCIPLE 5: HANDLE ERRORS GRACEFULLY

Return structured errors, don't throw exceptions:

❌ BAD:
    raise Exception("File not found")

✅ GOOD:
    return {
        "success": False,
        "error": "File not found: config.json",
        "error_code": "FILE_NOT_FOUND"
    }

WHY: Claude can understand and communicate errors to users.


🎯 PRINCIPLE 6: CONSISTENT RETURN FORMAT

Always return the same structure:

✅ SUCCESS:
    {
        "success": True,
        "data": {...},
        "metadata": {"took_ms": 150}
    }

✅ ERROR:
    {
        "success": False,
        "error": "Description",
        "error_code": "ERROR_TYPE"
    }

WHY: Predictable responses make tools easier to use.


🎯 PRINCIPLE 7: USE ENUMS FOR FIXED CHOICES

❌ BAD: "status": {"type": "string"}  (any string accepted)
✅ GOOD: "status": {"type": "string", "enum": ["active", "inactive", "pending"]}

WHY: Prevents invalid values, shows Claude the valid options.


🎯 PRINCIPLE 8: PROVIDE DEFAULTS FOR OPTIONAL PARAMS

✅ GOOD:
    "limit": {
        "type": "integer",
        "default": 10,
        "description": "Number of results (default: 10)"
    }

WHY: Makes the tool easier to use - Claude doesn't always need to specify.


🎯 PRINCIPLE 9: TOOL BOUNDARIES

Know when to use ONE tool vs MULTIPLE tools:

❌ BAD: Mega-tool that does everything
    "github_operations" with 50 parameters

✅ GOOD: Focused tools
    "create_github_issue"
    "list_github_prs"
    "merge_github_pr"

WHY: Easier to understand, use, and maintain.


🎯 PRINCIPLE 10: DOCUMENTATION IN SCHEMA

Put descriptions everywhere:

✅ Tool description
✅ Parameter descriptions
✅ Enum value meanings (if not obvious)
✅ Constraints explanation

WHY: Claude needs context to use tools correctly!
    """)


# ============================================================================
# EXAMPLE 4: Common Tool Patterns
# ============================================================================

def example_4_common_patterns():
    """
    COMMON PATTERNS: Real-world tool designs

    These patterns appear frequently in production.
    """
    print("\n\n" + "=" * 70)
    print("EXAMPLE 4: COMMON TOOL PATTERNS")
    print("=" * 70)

    patterns = {
        "CRUD Operations": {
            "description": "Create, Read, Update, Delete",
            "tools": [
                "create_user",
                "get_user",
                "update_user",
                "delete_user"
            ],
            "example": {
                "name": "create_user",
                "description": "Create a new user account in the database",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string", "format": "email"},
                        "name": {"type": "string"},
                        "role": {"type": "string", "enum": ["admin", "user", "guest"]}
                    },
                    "required": ["email", "name"]
                }
            }
        },
        "Search/Filter Pattern": {
            "description": "Search with filters, pagination, sorting",
            "tools": ["search_products", "search_users", "search_documents"],
            "common_params": {
                "query": "Search string",
                "filters": "Object with filter criteria",
                "page": "Page number",
                "limit": "Results per page",
                "sort_by": "Sorting field",
                "sort_order": "asc or desc"
            }
        },
        "External API Pattern": {
            "description": "Call external services (GitHub, Slack, etc.)",
            "tools": ["send_slack_message", "create_github_issue", "fetch_weather"],
            "best_practices": [
                "Handle rate limits",
                "Retry on failure",
                "Timeout protection",
                "Authentication handling"
            ]
        },
        "File Operations Pattern": {
            "description": "Work with files",
            "tools": ["read_file", "write_file", "list_files", "delete_file"],
            "security_considerations": [
                "Validate file paths (prevent ../../../etc/passwd)",
                "Check permissions",
                "Limit file size",
                "Sanitize filenames"
            ]
        },
        "Computation Pattern": {
            "description": "Perform calculations",
            "tools": ["calculate_tax", "calculate_distance", "analyze_data"],
            "characteristics": [
                "Pure functions (no side effects)",
                "Fast execution",
                "Deterministic results"
            ]
        }
    }

    for pattern_name, pattern_info in patterns.items():
        print(f"\n{'='*70}")
        print(f"PATTERN: {pattern_name}")
        print(f"{'='*70}")
        print(f"Description: {pattern_info['description']}")

        if 'tools' in pattern_info:
            print(f"Example Tools: {', '.join(pattern_info['tools'])}")

        if 'example' in pattern_info:
            print("\nExample Schema:")
            print(json.dumps(pattern_info['example'], indent=2))

        if 'common_params' in pattern_info:
            print("\nCommon Parameters:")
            for param, desc in pattern_info['common_params'].items():
                print(f"  • {param}: {desc}")

        if 'best_practices' in pattern_info:
            print("\nBest Practices:")
            for practice in pattern_info['best_practices']:
                print(f"  • {practice}")

        if 'security_considerations' in pattern_info:
            print("\nSecurity Considerations:")
            for consideration in pattern_info['security_considerations']:
                print(f"  ⚠️  {consideration}")


# ============================================================================
# EXAMPLE 5: Tool Design Mistakes (Exam Focus)
# ============================================================================

def example_5_common_mistakes():
    """
    COMMON MISTAKES: What NOT to do

    Exam questions often test your knowledge of these!
    """
    print("\n\n" + "=" * 70)
    print("EXAMPLE 5: COMMON TOOL DESIGN MISTAKES")
    print("=" * 70)

    mistakes = [
        {
            "mistake": "Vague descriptions",
            "bad": {"description": "Gets data"},
            "good": {"description": "Fetches user profile by ID from PostgreSQL, including name, email, created_at"},
            "why": "Claude needs to know WHAT data, WHERE from, WHAT fields"
        },
        {
            "mistake": "Missing parameter descriptions",
            "bad": {
                "user_id": {"type": "string"}
            },
            "good": {
                "user_id": {"type": "string", "description": "Unique user identifier (UUID format)"}
            },
            "why": "Claude needs to know what to pass and in what format"
        },
        {
            "mistake": "Wrong parameter types",
            "bad": {
                "age": {"type": "string"}  # Age should be a number!
            },
            "good": {
                "age": {"type": "integer", "minimum": 0, "maximum": 150}
            },
            "why": "Use correct types + constraints"
        },
        {
            "mistake": "No error handling",
            "bad": "raise Exception('Failed')",
            "good": "return {'success': False, 'error': 'Database connection failed', 'error_code': 'DB_ERROR'}",
            "why": "Claude can't catch Python exceptions - return structured errors"
        },
        {
            "mistake": "Too many parameters",
            "bad": "Tool with 15+ parameters",
            "good": "Break into multiple focused tools, or group related params in objects",
            "why": "Too complex = hard for Claude to use correctly"
        },
        {
            "mistake": "Inconsistent naming",
            "bad": "getUserData, fetch-user, get_user_info",
            "good": "get_user, get_user_profile, get_user_settings",
            "why": "Use consistent naming convention (snake_case for Python)"
        },
        {
            "mistake": "No validation",
            "bad": "Directly use inputs without checking",
            "good": "Validate all inputs match schema before executing",
            "why": "Prevent security issues and runtime errors"
        }
    ]

    for i, mistake_info in enumerate(mistakes, 1):
        print(f"\n{'─'*70}")
        print(f"MISTAKE #{i}: {mistake_info['mistake']}")
        print(f"{'─'*70}")
        print(f"\n❌ BAD:")
        print(f"   {mistake_info['bad']}")
        print(f"\n✅ GOOD:")
        print(f"   {mistake_info['good']}")
        print(f"\n💡 WHY:")
        print(f"   {mistake_info['why']}")


# ============================================================================
# EXAM SUMMARY
# ============================================================================

def show_exam_summary():
    """Key takeaways for the CCA exam"""
    print("\n\n" + "=" * 70)
    print("📚 EXAM SUMMARY: TOOL DESIGN")
    print("=" * 70)

    print("""
🎯 TOOL ANATOMY (Memorize This!):

1. NAME
   - snake_case
   - Descriptive (verb + noun)
   - Example: calculate_tax, send_email

2. DESCRIPTION
   - What it does
   - What it returns
   - Any important constraints
   - Claude READS this to decide when to use it!

3. INPUT_SCHEMA (JSON Schema)
   - type: "object"
   - properties: {param_name: {type, description, constraints}}
   - required: [list of required params]
   - Same structure as structured output from morning!

4. FUNCTION IMPLEMENTATION
   - Validate inputs
   - Execute logic
   - Return structured response (success/error)


🎯 EXAM DECISION PATTERNS:

Question: "How many tools should handle user CRUD operations?"
Answer: 4 separate tools (create_user, get_user, update_user, delete_user)
Why: Single responsibility - each tool does ONE thing

Question: "Should tool throw exceptions or return error objects?"
Answer: Return error objects
Why: Claude can't catch exceptions - needs structured errors

Question: "What's the most important part of a tool description?"
Answer: Clear explanation of what it does and when to use it
Why: Claude reads descriptions to choose tools


🎯 BEST PRACTICES CHECKLIST:

✅ Single responsibility (one tool = one action)
✅ Clear, descriptive name
✅ Detailed description (Claude reads this!)
✅ All parameters have descriptions
✅ Use enums for fixed choices
✅ Validate all inputs
✅ Handle errors gracefully (return objects, not exceptions)
✅ Consistent return format
✅ Security: sanitize inputs, check permissions


🎯 COMMON PATTERNS TO KNOW:

1. CRUD: create, read, update, delete (4 separate tools)
2. Search: query + filters + pagination + sorting
3. API: handle rate limits, retries, timeouts
4. File Ops: validate paths, check permissions
5. Computation: pure functions, fast, deterministic


⚠️ WHAT TO AVOID:

❌ Vague descriptions ("does stuff")
❌ Missing parameter descriptions
❌ Wrong types (age as string instead of integer)
❌ No error handling
❌ Too many parameters (>7-8 is too complex)
❌ Inconsistent naming
❌ No input validation


🔗 CONNECTS TO:

MORNING SESSION (Structured Output):
   • input_schema uses JSON Schema
   • Same validation patterns
   • Return structured data

AFTERNOON (MCP):
   • MCP servers expose multiple related tools
   • Same tool design principles apply
   • Tools are building blocks for MCP servers


💡 EXAM TIP:

Questions will show you a tool definition and ask:
- "What's wrong with this tool?"
- "Which design principle is violated?"
- "How should this be improved?"

Look for: vague descriptions, missing validations, wrong types,
too many parameters, no error handling.
    """)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                    🎯 TOOL DESIGN - COMPLETE GUIDE                  ║
║                                                                      ║
║   Learn to design custom tools for Claude (18% of exam)             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")

    # Run all examples
    example_1_simple_tool()
    example_2_complex_parameters()
    example_3_best_practices()
    example_4_common_patterns()
    example_5_common_mistakes()
    show_exam_summary()

    print("\n" + "=" * 70)
    print("✅ TOOL DESIGN GUIDE COMPLETE!")
    print("=" * 70)
    print("\nYou now understand:")
    print("   ✓ Tool anatomy (name, description, schema, function)")
    print("   ✓ Best practices (single responsibility, validation, errors)")
    print("   ✓ Common patterns (CRUD, Search, API, File Ops)")
    print("   ✓ What to avoid (common mistakes)")
    print("\n🚀 Next: Build a working tool + MCP server!")
