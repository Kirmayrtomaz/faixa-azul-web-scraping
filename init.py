

import tweepy
from tweepy import OAuthHandler

import json
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.


 
# consumer_key = 'YOUR-CONSUMER-KEY'
# consumer_secret = 'YOUR-CONSUMER-SECRET'
# access_token = 'YOUR-ACCESS-TOKEN'
# access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)


# If the authentication was successful, you should
# see the name of the account print out
# print(api.me())

#query que vc quer buscar
query = 'flamengo'
page_count = 0

#varrendo o resultado da consulta
for twetts in tweepy.Cursor(api.search,q=query,count = 1,result_type="recent").pages():


	page_count =+ 1

	#salvando o primeiro objeto no json
	file_ = open('twett.json', 'w')
	file_.write(json.dumps(twetts[0]._json))
	file_.close()
	#if page_count >= 200:  
	break





