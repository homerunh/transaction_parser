#!/cygdrive/d/cygwin64/bin/python3

import pymysql
import datetime
import json

from models.nfl_player import nfl_player
from models.transaction import transaction
import db
import api

#db.testing_testing_123("select `id` from manager")


def sync_transactions(year):

    toCsv = False
    toDB = True

    
    data = api.get_league_transactions(year).json()

    league_details = data['fantasy_content']['league'][0]
    year = league_details['season']
    
    season_transaction_count = data['fantasy_content']['league'][1]['transactions']['count']
    for i in range(0, season_transaction_count - 1):
        transaction_details = data['fantasy_content']['league'][1]['transactions'][str(i)]['transaction'][0]
        transaction_type = transaction_details['type']
        transaction_key = transaction_details['transaction_key']
        timestamp = datetime.datetime.fromtimestamp(int(transaction_details['timestamp']))

        if (transaction_type == 'commish'):
            players = []
            # TODO: print commish row

        elif (transaction_type == 'trade' and transaction_details['status'] == 'successful'):
            players = data['fantasy_content']['league'][1]['transactions'][str(i)]['transaction'][1]['players']
            for j in range(0, players['count']):
                player_info = players[str(j)]['player'][0]
                player_key = player_info[0]['player_key']
                player_id = player_info[1]['player_id']
                first_name = player_info[2]['name']['first']
                last_name = player_info[2]['name']['last']
                full_name = player_info[2]['name']['full']
                nfl_team = player_info[3]['editorial_team_abbr']
                position = player_info[4]['display_position']

                x = nfl_player(player_key, player_id, first_name, last_name, full_name, nfl_team, position)
                # x.printME()
                if (toDB):
                    db.insert_player(x)


                player_transaction_type = players[str(j)]['player'][1]['transaction_data'][0]['type']

                source_team_name = players[str(j)]['player'][1]['transaction_data'][0]['source_team_name']
                source_team_key = players[str(j)]['player'][1]['transaction_data'][0]['source_team_key']
                destination_team_name = players[str(j)]['player'][1]['transaction_data'][0]['destination_team_name']
                destination_team_key = players[str(j)]['player'][1]['transaction_data'][0]['destination_team_key']

                y = transaction(year, transaction_key, x.player_id, destination_team_key, 'trade_add', timestamp)
                #y.printME()
                if (toDB):
                    db.insert_transaction(y)

                if (toCsv):
                    print(",".join(map(str, [year, transaction_key, timestamp, full_name, nfl_team, position, player_transaction_type, source_team_name, destination_team_name])))
        else:
            players = data['fantasy_content']['league'][1]['transactions'][str(i)]['transaction'][1]['players']

            for j in range(0, players['count']):
                player_info = players[str(j)]['player'][0]
                player_key = player_info[0]['player_key']
                player_id = player_info[1]['player_id']
                first_name = player_info[2]['name']['first']
                last_name = player_info[2]['name']['last']
                full_name = player_info[2]['name']['full']
                nfl_team = player_info[3]['editorial_team_abbr']
                position = player_info[4]['display_position']

                x = nfl_player(player_key, player_id, first_name, last_name, full_name, nfl_team, position)
                # x.printME()
                if (toDB):
                    db.insert_player(x)

                # tData = players[str(j)]['player'][1]['transaction_data'][0]
                if type(players[str(j)]['player'][1]['transaction_data']) is list:
                    player_transaction_type = players[str(j)]['player'][1]['transaction_data'][0]['type']
                else:
                    player_transaction_type = players[str(j)]['player'][1]['transaction_data']['type']

                if player_transaction_type == 'add':
                    destination_team_name = players[str(j)]['player'][1]['transaction_data'][0]['destination_team_name']
                    destination_team_key = players[str(j)]['player'][1]['transaction_data'][0]['destination_team_key']
                    # print("\nTEAM KEY: %s" % destination_team_key)
                    destination_type = players[str(j)]['player'][1]['transaction_data'][0]['destination_type']
                    source_type = players[str(j)]['player'][1]['transaction_data'][0]['source_type']
                    # print('%s %s %s %s %s %s %s %s %s      src: %s' % (year, transaction_key, timestamp,full_name, nfl_team, position, player_transaction_type, destination_type, destination_team_name, source_type))
                    # print('%s %s %s %s %s %s %s %s %s' % (year, transaction_key, timestamp,full_name, nfl_team, position, player_transaction_type, source_type, destination_team_name))
                    y = transaction(year, transaction_key, x.player_id, destination_team_key, 'add', timestamp)
                    if (toDB):
                        db.insert_transaction(y)
                    if (toCsv):
                        print(",".join(map(str, [year, transaction_key, timestamp, full_name, nfl_team, position, player_transaction_type, source_type, destination_team_name])))
                if player_transaction_type == 'drop':
                    source_team_name = players[str(j)]['player'][1]['transaction_data']['source_team_name']
                    source_team_key = players[str(j)]['player'][1]['transaction_data']['source_team_key']
                    # print("\nTEAM KEY: %s" % source_team_key)
                    destination_type = players[str(j)]['player'][1]['transaction_data']['destination_type']
                    source_type = players[str(j)]['player'][1]['transaction_data']['source_type']
                    # print('%s %s %s %s %s %s %s %s %s' % (year, transaction_key, timestamp,full_name, nfl_team, position, player_transaction_type, destination_type, source_team_name))
                    y = transaction(year, transaction_key, x.player_id, source_team_key, 'drop', timestamp)
                    if (toDB):
                        db.insert_transaction(y)
                    if (toCsv):
                        print(",".join(map(str, [year, transaction_key, timestamp, full_name, nfl_team, position, player_transaction_type, destination_type, source_team_name])))
    # print(transaction_details)
    # print(transaction_data)
    # print(i)
    # print(transaction_type)
    # print(timestamp)
    # print(players)

# print("HEY! %s" % (sys.argv[1]))


def sync_draft_results(year):
    data = api.get_draft_results(year).json()

    year = data['fantasy_content']['league'][0]['season']
    count = data['fantasy_content']['league'][1]['draft_results']['count']

    draft_results = data['fantasy_content']['league'][1]['draft_results']

    for i in range(0, count):
        draft_result = data['fantasy_content']['league'][1]['draft_results'][str(i)]['draft_result']

        team_key = draft_result['team_key']
        player_key = draft_result['player_key']
        player_id = draft_result['player_key'].split(".")[2]
        print("%s   %s" % (draft_result, player_id))


