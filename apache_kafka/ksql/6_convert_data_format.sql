-- Converting Data Formats with ksqlDB
-- print raw records
PRINT orders_flat FROM BEGINNING;

-- create new stream with VALUE_FORMAT='delimited' 
CREATE STREAM orders_csv
WITH(VALUE_FORMAT='delimited', KAFKA_TOPIC='orders_csv') AS
SELECT * FROM orders_flat EMIT CHANGES;

-- print raw records
PRINT orders_csv FROM BEGINNING;