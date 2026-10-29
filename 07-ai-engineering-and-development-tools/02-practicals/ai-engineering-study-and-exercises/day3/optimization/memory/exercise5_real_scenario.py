"""
Exercise 5: Real-World Memory Scenario
======================================

Apply all memory concepts in a realistic scenario.

SCENARIO:
You're working with a user over multiple conversation sessions.
You need to save, retrieve, verify, and use memories appropriately.

TASKS:
1. Identify what to save from conversations
2. Structure memories correctly
3. Verify memories before using
4. Update or remove stale memories
5. Apply memories to inform your work
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class ConversationTurn:
    """A turn in a conversation"""
    turn_id: int
    user_message: str
    session: int  # Which conversation session
    date: datetime


class MemorySystem:
    """Complete memory system simulation"""

    def __init__(self):
        self.memories: Dict[str, Dict] = {}  # filename -> memory data
        self.index: List[str] = []

    def should_save_memory(self, turn: ConversationTurn) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Decide if this turn should create/update a memory.

        Returns:
            (should_save, memory_type, reason)

        TODO: Implement decision logic
        """
        msg = turn.user_message.lower()

        # Check for memory-worthy content
        # USER type indicators
        if any(kw in msg for kw in ["i'm a", "i work", "i prefer", "my role", "i've been"]):
            return (True, "user", "User profile information")

        # FEEDBACK type indicators
        if any(kw in msg for kw in ["don't", "stop", "keep doing", "that worked", "perfect"]):
            return (True, "feedback", "Guidance on approach")

        # PROJECT type indicators
        if any(kw in msg for kw in ["deadline", "sprint", "working on", "freeze", "release"]):
            return (True, "project", "Project context")

        # REFERENCE type indicators
        if any(kw in msg for kw in ["check", "dashboard", "url", "wiki", "docs at"]):
            return (True, "reference", "External resource pointer")

        # DO NOT SAVE indicators
        if any(kw in msg for kw in ["the code", "this function", "commit", "yesterday"]):
            return (False, None, "Code/git/ephemeral content")

        return (False, None, "Not memory-worthy")

    def save_memory(self, memory_type: str, name: str,
                   description: str, content: str) -> str:
        """Save a memory with proper structure."""
        filename = f"{name.replace(' ', '_').lower()}.md"

        # Add Why and How to apply for feedback/project types
        if memory_type in ["feedback", "project"]:
            if "**Why:**" not in content and "**How to apply:**" not in content:
                content += "\n\n**Why:** [To be filled based on context]\n**How to apply:** [To be filled based on context]"

        self.memories[filename] = {
            'name': name,
            'description': description,
            'type': memory_type,
            'content': content,
            'created': datetime.now()
        }

        # Add to index
        index_entry = f"- [{name}]({filename}) — {description}"
        self.index.append(index_entry)

        return filename

    def verify_memory(self, filename: str, current_codebase: Dict) -> tuple[bool, str]:
        """
        Verify memory is still valid before using.

        Args:
            current_codebase: {'files': [...], 'functions': {...}}

        Returns:
            (is_valid, reason)
        """
        if filename not in self.memories:
            return (False, "Memory file not found")

        memory = self.memories[filename]
        content = memory['content']

        # Check if memory references files that no longer exist
        for file in current_codebase['files']:
            if file in content and file not in current_codebase['files']:
                return (False, f"Referenced file {file} no longer exists")

        # Check age for project memories
        if memory['type'] == 'project':
            age = (datetime.now() - memory['created']).days
            if age > 30:
                return (False, f"Project memory is {age} days old")

        return (True, "Memory is valid")

    def get_relevant_memories(self, query: str) -> List[str]:
        """
        Get memories relevant to a query.

        This simulates how Claude Code loads memories based on relevance.
        """
        relevant = []

        query_lower = query.lower()

        for filename, memory in self.memories.items():
            # Check if query keywords match description or content
            desc_lower = memory['description'].lower()
            content_lower = memory['content'].lower()

            if any(word in desc_lower or word in content_lower
                   for word in query_lower.split()):
                relevant.append(filename)

        return relevant


def run_scenario():
    """Run through a real-world scenario."""
    print("="*70)
    print("REAL-WORLD MEMORY SCENARIO")
    print("="*70)
    print("\nScenario: Multi-session work with a user on their API project\n")

    memory_system = MemorySystem()

    # Conversation turns across 3 sessions
    conversations = [
        # Session 1 - Initial setup
        ConversationTurn(1, "I'm a senior backend engineer working on our API rewrite", 1, datetime.now() - timedelta(days=7)),
        ConversationTurn(2, "I prefer FastAPI over Flask for this project", 1, datetime.now() - timedelta(days=7)),
        ConversationTurn(3, "Don't use mocks for database tests - we got burned by that before", 1, datetime.now() - timedelta(days=7)),
        ConversationTurn(4, "We're in a code freeze until March 15th for the release", 1, datetime.now() - timedelta(days=7)),

        # Session 2 - Development work (3 days later)
        ConversationTurn(5, "Check the API docs at https://api-docs.internal for endpoint specs", 2, datetime.now() - timedelta(days=4)),
        ConversationTurn(6, "The login function in auth.py handles OAuth flow", 2, datetime.now() - timedelta(days=4)),
        ConversationTurn(7, "Perfect, the integration test approach worked great", 2, datetime.now() - timedelta(days=4)),

        # Session 3 - Current session
        ConversationTurn(8, "What was our policy on database testing?", 3, datetime.now()),
        ConversationTurn(9, "Can you check if the code freeze is still active?", 3, datetime.now()),
    ]

    # Process turns from sessions 1 and 2
    print("Processing previous conversations...\n")
    print("-"*70)

    for turn in conversations[:7]:  # First 7 turns
        print(f"\nSession {turn.session}, Turn {turn.turn_id}:")
        print(f"User: '{turn.user_message}'")

        should_save, mem_type, reason = memory_system.should_save_memory(turn)

        if should_save:
            print(f"→ SAVE: {mem_type} memory ({reason})")

            # Create memory name and description
            name = f"Memory_{turn.turn_id}"
            if "i'm a" in turn.user_message.lower():
                name = "User Role"
                desc = "User is a senior backend engineer"
            elif "prefer" in turn.user_message.lower():
                name = "Framework Preference"
                desc = "User prefers FastAPI over Flask"
            elif "don't use mocks" in turn.user_message.lower():
                name = "Testing Policy"
                desc = "No mocks for database tests due to past issues"
            elif "freeze" in turn.user_message.lower():
                name = "Code Freeze"
                desc = "Code freeze until March 15th for release"
            elif "check" in turn.user_message.lower() and "http" in turn.user_message.lower():
                name = "API Docs URL"
                desc = "Internal API documentation location"
            elif "worked great" in turn.user_message.lower():
                name = "Integration Test Success"
                desc = "Integration test approach validated"
            else:
                desc = "Additional context"

            filename = memory_system.save_memory(mem_type, name, desc, turn.user_message)
            print(f"   Saved to: {filename}")
        else:
            print(f"→ SKIP: {reason}")

    # Current session - apply memories
    print("\n" + "="*70)
    print("CURRENT SESSION (Session 3)")
    print("="*70)

    current_codebase = {
        'files': ['auth.py', 'api.py', 'models.py', 'tests/'],
        'functions': {
            'auth.py': ['login', 'logout', 'validate_token']
        }
    }

    for turn in conversations[7:]:  # Turns 8-9
        print(f"\nTurn {turn.turn_id}:")
        print(f"User: '{turn.user_message}'")

        # Find relevant memories
        relevant = memory_system.get_relevant_memories(turn.user_message)

        if relevant:
            print(f"\nRelevant memories found: {len(relevant)}")

            for filename in relevant:
                print(f"\n  Checking: {filename}")

                # CRITICAL: Verify before using
                is_valid, reason = memory_system.verify_memory(filename, current_codebase)

                memory = memory_system.memories[filename]

                if is_valid:
                    print(f"  ✓ Valid: {reason}")
                    print(f"  Content: {memory['content'][:100]}...")
                    print(f"  → USE this memory to inform response")
                else:
                    print(f"  ✗ Stale: {reason}")
                    print(f"  → VERIFY current state instead of using memory")
        else:
            print("\nNo relevant memories found")

    # Summary
    print("\n" + "="*70)
    print("MEMORY SYSTEM STATE")
    print("="*70)

    print(f"\nTotal memories saved: {len(memory_system.memories)}")

    print("\nMemory Index (MEMORY.md):")
    for entry in memory_system.index:
        print(f"  {entry}")

    print("\n✅ Scenario complete!")


if __name__ == "__main__":
    run_scenario()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Save memories that persist across sessions")
    print("2. Don't save code patterns or ephemeral details")
    print("3. Structure feedback/project memories with Why + How to apply")
    print("4. ALWAYS verify memories before using them")
    print("5. Update stale memories or remove them")
    print("\nCRITICAL EXAM POINTS:")
    print("- Memory is for cross-conversation context")
    print("- Verification is mandatory before using")
    print("- Trust current state over stale memories")
    print("- Index (MEMORY.md) is always loaded, files on demand")
    print("\nYou're now ready for memory questions on the exam!")
