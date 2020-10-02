use dynasty;
SELECT * FROM dynasty.league_week_matchup;

#head to head matchups breakdown - Dave and Ed
select m.name as 'Winner', lwm.league_year, lwm.week, lwm.week_start, lwm.is_playoffs, lwm.is_consolation, lwm.team_1_points, lwm.team_2_points
from league_week_matchup lwm
join manager_league_team_assignment mlta on mlta.team_key=lwm.team_key_1
join manager_league_team_assignment mlta2 on mlta2.team_key=lwm.team_key_2
join manager_league_team_assignment mlta3 on mlta3.team_key=lwm.winner_team_key
join manager m on m.id=mlta3.manager_id
where lwm.league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607')
AND ((mlta.manager_id=25 and mlta2.manager_id=9) OR ( mlta.manager_id=9 and mlta2.manager_id=25));

#head to head matchups breakdown - Sammy and Ed
select m.name as 'Winner', lwm.league_year, lwm.week, lwm.week_start, lwm.is_playoffs, lwm.is_consolation, lwm.team_1_points, lwm.team_2_points
from league_week_matchup lwm
join manager_league_team_assignment mlta on mlta.team_key=lwm.team_key_1
join manager_league_team_assignment mlta2 on mlta2.team_key=lwm.team_key_2
join manager_league_team_assignment mlta3 on mlta3.team_key=lwm.winner_team_key
join manager m on m.id=mlta3.manager_id
where lwm.league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607')
AND ((mlta.manager_id=25 and mlta2.manager_id=6) OR ( mlta.manager_id=6 and mlta2.manager_id=25));


select * 
from manager_league_team_assignment mlta
join manager m on m.id=mlta.manager_id
where m.id=3;


#head to head matchup count
select m.name as 'Winner', count(*)
from league_week_matchup lwm
join manager_league_team_assignment mlta on mlta.team_key=lwm.team_key_1
join manager_league_team_assignment mlta2 on mlta2.team_key=lwm.team_key_2
join manager_league_team_assignment mlta3 on mlta3.team_key=lwm.winner_team_key
join manager m on m.id=mlta3.manager_id
where lwm.league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607')
AND ((mlta.manager_id=25 and mlta2.manager_id=9) OR ( mlta.manager_id=9 and mlta2.manager_id=25))
group by m.name;

#head to head matchup count
select m.name as 'Winner', count(*)
from league_week_matchup lwm
join manager_league_team_assignment mlta on mlta.team_key=lwm.team_key_1
join manager_league_team_assignment mlta2 on mlta2.team_key=lwm.team_key_2
join manager_league_team_assignment mlta3 on mlta3.team_key=lwm.winner_team_key
join manager m on m.id=mlta3.manager_id
where lwm.league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607')
AND ((mlta.manager_id=25 and mlta2.manager_id=6) OR ( mlta.manager_id=6 and mlta2.manager_id=25))
group by m.name;
























#head to head matchups breakdown - Sammy and Ed
select m.name as 'Winner', lwm.league_year, lwm.week, lwm.week_start, lwm.is_playoffs, lwm.is_consolation, lwm.team_1_points, lwm.team_2_points
from league_week_matchup lwm
join manager_league_team_assignment mlta on mlta.team_key=lwm.team_key_1
join manager_league_team_assignment mlta2 on mlta2.team_key=lwm.team_key_2
join manager_league_team_assignment mlta3 on mlta3.team_key=lwm.winner_team_key
join manager m on m.id=mlta3.manager_id
where lwm.league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607')
and lwm.week>=14
AND ((mlta.manager_id=3 or mlta2.manager_id=3));


