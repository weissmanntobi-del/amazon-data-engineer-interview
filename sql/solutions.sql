-- SQL 01
WITH ranked_orders AS (
    SELECT
        order_id,
        order_ts,
        status,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY updated_at DESC
        ) AS rn
    FROM orders
)
SELECT
    CAST(order_ts AS DATE) AS order_date,
    COUNT(*) AS successful_orders,
    SUM(amount) AS revenue
FROM ranked_orders
WHERE rn = 1
  AND status = 'COMPLETED'
GROUP BY CAST(order_ts AS DATE)
ORDER BY order_date;

-- SQL 02
WITH ranked_customers AS (
    SELECT
        customer_id,
        email,
        country,
        event_ts,
        ingested_at,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY event_ts DESC, ingested_at DESC
        ) AS rn
    FROM customer_updates
    WHERE customer_id IS NOT NULL
)
SELECT customer_id, email, country, event_ts, ingested_at
FROM ranked_customers
WHERE rn = 1;
