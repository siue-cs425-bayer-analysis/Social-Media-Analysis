#   Author: Carl Grissom
#   Date: 03/29/2019
#   File name: test.py
#   Description: test file for Bayer twiiter search and sentiment analysis.
#
#   All rights reserved.

import collections
import json
import nltk
import re


# local twitter imports
import sentiment
import twitterAuth   
                 

def getSearchResults(searchTerm = '', tweetCount = 10, popOrRecent='recent', location=''):
    ''' Makes a search request to twitter, returns dictionary of found tweets. '''
    requestDataList = []
    request = twitterAuth.api.GetSearch(searchTerm,
                                        geocode="",
                                        count=tweetCount,
                                        max_id=None, 
                                        lang="en", 
                                        result_type=popOrRecent,
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
                                                result_type = popOrRecent,
                                                return_json=True) 
    return requestDataList

getSearchResults()

