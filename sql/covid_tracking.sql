SELECT * FROM dynasty.league_details;

select * from dynasty.current_roster;
select * from dynasty.manager;
use dynasty;
SELECT m.name, count(*) as roster_count FROM dynasty.current_roster cr join player p on p.player_id=cr.player_id join manager_league_team_assignment mlta on mlta.team_key=cr.team_key join manager m on m.id=mlta.manager_id group by m.name;


truncate dynasty.player;

select * from league_details where league_key='406.l.115174';
select * from league_details where league_key='414.l.717209';

select * from player p where p.player_id='28493';

select * from player where covid_status<>'none';
select count(*) from player;

alter table player
add covid_status varchar(128) DEFAULT 'none';

drop table player;

create table player(
	`player_key` varchar(128) NOT NULL,
	`player_id` varchar(128) NOT NULL,
	`first_name` varchar(128) NOT NULL,
	`last_name` varchar(128) NOT NULL,
	`full_name` varchar(128) NOT NULL,
	`nfl_team` varchar(128) NOT NULL,
	`position` varchar(128) NOT NULL,
	`covid_status` varchar(128) DEFAULT 'none',
	PRIMARY KEY(`player_key`)
);

create table transaction_audit(
	`year` bigint(11) DEFAULT 0,
	`transaction_key` VARCHAR(128) NOT NULL,
	`player_key` varchar(128) NOT NULL,
	`team_key` varchar(128) NOT NULL,
	`transaction_type` varchar(128) NOT NULL,
	`timestamp` DATETIME NOT NULL,
	PRIMARY KEY(`transaction_key`, `player_key`),
	FOREIGN KEY(player_key) REFERENCES player(player_key),
	FOREIGN KEY(team_key) REFERENCES manager_league_team_assignment(team_key)
);

create table current_roster(
	`team_key` varchar(128) NOT NULL,
	`player_key` varchar(128) NOT NULL,
	PRIMARY KEY(`team_key`, `player_key`),
	FOREIGN KEY(team_key) REFERENCES manager_league_team_assignment(team_key),
	FOREIGN KEY(player_key) REFERENCES player(player_key)
);

drop table league_standings;
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

