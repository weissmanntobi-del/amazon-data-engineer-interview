# Amazon Data Engineer Interview Starter

A small, practical repository for candidates preparing for **Data Engineer interviews**, with an Amazon-oriented focus on SQL, Python, data-pipeline reasoning, system design, and behavioral preparation.

> Independent educational material. This repository is not affiliated with or endorsed by Amazon. Interview formats vary by team, level, and location; confirm the current process with your recruiter.

## What this repo helps you practice

- SQL: joins, deduplication, window functions, aggregation, data quality
- Python: record transformation, malformed rows, deterministic output
- Data engineering: grain, idempotency, late data, validation, backfills
- System design: batch + near-real-time pipeline tradeoffs
- Behavioral: STAR stories with measurable data-engineering impact



## Repository structure

```text
amazon-data-engineer-interview-starter/
├── README.md
├── LICENSE
├── sql/
│   ├── 01_daily_revenue.md
│   ├── 02_latest_customer_record.md
│   └── solutions.sql
├── python/
│   ├── 01_dedupe_events.py
│   └── README.md
├── data/
│   └── events.jsonl
├── system-design/
│   └── event_pipeline_case.md
├── behavioral/
│   └── star_story_template.md
├── tests/
│   └── test_dedupe_events.py
└── .github/workflows/
    └── tests.yml
```

## Recommended practice loop

1. Solve each problem without looking at the solution.
2. State the **grain** of the output before writing code.
3. Call out nulls, duplicates, late records, and malformed inputs.
4. Explain how your solution changes at larger scale.
5. Add one validation check before you declare the answer complete.

A useful interview answer pattern is:

**Clarify -> Define grain -> Solve simply -> Validate -> Harden for scale/reliability/cost**

## Quick start

Requires Python 3.11+.

```bash
python -m unittest discover -s tests -v
python python/01_dedupe_events.py data/events.jsonl
```

The SQL exercises use portable SQL concepts. Minor syntax changes may be required for PostgreSQL, Redshift, Snowflake, BigQuery, or another warehouse.

## Practice set

### SQL 01 - Daily Revenue
Aggregate successful order revenue per day while handling cancelled orders and duplicate order rows.

### SQL 02 - Latest Customer Record
Use a window function to select the latest valid customer record per customer from an append-only feed.

### Python 01 - Deduplicate Events
Read JSONL events, reject malformed rows, deduplicate by event ID, and preserve the latest event by timestamp.

### System Design - Customer Activity Pipeline
Design a reliable pipeline from application events to business dashboards. Discuss ingestion, storage, transformation, data quality, retries, backfills, monitoring, and cost.

### Behavioral - STAR+Data Story
Build a reusable story showing ownership, technical depth, measurable impact, and what mechanism you introduced afterward.

## Interview self-check

Before finishing a technical answer, ask:

- What is the output grain?
- Can duplicates change my answer?
- How do I handle nulls or bad records?
- What happens when data arrives late?
- Is the transformation idempotent?
- How would I validate correctness?
- What breaks at 100x scale?
- How would I monitor and backfill it?

## License

MIT. See [LICENSE](LICENSE).
