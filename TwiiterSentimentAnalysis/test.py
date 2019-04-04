#   Author: Carl Grissom
#   Date: 03/29/2019
#   File name: test.py
#   Description: test file for Bayer twiiter search and sentiment analysis.
#
#   All rights reserved.

import collections
import json
import nltk

# local twitter imports
import sentiment
import twitterAuth  
from locations import *                 


# search parameters default values
searchTerm = "Bayer" 
tweetCount = 15
filename = 'test.txt'
location = "None"

stopWordsFile = "resources/stop_words.txt"
twitterStopWordsFile = "resources/twitter_stop_words.txt"


#  dictionary to hold parsed twitter search results
#TODO ADD ADDITIONAL DATA VALUES
#TODO WHEN DONE TESTING MOVE THIS TO twitter.py

# list to hold tweetData 
requestDataList = []

requestSearchTerm = "Enter a search term, or press enter for default (#Bayer)"
requestNumberOfTweets = "Enter number of tweets to collect, or press enter for default (15):"
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
    
print(searchTerm, tweetCount, location)

request = twitterAuth.api.GetSearch(searchTerm, count=tweetCount, geocode=location, lang="en", return_json=True) # returns a Dict object

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

print(counter)

with open(stopWordsFile) as stopWords:
    stopWordList = stopWords.read().splitlines()

with open(twitterStopWordsFile) as twitterStopWords:
    stopWordList.extend(twitterStopWords.read().splitlines())
    
print(str(len(stopWordList)))

for key in stopWordList:
    if key in counter:
        del counter[key]

print(counter)
   
    


