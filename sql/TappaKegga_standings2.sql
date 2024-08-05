use TappaKegga;
use Bodos;

# regular season wins - average
select m.name, avg(ls.regular_season_wins) from league_standings ls
join manager_league_team_assignment mlta on mlta.team_key=ls.team_key
join manager m on m.id=mlta.manager_id
group by m.id;

# playoff appearances
select m.name, count(*) from league_standings ls
join manager_league_team_assignment mlta on mlta.team_key=ls.team_key
join manager m on m.id=mlta.manager_id
where ls.is_clinched_playoff=1
group by m.id;

# percentage
select m.name, count(*), x1.count from league_standings ls
join manager_league_team_assignment mlta on mlta.team_key=ls.team_key
join manager m on m.id=mlta.manager_id
join (SELECT m.id, count(*) as count FROM manager_league_team_assignment mlta
join manager m on mlta.manager_id=m.id
group by manager_id) x1
where ls.is_clinched_playoff=1
and x1.id = m.id
group by m.id;

# percentage take 2
select m.name, count(*) as 'made_playoffs', x1.count as 'seasons_played', CAST( count(*) / x1.count AS DECIMAL(3,3)) as 'playoff percentage'
from league_standings ls
join manager_league_team_assignment mlta on mlta.team_key=ls.team_key
join manager m on m.id=mlta.manager_id
join (SELECT m.id, count(*) as count FROM manager_league_team_assignment mlta
join manager m on mlta.manager_id=m.id
group by manager_id) x1
where ls.is_clinched_playoff=1
and x1.id = m.id
group by m.id;