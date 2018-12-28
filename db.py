import pymysql

from models.nfl_player import nfl_player
from models.transaction import transaction
import creds.db_creds


def conn():
	return pymysql.connect(host=creds.db_creds.HOST, \
	    user=creds.db_creds.USER, \
	    password=creds.db_creds.PASSWORD, \
	    db=creds.db_creds.DB,\
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
			sql = "INSERT IGNORE INTO `player` VALUES (%s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(sql, (player.player_key, player.player_id, player.first_name, player.last_name, player.full_name, player.nfl_team, player.position))

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
			cursor.execute(sql, (int(transaction.year), transaction.transaction_key, transaction.player_id, transaction.team_key, transaction.transaction_type, transaction.timestamp))
	except Exception as err:
		print("Failed to insert transaction: %s" % err)
	finally:
		db.close()