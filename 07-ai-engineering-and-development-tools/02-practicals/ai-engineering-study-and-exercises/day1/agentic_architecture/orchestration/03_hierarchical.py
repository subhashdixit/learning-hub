"""
Exercise 3: Hierarchical Orchestration
Learn: Main agent coordinating sub-agents
"""

def sub_agent_summarize(text):
    """Sub-agent 1: Summarize text"""
    print(f"   📝 Sub-agent 1: Summarizing text...")
    words = len(text.split())
    summary = f"Text has {words} words. Main topic: AI agents."
    print(f"      ✓ Summary created")
    return summary

def sub_agent_translate(text):
    """Sub-agent 2: Translate to Spanish"""
    print(f"   🌍 Sub-agent 2: Translating to Spanish...")
    # Simplified translation
    translation = "Texto sobre agentes de IA"
    print(f"      ✓ Translation done")
    return translation

def sub_agent_sentiment(text):
    """Sub-agent 3: Analyze sentiment"""
    print(f"   😊 Sub-agent 3: Analyzing sentiment...")
    sentiment = "positive"
    confidence = 0.85
    print(f"      ✓ Sentiment: {sentiment} ({confidence})")
    return {"sentiment": sentiment, "confidence": confidence}

def main_agent_coordinator(text):
    """
    Main agent that coordinates all sub-agents.
    Delegates work, collects results, and combines them.
    """
    print("=== HIERARCHICAL ORCHESTRATION ===\n")
    print("👔 Main Agent: Received task - analyze this text")
    print(f"   Text: '{text[:50]}...'\n")

    print("👔 Main Agent: Delegating to sub-agents...\n")

    # Delegate task 1
    summary = sub_agent_summarize(text)

    # Delegate task 2
    translation = sub_agent_translate(text)

    # Delegate task 3
    sentiment = sub_agent_sentiment(text)

    # Main agent combines all results
    print("\n👔 Main Agent: Collecting results from sub-agents...")

    final_report = {
        "original_text": text,
        "summary": summary,
        "translation": translation,
        "sentiment": sentiment
    }

    print("\n👔 Main Agent: Analysis complete!")
    print(f"\n📊 Final Report:")
    print(f"   - Summary: {final_report['summary']}")
    print(f"   - Translation: {final_report['translation']}")
    print(f"   - Sentiment: {final_report['sentiment']['sentiment']} "
          f"({final_report['sentiment']['confidence']})")

    return final_report

# Test it!
if __name__ == "__main__":
    text = "AI agents are revolutionizing software development by automating complex tasks and making intelligent decisions autonomously."

    result = main_agent_coordinator(text)
