class league_standing(object):
	team_key  = ''
	league_year = ''
	playoff_seed = ''
	final_rank = ''
	is_clinched_playoff = ''
	regular_season_wins = ''
	regular_season_losses = ''
	regular_season_ties = ''
	division_wins = ''
	division_losses = ''
	division_ties = ''
	points_for = ''
	points_against = ''

	def __init__(self, team_key, league_year, playoff_seed, final_rank, is_clinched_playoff, regular_season_wins, regular_season_losses, regular_season_ties, division_wins, division_losses, division_ties, points_for, points_against):
		self.team_key = team_key
		self.league_year = league_year
		self.playoff_seed = playoff_seed
		self.final_rank = final_rank
		self.is_clinched_playoff = is_clinched_playoff
		self.regular_season_wins = regular_season_wins
		self.regular_season_losses = regular_season_losses
		self.regular_season_ties = regular_season_ties
		self.division_wins = division_wins
		self.division_losses = division_losses
		self.division_ties = division_ties
		self.points_for = points_for
		self.points_against = points_against

	def printME(self):
		print(f"team_key: {self.team_key}\nleague_year: {self.league_year}\nplayoff_seed: {self.playoff_seed}\nfinal_rank: {self.final_rank}\nis_clinched_playoff: {self.is_clinched_playoff}\nregular_season_wins: {self.regular_season_wins}\nregular_season_losses: {self.regular_season_losses}\nregular_season_ties: {self.regular_season_ties}\ndivision_wins: {self.division_wins}\ndivision_losses: {self.division_losses}\ndivision_ties: {self.division_ties}\npoints_for: {self.points_for}\npoints_against: {self.points_against}")
