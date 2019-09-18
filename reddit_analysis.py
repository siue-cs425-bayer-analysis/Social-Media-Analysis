# File: reddit_analysis.py
# Project: Social-Media-Analysis
# Team: Bayer-Social-Media-Analysis
# Programmer: Jacob Grubb
# Description: Python script to gather raw posts from Reddit, then pass those posts into a sentiment analyzer to determine overall sentiment

import requests
import vaderSentiment
import json
import praw

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
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            #print("     " + comment.body)
            print(str(getAffinityValue(analyzer, comment.body)))
        #comments = parsePost(post)
        #for comment in comments[:15]:
        #    values.push(getAffinityValue(comment))
    print("Average Affinity of post is: " + str(values))

def prog_main(subreddit, search):
    posts = getPosts(search, subreddit, 0, 0)
    values = []
    for post in posts[:5]: #Top 5 posts
        comments = parsePost(post)
        for comment in comments[:15]: #Top 15 comments
            values.push(getAffinityValue(comment))
    print("Average Affinity of post is: " + str(values))

main()
