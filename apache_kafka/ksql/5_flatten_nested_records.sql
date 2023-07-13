-- drop previous stream
DROP STREAM orders_enriched DELETE TOPIC;
DROP STREAM orders_no_address DELETE TOPIC;
DROP STREAM orders DELETE TOPIC;

-- create new stream 
CREATE STREAM orders (
    ordertime BIGINT,
    orderid INTEGER,
    itemid VARCHAR, 
    orderunits INTEGER,
    address STRUCT <
        street  VARCHAR, city VARCHAR, state VARCHAR
        >
)
WITH (KAFKA_TOPIC='orders', VALUE_FORMAT='json', PARTITIONS=1);

-- insert into orders stream
INSERT INTO orders VALUES (1620504934723, 70, 'item_4', 1,
	STRUCT(street:='210 West Veterans Drive', city:='Sacramento', state:='California'));
INSERT INTO orders VALUES (16205059321941, 72, 'item_7', 9,
	STRUCT(street:='10043 Bella Vista Blvd', city:='Oakland', state:='California'));
INSERT INTO orders VALUES (16205069437125, 73, 'item_3', 4,
	STRUCT(street:='4921 Parker Place', city:='Pasadena', state:='California'));
INSERT INTO orders VALUES (1620508354284, 74, 'item_7', 3,
	STRUCT(street:='1009 First Street', city:='Fresno', state:='California'));

-- select stream
-- auto.offset.reset : earliest
SELECT * FROM orders EMIT CHANGES; 

-- select and flatten the records
CREATE STREAM orders_flat WITH (KAFKA_TOPIC='orders') AS 
SELECT ordertime, orderid, itemid, orderunits,
    address->street AS street,
    address->city AS city,
    address->state AS state
FROM orders
EMIT CHANGES; 

-- select stream
SELECT * FROM orders_flat EMIT CHANGES;