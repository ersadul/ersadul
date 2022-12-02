-- Exercise 2 - Write a query using grouping sets
select year, category, sum(billedamount) as totalbilledamount
from "FactBilling"
left join "DimCustomer"
on "FactBilling".customerid = "DimCustomer".customerid
left join "DimMonth"
on "FactBilling".monthid = "DimMonth".monthid
group by grouping sets(year, category);

-- Exercise 3 - Write a query using rollup
select year,category, sum(billedamount) as totalbilledamount
from "FactBilling"
left join "DimCustomer"
on "FactBilling".customerid = "DimCustomer".customerid
left join "DimMonth"
on "FactBilling".monthid="DimMonth".monthid
group by rollup(year, category)
order by year, category;

-- exercise 4 - write a query using cube
select year,category, sum(billedamount) as totalbilledamount
from "FactBilling"
left join "DimCustomer"
on "FactBilling".customerid = "DimCustomer".customerid
left join "DimMonth"
on "FactBilling".monthid="DimMonth".monthid
group by cube(year,category)
order by year, category;

-- exercise 5 create mqt 
CREATE MATERIALIZED VIEW countrystats (country, year, totalbilledamount) AS
(select country, year, sum(billedamount)
from "FactBilling"
left join "DimCustomer"
on "FactBilling".customerid = "DimCustomer".customerid
left join "DimMonth"
on "FactBilling".monthid="DimMonth".monthid
group by country,year);

REFRESH MATERIALIZED VIEW countrystats;

select * from countrystats;

-- Practice exercises
-- Problem 1: Create a grouping set for the columns year, quartername, sum(billedamount).
select year, quartername, sum(billedamount)
from "FactBilling"
left join "DimMonth"
on "FactBilling".monthid = "DimMonth".monthid
group by grouping sets(year, quartername);

-- Problem 2: Create a rollup for the columns country, category, sum(billedamount).
select country, category, sum(billedamount)
from "FactBilling"
left join "DimCustomer"
on "DimCustomer".customerid = "DimCustomer".customerid
group by rollup(country, category);

-- Problem 3: Create a cube for the columns year,country, category, sum(billedamount).
select year, quartername, sum(billedamount)
from "FactBilling"
left join "DimMonth"
on "DimMonth".monthid = "DimMonth".monthid
group by cube(year, quartername);

-- Problem 4: Create an MQT named average_billamount with columns year, quarter, category, country, average_bill_amount.
CREATE MATERIALIZED VIEW average_billamount (year,quarter,category,country, average_bill_amount) AS
    (select   year,quarter,category,country, avg(billedamount) as average_bill_amount
    from "FactBilling"
    left join  "DimCustomer"
    on "FactBilling".customerid =  "DimCustomer".customerid
    left join "DimMonth"
    on "FactBilling".monthid="DimMonth".monthid
    group by year,quarter,category,country
    );

refresh MATERIALIZED VIEW average_billamount;

