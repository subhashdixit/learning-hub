"""
Exercise 2: Memory Types Classification
========================================

Learn to correctly identify and create different memory types.

MEMORY TYPES:
1. USER - role, preferences, knowledge, responsibilities
2. FEEDBACK - guidance on what to do/avoid (with Why & How to apply)
3. PROJECT - ongoing work, deadlines, decisions (with Why & How to apply)
4. REFERENCE - pointers to external resources

KEY RULE: What NOT to save
- Code patterns (derive from reading files)
- Git history (use git log)
- Debugging solutions (in the code already)
- Ephemeral task details
"""

from typing import Tuple, List
from dataclasses import dataclass


@dataclass
class MemoryScenario:
    """A scenario requiring memory classification"""
    user_says: str
    correct_type: str
    reason: str
    should_save: bool = True


# Scenarios to classify
SCENARIOS = [
    MemoryScenario(
        user_says="I'm a data scientist working on the ML pipeline",
        correct_type="user",
        reason="User's role and current focus",
        should_save=True
    ),
    MemoryScenario(
        user_says="Don't use mocks for database tests - we got burned last quarter",
        correct_type="feedback",
        reason="Guidance on approach with reason why (past incident)",
        should_save=True
    ),
    MemoryScenario(
        user_says="We're in a merge freeze until Thursday for the mobile release",
        correct_type="project",
        reason="Ongoing project constraint with deadline",
        should_save=True
    ),
    MemoryScenario(
        user_says="Check the Linear project 'INGEST' for pipeline bugs",
        correct_type="reference",
        reason="Pointer to external resource location",
        should_save=True
    ),
    MemoryScenario(
        user_says="Here's how the auth middleware works: [explains code]",
        correct_type="none",
        reason="Code pattern - derive from reading files, not memory",
        should_save=False
    ),
    MemoryScenario(
        user_says="I fixed that bug in commit abc123",
        correct_type="none",
        reason="Git history - use git log, not memory",
        should_save=False
    ),
    MemoryScenario(
        user_says="I've been writing Go for 10 years but new to React here",
        correct_type="user",
        reason="User's expertise levels - helps tailor explanations",
        should_save=True
    ),
    MemoryScenario(
        user_says="Yeah, the bundled PR approach worked well here, keep doing that",
        correct_type="feedback",
        reason="Validation of approach - feedback from success, not just corrections",
        should_save=True
    ),
    MemoryScenario(
        user_says="Legal flagged the auth rewrite - it's for compliance, not tech debt",
        correct_type="project",
        reason="Project context with motivation - shapes scope decisions",
        should_save=True
    ),
    MemoryScenario(
        user_says="The oncall dashboard is at grafana.internal/d/api-latency",
        correct_type="reference",
        reason="External resource URL for monitoring",
        should_save=True
    ),
    MemoryScenario(
        user_says="We use the factory pattern for creating database connections",
        correct_type="none",
        reason="Architecture pattern - derive from reading code",
        should_save=False
    ),
    MemoryScenario(
        user_says="Can you summarize what we did yesterday?",
        correct_type="none",
        reason="Ephemeral context - not useful across conversations",
        should_save=False
    ),
]


def classify_memory(user_input: str) -> Tuple[str, str, bool]:
    """
    Classify user input into memory type.

    Returns:
        Tuple of (memory_type, reason, should_save)

    CLASSIFICATION RULES:
    - USER: Role, preferences, expertise, responsibilities
    - FEEDBACK: Guidance with WHY and HOW TO APPLY
    - PROJECT: Ongoing work, deadlines, decisions with context
    - REFERENCE: External resource pointers
    - NONE: Code patterns, git history, debugging, ephemeral

    TODO: Implement classification logic
    """

    # Hint: Look for keywords and context:
    # - "I'm a...", "I work on...", "I prefer..." -> user
    # - "Don't...", "Stop...", "Keep doing...", "We got burned..." -> feedback
    # - "We're in...", "deadline", "freeze", "for compliance" -> project
    # - "Check...", URLs, "dashboard at...", "in Linear..." -> reference
    # - Code explanations, git commits, patterns -> none

    lower_input = user_input.lower()

    # Check for DO NOT SAVE patterns first
    if any(keyword in lower_input for keyword in [
        'how the', 'works:', 'pattern for', 'architecture',
        'commit ', 'git ', 'fixed that', 'summarize what',
        'yesterday', 'debugging'
    ]):
        return ("none", "Code/git/ephemeral - not saved", False)

    # USER type
    if any(keyword in lower_input for keyword in [
        "i'm a", "i work", "i've been", "my role",
        "i prefer", "new to", "experience"
    ]):
        return ("user", "User profile/role/preferences", True)

    # FEEDBACK type
    if any(keyword in lower_input for keyword in [
        "don't", "stop", "keep doing", "got burned",
        "worked well", "yeah", "perfect"
    ]):
        return ("feedback", "Guidance from correction or validation", True)

    # PROJECT type
    if any(keyword in lower_input for keyword in [
        "freeze", "deadline", "until", "for compliance",
        "for the", "we're in", "flagged"
    ]):
        return ("project", "Project context/deadline/decision", True)

    # REFERENCE type
    if any(keyword in lower_input for keyword in [
        "check", "dashboard", "linear", "grafana",
        "http", ".internal", "project '"
    ]):
        return ("reference", "External resource pointer", True)

    return ("unknown", "Unable to classify", False)


def format_memory_content(scenario: MemoryScenario) -> str:
    """
    Format memory content based on type.

    FORMATTING RULES:
    - USER: Direct description
    - FEEDBACK: Rule, then **Why:** and **How to apply:**
    - PROJECT: Fact, then **Why:** and **How to apply:**
    - REFERENCE: Location and purpose
    """
    if scenario.correct_type == "user":
        return scenario.user_says

    elif scenario.correct_type == "feedback":
        # Extract rule and reason
        if "got burned" in scenario.user_says or "worked well" in scenario.user_says:
            return f"{scenario.user_says}\n\n**Why:** {scenario.reason}\n**How to apply:** Apply this guidance to similar scenarios."
        return scenario.user_says

    elif scenario.correct_type == "project":
        # Extract fact and context
        return f"{scenario.user_says}\n\n**Why:** {scenario.reason}\n**How to apply:** Consider this constraint in planning."

    elif scenario.correct_type == "reference":
        return f"{scenario.user_says}\nUse this resource for {scenario.reason}."

    return scenario.user_says


def test_classification():
    """Test memory type classification."""
    print("Testing Memory Type Classification...\n")
    print("="*70)

    correct = 0
    total = len(SCENARIOS)

    for i, scenario in enumerate(SCENARIOS, 1):
        print(f"\nScenario {i}:")
        print(f"User says: '{scenario.user_says}'")

        mem_type, reason, should_save = classify_memory(scenario.user_says)

        expected_type = scenario.correct_type if scenario.should_save else "none"
        is_correct = (mem_type == expected_type and should_save == scenario.should_save)

        if is_correct:
            correct += 1
            print(f"✓ CORRECT")
        else:
            print(f"✗ INCORRECT")

        print(f"  Your answer:     {mem_type} (save: {should_save})")
        print(f"  Expected answer: {expected_type} (save: {scenario.should_save})")
        print(f"  Reason: {scenario.reason}")

        if is_correct and scenario.should_save:
            formatted = format_memory_content(scenario)
            print(f"  Formatted content:")
            for line in formatted.split('\n'):
                print(f"    {line}")

        print("-"*70)

    print(f"\n{'='*70}")
    print(f"Score: {correct}/{total} ({correct/total*100:.0f}%)")
    print(f"{'='*70}")

    if correct == total:
        print("\n🎉 Perfect score! You understand memory types!")
    elif correct >= total * 0.8:
        print("\n✅ Good job! Review the incorrect ones.")
    else:
        print("\n⚠️  Keep practicing. Key points:")
        print("  - USER: Role, preferences, expertise")
        print("  - FEEDBACK: Guidance with Why + How to apply")
        print("  - PROJECT: Ongoing work with context")
        print("  - REFERENCE: External resource pointers")
        print("  - DON'T SAVE: Code patterns, git history, ephemeral")

    return correct == total


if __name__ == "__main__":
    success = test_classification()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. USER memories: Who the user is, their expertise level")
    print("2. FEEDBACK memories: What to do/avoid (Why + How to apply)")
    print("3. PROJECT memories: Current work context (Why + How to apply)")
    print("4. REFERENCE memories: Where to find external info")
    print("5. DON'T SAVE: Code patterns, git history, debugging, ephemeral")
    print("\nCRITICAL: Memory is for context that can't be derived from code!")

    if not success:
        print("\n⚠️  Review incorrect classifications before moving on.")
