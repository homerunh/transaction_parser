#!/cygdrive/d/cygwin64/bin/python3

# export const DYNASTY_LEAGUE_LOOKUP = {
#   2016: "359.l.302857",
#   2017: "371.l.15908",
#   2018: "380.l.11074",
# };

import sys;
import datetime;
import json;

transaction_data = list();
transaction_data.append('dynasty_2017_transactions.json');
transaction_data.append('dynasty_2016_transactions.json');
print(",".join(['League Year', 'Transaction key', 'Transaction Timestamp', 'Player Name', 'Player Team', 'Player Position', 'Transaction Type', 'Add From / Drop to', 'Add To / Drop From']))
for f in transaction_data:
  data = json.load(open(f));
  
  league_details = data['fantasy_content']['league'][0]
  year = league_details = data['fantasy_content']['league'][0]['season']
  season_transaction_count = len(data['fantasy_content']['league'][1]['transactions'].keys())
  for i in range(0, season_transaction_count - 1):
    transaction_details = data['fantasy_content']['league'][1]['transactions'][str(i)]['transaction'][0]
    transaction_type = transaction_details['type']
    transaction_key = transaction_details['transaction_key']
    timestamp = datetime.datetime.fromtimestamp(int(transaction_details['timestamp']))

    if (transaction_type == 'commish'):
      players = []
      ##TODO: print commish row
    else:
      players = data['fantasy_content']['league'][1]['transactions'][str(i)]['transaction'][1]['players']

      for j in range(0, players['count']):
        player_info = players[str(j)]['player'][0]
        full_name = players[str(j)]['player'][0][2]['name']['full']
        nfl_team = players[str(j)]['player'][0][3]['editorial_team_abbr']
        position = players[str(j)]['player'][0][4]['display_position']

        # tData = players[str(j)]['player'][1]['transaction_data'][0]
        if type(players[str(j)]['player'][1]['transaction_data']) is list:
          player_transaction_type = players[str(j)]['player'][1]['transaction_data'][0]['type']
        else:
          player_transaction_type = players[str(j)]['player'][1]['transaction_data']['type']

        if player_transaction_type == 'add':
          destination_team_name =  players[str(j)]['player'][1]['transaction_data'][0]['destination_team_name']
          destination_type =  players[str(j)]['player'][1]['transaction_data'][0]['destination_type']
          source_type = players[str(j)]['player'][1]['transaction_data'][0]['source_type']
          #print('%s %s %s %s %s %s %s %s %s      src: %s' % (year, transaction_key, timestamp,full_name, nfl_team, position, player_transaction_type, destination_type, destination_team_name, source_type))
          #print('%s %s %s %s %s %s %s %s %s' % (year, transaction_key, timestamp,full_name, nfl_team, position, player_transaction_type, source_type, destination_team_name))
          print(",".join(map( str, [year, transaction_key, timestamp, full_name, nfl_team, position, player_transaction_type, source_type, destination_team_name])))
        if player_transaction_type == 'drop':
          source_team_name =  players[str(j)]['player'][1]['transaction_data']['source_team_name']
          destination_type =  players[str(j)]['player'][1]['transaction_data']['destination_type']
          source_type = players[str(j)]['player'][1]['transaction_data']['source_type']
          #print('%s %s %s %s %s %s %s %s %s' % (year, transaction_key, timestamp,full_name, nfl_team, position, player_transaction_type, destination_type, source_team_name))
          print(",".join(map( str, [year, transaction_key, timestamp,full_name, nfl_team, position, player_transaction_type, destination_type, source_team_name])))

    


    # print(transaction_details)
    # print(transaction_data)
    # print(i)
    # print(transaction_type)
    # print(timestamp)
    # print(players)
  




  
# print("HEY! %s" % (sys.argv[1]));