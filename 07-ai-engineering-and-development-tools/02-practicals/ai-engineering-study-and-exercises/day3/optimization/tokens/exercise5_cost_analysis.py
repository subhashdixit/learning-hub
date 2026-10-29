"""
Exercise 5: Cost-Performance Analysis
======================================

Learn to balance cost vs performance through smart model and strategy selection.

CLAUDE MODELS:
1. Opus 4.6 - Most capable, highest cost
2. Sonnet 4.6 - Balanced capability and cost
3. Haiku 4.5 - Fast and economical

KEY DECISIONS:
- Which model for which task?
- When to optimize tokens vs just running the task?
- Prompt caching strategies
- Agent tool for context isolation

EXAM-CRITICAL:
- Know when each model is appropriate
- Understand token cost trade-offs
- Recognize optimization vs over-optimization
"""

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum


class Model(Enum):
    OPUS = "claude-opus-4-6"
    SONNET = "claude-sonnet-4-6"
    HAIKU = "claude-haiku-4-5-20251001"


@dataclass
class TaskSpec:
    """Specification of a task"""
    name: str
    description: str
    complexity: str  # simple, moderate, complex
    tokens_required: int
    needs_reasoning: bool


@dataclass
class CostAnalysis:
    """Cost analysis for a task"""
    task: TaskSpec
    recommended_model: Model
    token_strategy: str
    estimated_cost: float
    rationale: str


class CostPerformanceAnalyzer:
    """Analyzes cost vs performance trade-offs"""

    # Relative cost multipliers (for illustration)
    COST_MULTIPLIER = {
        Model.OPUS: 3.0,
        Model.SONNET: 1.0,
        Model.HAIKU: 0.2
    }

    @staticmethod
    def select_model(task: TaskSpec) -> Model:
        """
        Select appropriate model for a task.

        SELECTION CRITERIA:
        - Simple tasks (<5K tokens, no complex reasoning) -> Haiku
        - Moderate tasks (5-20K tokens, some reasoning) -> Sonnet
        - Complex tasks (>20K tokens, heavy reasoning) -> Opus

        TODO: Implement model selection logic
        """

        # Complex reasoning required -> Opus
        if task.complexity == "complex" or task.needs_reasoning:
            return Model.OPUS

        # Simple, quick tasks -> Haiku
        if task.complexity == "simple" and task.tokens_required < 5000:
            return Model.HAIKU

        # Default: Sonnet (balanced)
        return Model.SONNET

    @staticmethod
    def token_strategy(task: TaskSpec) -> str:
        """
        Determine token optimization strategy.

        STRATEGIES:
        - no_optimization: Task is small enough
        - basic_limits: Use head_limit, limit parameters
        - agent_isolation: Use Agent tool to isolate context
        - chunking: Process in chunks
        """

        if task.tokens_required < 5000:
            return "no_optimization"
        elif task.tokens_required < 20000:
            return "basic_limits"
        elif task.tokens_required < 50000:
            return "agent_isolation"
        else:
            return "chunking"

    @staticmethod
    def analyze_task(task: TaskSpec) -> CostAnalysis:
        """
        Perform full cost-performance analysis.

        Returns:
            Cost analysis with recommendations
        """
        model = CostPerformanceAnalyzer.select_model(task)
        strategy = CostPerformanceAnalyzer.token_strategy(task)

        # Calculate estimated cost (simplified)
        base_cost = task.tokens_required * 0.001  # $1 per 1M tokens (simplified)
        multiplier = CostPerformanceAnalyzer.COST_MULTIPLIER[model]
        estimated_cost = base_cost * multiplier

        # Generate rationale
        rationale = f"Using {model.value} because: "

        if model == Model.OPUS:
            rationale += "Complex reasoning or high token count requires most capable model"
        elif model == Model.HAIKU:
            rationale += "Simple task with low token count - most economical choice"
        else:
            rationale += "Moderate complexity - balanced cost and capability"

        rationale += f" | Token strategy: {strategy}"

        return CostAnalysis(
            task=task,
            recommended_model=model,
            token_strategy=strategy,
            estimated_cost=estimated_cost,
            rationale=rationale
        )


def test_cost_analysis():
    """Test cost-performance analysis for various tasks."""
    print("Testing Cost-Performance Analysis...\n")
    print("="*70)

    analyzer = CostPerformanceAnalyzer()

    # Define test tasks
    tasks = [
        TaskSpec(
            name="Find specific function",
            description="Search for and read a specific function definition",
            complexity="simple",
            tokens_required=3000,
            needs_reasoning=False
        ),
        TaskSpec(
            name="Refactor module architecture",
            description="Analyze and refactor a complex module with multiple dependencies",
            complexity="complex",
            tokens_required=45000,
            needs_reasoning=True
        ),
        TaskSpec(
            name="Review pull request",
            description="Review code changes and provide feedback",
            complexity="moderate",
            tokens_required=15000,
            needs_reasoning=True
        ),
        TaskSpec(
            name="Fix simple bug",
            description="Locate and fix a straightforward bug in a small file",
            complexity="simple",
            tokens_required=2000,
            needs_reasoning=False
        ),
        TaskSpec(
            name="Explore unfamiliar codebase",
            description="Understand architecture of large codebase",
            complexity="complex",
            tokens_required=80000,
            needs_reasoning=True
        ),
        TaskSpec(
            name="Write unit tests",
            description="Write tests for a single function",
            complexity="simple",
            tokens_required=4000,
            needs_reasoning=False
        ),
        TaskSpec(
            name="Design API architecture",
            description="Design complete API structure with multiple endpoints",
            complexity="complex",
            tokens_required=25000,
            needs_reasoning=True
        ),
    ]

    # Analyze each task
    print("TASK ANALYSIS")
    print("="*70)

    analyses = []
    for task in tasks:
        analysis = analyzer.analyze_task(task)
        analyses.append(analysis)

        print(f"\nTask: {task.name}")
        print(f"Description: {task.description}")
        print(f"Complexity: {task.complexity} | Reasoning needed: {task.needs_reasoning}")
        print(f"Tokens: ~{task.tokens_required:,}")
        print("-"*70)
        print(f"✓ Recommended: {analysis.recommended_model.value}")
        print(f"  Strategy: {analysis.token_strategy}")
        print(f"  Estimated cost: ${analysis.estimated_cost:.4f}")
        print(f"  Rationale: {analysis.rationale}")

    # Cost comparison
    print("\n\n" + "="*70)
    print("COST COMPARISON")
    print("="*70)

    total_cost = sum(a.estimated_cost for a in analyses)
    print(f"\nTotal estimated cost: ${total_cost:.4f}")

    # Group by model
    by_model = {}
    for analysis in analyses:
        model = analysis.recommended_model
        if model not in by_model:
            by_model[model] = []
        by_model[model].append(analysis.task.name)

    print("\nTasks by model:")
    for model, task_names in sorted(by_model.items(), key=lambda x: x[0].value):
        print(f"\n{model.value}:")
        for task_name in task_names:
            print(f"  - {task_name}")

    print("\n" + "="*70)
    print("✅ Cost analysis complete!")


def demonstrate_optimization_scenarios():
    """Demonstrate when to optimize vs when not to."""
    print("\n\n" + "="*70)
    print("OPTIMIZATION DECISION SCENARIOS")
    print("="*70)

    scenarios = [
        {
            'task': 'Read a 100-line config file',
            'tokens': 2000,
            'optimize': False,
            'reason': 'Already small - optimization overhead > benefit',
            'action': 'Just read the full file'
        },
        {
            'task': 'Search for function in 10K line file',
            'tokens': 200000,
            'optimize': True,
            'reason': 'Huge token cost if read fully',
            'action': 'Grep for function location, then targeted Read'
        },
        {
            'task': 'Explore large unfamiliar codebase',
            'tokens': 500000,
            'optimize': True,
            'reason': 'Would blow up context completely',
            'action': 'Use Agent tool with subagent_type=Explore'
        },
        {
            'task': 'Read 5 small files (<200 lines each)',
            'tokens': 20000,
            'optimize': False,
            'reason': 'Manageable size, full reads give better context',
            'action': 'Read all 5 files fully'
        },
        {
            'task': 'Find all TODOs across 100 files',
            'tokens': 25000,
            'optimize': True,
            'reason': 'Grep can do this efficiently',
            'action': 'Grep(pattern="TODO", output_mode="files_with_matches")'
        },
        {
            'task': 'Understand specific function (200 lines)',
            'tokens': 4000,
            'optimize': False,
            'reason': 'Need full context of function',
            'action': 'Read the full function with surrounding context'
        },
    ]

    print("\nWhen to optimize vs when NOT to optimize:")
    print("="*70)

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. {scenario['task']}")
        print(f"   Tokens: ~{scenario['tokens']:,}")
        decision = "✓ OPTIMIZE" if scenario['optimize'] else "✗ DON'T OPTIMIZE"
        print(f"   Decision: {decision}")
        print(f"   Reason: {scenario['reason']}")
        print(f"   Action: {scenario['action']}")


def demonstrate_prompt_caching():
    """Demonstrate prompt caching benefits."""
    print("\n\n" + "="*70)
    print("PROMPT CACHING")
    print("="*70)

    print("\nWhat is prompt caching?")
    print("-"*70)
    print("Claude caches parts of the prompt that don't change between requests.")
    print("This reduces cost for repeated context (like large files or documentation).")

    print("\n\nWhen caching helps:")
    print("-"*70)

    scenarios = [
        {
            'scenario': 'Multiple questions about same large file',
            'context_tokens': 50000,
            'cached': True,
            'benefit': 'Pay full cost once, then reduced cost for follow-ups'
        },
        {
            'scenario': 'Iterating on code in same file',
            'context_tokens': 10000,
            'cached': True,
            'benefit': 'File context cached, only pay for new changes'
        },
        {
            'scenario': 'Different files each request',
            'context_tokens': 10000,
            'cached': False,
            'benefit': 'No caching benefit - context changes each time'
        },
    ]

    for scenario in scenarios:
        print(f"\nScenario: {scenario['scenario']}")
        print(f"  Context: ~{scenario['context_tokens']:,} tokens")
        print(f"  Cached: {scenario['cached']}")
        print(f"  Benefit: {scenario['benefit']}")


if __name__ == "__main__":
    test_cost_analysis()
    demonstrate_optimization_scenarios()
    demonstrate_prompt_caching()

    print("\n" + "="*70)
    print("EXERCISE COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Model selection: Haiku (simple), Sonnet (moderate), Opus (complex)")
    print("2. Don't over-optimize - small tasks aren't worth optimizing")
    print("3. Optimization threshold: ~5K+ tokens worth optimizing")
    print("4. Agent tool isolates expensive exploration from main context")
    print("5. Prompt caching reduces cost for repeated context")
    print("\nEXAM CRITICAL:")
    print("- Know which model for which task type")
    print("- Understand when optimization overhead > benefit")
    print("- Recognize caching opportunities")
    print("- Balance cost vs development speed")
    print("\n🎉 ALL TOKEN OPTIMIZATION EXERCISES COMPLETE!")
