import requests

import auth
import constants


def get_player_info(year, player_id):
	url = "https://fantasysports.yahooapis.com/fantasy/v2/player/%s.p.%s" % (constants.YEAR_PREFIX[year], player_id)

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
	url = "https://fantasysports.yahooapis.com/fantasy/v2/player/%s" % (player_key)

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
	url = "https://fantasysports.yahooapis.com/fantasy/v2/league/%s/draftresults" % constants.LEAGUE_LOOKUP[year]

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
	url = "https://fantasysports.yahooapis.com/fantasy/v2/league/%s/transactions" % constants.LEAGUE_LOOKUP[year]

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