import pymysql

from models.nfl_player import nfl_player
from models.transaction import transaction
from models.team_manager import team_manager
from models.league_details import league_details
from models.league_week_matchup import league_week_matchup
from models.league_standing import league_standing
import creds
import constants


def conn():
	return pymysql.connect(host=creds.db_creds['HOST'], \
			port=creds.db_creds['PORT'], \
	    user=creds.db_creds['USER'], \
	    password=creds.db_creds['PASSWORD'], \
	    db=creds.db_creds['DB'],\
	    charset='utf8mb4',\
	    autocommit=True,\
	    cursorclass=pymysql.cursors.DictCursor)

def testing_testing_123(the_sql_string):

	try:
		with db.cursor() as cursor:
			sql = the_sql_string
			cursor.execute(sql)
			result= cursor.fetchone()
			print(result)

	except:
		print("FAILED!")

def insert_player(player):
	db = conn()
	print("\ninsering player: %s" % player.player_key)
	player.printME()
	try:
		with db.cursor() as cursor:
			sql = "INSERT IGNORE INTO `player` VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(sql, (player.player_key, \
				player.player_id, \
				player.first_name, \
				player.last_name, \
				player.full_name, \
				player.nfl_team, \
				player.position, \
				player.covid_status))

	except Exception as err:
		print("Failed to insert player: %s" % err)

	finally:
		db.close()

def insert_transaction(transaction):
	db = conn()
	print("\ninserting transaction: %s" %transaction.transaction_key)
	transaction.printME()
	try:
		with db.cursor() as cursor:
			sql = "INSERT IGNORE INTO `transaction_audit` VALUES (%s, %s, %s, %s, %s, %s)"
			cursor.execute(sql, (int(transaction.year), \
				transaction.transaction_key, \
				transaction.player_key, \
				transaction.team_key, \
				transaction.transaction_type, \
				transaction.timestamp))
	except Exception as err:
		print("Failed to insert transaction: %s" % err)
	finally:
		db.close()

def insert_player_current_roster(player, team_key):
	db = conn()
	print("\ninserting player: %s" % player.player_key)
	player.printME()
	try:
		with db.cursor() as cursor:
			sql = "INSERT IGNORE INTO `current_roster` VALUES (%s, %s)"
			cursor.execute(sql, (team_key, player.player_key))
	except Exception as err:
		print("Failed to inster transaction: %s" % err)
	finally:
		db.close()

def insert_team_manager(team_manager):
	db = conn()
	print("\ninserting team: %s" % team_manager.team_key)
	team_manager.printME()
	try:
		with db.cursor() as cursor:
			sql = "INSERT INTO `team_manager` VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(sql, (team_manager.league_key, \
			 team_manager.team_key, \
			 team_manager.team_name, \
			 team_manager.number_of_moves, \
			 team_manager.number_of_trades, \
			 team_manager.nickname, \
			 team_manager.guid, \
			 team_manager.email))
	except Exception as err:
		print("Failed to insert team_manager: %s" % err)
	finally:
		db.close()

def insert_league_details(league_details):
	db = conn()
	print("\ninserting league details: %s" % league_details.league_key)
	league_details.printME()
	try:
		with db.cursor() as cursor:
			sql = "INSERT INTO `league_details` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(sql, (league_details.league_key, \
				league_details.league_id, \
				league_details.league_name, \
				league_details.start_week, \
				league_details.start_date, \
				league_details.end_week, \
				league_details.end_date, \
				league_details.league_year, \
				league_details.team_count))
	except Exception as err:
		print("Failed to insert league details %s" % err)
	finally:
		db.close()

def insert_manager_league_team_assignment(team_manager):
	db = conn()
	print("\ninserting manager / league_team assignment\nmanager id: %s\nteam key: %s" % (team_manager.get_manager_id(), team_manager.team_key))
	try:
		with db.cursor() as cursor:
			sql = "INSERT INTO `manager_league_team_assignment` VALUES (%s, %s)"
			cursor.execute(sql, (team_manager.get_manager_id(), team_manager.team_key))
	except Exception as err:
		print("Failed to insert manager id: %s team key: %s" % (team_manager.get_manager_id(), team_manager.team_key))
	finally:
		db.close()

def insert_league_week_matchup(league_week_matchup):
	db = conn()
	print("\ninstering into league week matchup for week %s" % league_week_matchup.week)
	try:
		with db.cursor() as cursor:
			sql = "INSERT INTO `league_week_matchup` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			cursor.execute(sql, (league_week_matchup.league_key, \
				league_week_matchup.league_year, \
				league_week_matchup.week, \
				league_week_matchup.week_start, \
				league_week_matchup.status, \
				league_week_matchup.is_playoffs, \
				league_week_matchup.is_consolation, \
				league_week_matchup.is_matchup_recap_available, \
				league_week_matchup.is_tied, \
				league_week_matchup.winner_team_key, \
				league_week_matchup.team_key_1, \
				league_week_matchup.team_1_points, \
				league_week_matchup.team_key_2, \
				league_week_matchup.team_2_points))
	except Exception as err:
		print("Failed to insert league week matchup for week %s: %s" % (league_week_matchup.week, err))
	finally:
		db.close()



def insert_league_standing(league_standing):
	db = conn()
	print(f"\ninstering into league standing for year {league_standing.league_year}")
	try:
		with db.cursor() as cursor:
			sql = "INSERT IGNORE INTO `league_standings` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			cursor.execute(sql, (league_standing.team_key , \
				league_standing.league_year, \
				league_standing.playoff_seed, \
				league_standing.final_rank, \
				league_standing.is_clinched_playoff, \
				league_standing.regular_season_wins, \
				league_standing.regular_season_losses, \
				league_standing.regular_season_ties, \
				league_standing.division_wins, \
				league_standing.division_losses, \
				league_standing.division_ties, \
				league_standing.points_for, \
				league_standing.points_against))
			
	except Exception as err:
		print("Failed to insert league standing for year %s: %s" % (league_standing.league_year, err))
	finally:
		db.close()


def get_league_details(league_lookup_map):
	details = list()

	db = conn()
	try:
		with db.cursor() as cursor:
			sql = "SELECT * FROM `league_details` where league_key in (%s)"
			args = list(league_lookup_map.values())
			in_p = ', '.join(list(map(lambda x: '%s', args)))
			sql = sql % in_p
			
			cursor.execute(sql, args)
			result = cursor.fetchall()
			for row in result:
				details.append(league_details(row['league_key'], \
								row['league_id'], \
								row['league_name'], \
								row['start_week'], \
								row['start_date'], \
								row['end_week'], \
								row['end_date'], \
								row['league_year'], \
								row['team_count']))

			return details
	except Exception as err:
		print("failed to fetch league details: %s" % err)
	finally:
		db.close()


def get_current_rosters():

	roster_count = 'SELECT m.name, count(*) as roster_count FROM dynasty.current_roster cr join player p on p.player_key=cr.player_key join manager_league_team_assignment mlta on mlta.team_key=cr.team_key join manager m on m.id=mlta.manager_id group by m.name'
	qb_count = 'SELECT m.name, count(*) as qb_count FROM dynasty.current_roster cr  join player p on p.player_key=cr.player_key  join manager_league_team_assignment mlta on mlta.team_key=cr.team_key  join manager m on m.id=mlta.manager_id where p.position=\'QB\' group by m.name'
	covid_count = 'SELECT m.name, count(*) as covid_count FROM dynasty.current_roster cr join player p on p.player_key=cr.player_key join manager_league_team_assignment mlta on mlta.team_key=cr.team_key join manager m on m.id=mlta.manager_id where p.covid_status=\'COVID-19\' group by m.name;'

	db = conn()
	try:
		cur = db.cursor()
		cur.execute(roster_count)
		x= cur.fetchall()

		cur.execute(qb_count)
		y = cur.fetchall()

		cur.execute(covid_count)
		z = cur.fetchall()

		return x,y,z
	except Exception as err:
		print("failed to fetch current rosters: %s" % err)
	finally:
		db.close()

# def truncate_current_rosters():
# 	db = conn()

# 	try:
# 		cur = db.cursor()
# 		cur.execute('SET FOREIGN_KEY_CHECKS = 0;')
# 		cur.execute('truncate current_roster;')

# 	except Exception as err:
# 		print('failed to truncate current roster table: %s' % err)
# 	finally:
# 		db.close()

# def truncate_players():
# 	db = conn()

# 	try:
# 		cur = db.cursor()
# 		cur.execute('truncate player;')
# 		cur.execute('SET FOREIGN_KEY_CHECKS = 1;')

# 	except Exception as err:
# 		print('failed to truncate players table: %s' % err)
# 	finally:
# 		db.close()


def truncate_reset():
	db = conn()

	try:
		cur = db.cursor()
		cur.execute('SET FOREIGN_KEY_CHECKS = 0;')
		cur.execute('truncate transaction_audit;')
		cur.execute('truncate current_roster;')
		cur.execute('truncate player;')
		cur.execute('SET FOREIGN_KEY_CHECKS = 1;')

	except Exception as err:
		print('failed to truncate current roster table: %s' % err)
	finally:
		db.close()
