create table DQC01760.MyDimDate (
dateid INT NOT NULL PRIMARY KEY,
year year not null,
quarter int,
quartername varchar(5),
month int not null,
monthname varchar(20) not null,
day int not null,
dayname varchar(20) not null
);

create table DQC01760.MyDimWaste (
wasteid INT NOT NULL PRIMARY KEY,
wastetype varchar(45) not null,
trucktype varchar(45)
);

create table DQC01760.MyDimZone(
zoneid INT NOT NULL PRIMARY KEY,
collectionzone varchar(45) not null,
city varchar(45) not null,
station varchar(45)
);

create table DQC01760.MyFactTrips (
tripsid INT NOT NULL PRIMARY KEY,
wasteid INT not null,
zoneid INT not null,
dateid INT not null,
wastecollected float not null,
FOREIGN KEY (wasteid) REFERENCES MyDimWaste(wasteid),
FOREIGN KEY (dateid) REFERENCES MyDimDate(dateid),
FOREIGN KEY (zoneid) REFERENCES MyDimZone(zoneid)
);

