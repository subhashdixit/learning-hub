"""
🎯 STEP 3: MCP vs Regular Tools - Decision Guide

Learn WHEN to use each approach.
This is critical for real projects and exam questions!

Run: python3 03_MCP_VS_TOOLS_DECISION.py
"""

print("=" * 70)
print("MCP VS REGULAR TOOLS - DECISION GUIDE")
print("=" * 70)

# ============================================================================
# QUICK DECISION MATRIX
# ============================================================================

print("\n" + "=" * 70)
print("⚡ QUICK DECISION MATRIX")
print("=" * 70)

print("""
┌─────────────────────────────────────────┬─────────────┬─────────────┐
│ Question                                │ Regular Tool│ MCP Server  │
├─────────────────────────────────────────┼─────────────┼─────────────┤
│ Internal application logic?             │     ✅      │     ❌      │
│ External service integration?           │     ❌      │     ✅      │
│ Simple, self-contained function?        │     ✅      │     ❌      │
│ Multiple related operations?            │     ❌      │     ✅      │
│ Need authentication/connection mgmt?    │     ❌      │     ✅      │
│ Want to reuse across projects?          │     ❌      │     ✅      │
│ Community server might exist?           │     ❌      │     ✅      │
└─────────────────────────────────────────┴─────────────┴─────────────┘


🎯 SIMPLE RULE:

INTERNAL logic → Regular Tool
EXTERNAL service → MCP Server
""")

# ============================================================================
# REAL SCENARIOS - One by One
# ============================================================================

print("\n\n" + "=" * 70)
print("🌍 REAL SCENARIOS - DECISION PRACTICE")
print("=" * 70)

scenarios = [
    {
        "num": 1,
        "scenario": "Calculate sales tax in your e-commerce checkout",
        "details": "Formula: price * tax_rate, simple math, no external service",
        "decision": "Regular Tool",
        "why": [
            "Internal business logic",
            "Simple calculation (one function)",
            "No external service",
            "No authentication needed"
        ]
    },
    {
        "num": 2,
        "scenario": "Integrate with GitHub (issues, PRs, repos, comments)",
        "details": "Need to create issues, list PRs, merge, comment, etc.",
        "decision": "MCP Server",
        "why": [
            "External service (GitHub API)",
            "Multiple related operations (issues, PRs, repos)",
            "Authentication required (GitHub token)",
            "Reusable across projects",
            "Community server exists: @modelcontextprotocol/server-github"
        ]
    },
    {
        "num": 3,
        "scenario": "Validate email format",
        "details": "Check if string matches email pattern using regex",
        "decision": "Regular Tool",
        "why": [
            "Pure function (no side effects)",
            "No external service",
            "Fast execution",
            "Self-contained logic"
        ]
    },
    {
        "num": 4,
        "scenario": "Send notifications via Slack",
        "details": "Send messages, list channels, upload files, get user info",
        "decision": "MCP Server",
        "why": [
            "External service (Slack API)",
            "Multiple operations (messages, channels, files)",
            "Authentication required (Slack token)",
            "Reusable across projects",
            "Community server exists: @modelcontextprotocol/server-slack"
        ]
    },
    {
        "num": 5,
        "scenario": "Search your app's PostgreSQL database",
        "details": "Query products table with filters",
        "decision": "Could be either - depends!",
        "why": [
            "Simple query → Regular Tool (just run SQL)",
            "Complex integration → MCP Server if you need:",
            "  • Connection pooling",
            "  • Multiple database operations",
            "  • Reusable across projects",
            "  • Schema introspection",
            "Community server exists: @modelcontextprotocol/server-postgres"
        ]
    },
    {
        "num": 6,
        "scenario": "Generate PDF reports from data",
        "details": "Take JSON data, create formatted PDF",
        "decision": "Regular Tool",
        "why": [
            "Internal processing",
            "No external service",
            "Self-contained (data → PDF)",
            "Not reusable pattern (app-specific formatting)"
        ]
    },
    {
        "num": 7,
        "scenario": "Integrate with Salesforce CRM",
        "details": "Manage leads, contacts, opportunities, accounts",
        "decision": "MCP Server",
        "why": [
            "External CRM service",
            "Many related operations (leads, contacts, etc.)",
            "Complex authentication (OAuth)",
            "Reusable across projects",
            "Worth building MCP server for organization-wide use"
        ]
    },
    {
        "num": 8,
        "scenario": "Parse CSV file and extract data",
        "details": "Read CSV, validate format, return structured data",
        "decision": "Regular Tool",
        "why": [
            "File processing (internal)",
            "No external service",
            "Simple operation",
            "One-off task"
        ]
    }
]

for scenario in scenarios:
    print(f"\n{'='*70}")
    print(f"SCENARIO {scenario['num']}: {scenario['scenario']}")
    print(f"{'='*70}")
    print(f"\n📋 DETAILS:")
    print(f"   {scenario['details']}")
    print(f"\n✅ DECISION: {scenario['decision']}")
    print(f"\n💡 WHY:")
    for reason in scenario['why']:
        print(f"   • {reason}")

# ============================================================================
# DECISION FLOWCHART
# ============================================================================

print("\n\n" + "=" * 70)
print("🎯 DECISION FLOWCHART")
print("=" * 70)

print("""
START: Need to give Claude a capability
   |
   ├─ Does it integrate with EXTERNAL service?
   │  (GitHub, Slack, Database, API, etc.)
   │
   ├─ YES ──> Multiple related operations?
   │          │
   │          ├─ YES ──> Use MCP Server ✅
   │          │          (GitHub: issues, PRs, repos, comments)
   │          │
   │          └─ NO ──> Could use Regular Tool
   │                    (but MCP might exist already)
   │
   └─ NO ──> Internal application logic?
              │
              └─ YES ──> Use Regular Tool ✅
                         (calculate_tax, validate_email, parse_csv)


📊 EXTRA CONSIDERATIONS:

Already exists?
• Check if community MCP server exists
• npm search @modelcontextprotocol/server-*
• If exists → Use MCP (don't rebuild)

Authentication/Connection?
• Needs OAuth, API keys, connection pooling?
• → Lean toward MCP Server

Reusability?
• Need across multiple projects?
• → MCP Server (one server, many projects)

Complexity?
• Single simple operation?
• → Regular Tool
""")

# ============================================================================
# COMPARISON TABLE
# ============================================================================

print("\n\n" + "=" * 70)
print("📊 SIDE-BY-SIDE COMPARISON")
print("=" * 70)

print("""
┌────────────────────┬─────────────────────┬──────────────────────┐
│ Aspect             │ Regular Tool        │ MCP Server           │
├────────────────────┼─────────────────────┼──────────────────────┤
│ Location           │ In your app         │ Separate process     │
│ Protocol           │ Direct function call│ JSON-RPC over MCP    │
│ Best for           │ Internal logic      │ External services    │
│ Reusability        │ App-specific        │ Cross-project        │
│ Example            │ calculate_tax()     │ GitHub MCP           │
│ Setup              │ Write function      │ Install server       │
│ Maintenance        │ You maintain        │ Community maintains  │
│ Auth/Connection    │ You handle          │ Server handles       │
│ When API changes   │ You update code     │ Update package       │
└────────────────────┴─────────────────────┴──────────────────────┘
""")

# ============================================================================
# EXAM TIPS
# ============================================================================

print("\n\n" + "=" * 70)
print("🎯 EXAM TIPS")
print("=" * 70)

print("""
EXAM PATTERN:

Questions will give you a scenario and ask:
"Should you build custom tools or use an MCP server?"

TRIGGER WORDS:

Use MCP Server when you see:
• "integrate with GitHub"
• "send Slack messages"
• "access Salesforce"
• "query PostgreSQL"
• "external service"
• "API integration"
• "multiple related operations"
• "reusable across projects"

Use Regular Tool when you see:
• "calculate"
• "validate"
• "parse"
• "internal logic"
• "business rules"
• "simple function"
• "one operation"


EXAMPLE EXAM QUESTIONS:

Q1: "You need to integrate with GitHub to manage issues and PRs.
     What's the best approach?"

A: Use MCP Server
   Why: External service, multiple operations, community server exists


Q2: "You need to calculate tax based on state and price.
     What's the best approach?"

A: Use Regular Tool
   Why: Internal logic, simple calculation, no external service


Q3: "You need to send notifications to multiple channels: Slack, email, SMS.
     What's the best approach?"

A: Combination:
   • Slack → MCP Server (external, complex auth)
   • Email → Could be tool or MCP (depends on service)
   • SMS → Could be tool or MCP (depends on service)


🎯 KEY INSIGHT FOR EXAM:

Not always black and white!
• Simple database query → Regular Tool
• Complex database operations → MCP Server
• Judge based on complexity, reusability, and auth needs


WHEN IN DOUBT:
External service + multiple operations = MCP Server
Internal logic + simple operation = Regular Tool
""")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n\n" + "=" * 70)
print("📚 FINAL SUMMARY")
print("=" * 70)

print("""
✅ USE REGULAR TOOL WHEN:
   • Internal application logic
   • Simple, self-contained function
   • No external service
   • One operation
   • No complex authentication

   Examples:
   • calculate_tax(price, rate)
   • validate_email(email)
   • parse_csv(file_path)
   • generate_report(data)


✅ USE MCP SERVER WHEN:
   • External service integration
   • Multiple related operations
   • Authentication/connection management
   • Reusable across projects
   • Community server might exist

   Examples:
   • GitHub (issues, PRs, repos, comments)
   • Slack (messages, channels, files)
   • Salesforce (leads, contacts, opportunities)
   • PostgreSQL (complex operations with connection pooling)


🎯 GOLDEN RULE:

INTERNAL → Tool
EXTERNAL → MCP


💡 REAL-WORLD TIP:

Check if MCP server exists first!
$ npm search @modelcontextprotocol/server-*

If community server exists → Use it!
Don't rebuild what's already built.
""")

print("\n" + "=" * 70)
print("✅ STEP 3 COMPLETE - You know when to use MCP vs Tools!")
print("=" * 70)
print("\n🎉 MCP GUIDE COMPLETE!")
print("\nYou now understand:")
print("   ✓ WHY MCP exists (solve integration duplication)")
print("   ✓ HOW MCP works (3-layer architecture, 3 message types)")
print("   ✓ WHEN to use MCP vs Regular Tools (decision guide)")
print("\n🚀 Ready for Day 3 or review!")
