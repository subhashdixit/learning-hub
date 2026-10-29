"""
Exercise 4: Tool Output Optimization
=====================================

Learn to optimize tool output to minimize token usage.

KEY TOOLS WITH OPTIMIZATION PARAMETERS:
1. Grep: output_mode, head_limit, offset
2. Read: limit, offset
3. Glob: (returns file paths - already optimized)
4. Bash: (control output with shell commands)

GREP OUTPUT MODES:
- files_with_matches: Just file paths (most efficient)
- count: Match counts per file
- content: Full matching lines (least efficient)

EXAM-CRITICAL:
- Know when to use each output_mode
- Understand head_limit and offset for Grep
- Two-step approach: files first, then content
"""

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class ToolOutputStrategy:
    """Represents an optimized tool output strategy"""
    tool: str
    scenario: str
    poor_params: Dict
    poor_tokens: int
    optimal_params: Dict
    optimal_tokens: int
    rationale: str


class ToolOutputOptimizer:
    """Optimizes tool output to minimize tokens"""

    @staticmethod
    def optimize_grep(scenario: str) -> ToolOutputStrategy:
        """
        Optimize grep based on scenario.

        SCENARIOS:
        1. "find files" -> files_with_matches mode
        2. "count occurrences" -> count mode
        3. "see context" -> content mode with head_limit
        """

        if "find files" in scenario or "which files" in scenario:
            # Just need to know which files match
            return ToolOutputStrategy(
                tool="Grep",
                scenario=scenario,
                poor_params={
                    'pattern': 'keyword',
                    'output_mode': 'content',  # Too much!
                },
                poor_tokens=7500,  # 250 lines × 30 tokens/line
                optimal_params={
                    'pattern': 'keyword',
                    'output_mode': 'files_with_matches',
                    'head_limit': 50
                },
                optimal_tokens=500,  # 50 files × 10 tokens/file
                rationale="Use files_with_matches mode - only need file paths"
            )

        elif "count" in scenario or "how many" in scenario:
            # Need counts
            return ToolOutputStrategy(
                tool="Grep",
                scenario=scenario,
                poor_params={
                    'pattern': 'keyword',
                    'output_mode': 'content',
                },
                poor_tokens=7500,
                optimal_params={
                    'pattern': 'keyword',
                    'output_mode': 'count',
                    'head_limit': 100
                },
                optimal_tokens=500,  # 100 files × 5 tokens/count
                rationale="Use count mode - just need match counts"
            )

        elif "see matches" in scenario or "show content" in scenario:
            # Need actual content
            return ToolOutputStrategy(
                tool="Grep",
                scenario=scenario,
                poor_params={
                    'pattern': 'keyword',
                    'output_mode': 'content',
                    # No head_limit - gets all results!
                },
                poor_tokens=15000,  # Could be huge
                optimal_params={
                    'pattern': 'keyword',
                    'output_mode': 'content',
                    'head_limit': 20,  # Reasonable limit
                    '-C': 2  # Context lines
                },
                optimal_tokens=800,  # 20 results × 40 tokens
                rationale="Use content mode WITH head_limit - control output size"
            )

        else:
            # Default: two-step approach
            return ToolOutputStrategy(
                tool="Grep",
                scenario=scenario,
                poor_params={
                    'pattern': 'keyword',
                    'output_mode': 'content',
                },
                poor_tokens=7500,
                optimal_params={
                    'pattern': 'keyword',
                    'output_mode': 'files_with_matches',
                    'head_limit': 50
                },
                optimal_tokens=500,
                rationale="Two-step: files first, then Read specific files"
            )

    @staticmethod
    def two_step_approach(pattern: str, max_files: int = 5) -> List[Dict]:
        """
        Demonstrate two-step approach: Grep for files, then Read them.

        Returns:
            List of tool calls
        """
        return [
            {
                'tool': 'Grep',
                'params': {
                    'pattern': pattern,
                    'output_mode': 'files_with_matches',
                    'head_limit': max_files
                },
                'estimated_tokens': max_files * 10
            },
            {
                'tool': 'Read',
                'params': {
                    'file_path': '<file_from_grep_result>',
                    'limit': 100
                },
                'estimated_tokens': 2000,
                'note': 'Repeat for each relevant file'
            }
        ]


def test_tool_output_optimization():
    """Test tool output optimization strategies."""
    print("Testing Tool Output Optimization...\n")
    print("="*70)

    optimizer = ToolOutputOptimizer()

    # Test scenarios
    scenarios = [
        "Find files containing 'authentication'",
        "Count how many times 'TODO' appears",
        "See matches for 'def login' with context",
        "Search for error patterns",
    ]

    print("\nGREP OUTPUT OPTIMIZATION")
    print("="*70)

    total_savings = 0

    for scenario in scenarios:
        strategy = optimizer.optimize_grep(scenario)

        print(f"\nScenario: {scenario}")
        print("-"*70)

        print(f"✗ POOR:")
        print(f"  Params: {strategy.poor_params}")
        print(f"  Tokens: ~{strategy.poor_tokens:,}")

        print(f"\n✓ OPTIMAL:")
        print(f"  Params: {strategy.optimal_params}")
        print(f"  Tokens: ~{strategy.optimal_tokens:,}")

        savings = strategy.poor_tokens - strategy.optimal_tokens
        savings_pct = (savings / strategy.poor_tokens * 100) if strategy.poor_tokens > 0 else 0

        print(f"\n💰 Savings: {savings:,} tokens ({savings_pct:.0f}%)")
        print(f"Rationale: {strategy.rationale}")

        total_savings += savings

    print(f"\n{'='*70}")
    print(f"TOTAL SAVINGS: {total_savings:,} tokens across all scenarios")
    print(f"{'='*70}")

    # Demonstrate two-step approach
    print("\n\nTWO-STEP APPROACH")
    print("="*70)

    pattern = "authentication"
    steps = optimizer.two_step_approach(pattern, max_files=5)

    print(f"\nSearching for: '{pattern}'")
    print("-"*70)

    print("\nStep 1: Find files")
    step1 = steps[0]
    print(f"  Tool: {step1['tool']}")
    print(f"  Params: {step1['params']}")
    print(f"  Tokens: ~{step1['estimated_tokens']:,}")

    print("\nStep 2: Read relevant files")
    step2 = steps[1]
    print(f"  Tool: {step2['tool']}")
    print(f"  Params: {step2['params']}")
    print(f"  Tokens: ~{step2['estimated_tokens']:,} per file")
    print(f"  Note: {step2['note']}")

    total_two_step = step1['estimated_tokens'] + (step2['estimated_tokens'] * 3)  # 3 files
    one_step_content = 7500  # Grep with content mode

    print(f"\nComparison:")
    print(f"  Two-step approach: ~{total_two_step:,} tokens (files + 3 targeted reads)")
    print(f"  One-step (content): ~{one_step_content:,} tokens (all matches)")
    print(f"  Savings: {one_step_content - total_two_step:,} tokens")

    print("\n" + "="*70)
    print("✅ Tool output optimization complete!")


def demonstrate_grep_parameters():
    """Demonstrate all Grep optimization parameters."""
    print("\n\n" + "="*70)
    print("GREP OPTIMIZATION PARAMETERS")
    print("="*70)

    parameters = [
        {
            'name': 'output_mode',
            'values': ['files_with_matches', 'count', 'content'],
            'description': 'Controls what is returned',
            'tokens': {
                'files_with_matches': '~10 tokens per file path',
                'count': '~5 tokens per count entry',
                'content': '~30 tokens per matching line'
            },
            'when_to_use': {
                'files_with_matches': 'Just need to know which files match',
                'count': 'Need match counts per file',
                'content': 'Need to see actual matching lines'
            }
        },
        {
            'name': 'head_limit',
            'values': ['Default: 250', 'Recommended: 20-50 for content mode'],
            'description': 'Limits number of results returned',
            'tokens': {
                'no_limit': 'Can be 10K+ tokens if many matches',
                'with_limit': 'Controlled, predictable token usage'
            },
            'when_to_use': {
                'low (20-50)': 'Content mode - want to see some matches',
                'medium (100-250)': 'Files mode - want comprehensive list',
                'high (500+)': 'Rarely needed - use Agent instead'
            }
        },
        {
            'name': 'offset',
            'values': ['Default: 0', 'Use with head_limit for pagination'],
            'description': 'Skip first N results',
            'tokens': {
                'benefit': 'Can paginate through large result sets'
            },
            'when_to_use': {
                'pagination': 'Get results 100-200 after seeing 0-100'
            }
        },
        {
            'name': 'context (-A, -B, -C)',
            'values': ['-A: after', '-B: before', '-C: both'],
            'description': 'Show lines around matches',
            'tokens': {
                'impact': 'Each context line adds ~20 tokens per match'
            },
            'when_to_use': {
                'small context (2-3)': 'Need to understand match context',
                'no context': 'Just finding matches, no context needed'
            }
        },
    ]

    for param in parameters:
        print(f"\n{param['name'].upper()}")
        print("-"*70)
        print(f"Description: {param['description']}")

        print(f"\nValues:")
        if isinstance(param['values'], list):
            for val in param['values']:
                print(f"  - {val}")
        else:
            print(f"  {param['values']}")

        print(f"\nToken impact:")
        for key, value in param['tokens'].items():
            print(f"  - {key}: {value}")

        print(f"\nWhen to use:")
        for key, value in param['when_to_use'].items():
            print(f"  - {key}: {value}")


if __name__ == "__main__":
    test_tool_output_optimization()
    demonstrate_grep_parameters()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Grep output_mode significantly affects token usage")
    print("2. Always use head_limit with Grep (default is 250)")
    print("3. Two-step approach: files first, then targeted reads")
    print("4. files_with_matches is most token-efficient")
    print("5. Context lines (-A, -B, -C) add tokens per match")
    print("\nEXAM CRITICAL:")
    print("- Default head_limit is 250 (can still be large)")
    print("- output_mode='content' uses ~3x tokens vs 'files_with_matches'")
    print("- Always set head_limit explicitly for content mode")
    print("- Two-step approach often most efficient for exploration")
