"""
Exercise 3: Efficient File Reading Strategies
==============================================

Learn optimal file reading patterns for different scenarios.

READ TOOL PARAMETERS:
- file_path: Required, absolute path
- limit: Number of lines to read
- offset: Line number to start from (0-indexed)
- pages: For PDF files only

DEFAULT BEHAVIOR:
- Reads up to 2000 lines from start
- Uses cat -n format (line numbers start at 1)

EXAM-CRITICAL SCENARIOS:
1. Read specific function in large file
2. Read end of log file
3. Read middle section
4. Scan file structure without full read
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class FileReadStrategy:
    """Represents a file reading strategy"""
    scenario: str
    file_size_lines: int
    target_location: str
    optimal_params: Dict
    estimated_tokens: int
    rationale: str


class FileReadingOptimizer:
    """Optimizes file reading operations"""

    TOKENS_PER_LINE = 20  # Rough estimate

    @staticmethod
    def calculate_tokens(lines: int) -> int:
        """Calculate estimated tokens for reading N lines."""
        return lines * FileReadingOptimizer.TOKENS_PER_LINE

    @staticmethod
    def strategy_for_scenario(scenario: str, file_lines: int) -> FileReadStrategy:
        """
        Determine optimal reading strategy for a scenario.

        TODO: Implement strategy selection
        """

        if "start" in scenario or "beginning" in scenario:
            # Read from start
            params = {'limit': 100}
            return FileReadStrategy(
                scenario=scenario,
                file_size_lines=file_lines,
                target_location="start",
                optimal_params=params,
                estimated_tokens=FileReadingOptimizer.calculate_tokens(100),
                rationale="Reading start - use limit only"
            )

        elif "end" in scenario or "tail" in scenario or "recent" in scenario:
            # Read from end
            offset = max(0, file_lines - 100)
            params = {'limit': 100, 'offset': offset}
            return FileReadStrategy(
                scenario=scenario,
                file_size_lines=file_lines,
                target_location="end",
                optimal_params=params,
                estimated_tokens=FileReadingOptimizer.calculate_tokens(100),
                rationale=f"Reading end - use offset={offset}, limit=100"
            )

        elif "middle" in scenario or "around line" in scenario:
            # Read from middle
            offset = file_lines // 2
            params = {'limit': 100, 'offset': offset}
            return FileReadStrategy(
                scenario=scenario,
                file_size_lines=file_lines,
                target_location="middle",
                optimal_params=params,
                estimated_tokens=FileReadingOptimizer.calculate_tokens(100),
                rationale=f"Reading middle - use offset={offset}, limit=100"
            )

        elif "small file" in scenario or file_lines < 500:
            # Read full file
            params = {}
            return FileReadStrategy(
                scenario=scenario,
                file_size_lines=file_lines,
                target_location="full",
                optimal_params=params,
                estimated_tokens=FileReadingOptimizer.calculate_tokens(file_lines),
                rationale="Small file - read fully (no params needed)"
            )

        elif "scan" in scenario or "overview" in scenario:
            # Scan: read start, middle, end
            params = {'limit': 50}  # Just peek at start
            return FileReadStrategy(
                scenario=scenario,
                file_size_lines=file_lines,
                target_location="scan",
                optimal_params=params,
                estimated_tokens=FileReadingOptimizer.calculate_tokens(50 * 3),  # 3 reads
                rationale="Scan: read start (50), middle (50), end (50) in 3 calls"
            )

        else:
            # Default: read from start with limit
            params = {'limit': 200}
            return FileReadStrategy(
                scenario=scenario,
                file_size_lines=file_lines,
                target_location="start",
                optimal_params=params,
                estimated_tokens=FileReadingOptimizer.calculate_tokens(200),
                rationale="Default - read first 200 lines"
            )

    @staticmethod
    def multi_read_strategy(file_lines: int, target_line: int, context: int = 50) -> List[Dict]:
        """
        Strategy for reading around a specific line.

        Args:
            file_lines: Total lines in file
            target_line: Line number to read around (1-indexed)
            context: Lines before/after target

        Returns:
            List of read params
        """
        # Convert to 0-indexed offset
        target_offset = target_line - 1

        # Calculate range
        start_offset = max(0, target_offset - context)
        total_lines = min(context * 2, file_lines - start_offset)

        return [{
            'offset': start_offset,
            'limit': total_lines
        }]


def test_file_reading_strategies():
    """Test optimal file reading strategies."""
    print("Testing File Reading Strategies...\n")
    print("="*70)

    optimizer = FileReadingOptimizer()

    # Test scenarios
    scenarios = [
        ("Read start of small config file", 50),
        ("Read start of large log file", 10000),
        ("Read end of large log file (recent errors)", 10000),
        ("Read middle section of source file", 5000),
        ("Scan structure of large file", 8000),
        ("Read around line 2500 in large file", 5000),
    ]

    print("\nOPTIMAL FILE READING STRATEGIES")
    print("="*70)

    for scenario_desc, file_lines in scenarios:
        print(f"\nScenario: {scenario_desc}")
        print(f"File size: {file_lines} lines")
        print("-"*70)

        if "around line" in scenario_desc:
            # Special handling for targeted read
            target_line = 2500
            strategies = optimizer.multi_read_strategy(file_lines, target_line, context=50)
            tokens = optimizer.calculate_tokens(100)

            print(f"Strategy: Read around line {target_line}")
            print(f"Params: {strategies[0]}")
            print(f"Estimated tokens: ~{tokens:,}")
            print(f"Rationale: Read ±50 lines around target")
        else:
            strategy = optimizer.strategy_for_scenario(scenario_desc, file_lines)

            print(f"Strategy: {strategy.target_location}")
            print(f"Params: {strategy.optimal_params}")
            print(f"Estimated tokens: ~{strategy.estimated_tokens:,}")
            print(f"Rationale: {strategy.rationale}")

    # Compare: Full read vs Optimized read
    print("\n\n" + "="*70)
    print("OPTIMIZATION COMPARISON")
    print("="*70)

    large_file_lines = 10000

    print(f"\nFile: 10,000 lines")
    print("-"*70)

    full_read_tokens = optimizer.calculate_tokens(min(2000, large_file_lines))  # Default limit
    optimized_tokens = optimizer.calculate_tokens(100)

    print(f"Full read (default):     {full_read_tokens:,} tokens (2000 lines)")
    print(f"Optimized read (limit):  {optimized_tokens:,} tokens (100 lines)")
    print(f"Savings:                 {full_read_tokens - optimized_tokens:,} tokens ({(1 - optimized_tokens/full_read_tokens)*100:.0f}%)")

    print("\n" + "="*70)
    print("✅ File reading strategies complete!")


def demonstrate_real_scenarios():
    """Demonstrate real-world file reading scenarios."""
    print("\n\n" + "="*70)
    print("REAL-WORLD FILE READING SCENARIOS")
    print("="*70)

    scenarios = [
        {
            'title': "1. Finding a function in large source file",
            'approach': "Use Grep first to find line number, then Read with offset/limit",
            'steps': [
                "Grep(pattern='def target_function', output_mode='content', head_limit=5)",
                "Parse line number from grep output (e.g., line 2450)",
                "Read(file_path='file.py', offset=2440, limit=100)",
            ],
            'tokens': "~50 (grep) + ~2000 (read) = ~2050 tokens",
            'vs_full': "vs ~40K tokens for full file read"
        },
        {
            'title': "2. Checking recent log entries",
            'approach': "Read from end of file",
            'steps': [
                "Estimate file size (or use grep -c)",
                "Read(file_path='app.log', offset=9900, limit=100)  # Last 100 lines",
            ],
            'tokens': "~2000 tokens",
            'vs_full': "vs ~40K tokens for full log"
        },
        {
            'title': "3. Understanding file structure",
            'approach': "Scan: read start, then targeted sections",
            'steps': [
                "Read(file_path='file.py', limit=50)  # Imports and top-level",
                "Grep for class/function definitions",
                "Targeted reads of specific sections",
            ],
            'tokens': "~1000 (scan) + ~500 (grep) + ~2000 (targeted) = ~3500 tokens",
            'vs_full': "vs ~40K tokens for full file"
        },
        {
            'title': "4. Reading configuration file",
            'approach': "Full read (small file)",
            'steps': [
                "Read(file_path='config.json')  # No params needed",
            ],
            'tokens': "~500 tokens (small file)",
            'vs_full': "N/A - full read is optimal"
        },
    ]

    for scenario in scenarios:
        print(f"\n{scenario['title']}")
        print("-"*70)
        print(f"Approach: {scenario['approach']}")
        print(f"Steps:")
        for i, step in enumerate(scenario['steps'], 1):
            print(f"  {i}. {step}")
        print(f"Token cost: {scenario['tokens']}")
        print(f"Comparison: {scenario['vs_full']}")


if __name__ == "__main__":
    test_file_reading_strategies()
    demonstrate_real_scenarios()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Default Read limit: 2000 lines (~40K tokens)")
    print("2. Use 'limit' to control how many lines to read")
    print("3. Use 'offset' to start reading from specific line")
    print("4. For large files: Grep first, then targeted Read")
    print("5. For recent logs: Read from end (offset = file_size - limit)")
    print("6. For small files (<500 lines): Full read is fine")
    print("\nEXAM CRITICAL:")
    print("- offset is 0-indexed (first line is offset 0)")
    print("- Line numbers in output start at 1 (cat -n format)")
    print("- Combine Grep + Read for efficient large file navigation")
    print("- Know when full read vs optimized read is appropriate")
