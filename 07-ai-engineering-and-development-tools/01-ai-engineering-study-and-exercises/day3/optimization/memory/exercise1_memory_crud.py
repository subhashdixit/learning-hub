"""
Exercise 1: Memory CRUD Operations
===================================

Learn to create, read, update, and delete memories with proper structure.

KEY CONCEPTS:
- Memory file structure with frontmatter
- MEMORY.md index management
- Proper memory naming and descriptions
"""

import os
from pathlib import Path
from typing import Dict, List


class MemoryManager:
    """Simulates Claude Code's memory system"""

    def __init__(self, memory_dir: str = "./test_memory"):
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(exist_ok=True)
        self.index_file = self.memory_dir / "MEMORY.md"

    def create_memory(self, name: str, description: str,
                     memory_type: str, content: str) -> str:
        """
        Create a new memory file with proper frontmatter.

        Args:
            name: Memory name (used in filename)
            description: One-line description for relevance matching
            memory_type: user, feedback, project, or reference
            content: The actual memory content

        Returns:
            Path to created file
        """
        # TODO: Implement memory file creation
        # 1. Create filename from name (e.g., "user_role" -> "user_role.md")
        # 2. Write frontmatter (---\nname: ...\ndescription: ...\ntype: ...\n---)
        # 3. Write content after frontmatter
        # 4. Add entry to MEMORY.md index

        filename = f"{name.replace(' ', '_').lower()}.md"
        filepath = self.memory_dir / filename

        frontmatter = f"""---
name: {name}
description: {description}
type: {memory_type}
---

{content}
"""

        with open(filepath, 'w') as f:
            f.write(frontmatter)

        self._add_to_index(name, filename, description)

        return str(filepath)

    def read_memory(self, filename: str) -> Dict[str, str]:
        """
        Read a memory file and parse frontmatter + content.

        Returns:
            Dict with 'name', 'description', 'type', 'content'
        """
        # TODO: Implement memory reading
        # 1. Read file
        # 2. Parse frontmatter (between --- markers)
        # 3. Extract content after frontmatter
        # 4. Return structured dict

        filepath = self.memory_dir / filename

        if not filepath.exists():
            raise FileNotFoundError(f"Memory file not found: {filename}")

        with open(filepath, 'r') as f:
            content = f.read()

        # Split frontmatter and content
        parts = content.split('---\n')
        if len(parts) < 3:
            raise ValueError("Invalid memory file format")

        frontmatter_lines = parts[1].strip().split('\n')
        memory_content = parts[2].strip()

        memory_data = {'content': memory_content}
        for line in frontmatter_lines:
            if ':' in line:
                key, value = line.split(':', 1)
                memory_data[key.strip()] = value.strip()

        return memory_data

    def update_memory(self, filename: str, **updates) -> None:
        """
        Update specific fields in a memory file.

        Args:
            filename: Memory file to update
            **updates: Fields to update (name, description, type, content)
        """
        # TODO: Implement memory update
        # 1. Read existing memory
        # 2. Update specified fields
        # 3. Write back with proper formatting
        # 4. Update MEMORY.md if name/description changed

        memory = self.read_memory(filename)

        # Update fields
        for key, value in updates.items():
            if key in memory:
                memory[key] = value

        # Rewrite file
        frontmatter = f"""---
name: {memory['name']}
description: {memory['description']}
type: {memory['type']}
---

{memory['content']}
"""

        filepath = self.memory_dir / filename
        with open(filepath, 'w') as f:
            f.write(frontmatter)

        # Update index if needed
        if 'name' in updates or 'description' in updates:
            self._update_index(filename, memory['name'], memory['description'])

    def delete_memory(self, filename: str) -> None:
        """Delete a memory file and remove from index."""
        # TODO: Implement memory deletion
        # 1. Delete the file
        # 2. Remove from MEMORY.md index

        filepath = self.memory_dir / filename
        if filepath.exists():
            filepath.unlink()

        self._remove_from_index(filename)

    def _add_to_index(self, name: str, filename: str, description: str) -> None:
        """Add entry to MEMORY.md index."""
        entry = f"- [{name}]({filename}) — {description}\n"

        with open(self.index_file, 'a') as f:
            f.write(entry)

    def _update_index(self, filename: str, new_name: str, new_desc: str) -> None:
        """Update an entry in MEMORY.md index."""
        if not self.index_file.exists():
            return

        with open(self.index_file, 'r') as f:
            lines = f.readlines()

        # Find and update the line
        updated_lines = []
        for line in lines:
            if f"]({filename})" in line:
                updated_lines.append(f"- [{new_name}]({filename}) — {new_desc}\n")
            else:
                updated_lines.append(line)

        with open(self.index_file, 'w') as f:
            f.writelines(updated_lines)

    def _remove_from_index(self, filename: str) -> None:
        """Remove entry from MEMORY.md index."""
        if not self.index_file.exists():
            return

        with open(self.index_file, 'r') as f:
            lines = f.readlines()

        # Filter out the line
        filtered_lines = [line for line in lines if f"]({filename})" not in line]

        with open(self.index_file, 'w') as f:
            f.writelines(filtered_lines)

    def list_memories(self) -> List[str]:
        """List all memory files."""
        return [f.name for f in self.memory_dir.glob("*.md")
                if f.name != "MEMORY.md"]


def test_memory_crud():
    """Test all CRUD operations."""
    print("Testing Memory CRUD Operations...\n")

    # Clean up test directory
    import shutil
    if os.path.exists("./test_memory"):
        shutil.rmtree("./test_memory")

    manager = MemoryManager()

    # Test 1: Create memories
    print("1. Creating memories...")
    manager.create_memory(
        name="User Role",
        description="User is a senior backend engineer with 10 years Python experience",
        memory_type="user",
        content="User specializes in API design and database optimization. "
                "Prefers FastAPI over Flask. Strong in PostgreSQL."
    )

    manager.create_memory(
        name="Testing Preference",
        description="User prefers integration tests over mocks for database code",
        memory_type="feedback",
        content="Don't mock the database in these tests. "
                "**Why:** Prior incident where mock/prod divergence masked a broken migration.\n"
                "**How to apply:** Use real database for integration tests."
    )

    print("✓ Created 2 memories")

    # Test 2: Read memories
    print("\n2. Reading memories...")
    user_mem = manager.read_memory("user_role.md")
    print(f"✓ Read '{user_mem['name']}' - type: {user_mem['type']}")

    # Test 3: Update memory
    print("\n3. Updating memory...")
    manager.update_memory(
        "user_role.md",
        content="User specializes in API design and database optimization. "
                "Prefers FastAPI over Flask. Strong in PostgreSQL. "
                "Currently learning Rust."
    )
    print("✓ Updated user_role.md")

    # Test 4: List all memories
    print("\n4. Listing all memories...")
    memories = manager.list_memories()
    print(f"✓ Found {len(memories)} memories: {memories}")

    # Test 5: Check MEMORY.md index
    print("\n5. Checking MEMORY.md index...")
    with open(manager.index_file, 'r') as f:
        index_content = f.read()
    print("Index contents:")
    print(index_content)

    # Test 6: Delete memory
    print("\n6. Deleting memory...")
    manager.delete_memory("testing_preference.md")
    print(f"✓ Deleted testing_preference.md")
    print(f"Remaining memories: {manager.list_memories()}")

    print("\n✅ All CRUD operations completed successfully!")

    # Cleanup
    shutil.rmtree("./test_memory")


if __name__ == "__main__":
    test_memory_crud()

    print("\n" + "="*60)
    print("EXERCISE COMPLETE!")
    print("="*60)
    print("\nKey Takeaways:")
    print("1. Memory files have frontmatter (name, description, type)")
    print("2. MEMORY.md is the index - always kept in sync")
    print("3. Content comes after frontmatter with blank line")
    print("4. Update existing memories rather than creating duplicates")
    print("5. Memory filenames are lowercase with underscores")
