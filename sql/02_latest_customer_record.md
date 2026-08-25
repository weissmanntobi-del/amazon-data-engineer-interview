# SQL 02 - Latest Customer Record

An append-only table `customer_updates` contains:

```text
customer_id   VARCHAR
email         VARCHAR
country       VARCHAR
event_ts      TIMESTAMP
ingested_at   TIMESTAMP
```

Events may arrive late.

## Task

Return the latest business record per `customer_id`, using `event_ts` as the business timestamp and `ingested_at` as a deterministic tie-breaker.

Exclude rows where `customer_id` is null.

## Follow-ups

- Why might `MAX(event_ts)` plus a join produce duplicates?
- When would you choose `ingested_at` instead of `event_ts` as the primary ordering field?
- How would you make this incremental in a warehouse transformation?
