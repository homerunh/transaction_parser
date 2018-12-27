class nfl_player(object):
	player_key = ''
	player_id = ''
	first_name = ''
	last_name = ''
	full_name = ''
	nfl_team = ''
	position = ''

	def __init__(self, player_key, player_id, first_name, last_name, full_name, nfl_team, position):
		self.player_key = player_key
		self.player_id = player_id
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = full_name
		self.nfl_team = nfl_team
		self.position = position

	def printME(self):
		print("player_key: %s\nplayer_id: %s\nfirst_name: %s\nlast_name: %s\nfull_name: %s\nnfl_team: %s\nposition: %s\n" % \
			(self.player_key, self.player_id, self.first_name, self.last_name, self.full_name, self.nfl_team, self.position))