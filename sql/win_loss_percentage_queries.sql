use TappaKegga;
use Bodos;

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
    and lwm.is_playoffs=1
    and lwm.is_consolation=0
	group by m.name
) as A
join (
	select m.name as manager_name, count(*) as 'lose_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and mlta.team_key <> lwm.winner_team_key
	join manager m on m.id=mlta.manager_id
    and lwm.is_playoffs=1
    and lwm.is_consolation=0
	group by m.name
) as B on B.manager_name=A.manager_name
left join (
	select m.name as manager_name, count(*) as 'tie_count'
	from league_week_matchup lwm
	join manager_league_team_assignment mlta on (mlta.team_key=lwm.team_key_1 or mlta.team_key = lwm.team_key_2) and is_tied=1
	join manager m on m.id=mlta.manager_id
    and lwm.is_playoffs=1
    and lwm.is_consolation=0
	group by m.name
)as C on B.manager_name=C.manager_name;