from transaction_parser import *


## manager assignment
def bodos_league_manager_recon_and_assignment():
    _league_manager_recon_and_assignment(constants.LEAGUE_LOOKUP)


def tappa_kegga_league_manager_recon_and_assignment():
    _league_manager_recon_and_assignment(constants.LEAGUE_LOOKUP)


def _league_manager_recon_and_assignment(league_lookup_map):
    for year in league_lookup_map.keys():
        ldm = get_league_details_and_managers(league_lookup_map[year])
        for tm in ldm[1]:
            db.insert_manager_league_team_assignment(tm)


## weekly matchups (db based)
def bodos_league_weekly_matchups():
    _league_weekly_matchups(constants.LEAGUE_LOOKUP)


def tappa_kegge_league_weekly_matchups():
    _league_weekly_matchups(constants.LEAGUE_LOOKUP)


def _league_weekly_matchups(league_lookup_map):
    leagues = db.get_league_details(league_lookup_map)
    for i in range(0, len(leagues)):
        for w in range(leagues[i].start_week, leagues[i].end_week + 1):
            # get_scoreboard_for_league_week(str(leagues[i].league_year), w)
            get_scoreboard_for_league_week(league_lookup_map[str(leagues[i].league_year)], w)


## standings
def bodos_league_standings():
    _league_standings(constants.LEAGUE_LOOKUP)


def tappa_kegga_league_standings():
    _league_standings(constants.LEAGUE_LOOKUP)


def _league_standings(league_lookup_map):
    for year in league_lookup_map.keys():
        update_league_standings(year, league_lookup_map[year])


### main entry points:
def pull_bodos():
    bodos_league_manager_recon_and_assignment()
    bodos_league_weekly_matchups()
    bodos_league_standings()

def pull_tappa_kegga():
    tappa_kegga_league_manager_recon_and_assignment()
    tappa_kegge_league_weekly_matchups()
    tappa_kegga_league_standings()


def main():
    print('running main:')
    # run below to setup the DB from scratch
    # mysql -uroot -p<passwordHERE> < sql/Bodos_create.sql
    # then double check creds.py to be sure you hit Bodos DB
    # then run the script
    pull_bodos()

    # run below to setup the DB from scratch
    # mysql -uroot -p<passwordHERE> < sql/TappaKegga_create.sql
    # then double check creds.py to be sure you hit Bodos DB
    # then run the script
    # pull_tappa_kegga()



if __name__ == '__main__':
    main()