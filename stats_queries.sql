use dynasty;

# friends
# ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607', '399.l.123949')

# bodos
# ('49.l.122388', '79.l.134615', '101.l.390369', '124.l.156676', '153.l.448193', '175.l.352233', '199.l.132731', '222.l.121923', '242.l.73651', '257.l.49695', '273.l.102516', '314.l.23104', '331.l.83583', '348.l.252077', '359.l.96095', '371.l.157703', '380.l.192099', '390.l.134551', '399.l.884628')


######################################### FRIENDs ################################################################

# ALL time win counts - Friends
SELECT  m.name, count(*) 
from league_week_matchup lwm
join manager_league_team_assignment mlta on mlta.team_key=lwm.winner_team_key
join manager m on m.id=mlta.manager_id
where league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607', '399.l.123949')
group by m.name;

#ALL time loss count - Friends
SELECT  m.name, count(*) 
from league_week_matchup lwm
join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and mlta.team_key <> lwm.winner_team_key
join manager m on m.id=mlta.manager_id
where league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607', '399.l.123949')
group by m.name;

# single manager loss count
SELECT count(*) 
from league_week_matchup lwm
join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and mlta.team_key <> lwm.winner_team_key
join manager m on m.id=mlta.manager_id
where league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607', '399.l.123949')
and mlta.manager_id=3;

# ALL time win loss tie record and winning percentage
SELECT A.manager_name, 
A.win_count, 
B.lose_count, 
case when C.tie_count is null then 0 else C.tie_count end as'tie_count', 
CAST((win_count / (win_count+lose_count+case when C.tie_count is null then 0 else C.tie_count end)) AS DECIMAL(3,3)) as 'win %' 
FROM ( 
	select m.name as manager_name, count(*) as 'win_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on mlta.team_key=lwm.winner_team_key
	join manager m on m.id=mlta.manager_id
	where league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607', '399.l.123949')
	group by m.name
) as A
join (
	select m.name as manager_name, count(*) as 'lose_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and mlta.team_key <> lwm.winner_team_key
	join manager m on m.id=mlta.manager_id
	where league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607', '399.l.123949')
	group by m.name
) as B on B.manager_name=A.manager_name
left join (
	select m.name as manager_name, count(*) as 'tie_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and is_tied=1
	join manager m on m.id=mlta.manager_id
	where league_key in ('124.l.353149', '153.l.156972', '175.l.86206', '199.l.155373', '222.l.92711', '242.l.78082', '257.l.43112', '273.l.53730', '314.l.75102', '331.l.105923', '359.l.259156', '371.l.527788', '380.l.119485', '390.l.138607', '399.l.123949')
	group by m.name
)as C on B.manager_name=C.manager_name;

	



######################################### BODOs ################################################################

# ALL time win counts - Bodos
SELECT m.name, count(*) 
from league_week_matchup lwm
join manager_league_team_assignment mlta on mlta.team_key=lwm.winner_team_key
join manager m on m.id=mlta.manager_id
where league_key in ('49.l.122388', '79.l.134615', '101.l.390369', '124.l.156676', '153.l.448193', '175.l.352233', '199.l.132731', '222.l.121923', '242.l.73651', '257.l.49695', '273.l.102516', '314.l.23104', '331.l.83583', '348.l.252077', '359.l.96095', '371.l.157703', '380.l.192099', '390.l.134551', '399.l.884628')
group by m.name;

SELECT  m.name, count(*) 
from league_week_matchup lwm
join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and mlta.team_key <> lwm.winner_team_key
join manager m on m.id=mlta.manager_id
where league_key in ('49.l.122388', '79.l.134615', '101.l.390369', '124.l.156676', '153.l.448193', '175.l.352233', '199.l.132731', '222.l.121923', '242.l.73651', '257.l.49695', '273.l.102516', '314.l.23104', '331.l.83583', '348.l.252077', '359.l.96095', '371.l.157703', '380.l.192099', '390.l.134551', '399.l.884628')
group by m.name;

#ALL TIME win / loss / tie and winning percentage
SELECT A.manager_name, 
A.win_count, 
B.lose_count, 
case when C.tie_count is null then 0 else C.tie_count end as'tie_count', 
CAST((win_count / (win_count+lose_count+case when C.tie_count is null then 0 else C.tie_count end)) AS DECIMAL(3,3)) as 'win %' 
FROM ( 
	select m.name as manager_name, count(*) as 'win_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on mlta.team_key=lwm.winner_team_key
	join manager m on m.id=mlta.manager_id
	where league_key in ('49.l.122388', '79.l.134615', '101.l.390369', '124.l.156676', '153.l.448193', '175.l.352233', '199.l.132731', '222.l.121923', '242.l.73651', '257.l.49695', '273.l.102516', '314.l.23104', '331.l.83583', '348.l.252077', '359.l.96095', '371.l.157703', '380.l.192099', '390.l.134551', '399.l.884628')
	group by m.name
) as A
join (
	select m.name as manager_name, count(*) as 'lose_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and mlta.team_key <> lwm.winner_team_key
	join manager m on m.id=mlta.manager_id
	where league_key in ('49.l.122388', '79.l.134615', '101.l.390369', '124.l.156676', '153.l.448193', '175.l.352233', '199.l.132731', '222.l.121923', '242.l.73651', '257.l.49695', '273.l.102516', '314.l.23104', '331.l.83583', '348.l.252077', '359.l.96095', '371.l.157703', '380.l.192099', '390.l.134551', '399.l.884628')
	group by m.name
) as B on B.manager_name=A.manager_name
left join (
	select m.name as manager_name, count(*) as 'tie_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and is_tied=1
	join manager m on m.id=mlta.manager_id
	where league_key in ('49.l.122388', '79.l.134615', '101.l.390369', '124.l.156676', '153.l.448193', '175.l.352233', '199.l.132731', '222.l.121923', '242.l.73651', '257.l.49695', '273.l.102516', '314.l.23104', '331.l.83583', '348.l.252077', '359.l.96095', '371.l.157703', '380.l.192099', '390.l.134551', '399.l.884628')
	group by m.name
)as C on B.manager_name=C.manager_name;




select m.name as manager_name, count(*) as 'tie_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and is_tied=1
	join manager m on m.id=mlta.manager_id
	where league_key in ('49.l.122388', '79.l.134615', '101.l.390369', '124.l.156676', '153.l.448193', '175.l.352233', '199.l.132731', '222.l.121923', '242.l.73651', '257.l.49695', '273.l.102516', '314.l.23104', '331.l.83583', '348.l.252077', '359.l.96095', '371.l.157703', '380.l.192099', '390.l.134551', '399.l.884628')
	group by m.name