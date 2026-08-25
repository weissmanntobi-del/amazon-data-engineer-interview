# SQL 01 - Daily Revenue

You receive an `orders` table:

```text
order_id      VARCHAR
customer_id   VARCHAR
order_ts      TIMESTAMP
status        VARCHAR
amount        DECIMAL(12,2)
updated_at    TIMESTAMP
```

The source may resend an order multiple times. The row with the greatest `updated_at` is the current version.

## Task

Return one row per calendar day containing:

- `order_date`
- `successful_orders`
- `revenue`

Only the latest version of each order should count, and only rows whose latest status is `COMPLETED` contribute to the result.

## Follow-ups

1. Why is filtering `status = 'COMPLETED'` before deduplication incorrect?
2. What would you do if two versions had the same `updated_at`?
3. How would you validate this calculation against a source-of-truth system?
