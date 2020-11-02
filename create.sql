create table Athlete(
ID integer primary key,
Name varchar(100) not null,
Sex varchar(100) not null,
Height integer,
Weight integer
);

create table Team(
Name varchar(100) primary key,
NOC varchar(100) not null
);

create table Olympics
(
Year integer,
Season varchar(100),
City varchar(100) not null,
PRIMARY KEY (Year, Season)
);

create table Event(
Event varchar(100) primary key,
Sport varchar(100) not null,
Season varchar(100),
Year integer,
FOREIGN KEY (Year,Season) REFERENCES Olympics(Year, Season)
);

create table Competed_at(
ID integer,
Event varchar(100),
Year integer,
Season varchar(100),
Medal varchar(100),
Age integer,
FOREIGN KEY(ID) REFERENCES Athlete(ID),
FOREIGN KEY(Event) REFERENCES Event(Event),
FOREIGN KEY(Year,Season) REFERENCES Olympics(Year,Season)
);
