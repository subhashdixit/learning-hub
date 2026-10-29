"""
Exercise 2: Context Window Management
======================================

Learn to manage context windows effectively and avoid hitting limits.

CONTEXT WINDOW LIMITS:
- Input: Varies by model (Claude Opus: 200K tokens)
- Output: ~4K tokens per response (configurable)
- Tools add to input context

KEY STRATEGIES:
1. Use offset/limit for large files
2. Use head_limit for grep results
3. Agent tool for exploration (separate context)
4. Structured output to reduce parsing tokens

CRITICAL FOR EXAM:
- Know when to use Read with offset/limit
- Know when to use Grep with head_limit
- Understand Agent tool isolation
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class ToolCall:
    """Represents a tool call with token cost"""
    tool: str
    params: Dict
    estimated_output_tokens: int


class ContextWindowManager:
    """Manages context window usage"""

    def __init__(self, max_tokens: int = 200000):
        self.max_tokens = max_tokens
        self.current_usage = 0
        self.tool_calls: List[ToolCall] = []

    def estimate_tool_output(self, tool: str, params: Dict) -> int:
        """
        Estimate output tokens for a tool call.

        TODO: Implement output estimation for different tools
        """

        if tool == "Read":
            file_path = params.get('file_path', '')
            limit = params.get('limit')
            offset = params.get('offset', 0)

            if limit:
                # Reading with limit
                # Assume ~80 chars per line, ~20 tokens per line
                return limit * 20
            else:
                # Reading full file (default 2000 lines)
                return 2000 * 20  # 40K tokens!

        elif tool == "Grep":
            head_limit = params.get('head_limit', 250)  # Default is 250
            output_mode = params.get('output_mode', 'files_with_matches')

            if output_mode == 'files_with_matches':
                # Just file paths: ~10 tokens per result
                return head_limit * 10
            elif output_mode == 'content':
                # Full content lines: ~30 tokens per line
                return head_limit * 30
            elif output_mode == 'count':
                # Just counts: ~5 tokens per result
                return head_limit * 5

        elif tool == "Glob":
            # File paths only, usually compact
            return 500  # Conservative estimate

        elif tool == "Bash":
            # Highly variable, assume moderate
            return 1000

        elif tool == "WebFetch":
            # Web pages can be large
            return 10000

        elif tool == "Agent":
            # Agent runs in separate context!
            return 500  # Just the summary returned

        return 1000  # Default estimate

    def plan_tool_calls(self, scenario: str) -> List[ToolCall]:
        """
        Plan optimal tool calls for a scenario.

        Returns:
            List of tool calls with token estimates
        """
        planned_calls = []

        if "read large file" in scenario:
            # BAD: Read entire large file
            bad_call = ToolCall(
                tool="Read",
                params={'file_path': '/large_file.py'},
                estimated_output_tokens=self.estimate_tool_output("Read", {})
            )

            # GOOD: Read with limit and offset
            good_call = ToolCall(
                tool="Read",
                params={'file_path': '/large_file.py', 'limit': 100, 'offset': 0},
                estimated_output_tokens=self.estimate_tool_output("Read", {'limit': 100})
            )

            return [bad_call, good_call]

        elif "search codebase" in scenario:
            # BAD: Grep without head_limit
            bad_call = ToolCall(
                tool="Grep",
                params={'pattern': 'function', 'output_mode': 'content'},
                estimated_output_tokens=self.estimate_tool_output("Grep", {
                    'output_mode': 'content',
                    'head_limit': 1000  # Very large
                })
            )

            # GOOD: Grep with reasonable head_limit
            good_call = ToolCall(
                tool="Grep",
                params={'pattern': 'function', 'output_mode': 'content', 'head_limit': 50},
                estimated_output_tokens=self.estimate_tool_output("Grep", {
                    'output_mode': 'content',
                    'head_limit': 50
                })
            )

            return [bad_call, good_call]

        return planned_calls

    def should_use_agent(self, task: str) -> Tuple[bool, str]:
        """
        Decide if Agent tool should be used to save context.

        Returns:
            (should_use, reason)
        """
        # Use Agent for:
        # 1. Broad exploration that might blow up context
        # 2. Research that requires many tool calls
        # 3. Tasks that need isolation

        task_lower = task.lower()

        if any(kw in task_lower for kw in ['explore', 'research', 'investigate', 'find all']):
            return (True, "Broad exploration - Agent runs in separate context")

        if "multiple" in task_lower or "many" in task_lower:
            return (True, "Multiple operations - isolate in Agent context")

        if "large codebase" in task_lower:
            return (True, "Large codebase search - Agent prevents context bloat")

        return (False, "Targeted operation - direct tool use is fine")


def test_context_management():
    """Test context window management strategies."""
    print("Testing Context Window Management...\n")
    print("="*70)

    manager = ContextWindowManager()

    # Test 1: Reading large files
    print("\n1. Reading Large Files")
    print("-"*70)

    scenarios = [
        ("Read full file (no limits)", "Read", {}),
        ("Read first 100 lines", "Read", {'limit': 100}),
        ("Read lines 500-600", "Read", {'limit': 100, 'offset': 500}),
    ]

    for desc, tool, params in scenarios:
        tokens = manager.estimate_tool_output(tool, params)
        print(f"{desc:40s}: ~{tokens:6,} tokens")

    # Test 2: Grep operations
    print("\n\n2. Grep Operations")
    print("-"*70)

    grep_scenarios = [
        ("Grep files only (default)", "Grep", {'output_mode': 'files_with_matches'}),
        ("Grep files (head_limit=50)", "Grep", {'output_mode': 'files_with_matches', 'head_limit': 50}),
        ("Grep content (no limit)", "Grep", {'output_mode': 'content'}),
        ("Grep content (head_limit=50)", "Grep", {'output_mode': 'content', 'head_limit': 50}),
        ("Grep count (head_limit=100)", "Grep", {'output_mode': 'count', 'head_limit': 100}),
    ]

    for desc, tool, params in grep_scenarios:
        tokens = manager.estimate_tool_output(tool, params)
        print(f"{desc:40s}: ~{tokens:6,} tokens")

    # Test 3: Agent vs Direct
    print("\n\n3. Agent Tool vs Direct Tool Use")
    print("-"*70)

    tasks = [
        "Find the specific login function",
        "Explore the entire authentication system",
        "Research all API endpoints in the codebase",
        "Read one configuration file",
        "Investigate how error handling works across 50 files",
    ]

    for task in tasks:
        should_use, reason = manager.should_use_agent(task)
        decision = "✓ USE AGENT" if should_use else "✗ DIRECT TOOLS"
        print(f"\nTask: '{task}'")
        print(f"  {decision}")
        print(f"  Reason: {reason}")

    # Test 4: Optimization scenarios
    print("\n\n4. Optimization Scenarios")
    print("-"*70)

    optimization_scenarios = [
        ("Read large file", "read large file"),
        ("Search codebase", "search codebase"),
    ]

    for title, scenario in optimization_scenarios:
        print(f"\n{title}:")
        calls = manager.plan_tool_calls(scenario)

        if len(calls) >= 2:
            bad_call, good_call = calls[0], calls[1]

            print(f"  ✗ BAD:  {bad_call.tool}({bad_call.params})")
            print(f"         ~{bad_call.estimated_output_tokens:,} tokens")

            print(f"  ✓ GOOD: {good_call.tool}({good_call.params})")
            print(f"         ~{good_call.estimated_output_tokens:,} tokens")

            savings = bad_call.estimated_output_tokens - good_call.estimated_output_tokens
            pct = (savings / bad_call.estimated_output_tokens * 100) if bad_call.estimated_output_tokens > 0 else 0
            print(f"  💰 Savings: {savings:,} tokens ({pct:.0f}%)")

    print("\n" + "="*70)
    print("✅ Context management test complete!")


def demonstrate_best_practices():
    """Demonstrate context window best practices."""
    print("\n\n" + "="*70)
    print("CONTEXT WINDOW BEST PRACTICES")
    print("="*70)

    practices = [
        {
            'title': "1. Use Read with offset/limit for large files",
            'bad': "Read tool: Read(file_path='/large_file.py')",
            'bad_cost': "~40K tokens (2000 lines default)",
            'good': "Read tool: Read(file_path='/large_file.py', limit=100, offset=0)",
            'good_cost': "~2K tokens (100 lines)",
        },
        {
            'title': "2. Use Grep with head_limit",
            'bad': "Grep tool: Grep(pattern='error', output_mode='content')",
            'bad_cost': "~7.5K tokens (250 lines default)",
            'good': "Grep tool: Grep(pattern='error', output_mode='content', head_limit=20)",
            'good_cost': "~600 tokens (20 lines)",
        },
        {
            'title': "3. Use Agent for broad exploration",
            'bad': "Multiple Grep + Read calls (blows up main context)",
            'bad_cost': "50K+ tokens in main context",
            'good': "Agent tool with subagent_type='Explore'",
            'good_cost': "~500 tokens in main (Agent returns summary)",
        },
        {
            'title': "4. Use 'files_with_matches' before 'content'",
            'bad': "Grep(pattern='login', output_mode='content')",
            'bad_cost': "~7.5K tokens with full content",
            'good': "First: Grep(pattern='login', output_mode='files_with_matches')\nThen: Read specific files",
            'good_cost': "~2.5K tokens (250 file paths + targeted reads)",
        },
    ]

    for practice in practices:
        print(f"\n{practice['title']}")
        print("-"*70)
        print(f"✗ BAD:  {practice['bad']}")
        print(f"        Cost: {practice['bad_cost']}")
        print(f"\n✓ GOOD: {practice['good']}")
        print(f"        Cost: {practice['good_cost']}")


if __name__ == "__main__":
    test_context_management()
    demonstrate_best_practices()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Use offset/limit with Read for large files")
    print("2. Use head_limit with Grep to control output")
    print("3. Use Agent tool for broad exploration (separate context)")
    print("4. Use 'files_with_matches' before 'content' mode")
    print("5. Default Read limit is 2000 lines (~40K tokens)")
    print("6. Default Grep head_limit is 250 results")
    print("\nEXAM CRITICAL:")
    print("- Know when each parameter (offset, limit, head_limit) applies")
    print("- Understand Agent tool isolation benefits")
    print("- Recognize context-blowup anti-patterns")
