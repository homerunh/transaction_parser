import requests

import auth
import constants

def urlify(list_of_params):
	return "/".join(list_of_params)


def get_player_info(year, player_id):
	url = urlify([constants.API_BASE_URL, "player", "%s.p.%s" % (constants.YEAR_PREFIX[year], player_id)]) 

	querystring = {"format":"json"}

	payload = ""
	headers = {
	    'Authorization': "bearer " + auth.get_bearer_token(),
	    'cache-control': "no-cache",
	    'Postman-Token': "acc1f544-234e-4a1b-9eef-69b10de156d2"
	    }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

	# print(response.text)
	return response

def get_player_info_by_key(player_key):
	url = urlify([constants.API_BASE_URL, "player", player_key])

	querystring = {"format":"json"}

	payload = ""
	headers = {
	    'Authorization': "bearer " + auth.get_bearer_token(),
	    'cache-control': "no-cache",
	    'Postman-Token': "acc1f544-234e-4a1b-9eef-69b10de156d2"
	    }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

	# print(response.text)
	return response

def get_draft_results(year):
	url = urlify([constants.API_BASE_URL, "league", constants.LEAGUE_LOOKUP[year], "draftresults"])

	querystring = {"format":"json"}

	payload = ""
	headers = {
	    'Authorization': "bearer " + auth.get_bearer_token(),
	    'cache-control': "no-cache",
	    'Postman-Token': "175947ac-ffe1-44b3-8b63-fc451ff66601"
	    }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

	# print(response.text)
	return response

def get_league_transactions(year):
	url = urlify([constants.API_BASE_URL, "league", constants.LEAGUE_LOOKUP[year], "transactions"])

	querystring = {"format":"json"}

	payload = ""
	headers = {
	    'Authorization': "bearer " + auth.get_bearer_token(),
	    'cache-control': "no-cache",
	    'Postman-Token': "a6fec9cf-8b4e-4ca1-b788-d3f77b5b03a2"
	    }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

	# print(response.text)
	return response


def get_team_players(team_key):
	url = urlify([constants.API_BASE_URL, "team", team_key, "players"])

	querystring = {"format":"json"}

	payload = ""
	headers = {
	    'Authorization': "bearer " + auth.get_bearer_token(),
	    'cache-control': "no-cache",
	    'Postman-Token': "9ca3433a-736d-4524-9f6d-4c17e498f96c"
	    }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

	# print(response.text)
	return response