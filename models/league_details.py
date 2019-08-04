class league_details(object):
  league_key = ''
  league_id = ''
  league_name = ''
  start_week = ''
  start_date = ''
  end_week = ''
  end_date = ''
  league_year = ''

  def __init__(self, league_key, league_id, league_name, start_week, start_date, end_week, end_date, league_year):
    self.league_key = league_key
    self.league_id = league_id
    self.league_name = league_name
    self.start_week = start_week
    self.start_date = start_date
    self.end_week = end_week
    self.end_date = end_date
    self.league_year = league_year

  def printME(self):
    print("########################  %s  #################################" % (self.league_year))
    print("league_key: %s\nleague_id: %s\nleague_name: %s\nstart_week: %s\nstart_date: %s\nend_week: %s\nend_date: %s\nleague_year: %s\n" % \
      (self.league_key, self.league_id, self.league_name, self.start_week, self.start_date, self.end_week, self.end_date, self.league_year))