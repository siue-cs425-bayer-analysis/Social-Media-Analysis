from django.shortcuts import render
from django.http import HttpResponse

# user defined imports 
from . import twittersearch

# Create your views here.
def index(request):
    
    searchTerm = 'taco' 
    tweetCount = 1
    location=''
    requestDataList = []
    request = twitterAuth.api.GetSearch(searchTerm, 
                                        geocode=location,
                                        count=tweetCount,
                                        max_id=None, 
                                        lang="en", 
                                        result_type='recent',
                                        return_json=True) # returns a JSON object
    
    print(request['statuses'][0]['user']['id_str'])
    
    for tweets in request['statuses']:
        Tweet.objects.create(full_text=tweets['full_text'], 
                             user_id=tweets['user']['id_str'],    
                             tweet_id=tweets['id_str'], 
                             sentiment = 0.0)
    
    #numberOfTweets = tweetCount
    #while (numberOfTweets > 0):
        #if len(request["statuses"]) != 0:
            #for tweets in request['statuses']:
               #Tweet(full_text=tweets['full_text'], tweet_id=tweets['id_str'], sentiment = 0.0)
        #numberOfTweets -= 100
        #numberOfTweetsCollected = len(request["statuses"])
        #idOfLastTweet = request["statuses"][numberOfTweetsCollected - 1]['id_str']  
        #request = twitterAuth.api.GetSearch(searchTerm, 
                                            #geocode = location,
                                            #count = tweetCount,
                                            #max_id = idOfLastTweet, 
                                            #lang = "en", 
                                            #result_type = 'recent',
                                            #return_json=True) # returns a JSON object
    #print("number of tweets found") 
    #print(len(requestDataList))
    
    text = "number of tweets found " + str(len(request['statuses']))
    
    return HttpResponse(Tweet.objects.all())
