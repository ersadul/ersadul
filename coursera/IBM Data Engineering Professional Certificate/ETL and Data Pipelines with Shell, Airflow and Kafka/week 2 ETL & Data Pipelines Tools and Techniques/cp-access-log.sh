#Extract
cut -d"#" -f1-4 web-server-access-log.txt > extracted-data.txt

#Transform
tr "#" "," < extracted-data.txt > transformed-data.csv

#Load
#TRUNCATE TABLE access_log;
# truncate table if you want to delete all the data
echo "\c template1;\COPY access_log (timestamp,latitude,longitude,visitorid) FROM '/home/project/transformed-data.csv' DELIMITERS ',' CSV HEADER" | psql --username=postgres --host=localhost

echo '\c template1;\\SELECT DISTINCT * FROM access_log;'| psql --username=postgres --host=localhost

