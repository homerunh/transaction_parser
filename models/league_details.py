class league_details(object):
  league_key = ''
  league_id = ''
  league_name = ''
  start_week = 0
  start_date = ''
  end_week = 0
  end_date = ''
  league_year = ''
  team_count = 0

  def __init__(self, league_key, league_id, league_name, start_week, start_date, end_week, end_date, league_year, team_count):
    self.league_key = league_key
    self.league_id = league_id
    self.league_name = league_name
    self.start_week = start_week
    self.start_date = start_date
    self.end_week = end_week
    self.end_date = end_date
    self.league_year = league_year
    self.team_count = team_count

  def printME(self):
    print("########################  %s  #################################" % (self.league_year))
    print("league_key: %s\nleague_id: %s\nleague_name: %s\nstart_week: %d\nstart_date: %s\nend_week: %d\nend_date: %s\nleague_year: %s\nteam count: %d\n" % \
      (self.league_key, self.league_id, self.league_name, self.start_week, self.start_date, self.end_week, self.end_date, self.league_year, self.team_count))