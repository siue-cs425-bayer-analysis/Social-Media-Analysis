#
#   Author:         Carl Grissom
#   Date:           09/21/2019
#   Project:        Bayer Sentiment Analysis CS 499
#   Filename:       models.py
#   
#   Description: Twitter search models
#
#

from django.db import models
from  django.utils import timezone


class Tweet(models.Model):
    tweetId = models.CharField(primary_key = True, max_length=100)
    fullText = models.CharField(max_length=400) # full text of tweet
    userId = models.CharField(max_length=60)
    sentiment = models.DecimalField(max_digits=4, decimal_places=3)
#    date = models.DateTimeField()
    likes = models.PositiveIntegerField()
    retweets = models.PositiveIntegerField()
    location  = models.CharField(max_length=50)

    
    def __str__(self):
        tweet = self.fullText
        return tweet
    
    
class WordList(models.Model):
    word = models.CharField(max_length=50)
    #tweetId = models.ManyToManyField(Tweet)  
    
    class Meta:
     ordering = ('word',)   
    
    def __str__(self):
        word = self.word
        return word
    

class StopWord(models.Model):
    stopword = models.CharField(max_length=50)

    def __str__(self):
        word = self.stopword
        return word
    
    
class Location(models.Model):
    name = models.CharField(primary_key = True, max_length = 50)
    lat = models.CharField(max_length=50)
    log = models.CharField(max_length=50)
    
    def __str__(self):
        location = self.name + ' [\' ' + self.lat + ' , ' + self.log + ' \']'
        return location
    
    
class SearchTerm(models.Model):
    searchTerm = models.CharField(primary_key = True, max_length=50)

    def __str__(self):
        return self.searchTerm
    
