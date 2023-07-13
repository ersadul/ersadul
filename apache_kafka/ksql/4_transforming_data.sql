-- create new stream and insert data into it
DROP STREAM orders_enriched DELETE TOPIC;
DROP STREAM orders DELETE TOPIC;

CREATE STREAM orders (
    ordertime BIGINT,
    orderid INTEGER,
    itemid VARCHAR,
    orderunits INTEGER,
    address STRUCT 
        < street VARCHAR,
        city VARCHAR,
        state VARCHAR>
    )
WITH (KAFKA_TOPIC='orders', VALUE_FORMAT='avro', PARTITIONS=1);


INSERT INTO orders VALUES (1620504934723, 70, 'item_5', 1,
STRUCT(street:='210 West Veterans Drive', city:='Sacramento', state:='California Foo2'));
INSERT INTO orders VALUES (16205059321941, 72, 'item_6', 9,
STRUCT(street:='10043 Bella Vista Blvd', city:='Oakland', state:='California'));
INSERT INTO orders VALUES (1620503083019, 77, 'item_7', 12,
STRUCT(street:='10083 Garvey Ave', city:='Rosemead', state:='California'));

-- select stream data
select * from ORDERS EMIT CHANGES;

-- create new stream that transform the orders data format 
CREATE STREAM orders_no_address AS
SELECT TIMESTAMPTOSTRING(ordertime, 'yyyy-MM-dd HH:mm:ss') AS order_timestamp, orderid, itemid, orderunits
FROM orders EMIT CHANGES;

select * from orders_no_address EMIT CHANGES;
