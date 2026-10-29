"""
🎯 MCP (Model Context Protocol) - Complete Guide

MCP = Standard protocol for connecting Claude to external services

Think of it as: USB-C for AI integrations
- One protocol, works with everything
- Plug and play
- Reusable across projects

Run: python3 00_MCP_GUIDE.py
"""

import json
from typing import Dict, Any, List


# ============================================================================
# PART 1: What is MCP?
# ============================================================================

def part_1_what_is_mcp():
    """
    WHAT IS MCP?

    Understanding the architecture and purpose.
    """
    print("=" * 70)
    print("PART 1: WHAT IS MCP (MODEL CONTEXT PROTOCOL)?")
    print("=" * 70)

    print("""
🎯 THE PROBLEM MCP SOLVES:

BEFORE MCP:
  Every service integration was custom-built:

  Your App ──custom code──> GitHub API
  Your App ──custom code──> Slack API
  Your App ──custom code──> Database
  Your App ──custom code──> Google Drive

  Problems:
  • Reinvent the wheel for each integration
  • Different patterns for each service
  • Hard to maintain
  • Not reusable across projects


AFTER MCP:
  One standard protocol for all integrations:

  Your App ──MCP──> GitHub MCP Server ──> GitHub API
  Your App ──MCP──> Slack MCP Server ──> Slack API
  Your App ──MCP──> Database MCP Server ──> Database
  Your App ──MCP──> Google Drive MCP Server ──> Drive API

  Benefits:
  ✅ Standard protocol (JSON-RPC over stdio/HTTP)
  ✅ Reusable servers (use community MCP servers)
  ✅ Easy to maintain (consistent pattern)
  ✅ Plug and play (add new services easily)


🏗️ MCP ARCHITECTURE:

┌─────────────────────┐
│   Claude / Your App │  ← Your application
└──────────┬──────────┘
           │ MCP Protocol (JSON-RPC)
           │
┌──────────▼──────────┐
│    MCP Server       │  ← Server exposes tools
├─────────────────────┤
│ Tools:              │
│ - create_issue()    │
│ - list_prs()        │
│ - merge_pr()        │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│  External Service   │  ← GitHub, Slack, Database, etc.
│  (GitHub API)       │
└─────────────────────┘


🔑 KEY CONCEPTS:

1. MCP SERVER
   - Runs as a separate process
   - Exposes multiple related tools
   - Handles auth, rate limits, connection pooling
   - Example: GitHub MCP server, Slack MCP server

2. MCP PROTOCOL
   - Based on JSON-RPC 2.0
   - Communication over stdio (pipes) or HTTP/SSE
   - Standard messages: initialize, list_tools, call_tool

3. TOOLS
   - MCP server exposes tools (like we learned earlier!)
   - Same tool design principles apply
   - Tools are organized by service

4. CLIENT
   - Your app (or Claude Code)
   - Discovers tools from MCP server
   - Calls tools via JSON-RPC


📊 COMPARISON:

┌──────────────┬─────────────────┬─────────────────────┐
│ Aspect       │ Regular Tool    │ MCP Tool            │
├──────────────┼─────────────────┼─────────────────────┤
│ Location     │ In your app     │ Separate server     │
│ Protocol     │ Direct call     │ JSON-RPC over MCP   │
│ Reusability  │ App-specific    │ Cross-project       │
│ Example      │ calculate_tax() │ GitHub MCP          │
│ Best for     │ Internal logic  │ External services   │
└──────────────┴─────────────────┴─────────────────────┘
    """)


# ============================================================================
# PART 2: MCP Protocol Basics
# ============================================================================

def part_2_mcp_protocol():
    """
    MCP PROTOCOL BASICS

    Understanding JSON-RPC messages.
    """
    print("\n\n" + "=" * 70)
    print("PART 2: MCP PROTOCOL BASICS (JSON-RPC)")
    print("=" * 70)

    print("""
MCP uses JSON-RPC 2.0 for communication.
Three main message types:


1️⃣  INITIALIZE
   Client tells server who it is and what it supports.
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

    print("\n   CLIENT REQUEST:")
    print("   " + json.dumps(initialize_request, indent=2).replace("\n", "\n   "))
    print("\n   SERVER RESPONSE:")
    print("   " + json.dumps(initialize_response, indent=2).replace("\n", "\n   "))

    print("""

2️⃣  LIST TOOLS
   Client asks: "What tools do you have?"
    """)

    list_tools_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list"
    }

    list_tools_response = {
        "jsonrpc": "2.0",
        "id": 2,
        "result": {
            "tools": [
                {
                    "name": "create_github_issue",
                    "description": "Create a new issue in a GitHub repository",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "repo": {"type": "string", "description": "Repository (owner/name)"},
                            "title": {"type": "string", "description": "Issue title"},
                            "body": {"type": "string", "description": "Issue body"}
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

    print("\n   CLIENT REQUEST:")
    print("   " + json.dumps(list_tools_request, indent=2).replace("\n", "\n   "))
    print("\n   SERVER RESPONSE:")
    print("   " + json.dumps(list_tools_response, indent=2).replace("\n", "\n   "))

    print("""

3️⃣  CALL TOOL
   Client calls a specific tool with parameters.
    """)

    call_tool_request = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "create_github_issue",
            "arguments": {
                "repo": "anthropics/claude",
                "title": "Bug: Login fails on Safari",
                "body": "Steps to reproduce:\n1. Open Safari\n2. Try to login\n3. Error occurs"
            }
        }
    }

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

    print("\n   CLIENT REQUEST:")
    print("   " + json.dumps(call_tool_request, indent=2).replace("\n", "\n   "))
    print("\n   SERVER RESPONSE:")
    print("   " + json.dumps(call_tool_response, indent=2).replace("\n", "\n   "))

    print("""

💡 KEY POINTS:

• JSON-RPC 2.0: Standard RPC protocol
• "jsonrpc": "2.0" in every message
• "id": unique identifier for request/response matching
• "method": what operation to perform
• "params"/"result": data payload


🎯 EXAM TIP:

You don't need to memorize exact JSON structure.
Know the THREE message types:
1. initialize - handshake
2. tools/list - discover available tools
3. tools/call - execute a tool

And that it uses JSON-RPC 2.0 over stdio or HTTP/SSE.
    """)


# ============================================================================
# PART 3: Building a Simple MCP Server
# ============================================================================

def part_3_building_mcp_server():
    """
    BUILDING AN MCP SERVER

    Conceptual example (pseudo-code for learning).
    """
    print("\n\n" + "=" * 70)
    print("PART 3: BUILDING A SIMPLE MCP SERVER (Conceptual)")
    print("=" * 70)

    print("""
Let's build a Weather MCP Server that exposes weather-related tools.

STRUCTURE:

weather_mcp/
├── server.py          ← Main MCP server
├── tools/
│   ├── get_weather.py
│   └── get_forecast.py
└── config.json        ← API keys, settings


STEP 1: Define Tools
─────────────────────

First, define what tools your server exposes:
    """)

    tools = [
        {
            "name": "get_current_weather",
            "description": "Get current weather for a location",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name or ZIP code"
                    },
                    "units": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature units",
                        "default": "fahrenheit"
                    }
                },
                "required": ["location"]
            }
        },
        {
            "name": "get_forecast",
            "description": "Get 5-day weather forecast",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "days": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5}
                },
                "required": ["location"]
            }
        }
    ]

    print(json.dumps(tools, indent=2))

    print("""

STEP 2: Implement Tool Functions
─────────────────────────────────

# tools/get_weather.py
def get_current_weather(location: str, units: str = "fahrenheit"):
    # Call weather API
    # This is pseudo-code - actual implementation would call OpenWeather API
    weather_data = call_weather_api(location)

    return {
        "success": True,
        "data": {
            "location": location,
            "temperature": 72,
            "units": units,
            "conditions": "Partly cloudy",
            "humidity": 65,
            "wind_speed": 10
        }
    }


STEP 3: Handle MCP Protocol Messages
─────────────────────────────────────

# server.py
class WeatherMCPServer:
    def __init__(self):
        self.tools = load_tools()  # Load tool definitions

    def handle_message(self, message):
        method = message.get("method")

        if method == "initialize":
            return self.handle_initialize(message)

        elif method == "tools/list":
            return self.handle_list_tools(message)

        elif method == "tools/call":
            return self.handle_call_tool(message)

    def handle_initialize(self, message):
        return {
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {"name": "weather-mcp", "version": "1.0.0"},
                "capabilities": {"tools": {}}
            }
        }

    def handle_list_tools(self, message):
        return {
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {"tools": self.tools}
        }

    def handle_call_tool(self, message):
        tool_name = message["params"]["name"]
        arguments = message["params"]["arguments"]

        # Route to correct tool function
        if tool_name == "get_current_weather":
            result = get_current_weather(**arguments)
        elif tool_name == "get_forecast":
            result = get_forecast(**arguments)

        return {
            "jsonrpc": "2.0",
            "id": message["id"],
            "result": {"content": [{"type": "text", "text": json.dumps(result)}]}
        }


STEP 4: Start the Server
─────────────────────────

# Main entry point
if __name__ == "__main__":
    server = WeatherMCPServer()

    # Read JSON-RPC messages from stdin
    # Write responses to stdout
    # (MCP typically uses stdio for communication)

    while True:
        line = sys.stdin.readline()
        message = json.loads(line)
        response = server.handle_message(message)
        sys.stdout.write(json.dumps(response) + "\\n")
        sys.stdout.flush()


💡 KEY POINTS:

1. Server exposes tools via JSON-RPC
2. Three handlers: initialize, list_tools, call_tool
3. Tools are regular Python functions
4. Communication over stdin/stdout (or HTTP/SSE)
5. Same tool design principles from earlier!


🎯 EXAM FOCUS:

You DON'T need to write MCP server code on the exam.
You NEED to know:
• What MCP is (protocol for connecting services)
• Architecture (client ↔ MCP server ↔ external service)
• Three message types (initialize, list_tools, call_tool)
• When to use MCP vs regular tools
• Benefits (reusability, standard protocol, plug-and-play)
    """)


# ============================================================================
# PART 4: MCP vs Regular Tools - When to Use What
# ============================================================================

def part_4_when_to_use():
    """
    DECISION GUIDE: MCP vs Regular Tools
    """
    print("\n\n" + "=" * 70)
    print("PART 4: WHEN TO USE MCP VS REGULAR TOOLS")
    print("=" * 70)

    scenarios = [
        {
            "scenario": "Calculate sales tax in your e-commerce checkout",
            "decision": "Regular Tool",
            "why": "Internal business logic, simple calculation, no external service"
        },
        {
            "scenario": "Integrate with GitHub (issues, PRs, repos, comments)",
            "decision": "MCP Server",
            "why": "External service, multiple related operations, reusable across projects"
        },
        {
            "scenario": "Search your application's PostgreSQL database",
            "decision": "Could be either - depends on context",
            "why": "Regular tool if simple query. MCP if complex with connection pooling, auth, multiple operations"
        },
        {
            "scenario": "Send notifications via Slack (messages, channels, users)",
            "decision": "MCP Server",
            "why": "External service, multiple operations, authentication required, reusable"
        },
        {
            "scenario": "Validate user input (email format, password strength)",
            "decision": "Regular Tool",
            "why": "Pure function, no external service, fast execution"
        },
        {
            "scenario": "Integrate with Salesforce (leads, contacts, opportunities)",
            "decision": "MCP Server",
            "why": "External CRM, many related operations, complex auth, reusable"
        },
        {
            "scenario": "Generate PDF reports from data",
            "decision": "Regular Tool",
            "why": "Internal processing, no external service"
        },
        {
            "scenario": "Access Google Drive (files, folders, permissions)",
            "decision": "MCP Server",
            "why": "External service, OAuth required, multiple operations, reusable"
        }
    ]

    print("\n🎯 DECISION SCENARIOS:\n")

    for i, scenario_info in enumerate(scenarios, 1):
        print(f"{'='*70}")
        print(f"SCENARIO {i}: {scenario_info['scenario']}")
        print(f"{'='*70}")
        print(f"✅ DECISION: {scenario_info['decision']}")
        print(f"💡 WHY: {scenario_info['why']}\n")

    print("""
📊 QUICK DECISION MATRIX:

Use REGULAR TOOL when:
✅ Internal application logic
✅ Simple, self-contained function
✅ No external service
✅ One-off operation
✅ No authentication needed

Use MCP SERVER when:
✅ External service integration (GitHub, Slack, APIs)
✅ Multiple related operations
✅ Authentication/connection management needed
✅ Reusable across multiple projects
✅ Community MCP server might exist
    """)


# ============================================================================
# EXAM SUMMARY
# ============================================================================

def show_exam_summary():
    """Key takeaways for the CCA exam"""
    print("\n\n" + "=" * 70)
    print("📚 EXAM SUMMARY: MCP (MODEL CONTEXT PROTOCOL)")
    print("=" * 70)

    print("""
🎯 WHAT IS MCP?

Model Context Protocol = Standard protocol for connecting Claude to external services

Analogy: USB-C for AI integrations
- One protocol, works everywhere
- Plug and play
- Reusable


🏗️ MCP ARCHITECTURE:

Client (Claude/Your App)
    ↓ MCP Protocol (JSON-RPC)
MCP Server (exposes tools)
    ↓ API Calls
External Service (GitHub, Slack, Database, etc.)


🔑 KEY CONCEPTS:

1. MCP SERVER
   - Separate process
   - Exposes multiple related tools
   - Handles auth, rate limits, connections

2. MCP PROTOCOL
   - JSON-RPC 2.0
   - Communication: stdio (pipes) or HTTP/SSE
   - Three message types:
     • initialize - handshake
     • tools/list - discover tools
     • tools/call - execute tool

3. BENEFITS
   - Reusable across projects
   - Standard protocol
   - Plug-and-play integrations
   - Community MCP servers available


🎯 MCP VS REGULAR TOOLS:

┌─────────────────┬───────────────────┬─────────────────────┐
│ Aspect          │ Regular Tool      │ MCP Tool            │
├─────────────────┼───────────────────┼─────────────────────┤
│ Location        │ In your app       │ Separate server     │
│ Protocol        │ Direct call       │ JSON-RPC over MCP   │
│ Reusability     │ App-specific      │ Cross-project       │
│ Best for        │ Internal logic    │ External services   │
│ Example         │ calculate_tax()   │ GitHub MCP          │
└─────────────────┴───────────────────┴─────────────────────┘


🎯 WHEN TO USE MCP:

✅ External service (GitHub, Slack, Salesforce, APIs)
✅ Multiple related operations
✅ Authentication required
✅ Want reusability across projects
✅ Community MCP server might exist


🎯 WHEN TO USE REGULAR TOOL:

✅ Internal application logic
✅ Simple, self-contained function
✅ No external service
✅ No complex auth
✅ One-off operation


🎯 EXAM PATTERNS:

Question: "You need to integrate with GitHub. Should you build tools or use MCP?"
Answer: MCP Server (external service, multiple operations, reusable)

Question: "What protocol does MCP use?"
Answer: JSON-RPC 2.0 over stdio or HTTP/SSE

Question: "Name the three main MCP message types"
Answer: initialize, tools/list, tools/call

Question: "What's the main benefit of MCP?"
Answer: Standard protocol for service integrations - reusable, plug-and-play


💡 EXAM TIP:

You DON'T need to:
- Write MCP server code
- Memorize JSON-RPC message structure
- Know implementation details

You DO need to:
- Understand what MCP is (standard protocol)
- Know the architecture (client-server-service)
- Know when to use MCP vs regular tools
- Understand the three message types conceptually
- Know benefits (reusability, standard protocol)


🔗 CONNECTS TO:

TOOLS (earlier):
   • MCP servers expose tools
   • Same tool design principles
   • Tools are building blocks

CLAUDE CODE:
   • Claude Code can connect to MCP servers
   • Discovery tools automatically
   • Use them like built-in tools


🚀 REAL-WORLD EXAMPLES:

Official MCP Servers:
- @modelcontextprotocol/server-github (GitHub integration)
- @modelcontextprotocol/server-slack (Slack integration)
- @modelcontextprotocol/server-filesystem (file operations)
- @modelcontextprotocol/server-postgres (database)

You can:
1. Use existing community MCP servers (fastest)
2. Build custom MCP servers (for proprietary services)
3. Combine MCP servers with regular tools (hybrid approach)
    """)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            🎯 MCP (MODEL CONTEXT PROTOCOL) - COMPLETE GUIDE         ║
║                                                                      ║
║   Learn the standard protocol for service integrations (18% of exam)║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")

    # Run all parts
    part_1_what_is_mcp()
    part_2_mcp_protocol()
    part_3_building_mcp_server()
    part_4_when_to_use()
    show_exam_summary()

    print("\n" + "=" * 70)
    print("✅ MCP GUIDE COMPLETE!")
    print("=" * 70)
    print("\nYou now understand:")
    print("   ✓ What MCP is (standard protocol for service integrations)")
    print("   ✓ Architecture (client-server-service)")
    print("   ✓ JSON-RPC protocol (initialize, list_tools, call_tool)")
    print("   ✓ When to use MCP vs regular tools")
    print("   ✓ Benefits (reusability, plug-and-play)")
    print("\n🎉 Day 2 Afternoon COMPLETE!")
