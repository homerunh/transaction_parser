SELECT * FROM dynasty.team_manager;

# QB count
SELECT m.name, count(*) as qb_count 
FROM dynasty.current_roster cr  
join player p on p.player_key=cr.player_key  
join manager_league_team_assignment mlta on mlta.team_key=cr.team_key  
join manager m on m.id=mlta.manager_id where p.position='QB' group by m.name;



# covid count
SELECT m.name, count(*) as qb_count FROM dynasty.current_roster cr join player p on p.player_key=cr.player_key join manager_league_team_assignment mlta on mlta.team_key=cr.team_key join manager m on m.id=mlta.manager_id where p.covid_status='COVID-19' group by m.name;



