use TappaKegga;
use Bodos;

# generic query to find managers and teams
SELECT m.name, mlta.*, ls.* FROM league_standings ls
JOIN manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN manager m on m.id=mlta.manager_id;

# show a particular manager's season finishes
SELECT m.name, mlta.*, ls.* FROM league_standings ls
JOIN manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN manager m on m.id=mlta.manager_id
where m.id =3;

# query to show the champions!
SELECT m.name, ls.league_year, ls.playoff_seed, ls.regular_season_wins, ls.regular_season_losses, ls.points_for, ls.points_against FROM league_standings ls
JOIN manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN manager m on m.id=mlta.manager_id
where ls.final_rank=1;

# query to show championship counts
SELECT m.name, count(*) FROM league_standings ls
JOIN manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN manager m on m.id=mlta.manager_id
where ls.final_rank=1
group by m.name
order by count(*) desc;

SELECT m.name, count(*) FROM league_standings ls
JOIN manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN manager m on m.id=mlta.manager_id
where ls.final_rank=1 or ls.final_rank=2
group by m.name
order by count(*) desc;