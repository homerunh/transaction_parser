class league_week_matchup(object):
  league_key=''
  league_year=0
  week = ''
  week_start = ''
  status = ''
  is_playoffs = 0
  is_consolation = 0
  is_matchup_recap_available = 0
  is_tied = 0
  winner_team_key = ''
  team_key_1 = ''
  team_1_points = 0.0
  team_key_2 = ''
  team_2_points = 0.0

  def __init__(self, league_key, league_year, week, week_start, status, is_playoffs, is_consolation, is_matchup_recap_available, is_tied, winner_team_key, team_key_1, team_1_points, team_key_2 , team_2_points ):
    self.league_key = league_key
    self.league_year = league_year
    self.week = week
    self.week_start = week_start
    self.status = status
    self.is_playoffs = is_playoffs
    self.is_consolation = is_consolation
    self.is_matchup_recap_available = is_matchup_recap_available
    self.is_tied = is_tied
    self.winner_team_key = winner_team_key
    self.team_key_1 = team_key_1
    self.team_1_points = team_1_points
    self.team_key_2 = team_key_2
    self.team_2_points = team_2_points

  def printME(self):
    print("########################  %s   #################################" % (self.winner_team_key))
    print("league_key: %s\nleague_year: %s\nweek: %s\nweek_start: %s\nstatus: %s\nis_playoffs: %s\nis_consolation: %s\nis_matchup_recap_available: %s\nis_tied: %s\nwinner_team_key: %s\nteam key 1: %s\nteam 1 points: %s\nteam key 2: %s\nteam 2 points: %s\n" % \
      (self.league_key, self.league_year, self.week, self.week_start, self.status, self.is_playoffs, self.is_consolation, self.is_matchup_recap_available, self.is_tied, self.winner_team_key, self.team_key_1, self.team_1_points, self.team_key_2, self.team_2_points))