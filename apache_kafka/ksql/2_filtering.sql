-- auto.offset.reset = earliest
CREATE stream orders (id INTEGER KEY, item VARCHAR, address STRUCT <  
city  VARCHAR, state VARCHAR >)
WITH (KAFKA_TOPIC='orders', VALUE_FORMAT='json', partitions=1);

INSERT INTO orders(id, item, address)
VALUES(140, 'Mauve Widget', STRUCT(city:='Ithaca', state:='NY'));
INSERT INTO orders(id, item, address)
VALUES(141, 'Teal Widget', STRUCT(city:='Dallas', state:='TX'));
INSERT INTO orders(id, item, address)
VALUES(142, 'Violet Widget', STRUCT(city:='Pasadena', state:='CA'));
INSERT INTO orders(id, item, address)
VALUES(143, 'Purple Widget', STRUCT(city:='Yonkers', state:='NY'));
INSERT INTO orders(id, item, address)
VALUES(144, 'Tan Widget', STRUCT(city:='Amarillo', state:='TX'));

-- auto.offset.reset = earliest
CREATE STREAM ny_orders AS SELECT * FROM ORDERS WHERE
 ADDRESS->STATE='NY' EMIT CHANGES;

SELECT * FROM ny_orders EMIT CHANGES;