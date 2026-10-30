# 03 — Files, partitions, warehouses, lakes and dimensional models

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-03)

```mermaid
flowchart LR
 N0["Query patterns"] --> N1["File and table layout"] --> N2["Partition pruning"] --> N3["Scan cost"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** Storage layout is the shelving system: it should help common retrieval patterns without creating millions of tiny boxes.

CSV/JSON are useful interchange formats but offer limited typing and scan efficiency. Columnar formats such as Parquet can support compressed column selection and predicate-friendly scans. Partitioning organizes data by chosen keys; choose keys that match access patterns without excessive high-cardinality directories. Too many tiny files increase metadata/scheduling overhead.

Warehouses emphasize managed analytic querying; lakes emphasize flexible object storage; lakehouse table formats add selected transactional/schema/history capabilities. None removes the need for governance, contracts and a compute plan. Define ownership, retention and recovery explicitly.

Dimensional models separate measurable facts from descriptive dimensions. The fact grain controls valid sums. Slowly changing dimensions need effective-date rules, surrogate keys and nonoverlapping validity intervals. Raw, cleaned and curated layers are useful conventions when each has a clear responsibility; duplicating data through arbitrary layers adds cost without quality.

## Work through it

Partition a daily event table by date if queries regularly filter dates. Partitioning by unique event ID would create an enormous number of tiny partitions. A200MBcolumnar file may be more efficient than 200000 one-kilobytefiles, depending on the engine/workload.

A line-item fact must not sum a repeated order-level shipping total without allocating or deduplicating it at the correct grain.

## Common mistakes and practical limits

Partitioning is not the same as indexing. Updating a historical dimension can rewrite business history if current-state and historical meanings are mixed. Always reconcile before and after a model transformation.

---

[← Batch ingestion, CDC, watermarks and idempotency](lesson-02-batch-and-incremental.md) · [PySpark, lazy plans, partitions, joins and shuffles →](lesson-04-spark-and-distributed-compute.md)
