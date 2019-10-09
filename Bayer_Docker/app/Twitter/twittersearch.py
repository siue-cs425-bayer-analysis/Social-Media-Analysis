#   Carl Grissom
#   sentiment.py   
#   3/27/2019
#   Description: functions for sentiment analysis


from .models import Tweet
import collections
from nltk.tokenize import TweetTokenizer
from . import locations, sentiment, twitterAuth

def getRecentSearchResults(searchTerm = '#Bayer', tweetCount = 10000, popOrRecent='recent', location=''):
    ''' Makes a search request to twitter, returns dictionary of found tweets. '''
    requestDataList = []
    request = twitterAuth.api.GetSearch(searchTerm, 
                                        geocode=location,
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
        
def tweetsLoadIntoDatabase(listOfTweets):
    for tweet in listOfTweets:
        sentiment = sentiment.sentiment_analyzer_score(tweet['full_text'])
        Tweet.objects.create(full_text=tweet['full_text'], 
                            user_id=tweet['user']['id_str'],    
                            tweet_id=tweet['id_str'],
                            date = tweet['created_at'], 
                            favorite = tweet['favorite_count'], 
                            retweets = tweet['retweet_count'],
                            lang = tweet['lang'],
                            sentiment = 0.0)                    

def wordListLoadDatabase(listOfTweets):
    tokenizer = TweetTokenizer()
    counter = collections.Counter()
    wordDict = {}
    tweetId = ""
    
    # tokenize the tweet text
    for tweets in requestDataList:
        tokenizedtweet =  tokenizer(tweets[full_text])
        tweetId = tweet['id_str']
        
        for word in tokenizedtweet:
            
        
        
       
    
    return ""
