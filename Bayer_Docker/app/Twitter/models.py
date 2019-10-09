#
#   Author:         Carl Grissom
#   Date:           09/21/2019
#   Project:        Bayer Sentiment Analysis CS 499
#   Filename:       
#   
#   Description:
#
#



from django.db import models

# Create your models here.

class Tweet(models.Model):
    fullText = models.CharField(max_length=400) # full text of tweet
    userId = models.CharField(max_length=60)
    tweetId = models.CharField(unique = True, max_length=100)
    sentiment = models.DecimalField(max_digits=4, decimal_places=3)
    date = models.DateField(auto_now=False, auto_now_add=False)
    likes = models.PositiveIntegerField()
    retweets = models.PositiveIntegerField()
    location  = models.CharField(max_length=50)
    
    def __str__(self):
        tweet = self.full_text
        return tweet
    
    
class WordList(models.Model):
    word = models.CharField(max_length=50)
    wordCount = models.PositiveIntegerField()
    tweetId = models.ForeignKey(Tweet, on_delete=models.PROTECT)  
    
    def __str__(self):
        word = self.word + ': ' + self.count
        return word
    
    
class Hashtags(models.Model):
    # hashtags can seemingly be of length of the tweet making the whole tweet the hashtag,
    # so they need to big enough to hold that, but really are not that long in general so, 
    # limited to 100 char
    hashtag = models.CharField(max_length=100)
    hashtagCount = models.PositiveIntegerField()
    tweetId = models.ForeignKey(Tweet, on_delete=models.PROTECT)
    
    def __str__(self):
        hastag = self.hastag + ': ' + self.count
        return hastag
    

