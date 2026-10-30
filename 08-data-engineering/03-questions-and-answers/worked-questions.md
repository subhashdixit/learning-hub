# Data Engineering — questions and worked answers

[Subject home](../README.md) · [Theory map](../01-theory/README.md) · [Practicals](../02-practicals/README.md)

Try each answer first, then expand the explanation. Questions follow the lesson order. Programming and SQL practice sets include additional runnable solutions in Practicals.

- [01 — Sources, grain, schema, contracts and data quality](#lesson-01)
- [02 — Batch ingestion, CDC, watermarks and idempotency](#lesson-02)
- [03 — Files, partitions, warehouses, lakes and dimensional models](#lesson-03)
- [04 — PySpark, lazy plans, partitions, joins and shuffles](#lesson-04)
- [05 — Streams, event time, windows, retries and DAG orchestration](#lesson-05)
- [06 — Lineage, observability, access, retention and cost](#lesson-06)

<a id="lesson-01"></a>

## 01 — Sources, grain, schema, contracts and data quality

[Read the lesson](../01-theory/lesson-01-data-contracts.md)

### Q001. Why are types insufficient?

<details>
<summary>Answer</summary>

They do not establish units, grain, timing, uniqueness or business meaning.

</details>

### Q002. Why quarantine with reasons?

<details>
<summary>Answer</summary>

It preserves evidence for correction/audit rather than silently dropping records.

</details>

### Q003. Event time versus ingestion time?

<details>
<summary>Answer</summary>

Event time is when the source event occurred; ingestion time is when the system received it.

</details>

<a id="lesson-02"></a>

## 02 — Batch ingestion, CDC, watermarks and idempotency

[Read the lesson](../01-theory/lesson-02-batch-and-incremental.md)

### Q004. What is idempotency?

<details>
<summary>Answer</summary>

Replaying an operation produces the same intended final state rather than duplicated effects.

</details>

### Q005. Why can timestamps miss changes?

<details>
<summary>Answer</summary>

Late arrivals, equal timestamps, clock issues and updates to old records can evade a simple cutoff.

</details>

### Q006. What must exactly-once claims specify?

<details>
<summary>Answer</summary>

The processing/effect boundary and failure assumptions, not just a marketing label.

</details>

<a id="lesson-03"></a>

## 03 — Files, partitions, warehouses, lakes and dimensional models

[Read the lesson](../01-theory/lesson-03-storage-and-models.md)

### Q007. Why columnar storage for analytics?

<details>
<summary>Answer</summary>

Queries can read selected columns efficiently with compression and useful metadata, subject to engine support.

</details>

### Q008. Why avoid extreme partition cardinality?

<details>
<summary>Answer</summary>

It creates tiny files/metadata overhead and can hurt rather than help performance.

</details>

### Q009. What does a dimension describe?

<details>
<summary>Answer</summary>

Attributes used to filter/group facts under an explicit current/history model.

</details>

<a id="lesson-04"></a>

## 04 — PySpark, lazy plans, partitions, joins and shuffles

[Read the lesson](../01-theory/lesson-04-spark-and-distributed-compute.md)

### Q010. What does lazy evaluation mean?

<details>
<summary>Answer</summary>

Transformations define a plan; an action triggers the required execution.

</details>

### Q011. Why are shuffles costly?

<details>
<summary>Answer</summary>

They move and reorganize data across workers, adding network, disk and coordination cost.

</details>

### Q012. Why can more workers fail to fix skew?

<details>
<summary>Answer</summary>

A dominant key/partition may still concentrate work in one task.

</details>

<a id="lesson-05"></a>

## 05 — Streams, event time, windows, retries and DAG orchestration

[Read the lesson](../01-theory/lesson-05-streaming-and-orchestration.md)

### Q013. What does a watermark address?

<details>
<summary>Answer</summary>

Progress/state/late-data policy under the streaming engine, not a guarantee of no late events.

</details>

### Q014. Why reconciliation before publication?

<details>
<summary>Answer</summary>

Consumers should not receive outputs that violate known totals or contracts.

</details>

### Q015. Which failures should not be blindly retried?

<details>
<summary>Answer</summary>

Deterministic invalid input or contract violations that need correction rather than another identical attempt.

</details>

<a id="lesson-06"></a>

## 06 — Lineage, observability, access, retention and cost

[Read the lesson](../01-theory/lesson-06-observability-and-governance.md)

### Q016. Lineage versus monitoring?

<details>
<summary>Answer</summary>

Lineage explains dependencies/provenance; monitoring measures current behaviour and health.

</details>

### Q017. Does hashing guarantee anonymity?

<details>
<summary>Answer</summary>

No. Linkage, guessability and auxiliary information can still identify people.

</details>

### Q018. Why ownership on an alert?

<details>
<summary>Answer</summary>

Someone needs to investigate and resolve the issue within a defined response process.

</details>
