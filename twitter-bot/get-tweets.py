#!/usr/bin/env python
#more examples at https://www.blog.pythonlibrary.org/2019/08/06/using-twitter-with-python-and-tweepy/

import tweepy

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
my_tweets = api.user_timeline()
for t in my_tweets:
    print(t.text)
