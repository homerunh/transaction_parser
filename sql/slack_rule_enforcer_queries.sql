SELECT * FROM dynasty.team_manager;

# QB count
SELECT m.name, count(*) as qb_count 
FROM dynasty.current_roster cr  
join player p on p.player_key=cr.player_key  
join manager_league_team_assignment mlta on mlta.team_key=cr.team_key  
join manager m on m.id=mlta.manager_id where p.position='QB' group by m.name;



# covid count
SELECT m.name, count(*) as qb_count FROM dynasty.current_roster cr join player p on p.player_key=cr.player_key join manager_league_team_assignment mlta on mlta.team_key=cr.team_key join manager m on m.id=mlta.manager_id where p.covid_status='COVID-19' group by m.name;

select * from player where player_key='406.p.30158';


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

create table current_roster(
	`team_key` varchar(128) NOT NULL,
	`player_key` varchar(128) NOT NULL,
	PRIMARY KEY(`team_key`, `player_key`),
	FOREIGN KEY(team_key) REFERENCES manager_league_team_assignment(team_key),
	FOREIGN KEY(player_key) REFERENCES player(player_key)
	ON DELETE CASCADE
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


drop table transaction_audit;
drop table current_roster;
drop table player;


SET FOREIGN_KEY_CHECKS = 0;
SET FOREIGN_KEY_CHECKS = 1;



