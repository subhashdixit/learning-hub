"""
Exercise 4: Memory Index Management
====================================

Learn to manage the MEMORY.md index efficiently.

KEY CONCEPTS:
- MEMORY.md is ALWAYS loaded (first 200 lines)
- Individual memory files loaded on demand
- Index entries must be concise (~150 chars)
- Organize semantically, not chronologically

INDEX FORMAT:
- [Title](file.md) — one-line description

BEST PRACTICES:
1. Keep entries under 150 characters
2. Group by topic/domain
3. Most relevant memories at top
4. Remove stale entries
5. No duplicate entries
"""

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class IndexEntry:
    """Represents an entry in MEMORY.md"""
    title: str
    filename: str
    description: str

    def __str__(self) -> str:
        return f"- [{self.title}]({self.filename}) — {self.description}"

    def length(self) -> int:
        """Character length of the entry"""
        return len(str(self))


class MemoryIndex:
    """Manages the MEMORY.md index"""

    def __init__(self):
        self.entries: List[IndexEntry] = []

    def add_entry(self, title: str, filename: str, description: str) -> bool:
        """
        Add an entry to the index.

        Returns:
            True if added, False if too long or duplicate

        RULES:
        - Entry must be < 150 characters
        - No duplicate filenames
        - Description must be specific enough to determine relevance
        """
        # TODO: Implement entry addition with validation

        # Check for duplicates
        if any(e.filename == filename for e in self.entries):
            print(f"⚠️  Duplicate filename: {filename}")
            return False

        entry = IndexEntry(title, filename, description)

        # Check length
        if entry.length() > 150:
            print(f"⚠️  Entry too long: {entry.length()} chars (max 150)")
            print(f"    '{entry}'")
            return False

        # Check if description is specific enough
        if len(description.split()) < 4:
            print(f"⚠️  Description too vague: '{description}'")
            return False

        self.entries.append(entry)
        return True

    def organize_by_topic(self) -> Dict[str, List[IndexEntry]]:
        """
        Group entries by topic.

        TOPICS:
        - User Profile
        - Development Preferences
        - Project Context
        - External Resources
        - Team Conventions

        TODO: Implement topic grouping
        """
        topics = {
            "User Profile": [],
            "Development Preferences": [],
            "Project Context": [],
            "External Resources": [],
            "Team Conventions": []
        }

        for entry in self.entries:
            # Simple keyword-based classification
            content_lower = (entry.title + " " + entry.description).lower()

            if any(kw in content_lower for kw in ["user", "role", "expertise", "engineer"]):
                topics["User Profile"].append(entry)
            elif any(kw in content_lower for kw in ["prefer", "testing", "code style", "approach"]):
                topics["Development Preferences"].append(entry)
            elif any(kw in content_lower for kw in ["project", "sprint", "deadline", "freeze"]):
                topics["Project Context"].append(entry)
            elif any(kw in content_lower for kw in ["url", "dashboard", "linear", "docs", "wiki"]):
                topics["External Resources"].append(entry)
            else:
                topics["Team Conventions"].append(entry)

        return topics

    def generate_index_content(self) -> str:
        """
        Generate the full MEMORY.md content.

        FORMAT:
        # Memory Index

        ## [Topic]
        - [Entry 1]
        - [Entry 2]

        ## [Topic 2]
        - [Entry 3]

        RULES:
        - Organized by topic
        - Most important at top
        - Empty sections omitted
        - Total lines should stay under 200
        """
        topics = self.organize_by_topic()

        lines = ["# Memory Index\n"]

        # Define topic order (most important first)
        topic_order = [
            "User Profile",
            "Development Preferences",
            "Project Context",
            "External Resources",
            "Team Conventions"
        ]

        for topic in topic_order:
            entries = topics[topic]
            if entries:  # Only include non-empty sections
                lines.append(f"\n## {topic}\n")
                for entry in entries:
                    lines.append(f"{entry}\n")

        content = "".join(lines)

        # Check total line count
        line_count = content.count('\n')
        if line_count > 200:
            print(f"⚠️  Index has {line_count} lines (max 200 recommended)")

        return content

    def prune_stale(self, stale_filenames: List[str]) -> int:
        """Remove stale entries from index."""
        original_count = len(self.entries)
        self.entries = [e for e in self.entries if e.filename not in stale_filenames]
        removed = original_count - len(self.entries)
        return removed

    def get_entry(self, filename: str) -> IndexEntry:
        """Get entry by filename."""
        for entry in self.entries:
            if entry.filename == filename:
                return entry
        return None


def test_index_management():
    """Test memory index management."""
    print("Testing Memory Index Management...\n")
    print("="*70)

    index = MemoryIndex()

    # Test 1: Add valid entries
    print("1. Adding entries...\n")

    test_entries = [
        ("User Role", "user_role.md", "Senior backend engineer, 10 years Python, API design expert"),
        ("Testing Approach", "testing_pref.md", "Prefer integration tests over mocks for database code"),
        ("Current Sprint", "sprint_q1.md", "Working on API optimization, deadline March 31, 2026"),
        ("Dashboard URL", "grafana_dashboard.md", "Oncall latency dashboard at grafana.internal/d/api-latency"),
        ("Code Review", "code_review.md", "Team prefers small PRs, max 500 lines per review"),

        # Test edge cases
        ("Too Long Entry", "long.md", "This is a very long description that goes on and on and on and provides way too much detail that should really be in the memory file itself rather than in the index description which should be concise"),
        ("Short", "short.md", "Too vague"),  # Should fail - too vague
        ("Duplicate", "user_role.md", "Another user role entry"),  # Should fail - duplicate
    ]

    success_count = 0
    for title, filename, description in test_entries:
        result = index.add_entry(title, filename, description)
        if result:
            success_count += 1
            print(f"✓ Added: {title}")
        else:
            print(f"✗ Rejected: {title}")

    print(f"\nSuccessfully added: {success_count}/{len(test_entries)} entries")

    # Test 2: Organize by topic
    print(f"\n2. Organizing by topic...\n")
    topics = index.organize_by_topic()

    for topic, entries in topics.items():
        if entries:
            print(f"\n{topic}:")
            for entry in entries:
                print(f"  {entry}")

    # Test 3: Generate full index
    print(f"\n3. Generating MEMORY.md content...\n")
    content = index.generate_index_content()
    print(content)

    line_count = content.count('\n')
    print(f"Total lines: {line_count} (max 200 recommended)")

    # Test 4: Prune stale entries
    print(f"\n4. Pruning stale entries...\n")
    stale = ["sprint_q1.md"]  # Old sprint info
    removed = index.prune_stale(stale)
    print(f"Removed {removed} stale entries")

    print(f"\nRemaining entries: {len(index.entries)}")

    # Test 5: Check entry lengths
    print(f"\n5. Checking entry lengths...\n")
    for entry in index.entries:
        length = entry.length()
        status = "✓" if length <= 150 else "⚠️"
        print(f"{status} {length:3d} chars: {entry.title}")

    print("\n" + "="*70)
    print("✅ Index management test complete!")


if __name__ == "__main__":
    test_index_management()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. MEMORY.md is ALWAYS loaded (first 200 lines)")
    print("2. Individual memory files loaded on demand")
    print("3. Keep index entries under 150 characters")
    print("4. Organize by topic, not chronologically")
    print("5. Description must be specific enough to judge relevance")
    print("6. Prune stale entries to keep index clean")
    print("\nCRITICAL: Index is for discovery, not storage!")
    print("Put detailed content in the memory files, not the index.")
