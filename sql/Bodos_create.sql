

create database Bodos;
use Bodos;

-- drop table manager;
create table manager(
	`id` bigint(11) auto_increment,
	`name` VARCHAR(128) NOT NULL,
	PRIMARY KEY(`id`)
);

alter table manager 
add column email varchar(128) NOT NULL;

-- truncate manager;
insert ignore into `manager` VALUES
(1, "Mark Gearhart", ""),
(2, "Matty Gearhart", ""),
(3, "Ryan Harrigan", ""),
(4, "Bobby Shackleton", ""),
(5, "Adam Showalter", ""),
(6, "Sammy Baer", ""),
(7, "Billy aka Dave", ""),
(8, "James Fernald", ""),
(9, "Dave Blackman", ""),
(10, "Erick aka dead", ""),
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
(22, "Ricky Randall", ""),
(23, "Mike Harrington", ""),
(24, "Dylan McKenzie", ""),
(25, "Ed Bailey", ""),
(26, "Stefan Veldhuis", ""),
(27, "Seth Rogers", ""),
(28, "Joe Gilbert", ""),
(29, "Chris Quarterman", ""),
(30, "Keith Harrington", ""),
(31, "Cavin Keys", ""),
(32, "Tucker Titus", ""),
(33, "Gene", ""),
(34, "Pete", ""),
(35, "Ross", "");


create table league_details (
	`league_key` varchar(128) NOT NULL,
    `league_id` varchar(128) NOT NULL,
    `league_name` varchar(128) not null,
    `start_week` bigint(11) NOT NULL,
    `start_date` DATE NOT NULL,
    `end_week` bigint(11) NOT NULL,
    `end_date` DATE NOT NULL,
    `league_year` bigint(11) default 0,
    `team_count` bigint(11) default 0,
    PRIMARY KEY(`league_key`)
);

create table team_manager (
	`league_key` varchar(128) NOT NULL,
	`team_key` varchar(128) NOT NULL,
    `team_name` varchar(128) NOT NULL,
    `number_of_moves` bigint(11) default 0,
    `number_of_trades` bigint(11) default 0,
    `nickname` varchar(128),
    `guid` varchar(128) NOT NULL,
    `email` varchar(128) NOT NULL,
    PRIMARY KEY (`team_key`),
    FOREIGN KEY(league_key) REFERENCES league_details(league_key)
);

create table manager_league_team_assignment(
	`manager_id` bigint(11) NOT NULL,
	`team_key` varchar(128) NOT NULL,
	PRIMARY KEY (`team_key`),
	FOREIGN KEY(manager_id) REFERENCES manager(id),
    FOREIGN KEY(team_key) REFERENCES team_manager(team_key)
);

-- truncate league_week_matchup;
-- drop table league_week_matchup;
create table league_week_matchup(
  league_key varchar(128) NOT NULL,
  league_year bigint(11) default 0,
  week bigint(11), 
  week_start DATE NOT NULL,
  status varchar(128),
  is_playoffs TINYINT(1),
  is_consolation TINYINT(1),
  is_matchup_recap_available TINYINT(1),
  is_tied TINYINT(1),
  winner_team_key varchar(128),
  team_key_1 varchar(128) NOT NULL,
  team_1_points DECIMAL(9,2) default '0.00',
  team_key_2 varchar(128) NOT NULL,
  team_2_points DECIMAL(9,2) default '0.00',
  PRIMARY KEY(league_year, week, team_key_1, team_key_2),
  FOREIGN KEY(league_key) REFERENCES league_details(league_key),
  FOREIGN KEY(team_key_1) REFERENCES team_manager(team_key),
  FOREIGN KEY(team_key_2) REFERENCES team_manager(team_key)
);

-- truncate league_standings;
create table league_standings (
	`team_key` varchar(128) NOT NULL,
	`league_year` bigint(11) DEFAULT 0,
	`playoff_seed` bigint(11) DEFAULT 0,
	`final_rank` bigint(11) DEFAULT 99,
	`is_clinched_playoff` TINYINT(1),
	`regular_season_wins` bigint(11) DEFAULT 0,
	`regular_season_losses` bigint(11) DEFAULT 0,
	`regular_season_ties` bigint(11) DEFAULT 0,
	`division_wins` bigint(11) DEFAULT 0,
	`division_losses` bigint(11) DEFAULT 0,
	`division_ties` bigint(11) DEFAULT 0,
	`points_for` DECIMAL(9,2) DEFAULT '0.00',
	`points_against` DECIMAL(9,2) DEFAULT '0.00',
  PRIMARY KEY(`team_key`, `league_year`),
  FOREIGN KEY(team_key) REFERENCES manager_league_team_assignment(team_key)
);