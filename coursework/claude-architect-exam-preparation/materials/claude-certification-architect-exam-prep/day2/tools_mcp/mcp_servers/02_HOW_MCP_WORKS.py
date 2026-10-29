"""
🎯 STEP 2: HOW MCP WORKS - Architecture & Protocol

Learn the 3-layer architecture and 3 message types.

Run: python3 02_HOW_MCP_WORKS.py
"""

import json

print("=" * 70)
print("HOW MCP WORKS - ARCHITECTURE & PROTOCOL")
print("=" * 70)

# ============================================================================
# PART 1: MCP Architecture (3 Layers)
# ============================================================================

print("\n" + "=" * 70)
print("PART 1: MCP ARCHITECTURE (3 Layers)")
print("=" * 70)

print("""
MCP has 3 layers:

┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: CLIENT (Your App / Claude)                       │
│  • Your application or Claude Code                          │
│  • Discovers tools from MCP server                          │
│  • Calls tools via MCP protocol                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ MCP Protocol (JSON-RPC)
                     │ Communication over: stdio or HTTP/SSE
                     │
┌────────────────────▼────────────────────────────────────────┐
│  LAYER 2: MCP SERVER                                        │
│  • Runs as separate process                                 │
│  • Exposes tools (like we learned earlier!)                 │
│  • Handles: auth, rate limits, connection pooling           │
│  • Example: GitHub MCP Server                               │
│                                                              │
│  Tools exposed:                                             │
│  ├─ create_issue()                                          │
│  ├─ list_pull_requests()                                    │
│  ├─ merge_pr()                                              │
│  └─ comment_on_issue()                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ API Calls (REST, GraphQL, etc.)
                     │
┌────────────────────▼────────────────────────────────────────┐
│  LAYER 3: EXTERNAL SERVICE                                  │
│  • GitHub API                                               │
│  • Slack API                                                │
│  • PostgreSQL Database                                      │
│  • Any external service                                     │
└─────────────────────────────────────────────────────────────┘


💡 KEY POINTS:

1. CLIENT → MCP SERVER
   Uses MCP protocol (JSON-RPC over stdio/HTTP)

2. MCP SERVER → EXTERNAL SERVICE
   Uses service's native API (REST, GraphQL, SQL, etc.)

3. MCP SERVER = THE BRIDGE
   Translates between MCP protocol and service API
""")

# ============================================================================
# PART 2: Communication Method
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 2: COMMUNICATION METHOD")
print("=" * 70)

print("""
MCP uses JSON-RPC 2.0 protocol over:

1. STDIO (Standard Input/Output) - Most Common
   ┌────────┐     stdin/stdout     ┌────────────┐
   │ Client │ ←──────────────────→ │ MCP Server │
   └────────┘    (JSON messages)    └────────────┘

   • MCP server runs as child process
   • Client sends JSON to server's stdin
   • Server sends JSON to stdout
   • Like pipes in shell: command1 | command2

2. HTTP/SSE (Server-Sent Events)
   ┌────────┐        HTTP          ┌────────────┐
   │ Client │ ←──────────────────→ │ MCP Server │
   └────────┘                       └────────────┘

   • MCP server runs as HTTP server
   • Client makes HTTP requests
   • Used for remote servers


🎯 FOR EXAM: Just know it uses JSON-RPC over stdio or HTTP.
Don't need to know implementation details.
""")

# ============================================================================
# PART 3: The 3 Message Types (CRITICAL!)
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 3: THE 3 MESSAGE TYPES (CRITICAL FOR EXAM!)")
print("=" * 70)

print("""
MCP has exactly 3 message types. Memorize these!

1. initialize  - Handshake (client introduces itself)
2. tools/list  - Discovery (what tools are available?)
3. tools/call  - Execution (run a tool)
""")

# ───────────────────────────────────────────────────────────────────────────
# MESSAGE 1: initialize
# ───────────────────────────────────────────────────────────────────────────

print("\n" + "─" * 70)
print("MESSAGE 1: initialize - Handshake")
print("─" * 70)

print("""
When client connects, it sends 'initialize' message.

CLIENT → SERVER:
"Hi, I'm my-client v1.0, I support MCP protocol 2024-11-05"
""")

initialize_request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "clientInfo": {
            "name": "my-client",
            "version": "1.0.0"
        }
    }
}

print("JSON:")
print(json.dumps(initialize_request, indent=2))

print("""
SERVER → CLIENT:
"Hi, I'm github-mcp v1.0, I support tools"
""")

initialize_response = {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "protocolVersion": "2024-11-05",
        "serverInfo": {
            "name": "github-mcp",
            "version": "1.0.0"
        },
        "capabilities": {
            "tools": {}
        }
    }
}

print("JSON:")
print(json.dumps(initialize_response, indent=2))

print("""
💡 PURPOSE: Establish connection, check compatibility
""")

# ───────────────────────────────────────────────────────────────────────────
# MESSAGE 2: tools/list
# ───────────────────────────────────────────────────────────────────────────

print("\n" + "─" * 70)
print("MESSAGE 2: tools/list - Discovery")
print("─" * 70)

print("""
Client asks: "What tools do you have?"

CLIENT → SERVER:
""")

list_tools_request = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list"
}

print("JSON:")
print(json.dumps(list_tools_request, indent=2))

print("""
SERVER → CLIENT:
"I have these tools..."
""")

list_tools_response = {
    "jsonrpc": "2.0",
    "id": 2,
    "result": {
        "tools": [
            {
                "name": "create_github_issue",
                "description": "Create a new GitHub issue",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "repo": {"type": "string", "description": "Repository (owner/name)"},
                        "title": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["repo", "title"]
                }
            },
            {
                "name": "list_pull_requests",
                "description": "List pull requests in a repository",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "repo": {"type": "string"},
                        "state": {"type": "string", "enum": ["open", "closed", "all"]}
                    },
                    "required": ["repo"]
                }
            }
        ]
    }
}

print("JSON (shortened):")
print(json.dumps(list_tools_response, indent=2))

print("""
💡 PURPOSE: Client discovers what tools are available
💡 NOTICE: Same tool structure we learned earlier!
   - name, description, inputSchema
""")

# ───────────────────────────────────────────────────────────────────────────
# MESSAGE 3: tools/call
# ───────────────────────────────────────────────────────────────────────────

print("\n" + "─" * 70)
print("MESSAGE 3: tools/call - Execution")
print("─" * 70)

print("""
Client says: "Run this tool with these parameters"

CLIENT → SERVER:
""")

call_tool_request = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "create_github_issue",
        "arguments": {
            "repo": "anthropics/claude",
            "title": "Bug: Login fails",
            "body": "Steps to reproduce: 1. Open app 2. Click login"
        }
    }
}

print("JSON:")
print(json.dumps(call_tool_request, indent=2))

print("""
SERVER → CLIENT:
"Here's the result..."
""")

call_tool_response = {
    "jsonrpc": "2.0",
    "id": 3,
    "result": {
        "content": [
            {
                "type": "text",
                "text": json.dumps({
                    "success": True,
                    "issue_number": 42,
                    "url": "https://github.com/anthropics/claude/issues/42"
                }, indent=2)
            }
        ]
    }
}

print("JSON:")
print(json.dumps(call_tool_response, indent=2))

print("""
💡 PURPOSE: Execute a tool and get results
💡 NOTICE: Result is wrapped in "content" array with "text" type
""")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n\n" + "=" * 70)
print("📚 SUMMARY - HOW MCP WORKS")
print("=" * 70)

print("""
🏗️ ARCHITECTURE (3 Layers):

1. CLIENT (Your app / Claude)
   ↓ MCP Protocol (JSON-RPC)
2. MCP SERVER (Bridge)
   ↓ API Calls
3. EXTERNAL SERVICE (GitHub, Slack, etc.)


📨 3 MESSAGE TYPES (Memorize!):

1. initialize
   • Handshake when client connects
   • Exchange: name, version, capabilities

2. tools/list
   • Client discovers available tools
   • Server returns array of tools (name, description, inputSchema)

3. tools/call
   • Client executes a tool
   • Server returns result


🎯 FOR THE EXAM:

Questions will ask:
• "What are the 3 MCP message types?"
  Answer: initialize, tools/list, tools/call

• "What protocol does MCP use?"
  Answer: JSON-RPC 2.0 over stdio or HTTP/SSE

• "What's the 3-layer architecture?"
  Answer: Client → MCP Server → External Service

• "What does tools/list do?"
  Answer: Client discovers what tools are available from server


💡 KEY INSIGHT:

MCP Server = The Bridge
• Translates MCP protocol → Service API
• Handles auth, rate limits, connections
• Exposes tools to client
• Multiple clients can use same server


✅ YOU DON'T NEED TO:
• Write MCP server code
• Memorize exact JSON structure
• Know implementation details

✅ YOU DO NEED TO:
• Know the 3 message types
• Understand the architecture (3 layers)
• Know when to use MCP vs regular tools
""")

print("\n" + "=" * 70)
print("✅ STEP 2 COMPLETE - You understand HOW MCP works!")
print("=" * 70)
print("\nNext: When to use MCP vs Regular Tools (Decision Guide)")
