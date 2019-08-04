class team_manager(object):
  team_key = ''
  team_name = ''
  number_of_moves = 0
  number_of_trades = 0
  nickname = ''
  guid = ''
  email = ''

  def __init__(self, team_key, team_name, number_of_moves, number_of_trades, nickname, guid, email):
    self.team_key = team_key
    self.team_name = team_name
    self.number_of_moves = number_of_moves
    self.number_of_trades = number_of_trades
    self.nickname = nickname
    self.guid = guid
    self.email = email

  def printME(self):
    print("team_key: %s\nteam_name: %s\nnumber_of_moves: %d\nnumber_of_trades: %d\nnickname: %s\nguid: %s\nemail: %s\n" % \
      (self.team_key, self.team_name, self.number_of_moves, self.number_of_trades, self.nickname, self.guid, self.email))

  def get_manager_id(self):
    
    # 1 - Mark Gearhart
    if self.guid == 'LRLVUPAASJ5IL5MRLDEG2XORVE':
      return 1
    # 2 - Matt Gearhart
    elif self.guid == 'T7IBEYQNBMGWXFB5EENTDN6NLA':
      return 2
    # 3 - Ryan Harrigan
    elif self.guid == '2SMYLPAWM3H5R7LLENB3Z3UFFQ':
      return 3
    # 4 - Bobby Shackleton
    elif self.guid == 'LAMSPLVER4C3BLRJY6YB7VT32U':
      return 4
    # 5 - Adam Showalter
    elif self.guid == 'OIGPHIM47IIYPKRYA24Q63D27M':
      return 5
    # 6 - Sammy Baer
    elif self.guid == 'XDVZBCNA4GCVYUEXBBAOJVZPGQ' or self.guid == 'EUHTMSCMCT26H7XUH3APCBQF54' or self.guid == 'D4IOIYJDXJDSNDXU64P3EWTMME':
      return 6
    # 7 - Billy
    elif self.guid == '2S4J2BZQ2RIQAQW6H3UVBAELBM':
      return 7
    # 8 - James Fernald
    elif self.guid == 'ENIX3EOXMI2AZ7PRB3PSM4QVPU':
      return 8
    # 9 - Dave Blackman
    elif self.guid == 'I3YU2LYOXVESJU6ZUCK3YE756I':
      return 9
    # 10 - Erick - the pro?
    elif self.guid == 'XYSFVXDXMI7ETZ5I67UMUQKEMU':
      return 10
    # 11 - Sam Landesberg
    elif self.guid == 'CYKY4ZZ5CYJ3Z3PTSONFMNWRUM':
      return 11
    # 12 - Ryann Harris / Grant?
    elif self.team_key == '49.l.122388.t.2':
      return 12
    # 13 - Jason Austin 
    elif self.guid == '4JJQX7RRDPDVALS4JW7DZO2E6Y':
      return 13
    # 14 - John Vaughn
    elif self.guid == 'U4UNUKKCLUQNNW5ZJKDEXZPBKY':
      return 14
    # 15 - Deke Shipp
    elif self.guid == 'VF272APNYU27LXKVR3ROPPKATQ':
      return 15
    # 16 - Joel Harrigan
    elif self.email == 'joelh16@hotmail.com' or self.guid == 'UMAPSPIDD2XND7MBYZYPYLE7OI':
      return 16
    # 17 - Ben Brunjes 
    elif self.guid == 'GIZJGTHE5ZJMNEAOUOLDGQ2MRE':
      return 17
    # 18 - Chad Copeland
    elif self.guid == 'NF4SCQ2VMHTGGJAPYHZVLYTO6I':
      return 18
    # 19 - Jared Groot
    elif self.guid == 'NQMIKI3H5E7LEX3UOKCKXRYF5I':
      return 19
    # 20 - Anuj Singh 
    elif self.guid == 'STYSC63WV4MS2CRFZK65TCPZNI':
      return 20
    # 21 - Austin Morris
    elif self.team_key == '153.l.448193.t.8':
      return 21
    # 22 - Ricky Randall
    elif self.guid == 'JVERZJSUCJKS5HGLOXT7CULUX4':
      return 22
    # 23 - Mike Harrington
    elif self.team_key == '124.l.353149.t.3':
      return 23
    # 24 - Dylan McKenzie
    elif self.guid == 'AMMLHA4JI5PLXAE2TMOSGGOMJY':
      return 24
    # 25 - Ed Bailey
    elif self.guid == 'SPVAOCXZDWG4377AFX5RQ6IMU4' or self.guid == 'O2UMFNPIAV3SQKLPMZ65CP4OJI':
      return 25
    # 26 - Stefan Veldhuis
    elif self.team_key == '175.l.86206.t.8' or self.guid == 'BGV27ND3LVWX2RXZJNBDWKMFVM' or self.team_key =='257.l.43112.t.12':
      return 26
    # 27 - Seth Rogers
    elif self.guid == '2YZHA7AQZ7JX36QUD4S4HAHK2U':
      return 27
    # 28 - Joe Gilbert
    elif self.guid == 'V56E3L7MTGLKLFZFNCEMGL6LZ4':
      return 28
    # 29 - Chris Quarterman
    elif self.guid == 'L4LKZGFF4CVLI5NAWW6T7MX3WY':
      return 29   
    # 30 - Keith
    elif self.guid == 'KMMUMMTHTXLA2BIU4O4IOE3QMY':
      return 29   
    # 31 - Cavin Keys
    elif self.guid == 'RNTYM2XSPKCNRIM6JU2A456DEY':
      return 29   
    # 32 - Tucker
    elif self.guid == 'WNDV4I25AHS4ODKTSGJVMN2XWE':
      return 29                              
    else:
      return -1