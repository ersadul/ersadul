-- Apply Lambda Functions to Arrays and Maps

-- Transform Function
CREATE STREAM stream1 (
    id INT, name VARCHAR,
    exam_scores MAP<STRING, DOUBLE>
) WITH (
    kafka_topic = 'topic1', partitions = 1,
    value_format = 'json'
); 

CREATE STREAM transformed 
    AS SELECT id, name,
    TRANSFORM(exam_scores,(k, v) => UCASE(k), (k, v) => (ROUND(v))) AS rounded_scores
FROM stream1 EMIT CHANGES;

INSERT into stream1 values(1, 'Lisa', MAP('Nov':=93.53, 'Feb':=94.13, 'May':=96.83));
INSERT into stream1 values(1, 'Larry', MAP('Nov':=83.53, 'Feb':=84.82, 'May':=85.27));
INSERT into stream1 values(1, 'Melissa', MAP('Nov':=97.20, 'Feb':=96.47, 'May':=98.62));
INSERT into stream1 values(1, 'Chris', MAP('Nov':=92.78, 'Feb':=91.15, 'May':=93.91));

SELECT * FROM transformed EMIT CHANGES;


-- Reduce Function
CREATE STREAM stream2 (
    name VARCHAR,
    points ARRAY<INTEGER>
) WITH (
    kafka_topic = 'topic2', partitions = 1,
    value_format = 'json'
);

CREATE STREAM reduced 
    AS SELECT name,
    REDUCE(points,0,(s,x)=> (s+x)) AS total
FROM stream2 EMIT CHANGES;

INSERT INTO stream2 VALUES('Misty', Array[7, 5, 8, 8, 6]);
INSERT INTO stream2 VALUES('Marty', Array[3, 5, 4, 6, 4]);
INSERT INTO stream2 VALUES('Mary', Array[9, 7, 8, 7, 8]);
INSERT INTO stream2 VALUES('Mickey', Array[8, 6, 8, 7, 5]);

SELECT * FROM reduced EMIT CHANGES;


-- Filter Function
CREATE STREAM stream3 (
    id VARCHAR,
    numbers ARRAY<INTEGER>
) WITH (
    kafka_topic = 'topic3', partitions = 1,
    value_format = 'json'
);

CREATE STREAM filtered 
    AS SELECT id,
    FILTER(numbers,x => (x%2 = 0)) AS even_numbers
FROM stream3 EMIT CHANGES;

INSERT INTO stream3 VALUES('Group1', ARRAY[1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]);

SELECT * FROM filtered EMIT CHANGES;