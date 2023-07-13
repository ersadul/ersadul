-- Merging Two Streams with ksqlDB

-- create order_uk stream and insert data into it
CREATE STREAM orders_uk (ordertime BIGINT, orderid INTEGER, itemid VARCHAR, orderunits INTEGER,
    address STRUCT< street VARCHAR, city VARCHAR, state VARCHAR>)
WITH (KAFKA_TOPIC='orders_uk', VALUE_FORMAT='json', PARTITIONS=1);

INSERT INTO orders_uk VALUES (1620501334477, 65, 'item_7', 5,
  STRUCT(street:='234 Thorpe Street', city:='York', state:='England'));
INSERT INTO orders_uk VALUES (1620502553626, 67, 'item_3', 2,
  STRUCT(street:='2923 Alexandra Road', city:='Birmingham', state:='England'));
INSERT INTO orders_uk VALUES (1620503110659, 68, 'item_7', 7,
  STRUCT(street:='536 Chancery Lane', city:='London', state:='England'));

-- create order_us stream and insert data into it
CREATE STREAM orders_us (ordertime BIGINT, orderid INTEGER, itemid VARCHAR, orderunits INTEGER,
    address STRUCT< street VARCHAR, city VARCHAR, state VARCHAR>)
WITH (KAFKA_TOPIC='orders_us', VALUE_FORMAT='json', PARTITIONS=1);

INSERT INTO orders_us VALUES (1620501334477, 65, 'item_7', 5,
  STRUCT(street:='6743 Lake Street', city:='Los Angeles', state:='California'));
INSERT INTO orders_us VALUES (1620502553626, 67, 'item_3', 2,
  STRUCT(street:='2923 Maple Ave', city:='Mountain View', state:='California'));
INSERT INTO orders_us VALUES (1620503110659, 68, 'item_7', 7,
  STRUCT(street:='1492 Wandering Way', city:='Berkley', state:='California'));

-- query and inspect our streams
SELECT * FROM orders_uk EMIT CHANGES;
SELECT * FROM orders_us EMIT CHANGES;

-- create merged stream and insert another stream
CREATE STREAM orders_combined AS
SELECT 'US' AS source, ordertime, orderid, itemid, orderunits, address
FROM orders_us;

INSERT INTO orders_combined
SELECT 'UK' AS source, ordertime, orderid, itemid, orderunits, address
FROM orders_uk;

