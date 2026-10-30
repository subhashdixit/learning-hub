# AI Engineering and Development Tools — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — LLM capabilities, system boundaries and task design](#lesson-01)
- [02 — Prompt design, examples, schemas and failure handling](#lesson-02)
- [03 — Embeddings, vector databases, similarity and hybrid search](#lesson-03)
- [04 — RAG ingestion, chunking, retrieval, reranking and grounded answers](#lesson-04)
- [05 — Tool calling, schemas, MCP and authorization](#lesson-05)
- [06 — LangChain components, LangGraph state and durable workflows](#lesson-06)
- [07 — Agents, planning, memory, evaluation and failure analysis](#lesson-07)
- [08 — LLMOps, caching, cost, deployment and security](#lesson-08)
- [09 — Spec-driven development, Claude Code, Copilot and reusable skills](#lesson-09)

<a id="lesson-01"></a>

## 01 — LLM capabilities, system boundaries and task design

[Read the lesson](../01-theory/lesson-01-llm-system-design.md)

### Q001. Does structured output guarantee factual accuracy?

<details>
<summary>Answer</summary>

No. It can enforce syntax/schema while values remain wrong.

</details>

### Q002. Why start with a workflow?

<details>
<summary>Answer</summary>

A bounded sequence is easier to test, observe and control than an unnecessary open-ended agent loop.

</details>

### Q003. Are tokens words?

<details>
<summary>Answer</summary>

Not generally. Tokenization depends on the model and language/text content.

</details>

<a id="lesson-02"></a>

## 02 — Prompt design, examples, schemas and failure handling

[Read the lesson](../01-theory/lesson-02-prompt-contracts.md)

### Q004. What should an uncertainty policy say?

<details>
<summary>Answer</summary>

When evidence is missing or conflicting, return a defined unknown/abstain result instead of inventing a value.

</details>

### Q005. Why version prompts?

<details>
<summary>Answer</summary>

Changes need reproducible comparison against the same evaluation set.

</details>

### Q006. Why validate after generation?

<details>
<summary>Answer</summary>

Language instructions are not a substitute for executable schema and business constraints.

</details>

<a id="lesson-03"></a>

## 03 — Embeddings, vector databases, similarity and hybrid search

[Read the lesson](../01-theory/lesson-03-embeddings-and-vector-search.md)

### Q007. Why not mix embedding versions?

<details>
<summary>Answer</summary>

Their coordinate systems/objectives may not be compatible even if dimensions match.

</details>

### Q008. What does ANN trade?

<details>
<summary>Answer</summary>

Speed/memory/update properties against exact-neighbour retrieval quality under particular settings.

</details>

### Q009. Why hybrid search?

<details>
<summary>Answer</summary>

Exact keyword and semantic signals can complement each other for IDs, rare terms and paraphrases.

</details>

<a id="lesson-04"></a>

## 04 — RAG ingestion, chunking, retrieval, reranking and grounded answers

[Read the lesson](../01-theory/lesson-04-rag-pipeline.md)

### Q010. Retrieval failure versus generation failure?

<details>
<summary>Answer</summary>

The right evidence may be missing, or present but misused; diagnose them separately.

</details>

### Q011. Does bigger top-k always help?

<details>
<summary>Answer</summary>

No. Extra irrelevant/duplicate context can increase cost and distract the generator.

</details>

### Q012. What should an unanswerable case do?

<details>
<summary>Answer</summary>

Produce the defined abstention or clarification behaviour instead of manufacturing evidence.

</details>

<a id="lesson-05"></a>

## 05 — Tool calling, schemas, MCP and authorization

[Read the lesson](../01-theory/lesson-05-tools-and-mcp.md)

### Q013. Does a proposed tool call authorize the action?

<details>
<summary>Answer</summary>

No. The host must enforce identity, scope, policy and any required user approval.

</details>

### Q014. What does MCP standardize?

<details>
<summary>Answer</summary>

Interfaces for connecting AI applications with external capabilities under the protocol; it is not blanket trust.

</details>

### Q015. Why idempotency?

<details>
<summary>Answer</summary>

Retries should not duplicate an intended one-time external effect.

</details>

<a id="lesson-06"></a>

## 06 — LangChain components, LangGraph state and durable workflows

[Read the lesson](../01-theory/lesson-06-langchain-and-langgraph.md)

### Q016. Why explicit state?

<details>
<summary>Answer</summary>

It makes progress, routing, resumption and validation inspectable.

</details>

### Q017. Does persistence prevent duplicate writes?

<details>
<summary>Answer</summary>

No. External effects still need an idempotency/replay strategy.

</details>

### Q018. When use deterministic nodes?

<details>
<summary>Answer</summary>

For operations with precise rules such as schema checks, arithmetic and permission enforcement.

</details>

<a id="lesson-07"></a>

## 07 — Agents, planning, memory, evaluation and failure analysis

[Read the lesson](../01-theory/lesson-07-agent-evaluations.md)

### Q019. When is an agent useful?

<details>
<summary>Answer</summary>

When the task benefits from dynamic action choices that a simpler bounded workflow cannot handle as well.

</details>

### Q020. Why trace failures by stage?

<details>
<summary>Answer</summary>

Different failure sources require different fixes; a prompt change cannot repair a broken tool permission check.

</details>

### Q021. What should a rubric include?

<details>
<summary>Answer</summary>

Observable task outcomes and constraints, including disallowed actions and acceptable abstention.

</details>

<a id="lesson-08"></a>

## 08 — LLMOps, caching, cost, deployment and security

[Read the lesson](../01-theory/lesson-08-llm-operations.md)

### Q022. Why version the corpus?

<details>
<summary>Answer</summary>

Changing retrieved evidence changes outputs even if model and prompt remain fixed.

</details>

### Q023. Why permission-aware caching?

<details>
<summary>Answer</summary>

An answer suitable for one identity may disclose information to another.

</details>

### Q024. Average versus tail latency?

<details>
<summary>Answer</summary>

A low average can hide slow high-percentile requests that harm user experience or exceed deadlines.

</details>

<a id="lesson-09"></a>

## 09 — Spec-driven development, Claude Code, Copilot and reusable skills

[Read the lesson](../01-theory/lesson-09-spec-driven-coding.md)

### Q025. What is spec-driven development?

<details>
<summary>Answer</summary>

Use explicit requirements and acceptance criteria to guide implementation and verification.

</details>

### Q026. Why review generated diffs?

<details>
<summary>Answer</summary>

An assistant can introduce incorrect logic, unsafe defaults or unrelated changes despite plausible explanations.

</details>

### Q027. What makes a reusable skill useful?

<details>
<summary>Answer</summary>

A clear recurring trigger, scoped procedure, required resources and concrete output/verification contract.

</details>
