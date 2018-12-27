#!/usr/bin/python

# export const DYNASTY_LEAGUE_LOOKUP = {
#   2016: "359.l.302857",
#   2017: "371.l.15908",
#   2018: "380.l.11074",
# };

# https://api.login.yahoo.com/oauth2/request_auth
# ?client_id=<id>
# &redirect_uri=oob
# &response_type=code

import time
import requests
import pickle
from pathlib import Path

import creds.api_creds

def request_token(code):

	now = int(time.time())

	url = "https://api.login.yahoo.com/oauth2/get_token"
	client_id=creds.api_creds.CLIENT_ID
	client_secret=creds.api_creds.CLIENT_SECRET
	redirect_uri="oob"
	grant_type="authorization_code"
	auth_code=code

	payload = "client_id="+ client_id +"&client_secret="+ client_secret +"&redirect_uri="+ redirect_uri +"&code="+ auth_code + "&grant_type=" + grant_type
	headers = {
	    'Content-Type': "application/x-www-form-urlencoded",
	    'Cache-Control': "no-cache",
	    'Postman-Token': "ae9442c8-0d76-4d66-a189-476dba6e1dd2"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)
	pickle.dump({'expires': now + 3500, 'response':response.json()}, open('token.p', 'wb'))
	return response

def get_bearer_token():
	token_pickle = Path("token.p")
	if token_pickle.is_file():
		details = pickle.load(open('token.p','rb'))
		if (int(time.time()) > details['expires']):
			code = input("Input an access code: ")
			return request_token(code).json()['access_token']
		else:
			print("TOKEN: %s" % details['response']['access_token'])
			return details['response']['access_token']

		
	else:
		code = input("Input an access code: ")
		return request_token(code).json()['access_token']