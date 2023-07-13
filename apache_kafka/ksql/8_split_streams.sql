-- Splitting Two Streams with ksqlDB

-- inspect existing stream
SELECT * FROM orders_combined EMIT CHANGES;

-- split stream
-- create new stream from combined one with filtering
CREATE STREAM us_orders AS
SELECT * FROM orders_combined
WHERE source = 'US';

-- create new stream from combined one with filtering
CREATE STREAM uk_orders AS
SELECT * FROM orders_combined
WHERE source = 'UK';

