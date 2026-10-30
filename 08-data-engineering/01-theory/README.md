# Data Engineering — theory in learning order

[Subject home](../README.md) · [Practicals](../02-practicals/README.md) · [Questions and answers](../03-questions-and-answers/README.md)

**[Algorithm story and family comparisons](ALGORITHM-STORY.md)** — understand the problem, mechanism, limitation and related alternatives.

Start with 01 and follow the numbered lessons. Each explains the idea in simple language, shows a worked example and identifies common mistakes. Run code examples and reproduce calculations before checking the answers.

**Sequence:** Sources → Contracts → Ingestion → Storage → Transform → Orchestrate → Observe

1. [Sources, grain, schema, contracts and data quality](lesson-01-data-contracts.md)
2. [Batch ingestion, CDC, watermarks and idempotency](lesson-02-batch-and-incremental.md)
3. [Files, partitions, warehouses, lakes and dimensional models](lesson-03-storage-and-models.md)
4. [PySpark, lazy plans, partitions, joins and shuffles](lesson-04-spark-and-distributed-compute.md)
5. [Streams, event time, windows, retries and DAG orchestration](lesson-05-streaming-and-orchestration.md)
6. [Lineage, observability, access, retention and cost](lesson-06-observability-and-governance.md)

## Extended worked guides

These retained guides provide longer derivations and additional original-note examples. Use them when a lesson needs a deeper worked treatment; the numbered course above is the main reading route.

- [Reliable data pipelines and PySpark](01-data-engineering.md)

## Primary references

These official texts/documentation support further detail and current API behaviour. The course examples are original teaching examples; check the installed version before using framework-specific APIs.

- [Spark SQL guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Apache Airflow concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html)
- [Apache Kafka documentation](https://kafka.apache.org/documentation/)
