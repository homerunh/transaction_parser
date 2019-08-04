#!/cygdrive/d/cygwin64/bin/python3

import pymysql
import datetime
import json
import csv

from models.nfl_player import nfl_player
from models.transaction import transaction
from models.team_manager import team_manager
from models.league_details import league_details
from models.league_week_matchup import league_week_matchup
import db
import api
import constants

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

    draft_day_timestamp = datetime.datetime.fromtimestamp(int('1467374400'))
    year = data['fantasy_content']['league'][0]['season']
    count = data['fantasy_content']['league'][1]['draft_results']['count']

    draft_results = data['fantasy_content']['league'][1]['draft_results']

    for i in range(0, count):
        draft_result = data['fantasy_content']['league'][1]['draft_results'][str(i)]['draft_result']

        pick = draft_result['pick']
        draft_round = draft_result['round']
        team_key = draft_result['team_key']
        player_key = draft_result['player_key']
        # print("%s   %s" % (draft_result, player_id))

        player_json = api.get_player_info_by_key(player_key).json()
        p = create_player_model_from_player_endpoint(player_json)
        #p.printME()
        db.insert_player(p)

        draft_transaction = transaction(year, "draft_pick_%s" % pick, p.player_id, team_key, 'startup_draft_pick_add', draft_day_timestamp)
        # draft_transaction.printME()
        db.insert_transaction(draft_transaction)

        draft_day_timestamp = draft_day_timestamp + datetime.timedelta(seconds=1)
        
        
# Helper function
def create_player_model_from_player_endpoint(player_json):
    player_key = player_json['fantasy_content']['player'][0][0]['player_key']
    player_id = player_json['fantasy_content']['player'][0][1]['player_id']
    first_name = player_json['fantasy_content']['player'][0][2]['name']['first']
    last_name = player_json['fantasy_content']['player'][0][2]['name']['last']
    full_name = player_json['fantasy_content']['player'][0][2]['name']['full']
    try:
        nfl_team = player_json['fantasy_content']['player'][0][7]['editorial_team_abbr']
    except:
        for j in range(0, len(player_json['fantasy_content']['player'][0])):
            if type(player_json['fantasy_content']['player'][0][j]) is dict and 'editorial_team_abbr' in player_json['fantasy_content']['player'][0][j].keys():
                nfl_team = player_json['fantasy_content']['player'][0][j]['editorial_team_abbr']
                break
    try:
        position = player_json['fantasy_content']['player'][0][10]['display_position']
    except:
        for j in range(0, len(player_json['fantasy_content']['player'][0])):
            if type(player_json['fantasy_content']['player'][0][j]) is dict and 'display_position' in player_json['fantasy_content']['player'][0][j].keys():
                position = player_json['fantasy_content']['player'][0][j]['display_position']
                break
        

    return nfl_player(player_key, player_id, first_name, last_name, full_name, nfl_team, position)



def sync_rookie_draft_from_file():

    draft_day_timestamp = datetime.datetime.fromtimestamp(int('1531584000'))
    pick = 1

    reader = csv.reader(open('2018_rookie_fa_draft.csv'), delimiter=',')
    next(reader) #skip header
    for row in reader:
        player_id = row[1]
        team_key = row[2]

        player_json = api.get_player_info_by_key('380.p.%s' % player_id).json()
        p = create_player_model_from_player_endpoint(player_json)
        # p.printME()
        db.insert_player(p)

        draft_transaction = transaction(2018, "2018_rookie_draft_pick_%s" % pick, p.player_id, team_key, '2018_rookie_fa_draft_add', draft_day_timestamp)
        # draft_transaction.printME()
        db.insert_transaction(draft_transaction)

        pick = pick + 1
        draft_day_timestamp = draft_day_timestamp + datetime.timedelta(seconds=1)

def sync_offseason_trade_from_file():
    pick = 1

    reader = csv.reader(open('2018_preseason_trades.csv'), delimiter=',')
    next(reader) #skip header
    for row in reader:
        player_id = row[1]
        team_key = row[2]
        draft_day_timestamp = datetime.datetime.fromtimestamp(int(row[4]))

        player_json = api.get_player_info_by_key('380.p.%s' % player_id).json()
        p = create_player_model_from_player_endpoint(player_json)
        # p.printME()
        db.insert_player(p)

        draft_transaction = transaction(2018, "2018_preseason_trade_%s" % pick, p.player_id, team_key, '2018_preseason_trade_add', draft_day_timestamp)
        # draft_transaction.printME()
        db.insert_transaction(draft_transaction)
    

        pick = pick + 1
        

def sync_current_roster(team_key):
    roster_json = api.get_team_players(team_key).json()
    players = roster_json['fantasy_content']['team'][1]['players']
    team_key = roster_json['fantasy_content']['team'][0][0]['team_key']

    for i in range(0, players['count']):
        player_key = players[str(i)]['player'][0][0]['player_key']
        player_id = players[str(i)]['player'][0][1]['player_id']
        first_name = players[str(i)]['player'][0][2]['name']['first']
        last_name = players[str(i)]['player'][0][2]['name']['last']
        full_name = players[str(i)]['player'][0][2]['name']['full']
        try:
            nfl_team = players[str(i)]['player'][0][7]['editorial_team_abbr']
        except:
            for j in range(0, len(players[str(i)]['player'][0])):
                if type(players[str(i)]['player'][0][j]) is dict and 'editorial_team_abbr' in players[str(i)]['player'][0][j].keys():
                    nfl_team = players[str(i)]['player'][0][j]['editorial_team_abbr']
                    break
        try:
            position = players[str(i)]['player'][0][10]['display_position']
        except:
            for j in range(0, len(players[str(i)]['player'][0])):
                if type(players[str(i)]['player'][0][j]) is dict and 'display_position' in players[str(i)]['player'][0][j].keys():
                    position = players[str(i)]['player'][0][j]['display_position']
                    break


        p = nfl_player(player_key, player_id, first_name, last_name, full_name, nfl_team, position)        
        # p.printME()
        # print(team_key)
        db.insert_player(p)
        db.insert_player_current_roster(p, team_key)

def sync_rosters():
    teams = ['380.l.11074.t.1',\
    '380.l.11074.t.2',\
    '380.l.11074.t.3',\
    '380.l.11074.t.4',\
    '380.l.11074.t.5',\
    '380.l.11074.t.6',\
    '380.l.11074.t.7',\
    '380.l.11074.t.8',\
    '380.l.11074.t.9',\
    '380.l.11074.t.10']

    for team in teams:
        sync_current_roster(team)

def spin_up_new():
    sync_draft_results('2016')
    sync_transactions('2016')
    sync_transactions('2017')
    sync_rookie_draft_from_file()
    sync_offseason_trade_from_file()
    sync_transactions('2018')
    sync_rosters()

def get_league_details_and_managers(year):
    data = api.get_league_teams(year).json()
    
    league_url = data['fantasy_content']['yahoo:uri']
    league = data['fantasy_content']['league'][0]
    teams = data['fantasy_content']['league'][1]['teams']
    team_count = teams['count']

    #print_league_details()
    league_key = league['league_key']
    league_id = league['league_id']
    league_name = league['name']
    start_week = int(league['start_week'])
    start_date = league['start_date']
    end_week = int(league['end_week'])
    end_date = league['end_date']
    league_year = league['season']

    the_league_details = league_details(league_key, league_id, league_name, start_week, start_date, end_week, end_date, league_year, team_count)
    the_league_details.printME()
    db.insert_league_details(the_league_details)

    #print league teams details
    all_managers = list()
    for i in range(0, team_count):
        team_details = teams[str(i)]['team']

        team_key = teams[str(i)]['team'][0][0]['team_key']
        team_name = teams[str(i)]['team'][0][2]['name']
        number_of_moves = int(teams[str(i)]['team'][0][9]['number_of_moves'])
        number_of_trades = int(teams[str(i)]['team'][0][10]['number_of_trades'])
        nickname = teams[str(i)]['team'][0][19]['managers'][0]['manager']['nickname']
        try:
            guid = teams[str(i)]['team'][0][19]['managers'][0]['manager']['guid']
        except:
            guid = 'NONE'
        try:
            email = teams[str(i)]['team'][0][19]['managers'][0]['manager']['email']
        except:
            email = 'NONE'

        a_league_manager = team_manager(league_key, team_key, team_name, number_of_moves, number_of_trades, nickname, guid, email)
        a_league_manager.printME()
        all_managers.append(a_league_manager)
        db.insert_team_manager(a_league_manager)

    return (the_league_details, all_managers)

def do_league_manager_recon():
    for year in constants.LEAGUE_LOOKUP.keys():
        ldm = get_league_details_and_managers(year)
        for tm in ldm[1]:
            db.insert_manager_league_team_assignment(tm)

def get_scoreboard_for_league_week(year, week_number):
    data = api.get_league_scoreboard_for_week(year, week_number).json()
    league_year = league = int(data['fantasy_content']['league'][0]['season'])
    league_key = league = data['fantasy_content']['league'][0]['league_key']
    matchups = data['fantasy_content']['league'][1]['scoreboard']['0']['matchups']
    matchup_count = matchups['count']

    for i in range(0, matchup_count):
        matchup = matchups[str(i)]['matchup']
        week = matchup['week']
        week_start = matchup['week_start']
        status = matchup['status']
        is_playoffs = matchup['is_playoffs']
        is_consolation = matchup['is_consolation']
        is_matchup_recap_available = matchup['is_matchup_recap_available']
        is_tied = matchup['is_tied']
        if not is_tied:
            winner_team_key = matchup['winner_team_key']
        else:
            winner_team_key = 'NONE'

        teams = matchups[str(i)]['matchup']['0']['teams']
        team_count = teams['count']

        if team_count == 2:
            team_key_1 = teams['0']['team'][0][0]['team_key']
            team_1_points = teams['0']['team'][1]['team_points']['total']
            team_key_2 = teams['1']['team'][0][0]['team_key']
            team_2_points = teams['1']['team'][1]['team_points']['total']
            

        elif team_count == 1:
            team_key_1 = teams['0']['team'][0][0]['team_key']
            team_1_points = teams['0']['team'][1]['team_points']['total']
            team_key_2 = 'NONE'
            team_2_points = 0.0

        m = league_week_matchup(league_key, \
            league_year, \
            int(week), \
            week_start, \
            status, \
            int(is_playoffs), \
            int(is_consolation), \
            int(is_matchup_recap_available), \
            int(is_tied), \
            winner_team_key, \
            team_key_1, \
            float(team_1_points), \
            team_key_2, \
            float(team_2_points))
        m.printME()

        db.insert_league_week_matchup(m)

def do_matchup_recon():
    leagues = db.get_league_details()
    for i in range(0, len(leagues)):
        for w in range(leagues[i].start_week, leagues[i].end_week +1):
            get_scoreboard_for_league_week(str(leagues[i].league_year), w)


# do_league_manager_recon()
# do_matchup_recon()

get_scoreboard_for_league_week('2018', 16)
