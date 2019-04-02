# File: reddit_analysis.py
# Project: Social-Media-Analysis
# Team: Bayer-Social-Media-Analysis
# Programmer: Jacob Grubb
# Description: Python script to gather raw posts from Reddit, then pass those posts into a sentiment analyzer to determine overall sentiment

import requests
import vaderSentiment
import json

getAffinityValue(text):
    return vaderSentiment.vaderSentiment.SentimentIntensityAnalyzer.polar_scores(text)

parsePost(post):
    content = []
    for comment in post[1][data][children]:
        content.push(comment[data][body])
    return content

getPosts(keyword, subreddit, opt_startDate, opt_endDate):
    query = "https://www.reddit.com/r/" + subreddit + "/search/" + keyword
    searchResponse = requests.get(query)
    return searchResponse.parseJSON(list of posts)

main():
    subreddit = input("Input subreddit to search: ")
    search = input("Input search term: ")
    posts = getPosts(search, subreddit, 0,)0)
    values = []
    for post in posts[:5]:
        comments = parsePost(post)
        for comment in comments[:15]:
            values.push(getAffinityValue(comment))
    print("Average Affinity of post is: " + str(values))

main(subreddit, search):
    posts = getPosts(search, subreddit, 0,)0)
    values = []
    for post in posts[:5]: #Top 5 posts
        comments = parsePost(post)
        for comment in comments[:15]: #Top 15 comments
            values.push(getAffinityValue(comment))
    print("Average Affinity of post is: " + str(values))

main()