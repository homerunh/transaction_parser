# generic query to find managers and teams
SELECT m.name, mlta.*, ls.* FROM TappaKegga.league_standings ls
JOIN TappaKegga.manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN TappaKegga.manager m on m.id=mlta.manager_id;

# query to show the champions!
SELECT m.name, mlta.*, ls.league_year FROM TappaKegga.league_standings ls
JOIN TappaKegga.manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN TappaKegga.manager m on m.id=mlta.manager_id
where ls.final_rank=1;

# query to show championship counts
SELECT m.name, count(*) FROM TappaKegga.league_standings ls
JOIN TappaKegga.manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN TappaKegga.manager m on m.id=mlta.manager_id
where ls.final_rank=1
group by m.name;