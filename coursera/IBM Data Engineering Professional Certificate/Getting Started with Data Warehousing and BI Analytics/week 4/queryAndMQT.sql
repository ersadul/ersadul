select * from DIMDATE limit 5;select * from DIMSTATION limit 5;select * from DIMTRUCK limit 5;select * from FACTTRIPS limit 5;

select DIMDATE.year, DIMSTATION.city, DIMSTATION.stationid, avg(wastecollected) total_waste_collected
from FACTTRIPS
left join dimstation
on dimstation.stationid = FACTTRIPS.stationid
left join DIMDATE
on DIMDATE.DATEID = FACTTRIPS.DATEID
group by cube(DIMDATE.year, DIMSTATION.city, DIMSTATION.stationid);


CREATE TABLE maxwastestats AS
(select dimstation.city, dimstation.stationid, dimtruck.trucktype, max(wastecollected) max_waste_collected
from FACTTRIPS
left join dimstation
on dimstation.stationid = FACTTRIPS.stationid
left join dimtruck
on dimtruck.TRUCKID = FACTTRIPS.TRUCKID
group by grouping sets(dimstation.city, dimstation.stationid, dimtruck.trucktype))

DATA INITIALLY DEFERRED         
REFRESH DEFERRED;










