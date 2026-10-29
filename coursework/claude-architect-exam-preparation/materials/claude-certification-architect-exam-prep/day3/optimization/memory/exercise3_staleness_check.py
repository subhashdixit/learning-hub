"""
Exercise 3: Memory Staleness Detection
======================================

Learn to detect and handle stale memories.

KEY CONCEPT:
- Memories can become outdated
- Always VERIFY before using
- Check if referenced files/functions still exist
- Trust current state over memory

STALENESS INDICATORS:
1. Named file/function doesn't exist
2. Conflicting current state
3. Old dates/versions
4. Architecture has changed
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import os


@dataclass
class Memory:
    """Represents a memory entry"""
    name: str
    type: str
    content: str
    created: datetime
    references: List[str] = None  # Files/functions referenced

    def __post_init__(self):
        if self.references is None:
            self.references = []


@dataclass
class CodebaseState:
    """Current state of codebase"""
    files: List[str]
    functions: Dict[str, List[str]]  # file -> functions
    architecture: str


class StalenessDe tector:
    """Detects if memories are stale"""

    def __init__(self, current_state: CodebaseState):
        self.current_state = current_state

    def check_staleness(self, memory: Memory) -> tuple[bool, str]:
        """
        Check if a memory is stale.

        Returns:
            (is_stale, reason)

        STALENESS RULES:
        1. If memory references files that don't exist -> STALE
        2. If memory references functions that don't exist -> STALE
        3. If memory has old project deadlines (>30 days) -> STALE
        4. If memory conflicts with current architecture -> STALE

        TODO: Implement staleness detection
        """

        # Rule 1: Check file references
        for ref in memory.references:
            if ref.endswith('.py') or ref.endswith('.js') or ref.endswith('.ts'):
                if ref not in self.current_state.files:
                    return (True, f"Referenced file '{ref}' no longer exists")

        # Rule 2: Check function references
        for ref in memory.references:
            if '::' in ref:  # format: file.py::function_name
                file_part, func_part = ref.split('::', 1)
                if file_part in self.current_state.functions:
                    if func_part not in self.current_state.functions[file_part]:
                        return (True, f"Function '{func_part}' not found in '{file_part}'")
                else:
                    return (True, f"File '{file_part}' not found")

        # Rule 3: Check date staleness (project memories with deadlines)
        if memory.type == "project":
            age_days = (datetime.now() - memory.created).days
            if age_days > 30:
                return (True, f"Project memory is {age_days} days old - likely outdated")

            # Check for deadline mentions in content
            if "until" in memory.content.lower() or "deadline" in memory.content.lower():
                # Extract date-like patterns (simplified)
                import re
                date_pattern = r'\d{4}-\d{2}-\d{2}'
                dates = re.findall(date_pattern, memory.content)
                for date_str in dates:
                    deadline = datetime.strptime(date_str, '%Y-%m-%d')
                    if deadline < datetime.now():
                        return (True, f"Deadline {date_str} has passed")

        # Rule 4: Check architecture conflicts
        if "architecture" in memory.content.lower():
            # Simple check: does memory mention current architecture?
            if self.current_state.architecture not in memory.content:
                return (True, f"Memory references old architecture (current: {self.current_state.architecture})")

        return (False, "Memory appears fresh")

    def verify_before_using(self, memory: Memory) -> Optional[str]:
        """
        Verification steps before using a memory.

        Returns:
            Warning message if verification fails, None if OK
        """
        is_stale, reason = self.check_staleness(memory)

        if is_stale:
            return f"⚠️  Memory '{memory.name}' may be stale: {reason}"

        # Additional verifications based on type
        if memory.type == "reference":
            # Should verify external URLs still work
            return "✓ Consider verifying external URL is still valid"

        if memory.type == "user":
            # User memories rarely go stale, but preferences might
            age_days = (datetime.now() - memory.created).days
            if age_days > 180:  # 6 months
                return "✓ User memory is old - preferences may have changed"

        return None


def test_staleness_detection():
    """Test staleness detection scenarios."""
    print("Testing Memory Staleness Detection...\n")
    print("="*70)

    # Setup current codebase state
    current_state = CodebaseState(
        files=["auth.py", "api.py", "models.py", "utils.py"],
        functions={
            "auth.py": ["login", "logout", "validate_token"],
            "api.py": ["get_user", "create_user", "delete_user"],
        },
        architecture="microservices"
    )

    detector = StalenessDetector(current_state)

    # Test scenarios
    scenarios = [
        # Scenario 1: Stale - references deleted file
        Memory(
            name="Old Auth Memory",
            type="reference",
            content="Check auth_old.py for authentication logic",
            created=datetime.now() - timedelta(days=10),
            references=["auth_old.py"]
        ),

        # Scenario 2: Stale - references deleted function
        Memory(
            name="Auth Function",
            type="reference",
            content="Use the refresh_token function in auth.py",
            created=datetime.now() - timedelta(days=5),
            references=["auth.py::refresh_token"]
        ),

        # Scenario 3: Fresh - valid references
        Memory(
            name="Current Auth",
            type="reference",
            content="Use the login function in auth.py",
            created=datetime.now() - timedelta(days=2),
            references=["auth.py::login"]
        ),

        # Scenario 4: Stale - old project deadline
        Memory(
            name="Release Freeze",
            type="project",
            content="Merge freeze until 2026-01-15 for release",
            created=datetime.now() - timedelta(days=90),
            references=[]
        ),

        # Scenario 5: Fresh - recent project memory
        Memory(
            name="Current Sprint",
            type="project",
            content="Working on API optimization this sprint",
            created=datetime.now() - timedelta(days=5),
            references=[]
        ),

        # Scenario 6: Stale - mentions old architecture
        Memory(
            name="Architecture Note",
            type="project",
            content="We use monolithic architecture for the backend",
            created=datetime.now() - timedelta(days=60),
            references=[]
        ),

        # Scenario 7: Fresh - user memory (rarely stale)
        Memory(
            name="User Role",
            type="user",
            content="User is a senior backend engineer",
            created=datetime.now() - timedelta(days=100),
            references=[]
        ),
    ]

    results = []
    for i, memory in enumerate(scenarios, 1):
        print(f"\nScenario {i}: {memory.name}")
        print(f"Type: {memory.type}")
        print(f"Content: {memory.content}")
        print(f"Age: {(datetime.now() - memory.created).days} days")

        is_stale, reason = detector.check_staleness(memory)
        warning = detector.verify_before_using(memory)

        print(f"Stale: {is_stale}")
        print(f"Reason: {reason}")
        if warning:
            print(f"Warning: {warning}")

        results.append({
            'memory': memory.name,
            'stale': is_stale,
            'reason': reason
        })

        print("-"*70)

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")

    stale_count = sum(1 for r in results if r['stale'])
    fresh_count = len(results) - stale_count

    print(f"Stale memories: {stale_count}")
    print(f"Fresh memories: {fresh_count}")

    print("\nStale memories detected:")
    for r in results:
        if r['stale']:
            print(f"  - {r['memory']}: {r['reason']}")

    print("\n✅ Staleness detection complete!")


if __name__ == "__main__":
    test_staleness_detection()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. ALWAYS verify memory before using it")
    print("2. Check if referenced files/functions still exist")
    print("3. Project memories with deadlines can become stale quickly")
    print("4. Architecture changes make related memories stale")
    print("5. When memory conflicts with current state, trust current state")
    print("\nCRITICAL: 'Memory says X exists' ≠ 'X exists now'")
    print("ALWAYS grep/read to verify before recommending from memory!")
