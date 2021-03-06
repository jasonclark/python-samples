#!/usr/bin/env python

import tweepy
import time
import sys

#single file line text source for bot to read
source = str(sys.argv[1])

#ADD info from your registered Twitter application:
CONSUMER_KEY = 'ADD your consumer key'
CONSUMER_SECRET = 'ADD your consumer secret'
ACCESS_KEY = 'ADD your access key' 
ACCESS_SECRET = 'ADD your access secret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open(source, "r") as filename:
    data = filename.readlines()
    filename.close()

for line in data:
    api.update_status(line)
    tweet every 15 minutes
    time.sleep(900)
