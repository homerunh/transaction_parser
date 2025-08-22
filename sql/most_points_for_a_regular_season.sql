SELECT m.name, ls.league_year, ls.regular_season_wins, ls.regular_season_losses, ls.points_for, ls.points_against FROM TappaKegga.league_standings ls
JOIN manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN manager m on m.id=mlta.manager_id
order by ls.points_for DESC;

# before superflex:
SELECT m.name, ls.league_year, ls.regular_season_wins, ls.regular_season_losses, ls.points_for, ls.points_against FROM TappaKegga.league_standings ls
JOIN manager_league_team_assignment mlta on mlta.team_key=ls.team_key 
JOIN manager m on m.id=mlta.manager_id
where ls.league_year < 2020
order by ls.points_for DESC;