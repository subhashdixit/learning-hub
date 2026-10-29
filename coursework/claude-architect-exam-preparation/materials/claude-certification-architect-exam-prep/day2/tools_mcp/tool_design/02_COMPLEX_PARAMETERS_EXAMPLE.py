"""
🎯 EXAMPLE 2: Tool with Complex Parameters

Real-world tools often have:
- Nested objects (filters with multiple fields)
- Optional parameters (not everything is required)
- Arrays (lists of items)
- Defaults (fallback values)

Run: python3 02_COMPLEX_PARAMETERS_EXAMPLE.py
"""

import json
from typing import Dict, Any, List

print("=" * 70)
print("EXAMPLE 2: TOOL WITH COMPLEX PARAMETERS")
print("=" * 70)

print("""
Real-world scenario: Search an e-commerce product database

Requirements:
- Search query (required)
- Filters: category, price range, availability (optional)
- Sorting options (optional)
- Limit number of results (optional, default 10)
""")

# ============================================================================
# TOOL DEFINITION
# ============================================================================

tool_definition = {
    "name": "search_products",
    "description": "Search product database with filters and sorting options",
    "input_schema": {
        "type": "object",
        "properties": {
            # REQUIRED: Basic search query
            "query": {
                "type": "string",
                "description": "Search keywords (product name, description)"
            },

            # OPTIONAL: Nested object with multiple filters
            "filters": {
                "type": "object",
                "description": "Optional filters to narrow results",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["electronics", "clothing", "books", "food"],
                        "description": "Product category"
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
                        "description": "Only show available items"
                    }
                }
                # Notice: No "required" - all filters are optional!
            },

            # OPTIONAL: Sorting
            "sort_by": {
                "type": "string",
                "enum": ["price_asc", "price_desc", "name", "popularity"],
                "description": "How to sort results",
                "default": "popularity"
            },

            # OPTIONAL: Limit with constraints
            "limit": {
                "type": "integer",
                "description": "Max results to return",
                "minimum": 1,
                "maximum": 100,
                "default": 10
            }
        },
        "required": ["query"]  # Only query is required!
    }
}

print("\n" + "=" * 70)
print("TOOL DEFINITION")
print("=" * 70)
print(json.dumps(tool_definition, indent=2))

print("\n💡 KEY POINTS:")
print("   • Only 'query' is required")
print("   • 'filters' is a NESTED OBJECT with sub-properties")
print("   • 'sort_by' and 'limit' have DEFAULT values")
print("   • 'limit' has CONSTRAINTS (min=1, max=100)")
print("   • Enums show valid choices")

# ============================================================================
# FUNCTION IMPLEMENTATION
# ============================================================================

def search_products(query: str,
                   filters: Dict[str, Any] = None,
                   sort_by: str = "popularity",
                   limit: int = 10) -> Dict[str, Any]:
    """
    Search product database

    This is pseudo-code - in real life, this would query a database
    """
    # Handle optional filters
    if filters is None:
        filters = {}

    # Simulate database search
    print(f"\n🔍 Searching for: '{query}'")

    if filters:
        print(f"📋 Applying filters: {filters}")

    print(f"📊 Sort by: {sort_by}")
    print(f"📏 Limit: {limit} results")

    # Simulated results
    results = [
        {
            "id": 1,
            "name": "Wireless Mouse",
            "category": "electronics",
            "price": 29.99,
            "in_stock": True
        },
        {
            "id": 2,
            "name": "USB Keyboard",
            "category": "electronics",
            "price": 49.99,
            "in_stock": True
        }
    ]

    return {
        "success": True,
        "query": query,
        "filters_applied": filters,
        "results_count": len(results),
        "results": results[:limit]
    }

print("\n" + "=" * 70)
print("FUNCTION IMPLEMENTATION")
print("=" * 70)
print("""
def search_products(query: str,
                   filters: Dict[str, Any] = None,  # ← Optional with default
                   sort_by: str = "popularity",      # ← Optional with default
                   limit: int = 10) -> Dict[str, Any]:  # ← Optional with default

    # Handle optional filters
    if filters is None:
        filters = {}

    # Query database with filters, sorting, and limit
    # ... (search logic here)

    return {
        "success": True,
        "results": [...]
    }
""")

# ============================================================================
# TEST CASES
# ============================================================================

print("\n" + "=" * 70)
print("🧪 TEST CASES - Different Ways to Call This Tool")
print("=" * 70)

print("\n" + "─" * 70)
print("TEST 1: Minimal - Only Required Parameter")
print("─" * 70)
result = search_products(query="laptop")
print(f"Result: {result['results_count']} products found")

print("\n" + "─" * 70)
print("TEST 2: With Filters (nested object)")
print("─" * 70)
result = search_products(
    query="laptop",
    filters={
        "category": "electronics",
        "max_price": 1000,
        "in_stock": True
    }
)
print(f"Result: {result['results_count']} products found")

print("\n" + "─" * 70)
print("TEST 3: With Sorting and Limit")
print("─" * 70)
result = search_products(
    query="shoes",
    sort_by="price_asc",
    limit=5
)
print(f"Result: {result['results_count']} products found")

print("\n" + "─" * 70)
print("TEST 4: Everything Combined")
print("─" * 70)
result = search_products(
    query="book",
    filters={
        "category": "books",
        "min_price": 10,
        "max_price": 50
    },
    sort_by="popularity",
    limit=3
)
print(f"Result: {result['results_count']} products found")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("📚 WHAT WE LEARNED - COMPLEX PARAMETERS")
print("=" * 70)
print("""
🎯 NESTED OBJECTS:
   "filters": {
       "type": "object",
       "properties": { ... }
   }

   Groups related parameters together!
   Example: All filter options in one object


🎯 OPTIONAL PARAMETERS:
   Only "query" is in "required": ["query"]

   filters, sort_by, limit are optional
   Claude can call with just: {"query": "laptop"}


🎯 DEFAULT VALUES:
   "default": 10

   If Claude doesn't provide a value, use default
   Makes tools easier to use


🎯 CONSTRAINTS:
   "minimum": 1,
   "maximum": 100

   Validate input ranges
   Prevent invalid values


🎯 ENUMS:
   "enum": ["price_asc", "price_desc", "name", "popularity"]

   Fixed set of valid choices
   Shows Claude what options are available


✅ WHY THIS MATTERS FOR EXAM:

Real-world tools are complex! You need to know:
• How to structure nested objects
• Which parameters should be required vs optional
• When to use defaults
• How to set constraints
• When to use enums


📊 COMPARISON:

Simple Tool (Example 1):
├─ 3 parameters, all required
└─ Flat structure

Complex Tool (Example 2):
├─ 1 required, 3 optional
├─ Nested object (filters)
├─ Defaults (sort_by, limit)
├─ Constraints (min/max)
└─ Enums (category, sort_by)
""")

print("\n" + "=" * 70)
print("✅ EXAMPLE 2 COMPLETE!")
print("=" * 70)
