"""
Exercise 1: Token Counting Fundamentals
========================================

Learn how tokens are counted and how to estimate token usage.

KEY CONCEPTS:
- 1 token ≈ 4 characters (English text)
- Code is often more efficient (symbols, keywords)
- Whitespace counts
- Structure (JSON, XML) adds tokens

IMPORTANT FOR EXAM:
- Understand approximate token calculations
- Know which operations are token-heavy
- Recognize when optimization is needed
"""

from typing import Dict, List
import json


class TokenEstimator:
    """Estimates token counts for different content types"""

    @staticmethod
    def estimate_text(text: str) -> int:
        """
        Estimate tokens for plain text.

        Rule of thumb: ~4 characters per token for English

        TODO: Implement token estimation
        """
        # Simple estimation: divide character count by 4
        return len(text) // 4

    @staticmethod
    def estimate_code(code: str) -> int:
        """
        Estimate tokens for code.

        Code often tokenizes more efficiently due to:
        - Keywords (def, if, class)
        - Common symbols ((), {}, [])
        - Operators (+, -, *, /)

        Rule of thumb: ~3.5 characters per token for code

        TODO: Implement code token estimation
        """
        return len(code) * 10 // 35  # More efficient than prose

    @staticmethod
    def estimate_structured(data: dict) -> int:
        """
        Estimate tokens for structured data (JSON, XML).

        JSON has overhead:
        - Brackets, braces, quotes
        - Key names repeated
        - Formatting whitespace

        TODO: Implement structured data estimation
        """
        json_str = json.dumps(data, indent=2)
        # JSON is less efficient due to structural overhead
        return len(json_str) // 3

    @staticmethod
    def compare_formats(data: dict) -> Dict[str, int]:
        """
        Compare token usage across different formats.

        Returns:
            Dict with format -> estimated tokens
        """
        results = {}

        # JSON with indentation
        json_pretty = json.dumps(data, indent=2)
        results['json_pretty'] = len(json_pretty) // 3

        # JSON compact
        json_compact = json.dumps(data)
        results['json_compact'] = len(json_compact) // 3

        # Python repr (similar to dict string)
        python_repr = str(data)
        results['python_repr'] = len(python_repr) // 3

        return results


def test_token_estimation():
    """Test token estimation for different content types."""
    print("Testing Token Estimation...\n")
    print("="*70)

    estimator = TokenEstimator()

    # Test 1: Plain text
    print("\n1. Plain Text Token Estimation")
    print("-"*70)

    texts = [
        "Hello, world!",
        "This is a simple sentence.",
        "The quick brown fox jumps over the lazy dog. " * 5,
        "A" * 400,  # 400 characters
    ]

    for text in texts:
        tokens = estimator.estimate_text(text)
        chars = len(text)
        ratio = chars / tokens if tokens > 0 else 0
        print(f"Text: '{text[:50]}{'...' if len(text) > 50 else ''}'")
        print(f"  Chars: {chars}, Estimated tokens: {tokens}, Ratio: {ratio:.2f} chars/token\n")

    # Test 2: Code
    print("\n2. Code Token Estimation")
    print("-"*70)

    code_samples = [
        "def hello(): return 'world'",
        """
def calculate_sum(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total
""",
        """
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def greet(self) -> str:
        return f"Hello, {self.name}!"
""",
    ]

    for code in code_samples:
        tokens = estimator.estimate_code(code)
        chars = len(code)
        ratio = chars / tokens if tokens > 0 else 0
        print(f"Code: '{code.strip()[:50]}{'...' if len(code.strip()) > 50 else ''}'")
        print(f"  Chars: {chars}, Estimated tokens: {tokens}, Ratio: {ratio:.2f} chars/token\n")

    # Test 3: Structured data
    print("\n3. Structured Data Token Estimation")
    print("-"*70)

    data_samples = [
        {"name": "Alice", "age": 30},
        {
            "users": [
                {"id": 1, "name": "Alice", "email": "alice@example.com"},
                {"id": 2, "name": "Bob", "email": "bob@example.com"},
                {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
            ]
        },
        {
            "config": {
                "database": {
                    "host": "localhost",
                    "port": 5432,
                    "name": "mydb",
                    "credentials": {
                        "user": "admin",
                        "password": "secret"
                    }
                },
                "cache": {
                    "enabled": True,
                    "ttl": 3600
                }
            }
        }
    ]

    for data in data_samples:
        tokens = estimator.estimate_structured(data)
        json_str = json.dumps(data, indent=2)
        chars = len(json_str)
        ratio = chars / tokens if tokens > 0 else 0
        print(f"Data: {json.dumps(data, indent=2)[:100]}{'...' if len(json_str) > 100 else ''}")
        print(f"  Chars: {chars}, Estimated tokens: {tokens}, Ratio: {ratio:.2f} chars/token\n")

    # Test 4: Format comparison
    print("\n4. Format Comparison")
    print("-"*70)

    sample_data = {
        "users": [
            {"id": i, "name": f"User{i}", "email": f"user{i}@example.com"}
            for i in range(10)
        ]
    }

    format_tokens = estimator.compare_formats(sample_data)

    print("Same data in different formats:")
    for format_name, tokens in sorted(format_tokens.items(), key=lambda x: x[1]):
        print(f"  {format_name:20s}: {tokens:5d} tokens")

    savings = format_tokens['json_pretty'] - format_tokens['json_compact']
    print(f"\n  Savings (compact vs pretty): {savings} tokens ({savings/format_tokens['json_pretty']*100:.1f}%)")

    print("\n" + "="*70)
    print("✅ Token estimation complete!")


def demonstrate_optimization():
    """Demonstrate token optimization strategies."""
    print("\n\n" + "="*70)
    print("TOKEN OPTIMIZATION STRATEGIES")
    print("="*70)

    # Strategy 1: Compact JSON
    print("\n1. Use Compact JSON Format")
    print("-"*70)

    data = {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}

    pretty = json.dumps(data, indent=2)
    compact = json.dumps(data)

    print(f"Pretty JSON:\n{pretty}")
    print(f"Tokens: ~{len(pretty) // 3}")

    print(f"\nCompact JSON:\n{compact}")
    print(f"Tokens: ~{len(compact) // 3}")

    print(f"\n✓ Saved ~{(len(pretty) - len(compact)) // 3} tokens")

    # Strategy 2: Avoid redundant information
    print("\n2. Avoid Redundant Information")
    print("-"*70)

    redundant = """
The user's name is Alice.
The user's email is alice@example.com.
The user's age is 30.
The user's role is admin.
"""

    concise = """
User: Alice, alice@example.com, 30, admin
"""

    print(f"Redundant: {len(redundant)} chars, ~{len(redundant) // 4} tokens")
    print(f"Concise: {len(concise)} chars, ~{len(concise) // 4} tokens")
    print(f"✓ Saved ~{(len(redundant) - len(concise)) // 4} tokens")

    # Strategy 3: Use structured output
    print("\n3. Use Structured Output")
    print("-"*70)

    prose = """
Based on the analysis, the system has 3 critical issues and 7 warnings.
The critical issues are: database connection failure, memory leak in auth module,
and missing configuration for email service. The warnings include...
"""

    structured = {
        "critical": 3,
        "warnings": 7,
        "issues": ["db_connection", "memory_leak", "missing_config"]
    }

    print(f"Prose: ~{len(prose) // 4} tokens")
    print(f"Structured: ~{len(json.dumps(structured)) // 3} tokens")
    print(f"✓ More efficient AND easier to parse")


if __name__ == "__main__":
    test_token_estimation()
    demonstrate_optimization()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Rough estimate: ~4 chars/token for text, ~3.5 for code")
    print("2. Compact JSON uses fewer tokens than pretty-printed")
    print("3. Structured output is token-efficient and easier to parse")
    print("4. Avoid redundant information and verbose prose")
    print("5. Code tokenizes efficiently due to common keywords/symbols")
    print("\nEXAM TIP: You don't need exact token counts, just relative understanding!")
