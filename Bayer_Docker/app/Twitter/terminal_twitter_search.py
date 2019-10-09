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
from locations import *                 


# search parameters default values
searchTerm = "#Bayer" 
tweetCount = 1
filename = 'test.txt'
location = "None"

stopWordsFile = "resources/stop_words.txt"
twitterStopWordsFile = "resources/twitter_stop_words.txt"


#  dictionary to hold parsed twitter search results
#TODO ADD ADDITIONAL DATA VALUES
#TODO WHEN DONE TESTING MOVE THIS TO twitter.py

# list to hold tweetData 
requestDataList = []

requestSearchTerm = "Enter a search term, or press enter for default #Bayer: "
requestNumberOfTweets = "Enter number of tweets to collect, or press enter for default (100):"
requestLocation = "Please Enter the name of a valid location, valid locations are "

for locations in LOCATIONS:
     requestLocation += "\n" + locations
requestLocation += '\n'

temp = input(requestSearchTerm)

if temp != '':
    searchTerm = temp;

while True:
    temp = input(requestNumberOfTweets)
    if temp != '':
        try:
            tweetCount = int(temp);
        except ValueError:
            print("Input was not an integer")
        else: 
            tweetCount = str(tweetCount)
            break
    if temp == '':
        break
               
        
location = input(requestLocation)
display_location = ""

for key in LOCATIONS:
    if key.lower() == location.lower():
        display_location = key
        location = LOCATIONS[key]

print("Search Term\tReturn Count\tLocation")    
print("%s\t\t%s\t\t%s" %(searchTerm, tweetCount, display_location))

request = twitterAuth.api.GetSearch(searchTerm, 
                                    count=tweetCount, 
                                    geocode=location, 
                                    lang="en", 
                                    return_json=True) # returns a Dict object
averageSentiment = ""
requestJSON = json.dumps(request, indent = 2)
counter = collections.Counter()
wordList = []
words = ""
if len(request["statuses"]) != 0:
    for tweets in request['statuses']:
        tweetData = {
             'text': tweets['full_text'],
             'user': tweets['id'],           
             'sentiment': sentiment.sentiment_analyzer_score(tweets["full_text"])
             }
        requestDataList.append(tweetData)
    
    totalSentimentValue = 0    
    averageSentiment = 0
    
    for data in requestDataList:
        print('\n', data['text'], '\n', data['user'])
        print(data['sentiment']['compound'])
        totalSentimentValue += data['sentiment']['compound']  
    
    averageSentiment = totalSentimentValue / len(requestDataList)
    
    for text in requestDataList:
        tokens = nltk.word_tokenize(text['text'])
        wordList.extend(tokens)
        words += text['text']
    
    for word in wordList:
       counter[word] += 1
    
else:
    print("no tweets found")

print("Sentiment analysis on all tweets as single text: %s" 
    % sentiment.sentiment_analyzer_score(words))
print("Average Sentiment of all tweets: %s" % averageSentiment)


# strip stop words from counter Set
with open(stopWordsFile) as stopWords:
    stopWordList = stopWords.read().splitlines()

with open(twitterStopWordsFile) as twitterStopWords:
    stopWordList.extend(twitterStopWords.read().splitlines())

for key in stopWordList:
    if key in counter:
        del counter[key]
      
for key, value in list(counter.items()):
    if value < 5:
        del counter[key]
    
for key in list(counter.keys()):
    if key.startswith('//'):
        del counter[key]

for key, value in counter.items():
    print(key," ", value)
