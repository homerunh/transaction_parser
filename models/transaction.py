class transaction(object):
	year = 0
	transaction_key = ''
	player_key = ''
	team_key = ''
	transaction_type = ''
	timestamp = ''

	def __init__(self, year, transaction_key, player_key, team_key, transaction_type, timestamp):
		self.year = year
		self.transaction_key = transaction_key
		self.player_key = player_key
		self.team_key = team_key
		self.transaction_type = transaction_type
		self.timestamp = timestamp

	def printME(self):
		print("year: %s\ntransaction_key: %s\nplayer_key: %s\nteam_key: %s\ntransaction_type: %s\ntimestamp: %s\n" % \
			(self.year, self.transaction_key, self.player_key, self.team_key, self.transaction_type, self.timestamp))