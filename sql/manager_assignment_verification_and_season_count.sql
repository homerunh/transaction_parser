use TappaKegga;
use Bodos;

SELECT count(*) FROM manager_league_team_assignment;

SELECT m.name, count(*) as count FROM manager_league_team_assignment mlta
join manager m on mlta.manager_id=m.id
group by manager_id;

select sum(team_count) from league_details;
