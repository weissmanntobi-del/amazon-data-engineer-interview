# Python Exercise

## Deduplicate an event stream

Input is newline-delimited JSON. Each record should contain:

- `event_id`
- `event_ts` in ISO-8601 format
- `customer_id`
- `event_type`

Requirements:

1. Ignore malformed JSON and records missing `event_id` or `event_ts`.
2. Keep the record with the greatest `event_ts` for each `event_id`.
3. If timestamps tie, keep the record appearing later in the input.
4. Return records ordered by `(event_ts, event_id)` for deterministic output.
5. Track the number of rejected rows.

Discuss how you would change the implementation if the input no longer fits in memory.
