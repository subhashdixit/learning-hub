"""
Zero-Shot Prompting Exercise - DEMONSTRATION VERSION

Zero-shot = Give Claude a task with NO examples, just clear instructions.
Claude uses its training to understand and complete the task.

Key exam points:
- When to use: Novel tasks, unique formats, quick iterations
- Strengths: Fast, flexible, no example needed
- Weaknesses: May need refinement for complex formats

Run: python3 01_zero_shot.py
"""

from typing import Dict, Any


def demo_zero_shot_classification():
    """
    EXAMPLE 1: Zero-shot sentiment classification

    THE PROMPT (what you send to Claude):
    """
    prompt = """Classify the sentiment of this text as positive, negative, or neutral.
Return only one word: positive, negative, or neutral.

Text: This product exceeded my expectations! Best purchase ever."""

    print("📝 PROMPT SENT:")
    print(prompt)
    print("\n" + "="*60)

    # What Claude would return
    response = "positive"

    print("✅ CLAUDE'S RESPONSE:")
    print(response)
    print("\n" + "="*60)

    print("💡 WHY THIS WORKS:")
    print("- Clear task: 'Classify the sentiment'")
    print("- Explicit format: 'Return only one word'")
    print("- Three options given: positive/negative/neutral")
    print("- No examples needed - Claude knows what sentiment is")


def demo_zero_shot_extraction():
    """
    EXAMPLE 2: Zero-shot entity extraction

    THE PROMPT:
    """
    prompt = """Extract all named entities from this text.
Identify: person names, companies, locations, dates.
Format as a simple list.

Text: Apple CEO Tim Cook announced the new iPhone launch in Cupertino on September 12, 2023."""

    print("📝 PROMPT SENT:")
    print(prompt)
    print("\n" + "="*60)

    # What Claude would return
    response = """- Tim Cook (Person)
- Apple (Company)
- iPhone (Product)
- Cupertino (Location)
- September 12, 2023 (Date)"""

    print("✅ CLAUDE'S RESPONSE:")
    print(response)
    print("\n" + "="*60)

    print("💡 WHY THIS WORKS:")
    print("- Specific task: 'Extract all named entities'")
    print("- Categories listed: person, companies, locations, dates")
    print("- Format specified: 'simple list'")
    print("- No examples - Claude recognizes entity types")


def demo_zero_shot_generation():
    """
    EXAMPLE 3: Zero-shot content generation

    THE PROMPT:
    """
    prompt = """Write a professional email about: requesting a meeting to discuss Q4 budget

Requirements:
- Professional tone
- 3 paragraphs: intro, body, closing
- Include a clear call-to-action
- Keep under 150 words"""

    print("📝 PROMPT SENT:")
    print(prompt)
    print("\n" + "="*60)

    # What Claude would return
    response = """Subject: Request for Q4 Budget Discussion Meeting

Dear [Recipient],

I hope this email finds you well. I'm reaching out to request a meeting to discuss our Q4 budget allocation and review our financial projections for the upcoming quarter.

Given the recent market changes and our current project pipeline, I believe it would be valuable to align on budget priorities and resource allocation. I've prepared a preliminary analysis that I'd like to share with you and get your input on key spending decisions.

Would you be available next week for a 30-minute discussion? Please let me know your availability, and I'll send a calendar invite.

Best regards"""

    print("✅ CLAUDE'S RESPONSE:")
    print(response)
    print("\n" + "="*60)

    print("💡 WHY THIS WORKS:")
    print("- Clear goal: write professional email")
    print("- Structure defined: 3 paragraphs")
    print("- Tone specified: professional")
    print("- Constraint: under 150 words, includes CTA")
    print("- No example email needed - Claude knows business writing")


def run_all_examples():
    """Run all zero-shot demonstration examples"""

    print("=" * 70)
    print("ZERO-SHOT PROMPTING - LEARNING DEMONSTRATIONS")
    print("=" * 70)
    print("\nThese examples show WHAT you'd send to Claude and WHAT you'd get back.")
    print("Perfect for learning patterns for the CCA exam!\n")

    # Example 1: Sentiment Classification
    print("\n" + "=" * 70)
    print("EXAMPLE 1: SENTIMENT CLASSIFICATION (Zero-Shot)")
    print("=" * 70)
    demo_zero_shot_classification()

    # Example 2: Entity Extraction
    print("\n" + "=" * 70)
    print("EXAMPLE 2: ENTITY EXTRACTION (Zero-Shot)")
    print("=" * 70)
    demo_zero_shot_extraction()

    # Example 3: Content Generation
    print("\n" + "=" * 70)
    print("EXAMPLE 3: CONTENT GENERATION (Zero-Shot)")
    print("=" * 70)
    demo_zero_shot_generation()

    # Key Takeaways
    print("\n" + "=" * 70)
    print("📚 KEY TAKEAWAYS FOR CCA EXAM:")
    print("=" * 70)
    print("""
✅ WHEN TO USE ZERO-SHOT:
   • Task is straightforward and well-defined
   • Claude has likely seen similar tasks in training
   • You need quick results without crafting examples
   • Simple classification, extraction, or generation

✅ BEST PRACTICES:
   • Clear, specific instructions
   • State the output format explicitly
   • Use simple, direct language
   • Define constraints (word count, tone, etc.)
   • One task per prompt (don't chain without CoT)

❌ WHEN ZERO-SHOT ISN'T ENOUGH:
   • Complex or unusual formatting → Use FEW-SHOT with examples
   • Multi-step reasoning → Use CHAIN-OF-THOUGHT
   • Structured data (JSON/XML) → Use STRUCTURED OUTPUT
   • Domain-specific formats → Show examples with FEW-SHOT

🎯 EXAM TIP:
   Know how to recognize scenarios where zero-shot is sufficient
   vs when you need to upgrade to few-shot or structured approaches.

   Questions may ask: "What's the BEST prompting technique for X?"
   - If X is simple/common → Zero-shot
   - If X needs format examples → Few-shot
   - If X needs reasoning → Chain-of-Thought
   - If X needs guaranteed structure → Structured output

📊 ZERO-SHOT CHARACTERISTICS:
   Speed: ⚡⚡⚡ Very Fast (no examples to process)
   Accuracy: ⭐⭐⭐ Good for common tasks
   Flexibility: ⚡⚡⚡ Very flexible
   Token Cost: 💰 Low (minimal prompt)
    """)


if __name__ == "__main__":
    run_all_examples()
