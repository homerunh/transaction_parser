SELECT m.name, p.* FROM dynasty.current_roster cr join player p on p.player_id=cr.player_id join manager_league_team_assignment mlta on mlta.team_key=cr.team_key join manager m on m.id=mlta.manager_id;

SELECT m.name, count(*) 
FROM dynasty.current_roster cr 
join player p on p.player_id=cr.player_id 
join manager_league_team_assignment mlta on mlta.team_key=cr.team_key 
join manager m on m.id=mlta.manager_id
group by m.name;

SELECT m.name, count(*) 
FROM dynasty.current_roster cr 
join player p on p.player_id=cr.player_id 
join manager_league_team_assignment mlta on mlta.team_key=cr.team_key 
join manager m on m.id=mlta.manager_id
where p.position='QB'
group by m.name;