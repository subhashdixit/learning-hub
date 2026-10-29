"""
🎯 STRUCTURED OUTPUT - JSON Schema Validation

This is CRITICAL for:
- Tool Design (afternoon session)
- MCP Integration (afternoon session)
- API integrations
- Database operations

Learn:
1. JSON schema definition
2. Validation logic
3. Error handling
4. Real-world patterns

Run: python3 01_json_schema_validation.py
"""

import json
from typing import Dict, Any, List, Optional
from datetime import datetime


# ============================================================================
# EXAMPLE 1: Basic JSON Schema
# ============================================================================

def example_1_basic_schema():
    """
    BASIC JSON SCHEMA: Product extraction

    This is the FOUNDATION for tool design!
    """
    print("=" * 70)
    print("EXAMPLE 1: BASIC JSON SCHEMA")
    print("=" * 70)

    # Define the schema (what you WANT from Claude)
    schema = {
        "type": "object",
        "properties": {
            "product_name": {"type": "string"},
            "price": {"type": "number"},
            "in_stock": {"type": "boolean"},
            "categories": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["product_name", "price", "in_stock"]
    }

    print("\n📋 SCHEMA DEFINITION:")
    print(json.dumps(schema, indent=2))

    # The prompt you'd send to Claude
    prompt = f"""Extract product information from this description and return ONLY valid JSON.

Schema:
{json.dumps(schema, indent=2)}

Description:
"The UltraBook Pro laptop is priced at $1299.99 and is currently available
in our inventory. Categories: Electronics, Computers, Premium."

Return ONLY the JSON:"""

    print("\n📝 PROMPT TO CLAUDE:")
    print(prompt)

    # What Claude returns
    claude_response = """{
  "product_name": "UltraBook Pro",
  "price": 1299.99,
  "in_stock": true,
  "categories": ["Electronics", "Computers", "Premium"]
}"""

    print("\n✅ CLAUDE'S RESPONSE:")
    print(claude_response)

    # Validate the response
    try:
        data = json.loads(claude_response)
        print("\n✅ VALIDATION: Valid JSON!")
        print(f"   - product_name: {data['product_name']} (type: {type(data['product_name']).__name__})")
        print(f"   - price: {data['price']} (type: {type(data['price']).__name__})")
        print(f"   - in_stock: {data['in_stock']} (type: {type(data['in_stock']).__name__})")
        print(f"   - categories: {data['categories']} (type: {type(data['categories']).__name__})")
    except json.JSONDecodeError as e:
        print(f"\n❌ VALIDATION FAILED: {e}")

    print("\n💡 KEY POINTS:")
    print("   • Schema defines EXACT structure")
    print("   • 'required' fields MUST be present")
    print("   • Types are enforced (string, number, boolean, array)")
    print("   • Can parse programmatically - no text parsing needed!")


# ============================================================================
# EXAMPLE 2: Complex Nested Schema
# ============================================================================

def example_2_nested_schema():
    """
    NESTED SCHEMA: Real-world complexity

    Like API responses with nested objects
    """
    print("\n\n" + "=" * 70)
    print("EXAMPLE 2: COMPLEX NESTED SCHEMA")
    print("=" * 70)

    schema = {
        "type": "object",
        "properties": {
            "order_id": {"type": "string"},
            "customer": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "loyalty_tier": {"type": "string", "enum": ["bronze", "silver", "gold", "platinum"]}
                },
                "required": ["name", "email"]
            },
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "price": {"type": "number"}
                    },
                    "required": ["product_id", "quantity", "price"]
                }
            },
            "total": {"type": "number"},
            "status": {"type": "string", "enum": ["pending", "processing", "shipped", "delivered"]}
        },
        "required": ["order_id", "customer", "items", "total", "status"]
    }

    print("\n📋 NESTED SCHEMA:")
    print(json.dumps(schema, indent=2))

    print("\n📝 STRUCTURE:")
    print("""
    order_id: string
    customer: {
        name: string
        email: string
        loyalty_tier: "bronze" | "silver" | "gold" | "platinum"
    }
    items: [{
        product_id: string
        quantity: integer
        price: number
    }]
    total: number
    status: "pending" | "processing" | "shipped" | "delivered"
    """)

    # Sample response
    response = {
        "order_id": "ORD-2024-001",
        "customer": {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "loyalty_tier": "gold"
        },
        "items": [
            {"product_id": "PROD-123", "quantity": 2, "price": 29.99},
            {"product_id": "PROD-456", "quantity": 1, "price": 49.99}
        ],
        "total": 109.97,
        "status": "processing"
    }

    print("✅ VALID RESPONSE:")
    print(json.dumps(response, indent=2))

    print("\n💡 KEY POINTS:")
    print("   • Nested objects: customer has sub-fields")
    print("   • Arrays of objects: items contains multiple products")
    print("   • Enums: loyalty_tier and status have fixed values")
    print("   • This pattern is common in APIs and databases!")


# ============================================================================
# EXAMPLE 3: Validation with Error Handling
# ============================================================================

def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> tuple[bool, List[str]]:
    """
    Simple validation function (real-world would use jsonschema library)

    Returns: (is_valid, list_of_errors)
    """
    errors = []

    # Check required fields
    required = schema.get("required", [])
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Check types
    properties = schema.get("properties", {})
    for field, field_schema in properties.items():
        if field in data:
            expected_type = field_schema.get("type")
            actual_value = data[field]

            # Type checking
            if expected_type == "string" and not isinstance(actual_value, str):
                errors.append(f"Field '{field}' should be string, got {type(actual_value).__name__}")
            elif expected_type == "number" and not isinstance(actual_value, (int, float)):
                errors.append(f"Field '{field}' should be number, got {type(actual_value).__name__}")
            elif expected_type == "integer" and not isinstance(actual_value, int):
                errors.append(f"Field '{field}' should be integer, got {type(actual_value).__name__}")
            elif expected_type == "boolean" and not isinstance(actual_value, bool):
                errors.append(f"Field '{field}' should be boolean, got {type(actual_value).__name__}")
            elif expected_type == "array" and not isinstance(actual_value, list):
                errors.append(f"Field '{field}' should be array, got {type(actual_value).__name__}")

            # Enum checking
            if "enum" in field_schema and actual_value not in field_schema["enum"]:
                errors.append(f"Field '{field}' must be one of {field_schema['enum']}, got '{actual_value}'")

    return len(errors) == 0, errors


def example_3_validation():
    """
    VALIDATION: Catch errors before they break your system
    """
    print("\n\n" + "=" * 70)
    print("EXAMPLE 3: VALIDATION WITH ERROR HANDLING")
    print("=" * 70)

    schema = {
        "type": "object",
        "properties": {
            "user_id": {"type": "integer"},
            "email": {"type": "string"},
            "role": {"type": "string", "enum": ["admin", "user", "guest"]},
            "active": {"type": "boolean"}
        },
        "required": ["user_id", "email", "role"]
    }

    print("\n📋 SCHEMA:")
    print(json.dumps(schema, indent=2))

    # Test Case 1: Valid data
    print("\n" + "-" * 70)
    print("TEST 1: VALID DATA")
    print("-" * 70)
    valid_data = {
        "user_id": 123,
        "email": "user@example.com",
        "role": "admin",
        "active": True
    }
    print("Data:", json.dumps(valid_data, indent=2))
    is_valid, errors = validate_json_schema(valid_data, schema)
    print(f"✅ Valid: {is_valid}")

    # Test Case 2: Missing required field
    print("\n" + "-" * 70)
    print("TEST 2: MISSING REQUIRED FIELD")
    print("-" * 70)
    invalid_data_1 = {
        "user_id": 123,
        "email": "user@example.com"
        # Missing 'role'
    }
    print("Data:", json.dumps(invalid_data_1, indent=2))
    is_valid, errors = validate_json_schema(invalid_data_1, schema)
    print(f"❌ Valid: {is_valid}")
    print(f"Errors: {errors}")

    # Test Case 3: Wrong type
    print("\n" + "-" * 70)
    print("TEST 3: WRONG TYPE")
    print("-" * 70)
    invalid_data_2 = {
        "user_id": "123",  # Should be integer, not string
        "email": "user@example.com",
        "role": "admin"
    }
    print("Data:", json.dumps(invalid_data_2, indent=2))
    is_valid, errors = validate_json_schema(invalid_data_2, schema)
    print(f"❌ Valid: {is_valid}")
    print(f"Errors: {errors}")

    # Test Case 4: Invalid enum value
    print("\n" + "-" * 70)
    print("TEST 4: INVALID ENUM VALUE")
    print("-" * 70)
    invalid_data_3 = {
        "user_id": 123,
        "email": "user@example.com",
        "role": "superadmin"  # Not in enum
    }
    print("Data:", json.dumps(invalid_data_3, indent=2))
    is_valid, errors = validate_json_schema(invalid_data_3, schema)
    print(f"❌ Valid: {is_valid}")
    print(f"Errors: {errors}")

    print("\n💡 KEY POINTS:")
    print("   • ALWAYS validate before using data")
    print("   • Catch errors early - don't wait for database to reject")
    print("   • Clear error messages help debugging")
    print("   • In production, use jsonschema library (pip install jsonschema)")


# ============================================================================
# EXAMPLE 4: Real-World API Integration Pattern
# ============================================================================

def example_4_api_pattern():
    """
    REAL-WORLD: How to use structured output with APIs

    This is the pattern you'll use for Tools & MCP!
    """
    print("\n\n" + "=" * 70)
    print("EXAMPLE 4: REAL-WORLD API INTEGRATION PATTERN")
    print("=" * 70)

    print("""
SCENARIO: You're building a tool that creates GitHub issues

WORKFLOW:
1. User describes the issue in natural language
2. Claude extracts structured data
3. Validate the data
4. Call GitHub API with structured data

Let's see the pattern:
    """)

    # Step 1: Define schema
    github_issue_schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string", "maxLength": 100},
            "body": {"type": "string"},
            "labels": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 10
            },
            "assignees": {
                "type": "array",
                "items": {"type": "string"}
            },
            "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]}
        },
        "required": ["title", "body"]
    }

    print("\n📋 STEP 1: DEFINE SCHEMA")
    print(json.dumps(github_issue_schema, indent=2))

    # Step 2: User input
    user_input = """
    We found a critical bug where users can't login after the last deployment.
    The error happens on the /auth/login endpoint. This needs immediate attention.
    Assign it to the backend team and mark it as critical.
    """

    print("\n📝 STEP 2: USER INPUT (Natural Language)")
    print(user_input.strip())

    # Step 3: Claude's structured extraction
    print("\n🤖 STEP 3: CLAUDE EXTRACTS STRUCTURED DATA")

    prompt = f"""Extract GitHub issue information from this description.

Schema:
{json.dumps(github_issue_schema, indent=2)}

Description:
{user_input}

Return ONLY valid JSON:"""

    claude_response = {
        "title": "Critical: Users unable to login after deployment",
        "body": "Bug found where users cannot login after the last deployment. Error occurs on /auth/login endpoint. Requires immediate attention.",
        "labels": ["bug", "critical", "auth", "backend"],
        "assignees": ["backend-team"],
        "priority": "critical"
    }

    print(json.dumps(claude_response, indent=2))

    # Step 4: Validate
    print("\n✅ STEP 4: VALIDATE")
    is_valid, errors = validate_json_schema(claude_response, github_issue_schema)
    print(f"Valid: {is_valid}")
    if not is_valid:
        print(f"Errors: {errors}")

    # Step 5: Use with API
    print("\n🚀 STEP 5: CALL GITHUB API")
    print("""
    # Pseudo-code for API call:
    import requests

    response = requests.post(
        'https://api.github.com/repos/owner/repo/issues',
        headers={'Authorization': f'token {GITHUB_TOKEN}'},
        json=claude_response  # ← Structured data ready to use!
    )
    """)

    print("\n💡 KEY POINTS:")
    print("   • Natural language → Structured data → API call")
    print("   • Schema ensures API compatibility")
    print("   • Validation prevents API errors")
    print("   • This is how Claude Code tools work internally!")
    print("   • MCP servers use the same pattern!")


# ============================================================================
# EXAM SUMMARY
# ============================================================================

def show_exam_summary():
    """Show key takeaways for the exam"""
    print("\n\n" + "=" * 70)
    print("📚 EXAM SUMMARY: STRUCTURED OUTPUT")
    print("=" * 70)

    print("""
🎯 WHEN TO USE STRUCTURED OUTPUT:

✅ MUST use when:
   • Integrating with APIs (GitHub, Slack, databases)
   • Storing data in databases
   • Building tools (afternoon session!)
   • Building MCP servers (afternoon session!)
   • Need to parse output programmatically
   • Zero tolerance for format errors

❌ DON'T use when:
   • Output is for human reading only
   • Format can be flexible
   • Natural language response is better

📋 JSON SCHEMA BASICS:

Common Types:
   • "string" - text
   • "number" - 1.5, 3.14, 100 (int or float)
   • "integer" - 1, 2, 3 (whole numbers only)
   • "boolean" - true, false
   • "array" - lists [1, 2, 3]
   • "object" - nested {...}

Key Properties:
   • "required": ["field1", "field2"] - must be present
   • "enum": ["value1", "value2"] - fixed set of values
   • "maxLength", "minLength" - string constraints
   • "minimum", "maximum" - number constraints

✅ VALIDATION CHECKLIST:

1. Parse JSON (json.loads) - catches syntax errors
2. Check required fields exist
3. Verify types match schema
4. Check enum values are valid
5. Validate constraints (length, min/max)
6. Handle errors gracefully

🔗 CONNECTS TO AFTERNOON TOPICS:

TOOL DESIGN:
   • Tools take structured input (parameters)
   • Tools return structured output (results)
   • Schema defines tool interface

MCP SERVERS:
   • MCP uses JSON-RPC (structured)
   • Tool schemas define capabilities
   • Responses must be valid JSON

🎯 EXAM PATTERNS:

Question: "What's the best way to integrate Claude with a database?"
Answer: Structured Output (need exact schema for DB insert)

Question: "User input needs to be stored in PostgreSQL..."
Answer: Structured Output + Injection Prevention (both!)

Question: "API expects specific JSON format..."
Answer: Structured Output (guarantee format)

💡 EXAM TIP:

Look for these keywords in questions:
- "API", "database", "parse", "integrate", "exact format"
- "must be valid", "strict format", "schema"
→ All point to Structured Output!

🚀 NEXT: Tools & MCP (Afternoon Session)

Now you understand structured output, you're ready for:
   • Tool Design - tools use schemas for parameters
   • MCP Servers - MCP uses structured JSON-RPC

Structured output is the FOUNDATION for the afternoon!
    """)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║           🎯 STRUCTURED OUTPUT - JSON SCHEMA VALIDATION             ║
║                                                                      ║
║   Master this for Tools & MCP (afternoon session)!                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")

    # Run all examples
    example_1_basic_schema()
    example_2_nested_schema()
    example_3_validation()
    example_4_api_pattern()
    show_exam_summary()

    print("\n" + "=" * 70)
    print("✅ STRUCTURED OUTPUT COMPLETE!")
    print("=" * 70)
    print("\nYou now understand:")
    print("   ✓ JSON schema definition")
    print("   ✓ Validation patterns")
    print("   ✓ Error handling")
    print("   ✓ Real-world API integration")
    print("\n🚀 Ready for afternoon: Tools & MCP!")
