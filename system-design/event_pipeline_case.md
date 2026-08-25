# System Design Case - Customer Activity Pipeline

## Scenario

A retail business wants customer-activity dashboards that show sessions, product views, cart events, purchases, and revenue. Application events arrive continuously. Analysts need trustworthy daily reporting, while operations wants important metrics within roughly 15 minutes.

## Your task

Design the data pipeline end-to-end.

Cover:

1. Requirements and consumers
2. Event contract and data grain
3. Ingestion
4. Raw storage
5. Transformation layers
6. Serving/warehouse model
7. Duplicate and late-event handling
8. Data-quality checks
9. Orchestration and retries
10. Backfills
11. Monitoring and alerting
12. Security/access controls
13. Cost/performance tradeoffs

## Interviewer probes

- The producer starts sending duplicate purchase events. What protects revenue metrics?
- A schema change silently turns `price` from decimal into string. Where should this fail?
- Yesterday's dashboard is 8% below finance totals. How do you investigate?
- You must backfill six months without delaying today's SLA. What changes?
- Event volume grows 20x. Which component becomes your first concern?

## Strong-answer checklist

A strong answer should explicitly address idempotency, replayability, business-vs-processing time, deterministic transformations, reconciliation, ownership, and failure recovery - not only name technologies.
