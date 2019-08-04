create database dynasty;
use dynasty;

drop table manager;
create table manager(
	`id` bigint(11) auto_increment,
	`name` VARCHAR(128) NOT NULL,
	PRIMARY KEY(`id`)
);

alter table manager 
add column email varchar(128) NOT NULL;

truncate manager;
insert ignore into `manager` VALUES
(1, "Mark", ""),
(2, "Matty", ""),
(3, "Ryan", ""),
(4, "Bobby", ""),
(5, "Adam", ""),
(6, "Sammy", ""),
(7, "Billy", ""),
(8, "James", ""),
(9, "Dave", ""),
(10, "Erick", ""),
(11, "Sam Landesberg", ""),
(12, "Ryan Harris / Grant?", ""),
(13, "Jason Austin", ""),
(14, "John Vaughn", ""),
(15, "Deke Shipp", ""),
(16, "Joel Harrigan", ""),
(17, "Ben Brunjes", ""),
(18, "Chad Copeland", ""),
(19, "Jared Groot", ""),
(20, "Anuj Singh", ""),
(21, "Austin Morris", ""),
(22, "Ricky Randall", "");


create table manager_league_team_assignment(
	`manager_id` bigint(11) NOT NULL,
	`team_key` varchar(128) NOT NULL,
	PRIMARY KEY (`team_key`),
	FOREIGN KEY(manager_id) REFERENCES manager(id)
);


drop table `manager_league_team_assignment`;
insert into `manager_league_team_assignment` VALUES
	( 9, "359.l.302857.t.1"),
	( 1, "359.l.302857.t.2"),
	( 6, "359.l.302857.t.3"),
	( 3, "359.l.302857.t.4"),
	( 7, "359.l.302857.t.5"),
	( 5, "359.l.302857.t.6"),
	( 2, "359.l.302857.t.7"),
	( 8, "359.l.302857.t.8"),
	( 4, "359.l.302857.t.9"),
	( 10, "359.l.302857.t.10"),
	( 9, "371.l.15908.t.1"),
	( 5, "371.l.15908.t.2"),
	( 8, "371.l.15908.t.3"),
	( 6, "371.l.15908.t.4"),
	( 7, "371.l.15908.t.5"),
	( 4, "371.l.15908.t.6"),
	( 1, "371.l.15908.t.7"),
	( 10, "371.l.15908.t.8"),
	( 2, "371.l.15908.t.9"),
	( 3, "371.l.15908.t.10"),
	( 9, "380.l.11074.t.1"),
	( 5, "380.l.11074.t.2"),
	( 7, "380.l.11074.t.3"),
	( 6, "380.l.11074.t.4"),
	( 8, "380.l.11074.t.5"),
	( 10, "380.l.11074.t.6"),
	( 2, "380.l.11074.t.7"),
	( 1, "380.l.11074.t.8"),
	( 4, "380.l.11074.t.9"),
	( 3, "380.l.11074.t.10")
;

select manager_id, count(*) from `manager_league_team_assignment` group by manager_id;


create table player(
	`player_key` varchar(128) NOT NULL,
	`player_id` varchar(128) NOT NULL,
	`first_name` varchar(128) NOT NULL,
	`last_name` varchar(128) NOT NULL,
	`full_name` varchar(128) NOT NULL,
	`nfl_team` varchar(128) NOT NULL,
	`position` varchar(128) NOT NULL,
	PRIMARY KEY(`player_id`)
);


create table transaction_audit(
	`year` bigint(11) DEFAULT 0,
	`transaction_key` VARCHAR(128) NOT NULL,
	`player_id` varchar(128) NOT NULL,
	`team_key` varchar(128) NOT NULL,
	`transaction_type` varchar(128) NOT NULL,
	`timestamp` DATETIME NOT NULL,
	PRIMARY KEY(`transaction_key`, `player_id`),
	FOREIGN KEY(player_id) REFERENCES player(player_id),
	FOREIGN KEY(team_key) REFERENCES manager_league_team_assignment(team_key)
);

drop table current_roster;
create table current_roster(
	`team_key` varchar(128) NOT NULL,
	`player_id` varchar(128) NOT NULL,
	PRIMARY KEY(`team_key`, `player_id`),
	FOREIGN KEY(team_key) REFERENCES manager_league_team_assignment(team_key),
	FOREIGN KEY(player_id) REFERENCES player(player_id)
);