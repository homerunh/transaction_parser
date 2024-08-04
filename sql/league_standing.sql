use dynasty;

SELECT m.name, ls.* 
FROM league_standings ls
join manager_league_team_assignment mlta on ls.team_key=mlta.team_key
join manager m on m.id=mlta.manager_id
-- where m.id=3 
order by league_year, playoff_seed asc;

select count(*) from league_standings;