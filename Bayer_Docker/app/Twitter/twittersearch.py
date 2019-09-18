#   Carl Grissom
#   sentiment.py   
#   3/27/2019
#   Description: functions for sentiment analysis
#
#
#

import logging

from .models import Tweet


from . import locations, sentiment, twitterAuth


#   create database object  
#     Tweet.objects.create(full_text=tweets['full_text'], user_id=tweets['user']['id_str'], tweet_id=tweets['id_str'], sentiment = 0.0)
    

def getSearchResults(searchTerm = '#Bayer', tweetCount = 1000, location=''):
    requestDataList = []
    request = twitterAuth.api.GetSearch(searchTerm, 
                                        geocode=location,
                                        count=tweetCount,
                                        max_id=None, 
                                        lang="en", 
                                        result_type='recent',
                                        return_json=True) # returns a JSON object
    numberOfTweets = tweetCount - 100
    while (numberOfTweets > 0):
        if len(request["statuses"]) != 0:
            for tweets in request['statuses']:
               requestDataList.append(tweets)
        numberOfTweets -= 100
        idOfLastTweet = requestDataList[-1]['id_str'] 
        print(idOfLastTweet)
        if (numberOfTweets > 0):
            request = twitterAuth.api.GetSearch(searchTerm, 
                                                geocode = location,
                                                count = tweetCount,
                                                max_id = idOfLastTweet, 
                                                lang = "en", 
                                                result_type = 'recent',
                                                return_json=True) 
    return requestDataList
    
def tweetSentiment(tweets):
    for tweet in tweets:
        tweet[sentiment] = sentiment.sentiment_analyzer_score(tweet["text"])
    
