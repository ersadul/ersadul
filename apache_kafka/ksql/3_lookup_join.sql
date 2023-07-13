-- create and insert lookup
CREATE TABLE items (id VARCHAR PRIMARY KEY, make VARCHAR, model VARCHAR, unit_price DOUBLE)
WITH (KAFKA_TOPIC='items', VALUE_FORMAT='avro', PARTITIONS=1);

INSERT INTO items VALUES('item_3', 'Spalding', 'TF-150', 19.99);
INSERT INTO items VALUES('item_4', 'Wilson', 'NCAA Replica', 29.99);
INSERT INTO items VALUES('item_7', 'SKLZ', 'Control Training', 49.99);

-- drop stream
DROP STREAM ny_orders;
DROP STREAM orders;

CREATE STREAM orders (ordertime BIGINT, orderid INTEGER, itemid VARCHAR, orderunits INTEGER)
WITH (KAFKA_TOPIC='item_orders', VALUE_FORMAT='avro', PARTITIONS=1);

CREATE STREAM orders_enriched AS
SELECT o.*, i.*, 
	o.orderunits * i.unit_price AS total_order_value
FROM orders o LEFT OUTER JOIN items i
on o.itemid = i.id;

INSERT INTO orders VALUES (1620501334477, 65, 'item_7', 5);
INSERT INTO orders VALUES (1620502553626, 67, 'item_3', 2);
INSERT INTO orders VALUES (1620503110659, 68, 'item_7', 7);
INSERT INTO orders VALUES (1620504934723, 70, 'item_4', 1);
INSERT INTO orders VALUES (1620505321941, 74, 'item_7', 3);
INSERT INTO orders VALUES (1620506437125, 72, 'item_7', 9);
INSERT INTO orders VALUES (1620508354284, 73, 'item_3', 4);

SELECT * FROM orders_enriched EMIT CHANGES;