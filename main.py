# -*- coding: utf-8 -*-
import requests
import json

from requests_oauthlib import OAuth1Session

from twitter import TwitterClient

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret_token = ''

twitter_client = TwitterClient(consumer_key, consumer_secret,
								access_token, access_secret_token)

for tweet in twitter_client.get_tweets('naruto', n=100, lang='pt-br'):
	print(tweet['text'])
