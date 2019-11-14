#   Carl Grissom
#   sentiment.py
#   3/27/2019
#   Description: functions for sentiment analysis

import datetime
import collections
from .models import Tweet, WordList
from nltk.tokenize import TweetTokenizer
from . import sentiment, twitterAuth
from itertools import islice


def getSearchResults(searchTerm='#Bayer', tweetCount=100):
    ''' Makes a search request to twitter, returns dictionary of found tweets. '''
    requestDataList = []
    location = ''
    request = twitterAuth.api.GetSearch(searchTerm,
                                        count=tweetCount,
                                        result_type='recent',
                                        return_json=True)  # returns a JSON object

    numberOfTweets = tweetCount - ((len(request["statuses"])) - 1)
    idOfLastTweet = ""

    while (numberOfTweets > 0):
        if len(request["statuses"]) > 0:
            for tweets in request['statuses'][:-2]:
                requestDataList.append(tweets)
        numberOfTweets -= (len(request["statuses"])) - 1
        idOfLastTweet = request['statuses'][-1]['id_str']
        if (numberOfTweets > 0):
            request = twitterAuth.api.GetSearch(searchTerm,
                                                count=tweetCount,
                                                max_id=idOfLastTweet,
                                                lang="en",
                                                return_json=True)
    return requestDataList


def loadDatabase(listOfTweets):
    Tweet.objects.all().delete()
    WordList.objects.all().delete()

    fullSearchText = ''
    starttime = datetime.datetime.now()

    for tweet in listOfTweets:
        try:
            # get sentiment
            tweetSentiment = sentiment.sentiment_analyzer_score(
                tweet['full_text'])
            # create tweet
            Tweet.objects.create(fullText=tweet['full_text'],
                                 userId=tweet['user']['id_str'],
                                 tweetId=tweet['id_str'],
                                 #date = tweet['created_at'],
                                 likes=tweet['favorite_count'],
                                 retweets=tweet['retweet_count'],
                                 sentiment=tweetSentiment['compound']
                                 )
            fullSearchText = fullSearchText + tweet['full_text']

        except:
            pass

    batch_size = 500
    objs = (WordList(word=token) for token in fullSearchText.lower().split())
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        WordList.objects.bulk_create(batch, batch_size)

    totaltime = datetime.datetime.now() - starttime

    print('total Tweets: ', len(listOfTweets))
    print('total time: ', totaltime)

    return None
