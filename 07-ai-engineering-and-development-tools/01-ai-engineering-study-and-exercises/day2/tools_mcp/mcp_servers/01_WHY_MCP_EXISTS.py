"""
🎯 STEP 1: WHY MCP EXISTS - The Problem It Solves

Before we learn MCP, understand WHY we need it.

Run: python3 01_WHY_MCP_EXISTS.py
"""

print("=" * 70)
print("WHY MCP EXISTS - THE PROBLEM")
print("=" * 70)

print("""
🏢 REAL SCENARIO: You're building an AI assistant that needs to:
   • Access GitHub (issues, PRs, repos)
   • Send Slack messages
   • Query PostgreSQL database
   • Access Google Drive files

HOW WOULD YOU BUILD THIS?
""")

# ============================================================================
# APPROACH 1: Custom Integration (Before MCP)
# ============================================================================

print("\n" + "=" * 70)
print("❌ APPROACH 1: CUSTOM INTEGRATION (Before MCP)")
print("=" * 70)

print("""
You build custom code for EACH service:

Your App:
├── github_integration.py     ← Custom GitHub code
│   ├── create_issue()
│   ├── list_prs()
│   └── merge_pr()
│
├── slack_integration.py      ← Custom Slack code
│   ├── send_message()
│   └── list_channels()
│
├── database_integration.py   ← Custom Database code
│   ├── query()
│   └── insert()
│
└── drive_integration.py      ← Custom Google Drive code
    ├── list_files()
    └── download_file()


⚠️  PROBLEMS:

1. REINVENT THE WHEEL
   • Every project builds GitHub integration from scratch
   • Everyone solves the same problems

2. INCONSISTENT PATTERNS
   • GitHub integration works differently than Slack
   • Each has different error handling
   • Different authentication approaches

3. NOT REUSABLE
   • Can't share GitHub integration with other projects
   • Have to copy-paste code

4. HARD TO MAINTAIN
   • GitHub changes API → update YOUR code
   • Bug in integration → fix in every project

5. DUPLICATED EFFORT
   • 1000 developers × 1000 projects = reinventing GitHub integration 1M times!


📊 WHAT YOU BUILT:

Project A ──custom code──> GitHub API
Project B ──custom code──> GitHub API
Project C ──custom code──> GitHub API  ← All different implementations!
Project D ──custom code──> GitHub API
""")

# ============================================================================
# APPROACH 2: MCP (The Solution)
# ============================================================================

print("\n\n" + "=" * 70)
print("✅ APPROACH 2: MCP (The Solution)")
print("=" * 70)

print("""
MCP = ONE standard protocol for ALL services!

Think of it like: USB-C for AI integrations
• One protocol
• Works with everything
• Plug and play


🏗️ HOW IT WORKS:

Your App ──MCP Protocol──> GitHub MCP Server ──> GitHub API
Your App ──MCP Protocol──> Slack MCP Server ──> Slack API
Your App ──MCP Protocol──> Database MCP Server ──> Database
Your App ──MCP Protocol──> Drive MCP Server ──> Google Drive


✅ BENEFITS:

1. REUSABLE
   • Use community MCP servers (don't build from scratch)
   • Example: @modelcontextprotocol/server-github
   • Install with npm, use immediately!

2. STANDARD PROTOCOL
   • Same pattern for all services
   • Learn once, use everywhere
   • Consistent error handling

3. PLUG AND PLAY
   • Want GitHub? Install GitHub MCP server
   • Want Slack? Install Slack MCP server
   • Just works!

4. MAINTAINED BY COMMUNITY
   • GitHub changes API? MCP server maintainer updates it
   • You just update the package
   • Bug fixes benefit everyone

5. NO DUPLICATION
   • One GitHub MCP server
   • Used by 1000s of projects
   • Collective effort!


📊 WHAT YOU USE:

Project A ──┐
Project B ──┼──> MCP Protocol ──> GitHub MCP Server ──> GitHub API
Project C ──┤                     (ONE implementation,
Project D ──┘                      used by everyone!)
""")

# ============================================================================
# ANALOGY
# ============================================================================

print("\n\n" + "=" * 70)
print("💡 ANALOGY: USB-C")
print("=" * 70)

print("""
BEFORE USB-C (Custom Integrations):
   • Every device had different cables
   • iPhone cable ≠ Android cable ≠ Laptop cable
   • Needed 10 different cables
   • Everyone reinvented charging

AFTER USB-C (MCP):
   • One standard cable
   • Works with iPhone, Android, Laptop, everything
   • Plug and play
   • Manufacturers follow the standard


SAME WITH MCP:

BEFORE MCP (Custom Integrations):
   • Every project had different GitHub integration code
   • Different patterns for each service
   • Reinvent the wheel

AFTER MCP:
   • One standard protocol (MCP)
   • Works with GitHub, Slack, Database, everything
   • Plug and play
   • Community provides MCP servers
""")

# ============================================================================
# REAL EXAMPLE
# ============================================================================

print("\n\n" + "=" * 70)
print("🌍 REAL EXAMPLE")
print("=" * 70)

print("""
WITHOUT MCP - You write this:

# Your custom GitHub code (100+ lines)
def create_github_issue(repo, title, body):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"https://api.github.com/repos/{repo}/issues"
    response = requests.post(url, headers=headers, json={...})
    # Handle errors, rate limits, retries, etc.
    return response.json()

# Do the same for Slack (100+ lines)
# Do the same for Database (100+ lines)
# Repeat for every service...


WITH MCP - You use this:

# Install community MCP server
$ npm install @modelcontextprotocol/server-github

# Configure in your app
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}

# That's it! Your app now has all GitHub tools:
# - create_issue
# - list_prs
# - merge_pr
# - comment_on_issue
# - etc.

Claude can now use these tools automatically!
""")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n\n" + "=" * 70)
print("📚 SUMMARY - WHY MCP EXISTS")
print("=" * 70)

print("""
🎯 THE PROBLEM MCP SOLVES:

Before: Everyone builds custom integrations
   • Duplicated effort
   • Inconsistent patterns
   • Not reusable
   • Hard to maintain

After: Standard protocol (MCP)
   • Reusable community servers
   • Consistent pattern
   • Plug and play
   • Maintained by community


🔑 KEY INSIGHT:

MCP = Standard protocol for connecting Claude to ANY service
Think: USB-C for AI integrations


✅ WHAT YOU NEED TO KNOW FOR EXAM:

1. MCP solves: integration duplication
2. MCP provides: standard protocol
3. MCP benefits: reusable, consistent, plug-and-play
4. Analogy: USB-C (one standard, works everywhere)
5. Use case: External services (GitHub, Slack, databases)


🚀 NEXT STEPS:

Now that you understand WHY MCP exists,
let's learn HOW it works:
   • MCP architecture
   • MCP protocol (3 message types)
   • When to use MCP vs regular tools
""")

print("\n" + "=" * 70)
print("✅ STEP 1 COMPLETE - You understand WHY MCP exists!")
print("=" * 70)
