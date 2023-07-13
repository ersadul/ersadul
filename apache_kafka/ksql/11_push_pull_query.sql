-- Push Queries and Pull Queries
-- pull: return latest state of table 
-- push: continously listen to occurs event in table or stream
 

-- pull query
SELECT LATEST_LOCATION, LOCATION_CHANGES, UNIQUE_LOCATIONS
FROM PERSON_STATS WHERE PERSON = 'Allison';

-- push query
SELECT LATEST_LOCATION, LOCATION_CHANGES, UNIQUE_LOCATIONS
FROM PERSON_STATS WHERE PERSON = 'Allison' EMIT CHANGES;