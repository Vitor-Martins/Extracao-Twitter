#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import tweepy
import json

#Autenticações
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# O Yahoo! Where On Earth ID para o Brasil é 23424768.
# Veja mais em https://dev.twitter.com/docs/api/1.1/get/trends/place e http://developer.yahoo.com/geo/geoplanet/
BRAZIL_WOE_ID = 23424768
 
brazil_trends = api.trends_place(BRAZIL_WOE_ID)
 
trends = json.loads(json.dumps(brazil_trends, indent=1))
 
for trend in trends[0]['trends']:
    print (trend['name'].strip('#'))
    #print (trend['name'])