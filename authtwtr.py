#! /home/alfa/tempy/env/bin/python
import os
import tweepy

def authtwtr():
	api_key = os.getenv('API_KEY')
	api_key_secret = os.getenv('API_KEY_SECRET')
	access_token = os.getenv('ACCESS_TOKEN')
	access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

	auth = tweepy.OAuthHandler(api_key, api_key_secret)
	auth.set_access_token(access_token, access_token_secret)

	global api
	api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
	return api
