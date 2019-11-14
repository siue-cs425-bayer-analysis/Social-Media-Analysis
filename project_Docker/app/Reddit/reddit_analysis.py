# File: reddit_analysis.py
# Project: Social-Media-Analysis
# Team: Bayer-Social-Media-Analysis
# Programmer: Jacob Grubb
# Description: Python script to gather raw posts from Reddit, then pass those posts into a sentiment analyzer to determine overall sentiment

import requests
import vaderSentiment
import json
import praw
import statistics
import random
import itertools

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getAffinityValue(analyzer, text):
    return analyzer.polarity_scores(text)

def getPosts(reddit, keyword, subreddit_name, opt_startDate, opt_endDate):
    #query = "https://www.reddit.com/search.json?q=" + keyword
    #searchResponse = requests.get(query)
    #Identify list of posts
    list_of_posts = reddit.subreddit(subreddit_name).search(keyword)
    #print(str(list_of_posts))
    return list_of_posts

def main():
    
    reddit = praw.Reddit('sentimentbot', user_agent='Python Sentiment Analyzer')
    subreddit = input("Input subreddit to search: ")
    search = input("Input search term: ")
    analyzer = SentimentIntensityAnalyzer()
    posts = getPosts(reddit, search, subreddit, 0, 0)
    values = []
    for post in posts:
        print(post.title)
        #print("Total analyzed comments: " + str(len(values)))
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            print("     " + comment.body)
            print(str(getAffinityValue(analyzer, comment.body)))
            values.append(getAffinityValue(analyzer, comment.body)['compound'])
        #comments = parsePost(post)
    print("Total number of comments analyzed: " + str(len(values)))
    print("Average Affinity of topic is: " + str(statistics.mean(values)))

def prog_main(subreddit, search):
    reddit = praw.Reddit('sentimentbot', user_agent='Python Sentiment Analyzer')
    analyzer = SentimentIntensityAnalyzer()
    posts = getPosts(reddit, search, subreddit, 0, 0)
    values = []
    commentsList = []
    num_comments = 0
    for post in itertools.islice(posts, 10): #Top 10 posts
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            num_comments = num_comments + 1
            comm_value = getAffinityValue(analyzer, comment.body)['compound']
            values.append(comm_value)
            if (random.random() < 0.02):
                commentsList.append((comment, comm_value))
    averageSentiment = str(statistics.mean(values))
    return averageSentiment, commentsList, num_comments

